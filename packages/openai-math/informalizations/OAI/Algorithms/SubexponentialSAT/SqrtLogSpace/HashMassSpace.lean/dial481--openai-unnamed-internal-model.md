---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashMassSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashMassSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashMassSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 All-prefix storage for the actual marked-record collector. The parser and
native addition have polynomial local work. Expensive marked queries supply
their own actual prefix bound; their total runtime is never used as workspace. 

### `state_stack_bound`

 All 896 words are charged, including the caller workspace and the unread
record tail. This also applies immediately after a query before its addition. 

### `loop_space`

 Actual record-loop executions have a common prefix cap. The accumulator
allowance is its initial word length plus the sum of per-record width growth. 

### `command_space`

 Initial parser setup and the actual final halt preserve the uniform cap.
This exposes a source stage for composition into the concrete mass attempt. 

### `collector_space`

 The actual compiled collector call inherits every prefix of its callee,
including the callee halt that is relocated to the caller's return jump. 

### `mass_halt_space`

 Reference generation, every marked query and addition, and final canonical
handoff all obey one bound. Only polynomial setup and finish costs occur in the
space expression; the expensive query contributes its independent prefix cap. 
