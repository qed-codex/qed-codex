---
{
  "module": "OAI/Computability/VPVNP/ShrinkStateOutput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkStateOutput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkStateOutput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The output state of a selected shrinking layout

The surviving output is already a directed regular lift over the old base
and the tag field. Its subdivisions supply the widths of the new numbered
arcs, including the zero widths on cyclic padding arcs.


### `shrinkOutputState`

 The tag becomes part of the base, and only the unconsumed binary lane
field participates in the next lift. 

### `shrinkOutputState_network`

 The output used by the local matrices is exactly the next state's network. 

### `shrinkOutputState_positions`

 Every list of motif choices packs the input sites by the same factor K. 

### `shrinkOutputState_energy`

 The energy on genuine motif slots equals the full state energy, since
the zero-width padding has zero charge. 
