---
{
  "module": "OAI/Computability/VPVNP/CompressedRAMMonomials.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressedRAMMonomials.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressedRAMMonomials.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Monomial paths in the iterated compression of the RAM network

Equation (12.2) sums the parameter monomials of the actual compression
procedure on the padded cursor graph. The two fixed templates determine
all the local witnesses. The chosen term may change both the next state and
its kernel, at every step and in every block.


### `procedureWitnesses`

 Every map entry of the scheduled block has finite monomial witnesses in
the common alphabet of the two templates. 

### `executeWitnesses`

 Local witnesses for the complete history in Theorem 7.1. 

### `compressedRAMCount`

 The sum over the expanded paths of the concrete compression is the
integer machine path count specialized to the coefficient ring. A choice
retains the term sequence, final edge values, and all local witnesses. 
