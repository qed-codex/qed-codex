---
{
  "module": "OAI/Computability/VPVNP/RadicalCertificate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RadicalCertificate.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RadicalCertificate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Clearing the Rabinowitsch certificate

In Appendix D.1 of *VP and VNP differ over every field*, the auxiliary equation
`1 - y f` converts a vanishing question into a certificate of inconsistency.
Index the original variables by `Fin t` and the extra variable by zero in
`Fin (t + 1)`. Substitution of `1/f` in the fraction field clears all denominators
with a single power `f ^ P` and controls the total degree of each new multiplier.


### `clearedMultiplier`

 The coefficient of `y ^ b` is multiplied by `f ^ (P - b)` to clear its denominator. 

### `clearedMultiplier_totalDegree`

 Total-degree control for the multipliers indexing the rows of the Macaulay matrix. 

### `clear_certificate`

 Bounded Rabinowitsch denominator clearing. From the identity for `1` in the extended
ring, obtain an identity for `f ^ P` in the original polynomial ring. 

### `mem_radical_of_certificate`

 The certificate witnesses membership in the radical of the ideal of the original equations. 
