# Scripts Needed for Finding Models Repo

- Script to run formatting and schema validation on all of the files
- Script to create an `index.json` file that has a quick usable list of all
  the finding model definitions
- Script that checks that we don't have any OIFM ID collisions (either for
  models or attributes)
- Script to create `index.md` and Markdown versions of each of the finding
  model definitions (where `index.md` has a link to each of the definition
  MD files)
- Set these up as pre-commit actions
- Make these a condition for pull requests