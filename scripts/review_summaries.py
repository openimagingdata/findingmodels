#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "textual",
# ]
# ///

from __future__ import annotations

import argparse
import glob
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from tempfile import NamedTemporaryFile

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Footer, Header, MarkdownViewer, OptionList, Static, TextArea

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REVIEW_DIR = REPO_ROOT / "reviews"
ENTRY_TITLE_RE = re.compile(r"(?m)^###\s+(.+?)\s*$")
RESPONSE_RE = re.compile(r"(?m)^\*\*Response:\*\*(.*)$")
SEPARATOR_RE = re.compile(r"(?m)^---\s*$")
GLOB_CHARS = set("*?[")


@dataclass
class ReviewEntry:
    review_file: "ReviewFile"
    index_in_file: int
    title: str
    body_before_response: str
    response: str
    original_response: str
    original_section: str

    @property
    def answered(self) -> bool:
        return bool(self.response.strip())

    def serialize(self) -> str:
        if self.response == self.original_response:
            return self.original_section.rstrip("\n")
        before = self.body_before_response.rstrip("\n")
        return f"{before}\n\n{format_response_block(self.response)}"


@dataclass
class ReviewFile:
    path: Path
    preamble: str
    trailing_separator: bool
    ending_newlines: int
    original_text: str
    entries: list[ReviewEntry] = field(default_factory=list)

    @property
    def short_label(self) -> str:
        stem = self.path.stem
        return stem.removeprefix("review_")

    def serialize(self) -> str:
        sections = [self.preamble.rstrip("\n")]
        sections.extend(entry.serialize().rstrip("\n") for entry in self.entries)
        rendered = "\n\n---\n\n".join(sections)
        if self.trailing_separator:
            rendered += "\n\n---"
            rendered += "\n" * self.ending_newlines
        else:
            rendered += "\n" * self.ending_newlines
        return rendered

    def dirty(self) -> bool:
        return self.serialize() != self.original_text


def format_response_block(response: str) -> str:
    cleaned = response.rstrip()
    if not cleaned:
        return "**Response:**  "
    if "\n" not in cleaned:
        return f"**Response:** {cleaned}"
    return f"**Response:**\n{cleaned}"


def extract_response_text(match: re.Match[str], section: str) -> str:
    inline_text = match.group(1).strip()
    tail_text = section[match.end() :].lstrip("\n").rstrip()
    if inline_text and tail_text:
        return f"{inline_text}\n{tail_text}"
    return inline_text or tail_text


def parse_review_file(path: Path) -> ReviewFile:
    text = path.read_text(encoding="utf-8")
    raw_sections = SEPARATOR_RE.split(text)
    trailing_separator = text.rstrip().endswith("---")
    ending_newlines = len(text) - len(text.rstrip("\n"))
    preamble = raw_sections[0].rstrip("\n")
    entry_sections = [section.strip("\n") for section in raw_sections[1:] if section.strip()]
    review_file = ReviewFile(
        path=path,
        preamble=preamble,
        trailing_separator=trailing_separator,
        ending_newlines=ending_newlines,
        original_text=text,
    )

    for entry_index, section in enumerate(entry_sections):
        title_match = ENTRY_TITLE_RE.search(section)
        if title_match is None:
            raise ValueError(f"{path}: could not find entry title in section {entry_index + 1}")
        response_match = RESPONSE_RE.search(section)
        if response_match is None:
            raise ValueError(f"{path}: could not find response block in section {entry_index + 1}")

        response = extract_response_text(response_match, section)
        review_file.entries.append(
            ReviewEntry(
                review_file=review_file,
                index_in_file=entry_index,
                title=title_match.group(1).strip(),
                body_before_response=section[: response_match.start()].rstrip("\n"),
                response=response,
                original_response=response,
                original_section=section,
            )
        )

    if not review_file.entries:
        raise ValueError(f"{path}: no review entries found")
    return review_file


def atomic_write(path: Path, text: str) -> None:
    with NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        handle.write(text)
        temp_path = Path(handle.name)
    temp_path.replace(path)


def has_glob_pattern(raw_input: str) -> bool:
    return any(char in raw_input for char in GLOB_CHARS)


def expand_glob_candidates(raw_input: str) -> list[Path]:
    candidate = Path(raw_input).expanduser()
    pattern_candidates: list[Path] = []

    explicit_pattern = candidate if candidate.is_absolute() else (Path.cwd() / candidate).resolve()
    pattern_candidates.append(explicit_pattern)

    if candidate.parent == Path("."):
        pattern_candidates.append((DEFAULT_REVIEW_DIR / candidate.name).resolve())

    matches: list[Path] = []
    seen: set[Path] = set()
    for pattern in pattern_candidates:
        for match in sorted(glob.glob(str(pattern))):
            resolved = Path(match).resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            matches.append(resolved)
    return matches


