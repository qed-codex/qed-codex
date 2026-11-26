---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpEnumerationSchedule.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpEnumerationSchedule.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpEnumerationSchedule.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Indexed cost schedules for actual interval enumeration

The loop invariant is asserted at loop entries. In particular, a callback may
extend an accumulator for the current index before the controller increments
that index: the invariant need only hold again after that increment. Callback
termination and cost are required only on invariant states with positive fuel.
The conclusions are actual executions of the existing fixed finite program.


### `BodyStep`

 Local callback obligation for an indexed loop. Every witness contains an
actual callback execution, exact preservation of the reserved counters, and
the invariant at the next loop entry. No claim about arbitrary states is used. 

### `loopBudget`

 Sum of the index-dependent callback bounds and every controller step. 

### `loopBudget_le`

 A constant allowance is needed only on the visited interval. Values of the
cost function outside that interval do not affect the execution bound. 

### `visits_bounded`

 The exact consecutive-index traversal exists under a loop-entry invariant.
All callback costs are summed individually, not maximized over arbitrary data. 

### `enumerate_bounded`

 Full enumerator bound, including the initial zero test. The entry invariant
is required at the actual post-test state, so the test may change flag bits. 

### `programBudget`

 Instruction count including the initial test and final halt. 

### `program_runsIn`

 The scheduled bound applies to the actual fixed instruction table. 

### `program_primitive_runsIn`

 The same actual run is simulated by the checked primitive compiler.
The overhead depends only on the fixed program, never on the input values. 
