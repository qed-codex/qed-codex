---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/ActivePlanProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ActivePlanProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ActivePlanProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing the active completion positions

A fixed program filters a runtime list of unary seed positions. It retains a
position precisely when it is at least the runtime threshold and belongs to
the runtime pair read plan. The plan and threshold are preserved. Applying the
program to the complete ascending seed list gives a duplicate-free completion
plan in ascending order.


### `member_eval`

 The membership phase copies the persistent pair plan, calls the existing
actual encoded-membership scanner, and clears every scan residual. 

### `compare_eval`

 The threshold comparison uses fresh copies and preserves both its unary
inputs, the membership answer, and the outer parser registers. 

### `command_eval`

 Complete execution of the fixed filter, including the order-restoring
pass. Its output is the encoded filtered list in the original input order. 

### `program_runsIn`

 Actual halted trace, with arbitrary runtime seed and plan lists. 

### `active_range_eq`

 Filtering the complete ascending seed enumeration is exactly filtering
the unprocessed suffix range; no sorting or deduplication is assumed. 

### `active_eq_remainingPlan`

 The runtime filter computes precisely the completion-support enumeration
used in the collision-leaf refinement. 

### `traceBound_quadratic`

 Quadratic in the total unary/encoded input size, with a fixed constant. 

### `inputStateThreshold`

 Raw counters are measured by length; their bit values are retained. 

### `program_runsIn_threshold`

 The actual program preserves an arbitrary raw threshold word and uses
only its length. In particular, a processed-counter prefix need not contain
canonical bit values. 
