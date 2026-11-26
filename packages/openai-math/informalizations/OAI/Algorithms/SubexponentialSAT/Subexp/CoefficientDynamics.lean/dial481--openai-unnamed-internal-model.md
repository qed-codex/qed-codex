---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/CoefficientDynamics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/CoefficientDynamics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/CoefficientDynamics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Division-free tests for the normalized binomial interpolant

The executable coefficient checker shifts a list by `a[j] + 2*a[j+1]`.
Its first entry after `t` shifts is the normalized binomial evaluation at
`t`. Thus no table of binomial coefficients is an input to the checker.


### `exists_normalized`

 Existence is used only to prove that the finite executable search will
succeed. It is not the implementation of coefficient selection. 
