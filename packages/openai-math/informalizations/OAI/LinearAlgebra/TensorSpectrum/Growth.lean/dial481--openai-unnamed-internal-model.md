---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/Growth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Growth.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Growth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact scalar growth from the diagonal inequalities

The auxiliary sequence is indexed from zero: `growthFactor n` is the paper's
`G_(n+1)`.  Cubing its recurrence gives the exact estimate `n + 1 ≤ G_(n+1)^3`.
Thus no logarithmic asymptotic estimate is needed for this component.

This module proves only the scalar consequence of the two diagonal inequalities.
It does not assume or assert that a tensor character supplies those inequalities.

