---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSpaceTravel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSpaceTravel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSpaceTravel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Signed head displacement in a two-tape routine

Positions on each bidirectional tape are measured from its initial head.
The same transition that writes the symbol and moves the tape contributes
one signed unit, or zero for a stationary head.


### `moveDelta`

 Directions 0, 1 and 2 in a table row mean stay, left and right. 

### `Travel`

 A deterministic physical run with the two net head displacements. 
