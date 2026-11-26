---
{
  "module": "OAI/LinearAlgebra/SpectralBooks/AlgebraicExtensionRank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/AlgebraicExtensionRank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/AlgebraicExtensionRank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Asymptotic rank is invariant under algebraic scalar extension

A decomposition of a fixed power has only finitely many coefficients.
Over an algebraic extension they lie in a finite-dimensional intermediate
field, so the finite-extension estimate applies to that power.


### `asymptoticRank_map_le`

 Exact rank does not increase under extension, hence neither does
asymptotic rank. 

### `asymptoticRank_map_eq_of_isAlgebraic`

 An algebraic extension leaves the asymptotic rank of every finite tensor unchanged. 
