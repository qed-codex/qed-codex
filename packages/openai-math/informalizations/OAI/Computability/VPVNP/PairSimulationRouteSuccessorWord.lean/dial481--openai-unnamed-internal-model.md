---
{
  "module": "OAI/Computability/VPVNP/PairSimulationRouteSuccessorWord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteSuccessorWord.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteSuccessorWord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing the successor mask and the inactive-send flag

A successor class uses the mask of its lowest `j + 1` bits. The zero-cursor
send is inactive when the site has no nonwrapping successor or its successor
changes a different set of bits. Native xor and self-division test the two
conditions on host words.


### `successor_values`

 The native mask word and rejection flag of a successor system at cursor zero. 
