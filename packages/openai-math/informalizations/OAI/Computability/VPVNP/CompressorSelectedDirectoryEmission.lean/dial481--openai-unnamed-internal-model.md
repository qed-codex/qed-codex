---
{
  "module": "OAI/Computability/VPVNP/CompressorSelectedDirectoryEmission.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSelectedDirectoryEmission.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSelectedDirectoryEmission.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native metadata publications for selected directory histories

The preimage worker supplies the arrays in the incoming memory. The
metadata worker leaves these arrays intact and installs the five directory
operands and the next state's DFS header. Later term-head publishers can
extend the emission by preserving precisely those cells.


### `PlacementWords`

 The five packet fields read by the traversal controller, in the
metadata writer's twelve-word order. 

### `Emission.prepend`

 Recover the pre-pass input after preliminary work on placement and incidence
arrays which leaves the DFS base and role of the active state intact. 

### `Emission.transfer`

 Term pointers and scheduler writes can follow the packet in the same
pass. They only need to frame its placement arrays and these header offsets. 

### `placement_words`

 The native writer evaluates the field bank in the metadata input memory
and publishes all five traversal operands with their exact word values. 

### `Emission.ofPublished`

 Construct the pass emission from the actual three metadata visits and
the completed native preimage rows. The owner column starts past the scalar
packet, and the entire directory ends before the successor header. 
