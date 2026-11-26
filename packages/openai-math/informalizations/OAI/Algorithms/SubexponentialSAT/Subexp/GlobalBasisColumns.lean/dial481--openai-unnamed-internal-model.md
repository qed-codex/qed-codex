---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisColumns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisColumns.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisColumns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical column descriptors for global basis matrices

Descriptors contain only block, color, and local-column indices, or a
leftover rank. They are constructed by actual framed-word emitters; no
matrix entries or global read plan are supplied to these programs.


### `field_eval`

 Copy and frame one retained descriptor field. Only the payload
accumulator changes; the source word and all surrounding data are preserved. 
