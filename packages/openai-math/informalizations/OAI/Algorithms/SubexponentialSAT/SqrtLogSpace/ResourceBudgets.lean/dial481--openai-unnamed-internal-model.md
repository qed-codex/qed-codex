---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/ResourceBudgets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/ResourceBudgets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/ResourceBudgets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed-degree numerical closure for measured streaming costs. 

### `fixedPolynomialCost_bound`

 A fixed polynomial in an old measured cost and the input length preserves
exactly the supplied runtime scale. This assigns no cost to an implementation. 

### `runtimeBound_le_rho`

 The literal manuscript exponent follows from the same measured bound. 

### `streamingFactors_le_square`

 Squaring the support count and the assignment factor costs only a fixed
square of their combined nonnegative budget, uniformly in all parameters. 

### `streamedTupleCost_le`

 Generator traversal and complete-tuple visitors are additive. A visitor
rescans one head at a time, so its assignment factor never multiplies the
predecessor-rescan factor of the generator. 

### `streamedPairTupleCost_le`

 The support-pair square and additive signature traversal are a fixed
square of the original combined combinatorial envelope. 

### `chosen_sparseBound_le_lambda`

 The native dyadic parameter program returns exactly this larger cap,
which bounds leaf occurrences and remains polynomial in the ceiling log. 

### `chosen_depth_polynomial`

 The depth factor in the disjoint tree bound is a fixed-degree input
polynomial for the actual selected threshold. 

### `chosen_sparseBound_eventually_le_log2_power`

 The chosen occurrence cap satisfies the original incidence algorithm's
integer logarithm hypothesis above a cutoff depending only on the width. 

### `count_lt_precision_modulus`

 The existing precision also separates the full ambient assignment count
when the raw formula has no clauses. 

### `chosen_trial_guards_cutoff`

 One width-dependent cutoff validates every original selector trial for
the actual dyadic sparsification bound, including losing scores and marks. 

### `chosen_exponent_length_le_input`

 The returned dyadic word has this polynomial length, even though its
numeric value is not charged as a unary representation. 

### `chosen_treeBudget_runtimeBound`

 Numerical tree size for the actual reciprocal schedule. The result is
an envelope for visits; each native visit still needs its measured cost. 

### `chosen_nativeEnvelope_cutoff`

 The exact chosen occurrence bound discharges the initial polylogarithm
field of the original worst-case envelope. All remaining fields below are
pointwise numerical obligations for the actual streamed construction. 

### `polynomialBudget_substitute`

 Fixed polynomial local budgets compose without allowing the exponent
to depend on the runtime input or the number of streamed iterations. 

### `compiledSpace_polynomial`

 Polynomial source-stack bounds remain polynomial under the actual guarded
compiler's all-tape, all-prefix visited-cell envelope. 

### `canonical_input_length_polynomial`

 The canonical finite-set input itself has a fixed polynomial size in
ambient n, including unused variables and the empty formula. 

### `inputPolynomial_ambient_power`

 A physical input-polynomial word cap yields the polynomial-in-n word
premise of the old explicit time envelope above one fixed cutoff. Constants,
degree and cutoff are all chosen before the input formula. 

### `boundaryStorage_le_square`

 A common bound on simultaneous physical fields gives a quadratic bound
on the entire DFS boundary, including the framed frontier and accumulator. 

### `dfsBoundary_polynomial`

 The concrete framed DFS boundary is polynomial in the original input
length: its depth is the original clause count times the fixed width, not
the number of visited nodes. The threshold field includes retained setup. 

### `dfsVisitSpace_le_fourth`

 The exact four summands of `DFSCountProgram.visitSpace`. The selector
coefficient is fixed by the clause width; no exponential visit count appears. 

### `dfsVisitTime_le`

 The actual DFS visit budget is polynomial in its retained fields times
the leaf budget, including splitter maxima and all cleanup passes. 

### `dfsCommandTime_le`

 Startup, all visits and full count-word export fit the product of the
visit count, the leaf budget and one fixed retained-field polynomial. 

### `chosen_sparseBound_le_input`

 The actual disjoint occurrence choice is bounded in original input
length, with coefficients and degree fixed by the width. 

### `chosen_leaf_input_cap`

 The complete ordinary size used by native leaf preparation is a fixed
input polynomial for the actual occurrence choice and sparse leaf count.
Physical input words remain independently bounded by their proved producer. 

### `polynomialCost_input_substitute`

 A physical input cap enters a measured time bound with a fixed degree,
independently of the size of the old exponential work counter. 

### `fixedPolynomialCost_with_input`

 Physical local storage may be substituted before a fixed-power time
comparison; the original runtime scale is unchanged. 
