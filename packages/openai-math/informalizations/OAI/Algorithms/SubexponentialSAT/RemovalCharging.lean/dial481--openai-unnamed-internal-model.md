---
{
  "module": "OAI/Algorithms/SubexponentialSAT/RemovalCharging.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/RemovalCharging.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/RemovalCharging.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Appendix A.2: charging removals to smaller insertions

The trace below records finite clause families before and after each replacement.
The cumulative insertion counter counts events, not distinct clauses.  Its
accounting identity therefore does not assume that reinsertion is impossible.


### `card_le_mul_of_cover`

 A finite relation covering its source gives an upper bound by the sum of
the sizes of its target fibers. No disjointness of fibers is required. 

### `card_le_mul_of_charge`

 In particular, an actual single-valued charge with bounded fibers has the
same bound. 

### `smaller_card_eq_sum_widthCount`

 Partition the new clauses of width below `j` by their exact widths. 

### `removed_widthCount_le`

 Every removed width-`j` clause contains a nonempty new clause.  Its fiber
is bounded by the degree of any literal in that new clause. 

### `widthCount_le_universe_mul`

 Summing per-literal bounds controls the number of live nonempty clauses. 

### `Trace`

 A finite replacement trace.  All fields are local properties of actual
finite sets; no cumulative counting conclusion is assumed. 

### `live`

 Clauses introduced by the trace that are still alive. Root clauses start
untracked; survival is tested against the actual next formula. 

### `live_has_origin`

 Every tracked clause has a genuine earlier insertion event. 

### `insertions`

 Cumulative individual insertion events, including clauses later removed. 

### `removed_has_later_subset`

 The absorbing subset is inserted strictly after the removed clause's
original insertion event, even though absorption and subset insertion share
the same replacement step. 

### `charge`

 Fix exactly one absorbing new clause for each removal event. This finite
witness selection is used only for counting, never as a SAT truth oracle. 

### `charge_fiber_bound`

 One inserted clause receives at most the per-literal degree bound in
charges from removed clauses of any fixed width. 

### `accounting_step`

 The one-step conservation law for insertion events. 

### `accounting`

 Telescoping counts insertions by their fate: still live or removed once.
This remains valid even without a no-reinsertion theorem. 

### `insertion_bound`

 The cumulative charging bound over an explicit finite trace. 

### `insertion_bound_two_n`

 Equation (A.1), with a literal universe of size at most `2*n`. 

### `descendant`

 Repeated replacement always leaves a live descendant of every old clause. 

### `removed_never_returns`

 A removed clause cannot return to a later antichain: its strict descendant
persists and would absorb it. 

### `degree_bound`

 Derive the degree premise of the charging theorem from actual batches and
the minimum-width pre-insertion bounds, using `InsertionInvariant`. 

### `insertion_bound_of_minimum_width`

 The cumulative bound with the per-state invariant discharged by the
one-per-literal and minimum-width properties of the branching trace. 

### `replacement_history_antichain`

 Antichains are maintained by actual `SAT.absorb` replacements. 

### `ofReplacements`

 Build the charging trace from literal-set replacement followed by actual
absorption. Freshness, survival, and strict-subset removal witnesses are proved,
not postulated, using `SunflowerBranch`'s finite-set lemmas. 

### `replacement_removed_never_returns`

 No-reinsertion for the concrete absorption histories used by the count. 

### `SunflowerStep`

 An actual choice of one of the two literal-set sunflower children, recording
the inserted batch and the selected width. 

### `ofSunflowerSteps`

 A path of actual sunflower choices automatically supplies every local
set-theoretic hypothesis of the charging trace. 

### `literalUniverse`

 An explicit finite universe containing the two signs of every variable. 

### `insertion_bound_cnf`

 Equation (A.1) for actual signed SAT literals, with no abstract universe
or final-live-count premise remaining. 

### `insertion_bound_cnf_of_replacements`

 The cumulative insertion bound for a finite sequence of actual
`SAT.absorb` replacements. The remaining local hypotheses are exactly the
batch and minimum-width properties supplied by sunflower branching. 

### `insertion_bound_sunflower_path`

 Equation (A.1) for a genuine finite minimum-width sunflower path. All
capacity, survivor-count, freshness, and absorption premises have been proved
from the path, rather than included in the conclusion's hypotheses. 

### `thresholdDegreeBound_eq_L`

 The threshold formula agrees with the recursive constants at every
positive width. Width zero is treated separately by `insertions_zero`. 

### `sunflower_path_cumulative_bound`

 Actual sunflower paths satisfy the cumulative insertion recurrence for
the concrete constants chosen in Appendix A.3. 

### `sunflower_path_depth_bound`

 Every branch inserts at least one smaller clause, so the cumulative
insertion budget bounds the number of branching steps on an actual path. 

### `BChoicesAtWidth`

 Count the B-choices whose selected branching width is exactly `w`. 

### `B_choices_width_insertion_budget`

 Each width-`w` B-choice accounts for a full threshold-sized batch among
all insertions below width `w`. 

### `sunflower_path_B_choices_bound`

 The integral B-choice bound for an actual path. Grouping by selected
width makes all per-width insertion charges disjoint as choice events. 

### `sunflower_path_budgets`

 Combined finite-path interface for the deterministic sparsification tree. 
