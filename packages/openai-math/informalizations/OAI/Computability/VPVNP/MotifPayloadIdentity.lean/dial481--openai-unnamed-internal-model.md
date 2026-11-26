---
{
  "module": "OAI/Computability/VPVNP/MotifPayloadIdentity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifPayloadIdentity.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifPayloadIdentity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Contraction of a single grouped payload

For a fixed global selector sequence, a matching payload width allows all
wire values to be split into independent fields for the repeated copies.
Summing over those fields factors into the product of the base contractions.
A mismatched width makes the local entry vanish at every party.


### `assignmentEquiv`

 Regroup the edgewise fields into one complete wire assignment per copy. 

### `sum_payload_indices`

 A fixed global sequence contributes precisely the product of its local
base contractions to the one outer term indexed by its accumulated widths. 
