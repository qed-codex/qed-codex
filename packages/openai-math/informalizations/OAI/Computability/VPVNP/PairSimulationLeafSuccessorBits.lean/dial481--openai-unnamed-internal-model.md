---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafSuccessorBits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSuccessorBits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSuccessorBits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Successor fields in the serialized incident buffer

At cursor zero every successor mask selects the flip arc for a send. A
receive selects that arc exactly for the mask reaching the last cursor bit.
The first site's absent receive and the final site's absent send each supply
one entire zero field.


### `succBits_eq`

 The outgoing and incoming successor blocks loaded by the native RAM
are the corresponding slices of the site's decoded cursor-zero input. 
