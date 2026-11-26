---
{
  "module": "OAI/Computability/VPVNP/RAMBitLocality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMBitLocality.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMBitLocality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The incident-bit input of a single RAM validator

A site's predicate depends only on its own header and its incident vector of
the width in equation (10.1). Equality of two such vectors gives equality of
the adjacent successor messages and both messages of every incident sorting
exchange. This applies to malformed assignments as well as accepted ones.


### `incidentBits`

 One site's physical bit vector in the contiguous layout of equation (10.1). 

### `AgreeAt`

 Equality of all of the physical sender arrays consulted at a single site. 

### `bitValidator_congr`

 A site's validator is a function of its own header and incident bit vector.
Both the canonicality test and the call/sort checks satisfy this locality. 
