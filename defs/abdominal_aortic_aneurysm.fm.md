{
  "oifm_id": "OIFM_MSFT_134126",
  "name": "abdominal aortic aneurysm",
  "description": "An abdominal aortic aneurysm (AAA) is a localized dilation of the abdominal aorta, typically defined as a diameter greater than 3 cm, which can lead to rupture and significant morbidity or mortality.",
  "synonyms": ["AAA"],
  "attributes": [
    {
      "oifma_id": "OIFMA_MSFT_898601",
      "name": "presence",
      "description": "Presence or absence of abdominal aortic aneurysm",
      "type": "choice",
      "values": [
        {
          "value_code": "OIFMA_MSFT_898601.0",
          "name": "absent",
          "description": "Abdominal aortic aneurysm is absent"
        },
        {
          "value_code": "OIFMA_MSFT_898601.1",
          "name": "present",
          "description": "Abdominal aortic aneurysm is present"
        },
        {
          "value_code": "OIFMA_MSFT_898601.2",
          "name": "indeterminate",
          "description": "Presence of abdominal aortic aneurysm cannot be determined"
        },
        {
          "value_code": "OIFMA_MSFT_898601.3",
          "name": "unknown",
          "description": "Presence of abdominal aortic aneurysm is unknown"
        }
      ],
      "required": false
    },
    {
      "oifma_id": "OIFMA_MSFT_783072",
      "name": "change from prior",
      "description": "Whether and how a abdominal aortic aneurysm has changed over time",
      "type": "choice",
      "values": [
        {
          "value_code": "OIFMA_MSFT_783072.0",
          "name": "unchanged",
          "description": "Abdominal aortic aneurysm is unchanged"
        },
        {
          "value_code": "OIFMA_MSFT_783072.1",
          "name": "stable",
          "description": "Abdominal aortic aneurysm is stable"
        },
        {
          "value_code": "OIFMA_MSFT_783072.2",
          "name": "increased",
          "description": "Abdominal aortic aneurysm has increased"
        },
        {
          "value_code": "OIFMA_MSFT_783072.3",
          "name": "decreased",
          "description": "Abdominal aortic aneurysm has decreased"
        },
        {
          "value_code": "OIFMA_MSFT_783072.4",
          "name": "new",
          "description": "Abdominal aortic aneurysm is new"
        }
      ],
      "required": false
    }
  ]
}
