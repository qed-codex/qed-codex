---
{
  "module": "OAI/Computability/VPVNP/VerifierMembership.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMembership.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMembership.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# VNP membership from Boolean verification

For a family of Boolean verifiers with polynomially many choice bits and gates, the
paired coefficient-counting polynomials lie in VNP. The size and degree estimates
come from the explicitly compiled arithmetic summand. For the machine-defined
family, the remaining input to this construction is a polynomial-size Boolean
circuit family implementing the canonical path verifier.


### `isVNP_of_counting_verifier`

 A bounded Boolean verifier gives a VNP representation of its paired counting
polynomial, with a formal summand on the visible variables and all witness bits. 

### `P_isVNP_of_verifier`

 Applying the generic verifier construction to the machine family (1.1). 
