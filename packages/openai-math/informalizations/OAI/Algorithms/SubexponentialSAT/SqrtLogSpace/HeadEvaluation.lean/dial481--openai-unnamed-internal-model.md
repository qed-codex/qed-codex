---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadEvaluation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadEvaluation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadEvaluation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Restricted sums over the actual Boolean heads. All products are formed in
one coefficient ring before any additive coefficient readout. 

### `fiber_sum_eq_rescan`

 An actual head rescan tests the entire key and the correction predicate.
The finite sum here specifies its result; it does not materialize a fiber. 

### `restricted_separation`

 Representatives belong to their signature fibers but need not satisfy
any of the additional local correction restrictions. 

### `corrected_group_locality`

 Immediate Boolean specialization makes the correction independent of the
summation assignment. Every factor still reads the one shared original row. 

### `restricted_assemble_iff`

 The current finite-difference support restricts original variables.
There is one Boolean choice per variable, including variables with no incidences. 

### `restricted_grouping`

 Reindex by attained full labels and perform each restricted head sum.
`hA` is the locality proved from the actual layout's integer kernels. 

### `specializeEntries_valid`

 Specialization may collide keys, so validity is proved before normalization;
no false uniqueness assumption is made about the filtered list. 

### `restricted_grouping_rescan`

 Each attained tuple is followed by one bounded-width raw head rescan;
the complete key is checked before a contribution is admitted. 
