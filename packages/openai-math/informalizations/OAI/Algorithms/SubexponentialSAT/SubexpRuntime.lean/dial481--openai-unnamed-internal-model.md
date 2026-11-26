---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpRuntime.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpRuntime.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpRuntime.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform runtime assembly with growing layout parameters

Unlike the older fixed-width-exponent accounting, all layout parameters are
input-dependent here. `GrowingParameters.entries` exposes every argument of
the polynomial costs in Proposition 4.2 and the layout construction. The
analytic lemmas also pay for the variable-degree sunflower search.

Only the purely numerical work/trace infrastructure from `RuntimeAssembly`
is reused; none of its fixed-prime or exponent-0.9 estimates is used.


### `GrowingParameters`

 Every growing argument in the construction and counting costs. The table
size `p^k` is included explicitly, even when the clause width is fixed. 

### `GrowingParameters.size_le`

 A simultaneous polynomial bound is derived from bounds on the explicitly
listed parameters, not from an input-dependent hidden polynomial degree. 

### `uniform_parameter_polynomial_bound`

 The full bit cost of a fixed-degree polynomial in the growing parameters
is bounded by one fixed-degree input polynomial, once each parameter is. 

### `eventually_logb_power_le`

 Any fixed power of log is eventually dominated by the input size, with
an arbitrary fixed positive coefficient and the source's shift by sixteen. 

### `eventually_loglog_polynomial_search`

 The exponent of the exhaustive per-node sunflower search is negligible
on the claimed scale, for every fixed degree. The degree is not allowed to
depend on n. This is stronger than merely assuming the search is polynomial. 

### `eventually_variable_degree_search`

 Actual natural-power operation count for a variable-degree exhaustive
search. A fixed polynomial bound on that degree suffices; no fixed-degree
polynomial-time claim is made for the search itself. 

### `selectedTree`

 The actual deterministic tree selected at inverse budget `s n`. 

### `selected_tree_node_bound`

 The all-node count of the actual selected tree, with constants chosen
before the input size and with the polynomial transferred to encoding length. 

### `selected_tree_search_bound`

 Multiplying all visited nodes by the explicit exhaustive-search count
still has the required rate. This is a counting theorem; primitive simulation
cost is charged separately by the compiler/runtime layer. 

### `eventually_chosen_candidate_bound`

 The actual candidate lists selected by the quantitative sparsifier have
subexponential length. The operation cost of checking/generating an entry is
not silently identified with one bit step. 

### `executable_visits_bound`

 The node-visit counter returned by the executable list worklist, not an
unrelated abstract tree, obeys one uniform subexponential envelope. 

### `total_bound_from_envelopes`

 Generic envelope composition for the actual phase-cost sum. The three
exponent constants respectively charge per-event work, tree cardinality,
and leaf enumeration. All remain fixed before n. 

### `pipeline_output_bound`

 Once all phase executions and local quantitative bounds are supplied,
the same concrete primitive run has the assembled subexponential bound. 