def expand_review_inputs(inputs: list[str]) -> list[Path]:
    if not inputs:
        candidates = sorted(DEFAULT_REVIEW_DIR.glob("review_*.md"))
    else:
        candidates: list[Path] = []
        for raw_input in inputs:
            if has_glob_pattern(raw_input):
                glob_matches = expand_glob_candidates(raw_input)
                if glob_matches:
                    candidates.extend(path for path in glob_matches if path.is_file())
                    continue
                raise FileNotFoundError(f"Review input not found: {raw_input}")

            candidate = Path(raw_input).expanduser()
            explicit_candidate = candidate if candidate.is_absolute() else (Path.cwd() / candidate).resolve()

            if explicit_candidate.is_dir():
                candidates.extend(sorted(explicit_candidate.glob("review_*.md")))
                continue

            if explicit_candidate.is_file():
                candidates.append(explicit_candidate)
                continue

            if candidate.parent == Path("."):
                reviews_candidate = (DEFAULT_REVIEW_DIR / candidate.name).resolve()
                if reviews_candidate.is_file():
                    candidates.append(reviews_candidate)
                    continue

                if not candidate.suffix:
                    stem_candidate = (DEFAULT_REVIEW_DIR / f"{candidate.name}.md").resolve()
                    if stem_candidate.is_file():
                        candidates.append(stem_candidate)
                        continue

            raise FileNotFoundError(f"Review input not found: {raw_input}")

    filtered = []
    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        filtered.append(resolved)
    return filtered


def load_review_files(inputs: list[str]) -> list[ReviewFile]:
    paths = expand_review_inputs(inputs)
    if not paths:
        raise FileNotFoundError("No review markdown files found")
    return [parse_review_file(path) for path in paths]


