---
{
  "module": "OAI/Computability/VPVNP/NetworkMonomialIso.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/NetworkMonomialIso.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/NetworkMonomialIso.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reindexing local kernel witnesses

The coordinate change on the input and output of a tensor substitution
transports the arguments of each local map. Its successful checks, choices
and parameter exponents remain the ones attached to the original map.


### `Term.reindexWitness`

 Transport witnesses for every local kernel entry of one placed term. 

### `Step.reindexInputWitness`

 A step written in new input coordinates carries the same finite
witnesses for every selected output term and local kernel. 
