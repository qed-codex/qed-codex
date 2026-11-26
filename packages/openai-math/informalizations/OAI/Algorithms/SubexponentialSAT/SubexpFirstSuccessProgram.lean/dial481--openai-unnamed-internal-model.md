---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpFirstSuccessProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFirstSuccessProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFirstSuccessProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# First-success search by fixed finite control

The current label and remaining count are binary stacks. The callback is an
actual fixed structured command (in particular it may call a finite bit
program). A Boolean test used in correctness statements is never an instruction
or an argument of the executable program. The success bit is cleared on entry,
so even an empty interval has a defined negative result.


### `result`

 The result is read from the retained current word and the success bit. 

### `Visits`

 Actual callback entries and their actual instruction counts. 

### `Visits.stack_preserved`

 Callback payload stacks remain framed during both successful and failed
controller transitions. 

### `Visits.steps_le`

 Costs are the sum of the actual callback counts plus a bound on the
binary controller. No global assumption about callback cost occurs here. 

### `Visits.costs_le_of_invariant`

 A uniform callback bound is needed only on invariant states actually
visited, and applies to the recorded cost list of those executions. 

### `BodyContract`

 A correctness contract supplies concrete body executions only on the
invariant states reached by the client. The executable program has no `test`
or `P` argument. 

### `visits_exists_guarded`

 Exact scan semantics, including the count and order of actual callbacks. 

### `visits_exists`

 Compatibility form for invariants stable under every controller advance. 

### `search_correct`

 The first successful binary label is retained. An exhausted interval
returns `none`, even when the incoming success register is dirty. 

### `search_measured`

 A whole-search instruction bound charges the measured callback costs.
The bound therefore remains useful for bodies bounded only on their reachable
invariant states. 

### `search_empty`

 No body execution is needed for an empty input interval, and clearing
the result flag makes its negative outcome independent of incoming registers. 
