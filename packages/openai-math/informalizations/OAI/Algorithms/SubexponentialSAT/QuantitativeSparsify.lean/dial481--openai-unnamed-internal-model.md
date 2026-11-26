---
{
  "module": "OAI/Algorithms/SubexponentialSAT/QuantitativeSparsify.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/QuantitativeSparsify.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/QuantitativeSparsify.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sparsification with a variable budget

The threshold parameter is an explicit input to this interface.  In particular,
none of these definitions uses the fixed `1/32` selector from the earlier
manuscript.  The returned list is the output of the terminating syntactic
sunflower algorithm.  Its pointwise semantics is a union of satisfying sets;
the leaves need not be disjoint.


### `clauseVector`

 Sorted literal codes padded with zero to a fixed width.  Real literal codes
are shifted by one, so padding cannot collide with a literal. 

### `clause_count_le`

 There are at most (2n+1)^k different clauses of width at most k, including
the empty clause.  No normalization or semantic assumption is needed. 

### `candidate_count_le`

 A bound on enumerated candidate pairs in terms of variable count.  This
counts candidates; testing and generating a candidate still require work. 

### `leavesFor`

 The actual deterministic leaf list for the explicit threshold parameter. 

### `decomposition_eval_iff`

 Every individual assignment is preserved by the union of leaves. 

### `leavesFor_satisfyingAssignments`

 A finite-set version of the pointwise statement.  This is a union, not a
sum of leaf counts: an assignment may satisfy several leaves. 

### `treeFor_nodeCount_le`

 The quantitative node bound for arbitrary real exponential budget.  The
two parameter inequalities are discharged by the separate arithmetic selector;
no property of an input-dependent branch path is an assumption here. 

### `polynomialBound_shift`

 A polynomial bound above index two extends to all indices after shifting
the base. The coefficient and degree are chosen before the index varies. 

### `polynomialBound_shift_power`

 The shifted base also absorbs the fixed coefficient. 

### `chosenLeaves`

 Reciprocal-budget output. The same fixed program selects all parameters
from k and s before it processes the formula. 

### `candidateExponent`

 The exponent in the finite candidate-count bound, with every dependence
on the chosen threshold still visible. 
