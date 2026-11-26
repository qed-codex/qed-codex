---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationAssemblyRelOuter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationAssemblyRelOuter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationAssemblyRelOuter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Relational native table traversal. Each executed iteration supplies its
own payload witness; no byte family uniform over initial registers is assumed. 

### `literalRecordBound`

 Space for one framed original-variable ID and one bounded payload. 

### `RelLiteralBody`

 The payload is existential after the actual incoming registers, not before
all executions. The accumulator bound is the complete table's size bound. 

### `literalLoop_rel_visits`

 Every witness is chosen along this actual run. The capacity invariant
reserves room for all remaining records before invoking the bounded body. 

### `literalLoop_rel_run`

 Relational counted loop with an explicit actual-register execution. 

### `prepareFactor_rel_run`

 Full native table producer with actual-run witnesses, measured master copy,
loop, and output move. No payload family uniform over registers is required. 

### `prepareFactor_rel_lookup`

 Exact lookup-table serialization of the actual relational output. 
