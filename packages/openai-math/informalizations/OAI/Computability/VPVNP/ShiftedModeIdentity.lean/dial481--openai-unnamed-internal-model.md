---
{
  "module": "OAI/Computability/VPVNP/ShiftedModeIdentity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShiftedModeIdentity.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShiftedModeIdentity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Matrix identity for shifted fermionic crossing

Each summand in the coefficient extracted in Appendix B is the product of
two finite matrices supported on opposite energy shifts. We recover these
matrices from the shifted residue, with one summand for each term of
`(z - w)^d`. The result is valid also between states of unequal energy.


### `shifted_operator_identity`

 Opposite-order fermionic modes recover the vacuum pairing times the
identity matrix, at any shift inside the enlarged cutoff. 
