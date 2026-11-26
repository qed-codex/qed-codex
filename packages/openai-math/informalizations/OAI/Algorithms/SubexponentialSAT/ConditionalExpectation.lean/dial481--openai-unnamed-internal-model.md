---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ConditionalExpectation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ConditionalExpectation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ConditionalExpectation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite conditional expectation by executable sequential search

An alphabet is given as an explicit nonempty list. With a duplicate-free list,
the averages below are uniform averages on words over that alphabet. No choice
oracle is used: `chooseMin` and `assign` are recursive finite algorithms.


### `mean`

 The arithmetic mean of a score on an explicitly enumerated alphabet. 

### `chooseMin`

 Deterministic finite search; ties favor the first candidate. 

### `exists_le_uniform_mean`

 The abstract finite-uniform interface. The proof applies the same finite
search to an enumeration; executable users can supply that enumeration directly
to `chooseMin`. 

### `conditionalMean`

 Conditional uniform mean over all assignments of the remaining variables.
The list `fixed` records coordinates already fixed, in reverse order. 

### `assign`

 Fix one coordinate at a time by minimizing its exact conditional mean. 

### `assignWithEvaluator`

 The same executable search accepts a separately implemented conditional
mean evaluator. Its computation cost is not hidden in the correctness theorem. 

### `evaluator_eq_conditionalMean`

 Terminal evaluation and the finite averaging identity independently
characterize the required conditional means. 

### `assignWithEvaluator_le`

 Correctness of the search with a supplied exact evaluator. An efficient
local-probability evaluator may replace exhaustive enumeration once its two
identities below and its separate runtime bounds have been established. 

### `assign_le_conditionalMean`

 Every step preserves the conditional-expectation upper bound. 

### `assign_mem`

 All newly selected coordinates belong to the supplied alphabet. 

### `completions`

 Explicit exhaustive enumeration of completions. Prefixes are stored in
reverse coordinate order, consistently with `assign`. 

### `assign_mem_completions`

 The returned assignment extends precisely the coordinates already fixed. 

### `conditionalMean_eq_mean_completions`

 The recursive conditional mean is the ordinary finite average over all
complete assignments extending the fixed coordinates. 

### `conditionalMeanCounted`

 An instrumented evaluator recording calls to the complete-assignment
objective. This deliberately exposes the cost of exhaustive evaluation. 

### `conditionalMeanCounted_evaluations`

 Exactly `q^n` complete-assignment evaluations for `n` remaining variables
over an alphabet of size `q`. This is not a polynomial-time evaluator. 

### `assign_le_initial_mean`

 Deterministic derandomization from any established bound on the initial
uniform average. This supplies both an explicit witness and its guarantee. 

### `chooseMinCounted`

 Instrumented minimum search. Its second component counts exactly one for
each rational comparison; evaluating a score is a separate cost. 

### `assignCounted`

 Instrumented sequential assignment. This measures rational comparisons,
not the bit cost of computing the conditional means supplied to the search. 
