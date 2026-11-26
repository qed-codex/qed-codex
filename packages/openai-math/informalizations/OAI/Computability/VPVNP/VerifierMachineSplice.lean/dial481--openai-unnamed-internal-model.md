---
{
  "module": "OAI/Computability/VPVNP/VerifierMachineSplice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineSplice.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineSplice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Substitution of compiled Boolean networks

Feeding all outputs of one circuit block into another takes the disjoint union of their
gate lists. Wires of the second block either select an output of the first block or
reference a gate in the appended list. This allows a verifier to use a compiled subroutine
more than once while sharing intermediate wires within each invocation.


### `subst`

 Substitute a compiled network for the free inputs of another. 
