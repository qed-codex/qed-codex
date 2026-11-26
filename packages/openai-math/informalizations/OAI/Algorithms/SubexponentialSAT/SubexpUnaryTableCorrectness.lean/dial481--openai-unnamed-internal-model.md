---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpUnaryTableCorrectness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpUnaryTableCorrectness.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpUnaryTableCorrectness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual table's row order and its connection to packed unary factors. 

### `table_getElem`

 Row position zero holds rank `p - 1`; the final position holds rank zero. 

### `table_getElem_matches_factor`

 This theorem follows the machine's descending order without silently
permuting the raw table bytes. 
