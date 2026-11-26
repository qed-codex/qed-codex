---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/Moments.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/Moments.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/Moments.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Squarefree coefficient extraction by independent head moments

The coefficient algebra is an explicit parameter: this file does not identify
ordinary total-degree truncation with Boolean squarefree reduction.  The
squarefree implementation supplies the coefficient add-homs and scalar law.
All sums below are finite, including empty buckets and arbitrary outer labels.


### `headMoment`

 The actual array of weighted local sums for one retained support. 

### `momentProduct`

 Multiply the local sums, retaining their full coefficient algebra. 

### `extractMoments`

 The complete coefficient-extraction algorithm for a finite support list. 

### `momentProduct_eq_sum`

 Finite distributivity is applied before coefficient extraction. 

### `coefficient_momentProduct`

 The single-support moment identity. No field or division is used. 

### `extractMoments_eq_sum`

 Sum all retained squarefree coefficients after the head products. 

### `extractMoments_eq_evaluated_sum`

 An evaluation expansion is the only bridge needed from the squarefree
algebra. Its support theorem will justify the supplied finite `supports`. 

### `extractMoments_actualBuckets`

 All integer-label tuples are handled separately; their local buckets can
have unequal sizes or be empty. The equivalence is the actual bucket map. 
