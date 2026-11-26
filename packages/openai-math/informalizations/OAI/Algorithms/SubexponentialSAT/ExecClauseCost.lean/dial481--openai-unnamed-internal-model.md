---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecClauseCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecClauseCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecClauseCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Explicit costs for the executable clause loops

These routines return their result together with the number of charged events
in the displayed recursive execution. A recursive list-case inspection costs
one event; a literal equality test costs one further event. These are list-loop
and comparison units, **not** primitive bit-machine transitions. In particular,
`DecidableEq α` is an equality interface, not a unit-cost bit implementation.
No cost is attached to an arbitrary uninstrumented function.


### `containsM`

 Instrumented membership: one list inspection and, for a cons, one equality. 

### `allM`

 Instrumented short-circuit universal scan. 

### `anyM`

 Instrumented short-circuit existential scan. 

### `filterM`

 Instrumented filter; every list cell is visited exactly once by this loop. 

### `lengthM`

 Length is computed recursively, rather than supplied as a free data query. 

### `notM`

 Negation adds one Boolean operation. 

### `andM`

 The second argument is delayed so the measured short circuit is real. 

### `orM`

 Delayed short-circuit disjunction. 

### `subsetM`

 Literal subset is an actual nested scan. 

### `intersectionM`

 Intersection implemented by filtering with membership tests. 

### `dedupLiteralsM`

 The exact last-occurrence literal deduplication, with all comparisons charged. 

### `dedupClausesM`

 The exact extensional clause deduplication, with its nested comparisons. 

### `pairBudget`

 A uniform concrete bound for comparing two width-bounded clauses. 

### `WidthBound`

 A useful invariant for executable (possibly not normalized) clause lists. 

### `absorbM`

 Explicit absorption: deduplicate, then scan all original clauses for each survivor. 

### `natEqM`

 A structural equality scan of natural counters. This is a count of natural
constructor inspections, not a claim about a binary-number implementation. 

### `checkM`

 An instrumented implementation of the complete executable sunflower test. 

### `countBudget`

 Explicit polynomial budgets. They count only events in the measured routines. 

### `checkM_cost_le`

 Full checker work bounded from the actual nested list loops. 

### `mapM`

 Measured map counts each list-case inspection and callback event. 

### `scanM`

 First-match scan, charging each actual callback and each visited list case. 

### `cleanLiteralsM`

 Measured form of literal-list cleanup, before any tautology test. 

### `childA_M`

 All rebuilding, comparison, and absorption loops in the core child. 

### `childB_M`

 All rebuilding, comparison, append, and absorption loops in the petal child. 

### `checkerBudget_expansion`

 The full checker budget is an explicit degree-four polynomial. 

### `oppositeContainsM`

 Negating a SAT literal changes its Boolean polarity; this is not an arbitrary
function with a supplied unit-cost annotation. 

### `normalizationBudget`

 An explicit event polynomial for input normalization. 

### `checkerBudget_le_quadratic`

 On generated candidates, selected clauses are a sublist of the input. The
checker cost is therefore quadratic in input clause count and fixed width. 

### `bitEqualityProgram`

 Fixed finite code comparing two bit strings destructively. Register 4 is the answer. 

### `bitEquality_runs`

 A genuine instruction trace. Comparison destroys the inspected prefixes;
it may leave residual tails on an early mismatch. 

### `bitEquality_runsIn_bounded`

 The additional size postcondition permits the caller to charge cleanup. 

### `bitEquality_primitive_runs`

 A real primitive-bit-machine execution from an encoded two-stack comparison
boundary. This is deliberately not a claim about raw one-stack SAT input. 

### `childBudget`

 A common explicit event budget for either concrete sunflower child. 

### `checkerBudget_le_variable_power`

 The full checker is polynomial in the variable count after normalized-clause
cardinality is supplied. This bounds measured events, not primitive bit steps. 
