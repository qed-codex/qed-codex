---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseBudget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseBudget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseBudget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sharp numerical budgets for disjoint counting sparsification

The frozen counting manuscript, Appendix A, lines 1991–2054. These numerical lemmas do not assert the
existence of a sparsification tree or a primitive implementation.


### `occurrenceCap`

 The literal-degree sum in the source's leaf occurrence estimate. 

### `control_exponent`

 An explicit constant exponent absorbs the affine term in the dyadic test. 

### `dyadic_witness`

 A dyadic witness of order `s log s`, rather than the old quadratic witness.
The source's test uses `clog 2 (4 C M)`, so every comparison is integral. 

### `parameterTest`

 Exact source test at the candidate `M = 2^e`, for the rational numerator `a`
and denominator `b`. Only integer arithmetic and a ceiling logarithm occur. 

### `inverseIndex`

 Conservative inverse of a positive rational budget. 

### `exists_parameter`

 The search terminates, with a fully explicit coefficient depending only on
`k`. This theorem counts candidates; primitive bit costs are proved separately. 

### `chooseExponent`

 First passing power of two in the source's deterministic search. 

### `choose_bounds`

 The first successful candidate inherits the sharp witness bound. Constants
are chosen before the rational budget numerator and denominator. 

### `chooseM_log_budget`

 The ceiling-log test implies the real exponent budget without a numerical
logarithm oracle. 

### `chooseM_real_bound`

 Sharp source asymptotics, with constants independent of both numerator and
 denominator. The logarithm is real base two. 

### `chooseForSigma`

 The source selector on a positive rational budget, preserving its exact
numerator and denominator in every comparison. 

### `nodeCount_le`

 The source's explicit node bound for a tree with the charged path budgets.
It applies to an actual finite tree and includes every internal node. 

### `leaf_occurrences_le`

 Terminality of the actual priority selector gives the sharp occurrence cap.
Unused variables contribute zero occurrences and are retained in the ambient type. 

### `choose_finite_scan`

 Concrete finite scanning of the exact Boolean tests. This counts test calls,
not primitive bit operations. 

### `choose_encoding_bounds`

 Search length is logarithmic in the positive rational denominator; candidate
values remain polynomial in it. This exposes the uniform parameter-size budget. 

### `selectedPaths_nodeCount_le`

 Discharge the numeric path premises from actual priority-selected paths. 
