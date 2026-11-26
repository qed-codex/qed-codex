---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/CoefficientSearch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/CoefficientSearch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/CoefficientSearch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable finite search for binomial interpolation coefficients

Execution uses an explicit residue alphabet, tuple enumeration, and equation
tests. The determinant-one interpolation theorem is used only to prove that
the search succeeds. No inverse or choice operator occurs in the algorithm.


### `tuples`

 Enumerate all fixed-length tuples over a given finite alphabet. 

### `checkAll`

 Short-circuit conjunction with an exact count of predicate evaluations. 

### `Report`

 Search result and the actual numbers of candidates and equations tested. 

### `scan`

 Return the first successful candidate, keeping both counters. 

### `alphabet`

 Explicit enumeration of the residue labels 0,...,p-1. 

### `Equations`

 The finite system specifying the desired parity interpolant. 

### `equationTest`

 One decidable equation test. 

### `checkVector`

 Test all R equations, counting those actually evaluated. 

### `search`

 Finite search: the only candidates are the p^R explicitly enumerated
coefficient vectors, independent of the instance dimension D. 

### `search_result_eq_find`

 The returned candidate is exactly the first one accepted by the test. 

### `search_success`

 The search succeeds because the determinant-one binomial matrix
guarantees that its finite candidate list contains a solution. 

### `coefficients`

 Executable coefficient selection. The zero fallback is unreachable for
positive p, as proved below. 

### `coefficients_eq_parity`

 Uniqueness identifies the executable search result with the previously
verified inverse-defined coefficients. The inverse is not executed. 

### `coefficientsNat`

 Executable zero extension matching the natural-number-indexed matrix
construction. 

### `coefficientsNat_spec_of_mem`

 The selected coefficients satisfy the required equation at every
integer weight in the interval, even when R exceeds p. 
