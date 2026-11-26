---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CounterLoops.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CounterLoops.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CounterLoops.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual binary counted loops whose invariant couples the current cursor to
remaining fuel. The invariant is transferred through the concrete decrement
and zero test, rather than through arbitrary changes to controller words. 

### `visits_exists_next`

 A measured callback can establish the next boundary invariant directly.
It is required only while the actual remaining counter value is positive. 

### `for_correct_measured_next`

 The initial test is explicit. No hypothesis allows changing the counter
arbitrarily, so cursor/fuel relations and terminal width exceptions survive. 

### `visits_stack_bound_next`

 Actual prefix space for the indexed invariant. The callback proves its
next boundary invariant through the concrete decrement, while every local
callback/controller prefix is bounded independently of numeric fuel. 
