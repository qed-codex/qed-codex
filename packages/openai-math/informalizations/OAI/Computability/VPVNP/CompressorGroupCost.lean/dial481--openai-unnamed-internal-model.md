---
{
  "module": "OAI/Computability/VPVNP/CompressorGroupCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGroupCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGroupCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Communication charges across a source-group split

Each source report and each descriptor row is charged once. A bound on the
full native pass therefore covers its two deterministic intervals and its
selected row at the same rate.


### `groupCost_append`

 Concatenating source groups adds their report and descriptor charges. 

### `groupCost_split_selector`

 Exact charge of a selector together with its forced prefix and suffix. 
