---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramEntryBankCovered.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramEntryBankCovered.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramEntryBankCovered.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `covered_uncovered_eval`

 No arithmetic is run when the selected row is covered and the selected
column is outside the covered blocks. Metadata cleanup is still charged. 

### `covered_eval`

 Both metadata records are covered: an actual comparison chooses the
cached universal entry or literal zero. The private caller bank is retained. 
