---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleRefinement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleRefinement.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleRefinement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual state refinements for the fixed attained-signature controller.
Each lemma follows concrete commands already installed in the native ABI. 

### `descend_leaf_eval`

 The last fresh representative reaches an actual leaf only after its
cursor is saved and all eight current-head tapes have been cleared. 

### `probe_endpoint_bound`

 The complete probe restores the same fixed boundary cap. Its larger
transient prefix bound is not fed back into the next iteration. 

### `advance_endpoint_bound`

 Counter advancement and key disposal also restore the original boundary
cap, including the terminal candidate whose word has one extra bit. 

### `probe_advance_ready`

 Scanner scratch is restored by each probe and is disjoint from both
binary counters. Thus advancing never requires a new allocation or scan. 

### `advance_scan_storage`

 A completed candidate is advanced once. Its full key is discarded, while
both attained-prefix frame banks and the physical head address survive. 

### `rootAscend_eval`

 An exhausted root, including return from the sole empty tuple, clears
its current arrays and halts without attempting to pop a missing frame. 

### `descend_current_bound`

 Recording a representative grows only the two persistent frame banks.
The tapes cleared on descent remain bounded by their original word cap. 

### `descend_leaf_stack_bound`

 Descent stores only one bounded representative and cursor. Its local
prefix bound counts all caller stacks and does not use the rescan's time. 

### `rootAscend_stack_bound`

 Root return has a polynomial local source-prefix bound, including every
caller stack. The number of earlier DFS leaves does not appear. 

### `setup_zero_eval`

 A zero-head instance enters the single empty-tuple callback; it does not
halt early or skip its neutral group product. 

### `checkedReturnState_stack`

 The presence test does not change any stack, and cleanup leaves both
persistent prefix banks intact. 

### `parent_return_prefix_eval`

 Restore the attained parent's saved bounded candidate and fuel without
rescanning any earlier candidate. The matrix reload follows this prefix. 

### `parent_return_ancestor_storage`

 The parent address and unary remaining-head word are reconstructed by
one paid ascent; no saved matrix or whole assignment table is retained. 

### `duplicate_iteration`

 A losing signature candidate executes the full native predicate and one
bounded advance. No matrix reload or fresh generator is invoked. 

### `descend_ancestor_storage`

 Current-head cleanup does not erase the newly attained child prefix or
its unary depth/address words. This also covers internal children. 

### `reset_scan_storage`

 Reset follows a real matrix load. It preserves the attained ancestor
frames and prepares exactly the first numeric assignment for this head. 

### `descend_internal_eval`

 Composition for an internal descent uses the supplied actual loader
evaluation, then the concrete power-of-two cursor initializer. 

### `descend_leaf_endpoint_bound`

 The larger transient descent bound is discharged at the next leaf
boundary using the global attained-prefix frame cap. 

### `fresh_leaf_iteration`

 A fresh signature at the final head executes the full actual rescan,
saves its attained representative, and reaches the cleaned visitor boundary. 

### `duplicate_run_space`

 One losing candidate has a joint actual run, polynomial all-stack
prefix bound, and the unchanged fixed boundary bound. The exponential
candidate value occurs only in the time estimate. 

### `fresh_leaf_run_space`

 The fresh final-head branch has the same uniform prefix cap as a losing
candidate: the rescan uses its own bound, while frame storage and cleanup
are charged by their polynomial local execution time. 

### `resume_loaded_storage`

 After the parent matrix reload, reset only the predecessor zero word
and advance the restored cursor once. Earlier candidates are not rescanned. 

### `parent_return_endpoint_bound`

 Restoring a suspended parent again fits the same global frame and word
cap before its matrix is reloaded. No transient cost is accumulated. 

### `ascend_loaded_run_space`

 A nonroot return composes the actual bounded frame restoration, actual
matrix reload evaluation, and one cursor advance. Its storage estimate uses
only this polynomial reload time, never the preceding traversal length. 

### `setup_loaded_run_space`

 Positive-depth setup reaches the first head through its actual loader
run and the fixed bounded-memory initializer. 

### `duplicate_stack_frame`

 A losing candidate changes only its two cursor words and the freshness
latch. In particular all accumulators, retained inputs, and caches survive. 
