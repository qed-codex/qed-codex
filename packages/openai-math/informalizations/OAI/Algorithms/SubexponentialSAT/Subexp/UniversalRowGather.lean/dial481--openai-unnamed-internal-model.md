---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowGather.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowGather.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowGather.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading actual scalar and difference-row data for universal rows

All tables are packed runtime arrays. The selected index is unary data on
stack 16. The three fixed reads preserve their source tables and index and
produce the correction scalar, inverse node, and complete difference row.


### `readIndex_eval`

 Each read has a fixed port map. Table widths and the selected position
are consumed only as runtime words by the existing array-access program. 
