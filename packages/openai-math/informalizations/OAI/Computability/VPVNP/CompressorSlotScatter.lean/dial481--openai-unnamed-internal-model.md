---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotScatter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotScatter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotScatter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Inverting a rectangular endpoint table in external RAM

The input is indexed by ordered incidence and gives the absolute endpoint field of
that incidence. One burst call reads this field and stores the incidence index at
that field in the inverse table. An injective input can leave holes in the inverse
table. The pass preserves every hole as well as all memory outside the table.


### `visit`

 Public words give the base of the field table and the base of the inverse table.
Register 0 is the incidence index and becomes the next call's persistent cursor. 

### `events`

 The read and the write in program order, including the intervening arithmetic. 

### `Regions`

 Both address intervals fit in a word and are disjoint. Either order is allowed. 

### `Prefix`

 At cursor `k` precisely the fields of incidences below `k` have been written. 

### `run`

 The complete scatter pass constructs the inverse at every occupied endpoint
field, returns the end cursor, and preserves all other cells. It spends exactly
three calls-plus-probes units per incidence, with ten instructions of fuel per call. 
