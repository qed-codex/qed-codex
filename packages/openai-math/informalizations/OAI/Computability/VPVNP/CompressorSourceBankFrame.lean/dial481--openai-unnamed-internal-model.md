---
{
  "module": "OAI/Computability/VPVNP/CompressorSourceBankFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceBankFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceBankFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The physical pointer bank across all calls of a descriptor row

The calendar tag, ordinal, active frame, recipe row and data workspace lie
above the six external pointer cells. Each original data call is charged its
own writes. Each scheduler call has its concrete memory effect. Consequently
the framing reads on every intervening call see the same pointers, and words
preceding the workspace, including the virtual header span, survive the row.


### `Stable`

 Preservation at every call boundary, including intermediate worker calls. 

### `preparation_stable`

 The three deterministic control calls retain all six physical pointers,
including in a selector row with no admitted terms. 

### `row_stable`

 Preparation, data and closing calls all preserve the low cells. The only
source footprint premise concerns the genuine data worker's own writes. 
