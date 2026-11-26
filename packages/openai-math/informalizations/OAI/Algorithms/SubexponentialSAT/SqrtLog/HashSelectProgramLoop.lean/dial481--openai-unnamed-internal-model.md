---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed unary-counter controller for K greedy rounds. The round command
must supply a paid actual execution; the counter is runtime stack data. 

### `RoundSpec`

 Invariance under the actual counter read and the paid round execution.
This is an integration contract, not an existence claim for the round code. 

### `iter_hash_run`

 The runtime controller's recurrence agrees with the semantic hash loop. 

### `BoundedRoundSpec`

 A bounded variant lets the callback cost depend on a certified maximum
number of rows. The bound is used only at iterations that actually run. 
