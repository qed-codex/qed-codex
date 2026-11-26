---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterHistory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterHistory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterHistory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Lifting a per-call memory invariant through a native RAM history

Consecutive post-assembly items occupy consecutive absolute cursor values.
A successful item transfers the real external memory (including its reads
and writes) to the next item. Matching rejection and success at each step
therefore gives matching rejection and success for the whole scheduled fold.


### `Ordered`

 Each item in the list has absolute cursor equal to its list index plus the starting offset. 

### `ordered_after`

 Identify all cursor values after a fixed list of preceding calls. 

### `Match`

 Simultaneous rejection, or two successful computations related by their
results. 

### `Step`

 A single-call proof supplies both directions of execution, the next
persistent control, the per-call probe bound, and the invariant on real
post-memory. 

### `fold_run`

 Match the entire parser fold with the genuine successive-call interpreter,
including exact cursor, memory, report length and individual probe bounds. 

### `within`

 Convert individual probe bounds and exact report length into the global
and per-call transcript caps. 
