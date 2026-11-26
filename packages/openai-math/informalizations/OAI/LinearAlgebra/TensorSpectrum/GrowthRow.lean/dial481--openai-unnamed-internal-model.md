---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/GrowthRow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/GrowthRow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/GrowthRow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite row bounds

For a concave positive row, one application of tripling bounds the row value
by a shifted index times the current increment.  Finite secant inequalities
then give the same bound for every increment.  Taking the infimum supplies
the slope required by the diagonal argument, without an asymptotic limit.