class ReviewSummaryApp(App[None]):
    TITLE = "Review Summaries"
    SUB_TITLE = "Rendered review markdown with in-place response editing"
    CSS = """
    Screen {
        layout: vertical;
    }

    #body {
        height: 1fr;
    }

    #entry-list {
        width: 40;
        border: round $accent;
    }

    #content {
        width: 1fr;
    }

    #status {
        height: 2;
        padding: 0 1;
        background: $panel;
        color: $text;
        content-align: left middle;
    }

    #prompt {
        height: 1fr;
        border: round $secondary;
        background: $surface;
        scrollbar-gutter: stable;
    }

    #response {
        height: 1fr;
        border: round $success;
    }
    """
    BINDINGS = [
        Binding("ctrl+q", "save_and_quit", "Save/Quit", priority=True),
        Binding("ctrl+s", "save", "Save", priority=True),
        Binding("ctrl+p", "previous_entry", "Prev", priority=True),
        Binding("ctrl+n", "next_entry", "Next", priority=True),
        Binding("ctrl+r", "next_unanswered", "Next Unread", priority=True),
        Binding("ctrl+o", "mark_ok", "Set OK", priority=True),
    ]

    def __init__(self, review_files: list[ReviewFile]) -> None:
        super().__init__()
        self.review_files = review_files
        self.entries = [entry for review_file in review_files for entry in review_file.entries]
        self.current_index = 0
        self.suppressed_response_change_events = 0
        self.status_note = ""

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(id="body"):
            yield OptionList(id="entry-list")
            with Vertical(id="content"):
                yield Static(id="status")
                yield MarkdownViewer(show_table_of_contents=False, id="prompt")
                yield TextArea(id="response")
        yield Footer()

    async def on_mount(self) -> None:
        prompt = self.query_one("#prompt", MarkdownViewer)
        response = self.query_one("#response", TextArea)
        response.soft_wrap = True
        response.show_line_numbers = False

        entry_list = self.query_one("#entry-list", OptionList)
        entry_list.border_title = "Entries"
        entry_list.border_subtitle = "Tab here, then Up/Down"
        prompt.border_title = "Summary"
        prompt.border_subtitle = "Tab here, then scroll"
        response.border_title = "Response"
        response.border_subtitle = "Type comments or Ctrl+O for ok"
        entry_list.add_options(self.option_prompts())
        await self.go_to_index(0, keep_focus=False)
        response.focus()

    def option_prompts(self) -> list[str]:
        return [self.format_option_label(index) for index in range(len(self.entries))]

    def format_option_label(self, index: int) -> str:
        entry = self.entries[index]
        answered = "[x]" if entry.answered else "[ ]"
        return f"{answered} {entry.title}"

    def unanswered_count(self) -> int:
        return sum(1 for entry in self.entries if not entry.answered)

    def dirty_file_count(self) -> int:
        return sum(1 for review_file in self.review_files if review_file.dirty())

    def current_entry(self) -> ReviewEntry:
        return self.entries[self.current_index]

    async def go_to_index(self, index: int, *, keep_focus: bool = True) -> None:
        if not self.entries:
            return
        index = max(0, min(index, len(self.entries) - 1))
        self.current_index = index

        response = self.query_one("#response", TextArea)
        prompt = self.query_one("#prompt", MarkdownViewer)
        entry_list = self.query_one("#entry-list", OptionList)
        focused = self.screen.focused if keep_focus else None

        if entry_list.highlighted != index:
            entry_list.highlighted = index
        entry_list.scroll_to_highlight()

        await prompt.document.update(self.build_prompt_text(self.entries[index]))
        prompt.scroll_home(animate=False, immediate=True)
        self.set_response_text(self.entries[index].response)

        self.update_status()
        if focused is response:
            response.focus()
        elif focused is entry_list:
            entry_list.focus()
        elif focused is prompt.document:
            prompt.document.focus()

    def build_prompt_text(self, entry: ReviewEntry) -> str:
        return entry.body_before_response.rstrip()

    def set_response_text(self, text: str) -> None:
        response = self.query_one("#response", TextArea)
        self.suppressed_response_change_events += 1
        response.text = text

    def refresh_entry_option(self, index: int) -> None:
        entry_list = self.query_one("#entry-list", OptionList)
        entry_list.replace_option_prompt_at_index(index, self.format_option_label(index))

    def set_status_note(self, note: str) -> None:
        self.status_note = note
        self.update_status()

    def clear_status_note(self) -> None:
        self.status_note = ""
        self.update_status()

    def update_status(self) -> None:
        entry = self.current_entry()
        review_file = entry.review_file
        try:
            display_path = str(review_file.path.relative_to(REPO_ROOT))
        except ValueError:
            display_path = str(review_file.path)
        status = (
            f"{display_path} | entry {self.current_index + 1}/{len(self.entries)}"
            f" | in file {entry.index_in_file + 1}/{len(review_file.entries)}"
            f" | unanswered {self.unanswered_count()}"
            f" | unsaved files {self.dirty_file_count()}"
        )
        if self.status_note:
            status = f"{status} | {self.status_note}"
        self.query_one("#status", Static).update(status)

    def save_all(self) -> int:
        saved_files = 0
        for review_file in self.review_files:
            rendered = review_file.serialize()
            if rendered == review_file.original_text:
                continue
            atomic_write(review_file.path, rendered)
            review_file.original_text = rendered
            saved_files += 1
        self.update_status()
        return saved_files

    async def on_option_list_option_highlighted(self, message: OptionList.OptionHighlighted) -> None:
        if message.option_index == self.current_index:
            return
        await self.go_to_index(message.option_index)

    async def on_option_list_option_selected(self, message: OptionList.OptionSelected) -> None:
        await self.go_to_index(message.option_index, keep_focus=False)
        self.query_one("#response", TextArea).focus()

    def on_text_area_changed(self, message: TextArea.Changed) -> None:
        if message.text_area.id != "response":
            return
        if self.suppressed_response_change_events:
            self.suppressed_response_change_events -= 1
            return
        entry = self.current_entry()
        entry.response = message.text_area.text
        self.refresh_entry_option(self.current_index)
        self.update_status()

    def action_save(self) -> None:
        saved_files = self.save_all()
        if saved_files == 0:
            self.set_status_note("Nothing to save")
            return
        self.set_status_note(f"Saved {saved_files} file(s)")

    async def action_previous_entry(self) -> None:
        if self.current_index <= 0:
            self.set_status_note("Already at the first entry")
            return
        self.clear_status_note()
        await self.go_to_index(self.current_index - 1)

    async def action_next_entry(self) -> None:
        if self.current_index >= len(self.entries) - 1:
            self.set_status_note("Already at the last entry")
            return
        self.clear_status_note()
        await self.go_to_index(self.current_index + 1)

    async def action_next_unanswered(self) -> None:
        total_entries = len(self.entries)
        for offset in range(1, total_entries + 1):
            next_index = (self.current_index + offset) % total_entries
            if not self.entries[next_index].answered:
                self.clear_status_note()
                await self.go_to_index(next_index)
                return
        self.set_status_note("Every entry already has a response")

    async def action_mark_ok(self) -> None:
        entry = self.current_entry()
        entry.response = "ok"
        self.set_response_text("ok")
        self.refresh_entry_option(self.current_index)

        if self.current_index >= len(self.entries) - 1:
            self.set_status_note("Set response to ok; already at the last entry")
            return

        self.clear_status_note()
        await self.go_to_index(self.current_index + 1)

    def action_save_and_quit(self) -> None:
        saved_files = self.save_all()
        if saved_files == 0:
            self.exit(message="No changes to save")
            return
        self.exit(message=f"Saved {saved_files} file(s)")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Browse review markdown files and edit the Response blocks in a Textual TUI."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Optional review files, directories, or glob patterns. Bare names resolve under reviews/. Defaults to reviews/review_*.md.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Parse and round-trip the selected review files without launching the TUI.",
    )
    return parser.parse_args(argv)


def run_check(review_files: list[ReviewFile]) -> int:
    mismatches = []
    for review_file in review_files:
        if review_file.serialize() != review_file.original_text:
            mismatches.append(str(review_file.path))
    if mismatches:
        print("Round-trip mismatch:", file=sys.stderr)
        for mismatch in mismatches:
            print(f"  {mismatch}", file=sys.stderr)
        return 1
    print(f"Validated {len(review_files)} review file(s)")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        review_files = load_review_files(args.paths)
    except (FileNotFoundError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if args.check:
        return run_check(review_files)

    app = ReviewSummaryApp(review_files)
    app.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
