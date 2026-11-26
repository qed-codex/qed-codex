---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/TagOptimized.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/TagOptimized.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/TagOptimized.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Optimizing the finite-fiber tag bound

The hypothesis here is the numeric inequality for each actual nonempty word
fiber. Its tensor-theoretic proof belongs to the restriction construction.
Taking roots of the letter weights makes the largest fiber capture the desired
sum; the remaining count of possible fibers is only polynomial in the power.


### `finset_prod_rpow_nonneg`

 A real power distributes over a finite product of nonnegative factors. 

### `countWeight_rpow`

 Powering a count weight is equivalent to powering its letter weights. 

### `tag_optimized_of_fiber_bounds`

 Optimized tag inequality from the finite-fiber inequalities. The constant
`5` and the polynomial number of possible count vectors disappear in the
tensor-power limit. The premise uses each fiber's actual finite cardinality. 
