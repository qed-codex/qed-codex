---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotBaseLookup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotBaseLookup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotBaseLookup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Extracting the base target and lane displacement from the endpoint arrays

The packed graph is a lift. At source lane zero the destination lane is the
base arc displacement. Unpacking the destination rectangular slot therefore
recovers both base-table words needed by the next substep, for real and dummy
arcs alike.


### `atLane`

 The actual arc at a given source-role lane over the padded base ID. 

### `baseIndex`

 Numeric order of the next graph's packed bases and their outgoing slots. 

### `packedCode`

 Linear index of a packed base vertex, with its tag index as the low digit. 

### `laneZeroRow`

 Source rectangular slot at lane zero, computed from the base arc's
numeric index by quotient and remainder. 

### `unpackBaseTarget`

 Decode a packed incoming rectangular index into the base arc and lane. 

### `base_lookup`

 On each lane-zero source row, the adjacent inverse field supplies the
actual graph's target base-arc index and displacement. 
