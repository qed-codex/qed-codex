---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryEvaluation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryEvaluation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryEvaluation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact natural-valued query semantics. These identities preserve the ambient
assignment type, including coordinates absent from every clause. 

### `acceptedCount_eq_count_of_mass_zero`

 At zero violation mass, the accepted count is the full CNF count. 

### `markedCount_le_two_pow`

 Each marked query, just like the unmarked query, counts at most all
assignments over the original declared variables. 

### `sum_markedCount_le`

 The greedy score sums actual marked query results and has a fixed binary
width even for candidates that lose the comparison. 

### `squarefreePolynomial`

 A proof-only multilinear representative of the existing squarefree algebra.
The evaluator never builds this multivariate polynomial or its support list. 

### `squarefreePolynomial_totalDegree`

 Existing positive-Taylor-degree support control implies the hypothesis of
Boolean finite differences, without a new backend or formal-variable expansion. 

### `squarefree_sum_eval_differences`

 Boolean finite differences apply directly to the source's squarefree
coefficients; the original support bound supplies the degree premise. 

### `specializeDense`

 Substitute correction variables immediately and retain only the two
bounded scalar coefficient indices. 

### `dense_jet_finite_differences`

 All Taylor and lifting coefficients use the same streamed pair family.
The sign is an integer action, so no multiplicativity of readout is needed. 

### `grouped_dense_query`

 The dense computation groups complete factors in the common coefficient
ring. The additive lifting-marker readout occurs only after the group product. 

### `dense_readout_source`

 The new bounded array readout is exactly the original shared-marker
coefficient sum, with the same Taylor truncation. 

### `colored_selected_dense_readout`

 Every actual colored factor, including neutral padding and the optional
marked clause, contributes to the one original query polynomial. 

### `colored_selected_dense_shift`

 Shifting at a reconstruction node retains the same source target. 
