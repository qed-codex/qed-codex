---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RowSelection.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RowSelection.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RowSelection.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The executable maximal-minor search returns exactly the rational rank many
independent original integer rows, with unchanged entry bounds. 

### `select_rank`

 The output uses the actual rank, without rounding up the search cap. 

### `select_rationalRowSpan`

 The exact integer-kernel interface consumed by the layout. 

### `select_bound`

 Output entries are original integer entries, not rational combinations. 
