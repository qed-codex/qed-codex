---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingNodeProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingNodeProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingNodeProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed physical program generating all nonzero radix nodes up to a runtime
bound. The bound counts down, so prepending each row gives ascending order. 

### `digits`

 Canonical padded radix digits, least significant coefficient first. 

### `stream`

 Nodes 1 through Q in order. This is a specification, not an instruction. 

### `ports`

 Only the remaining counter and its scratch are used by this controller. 

### `stepBudget`

 One node extraction including binary decrement and the next loop test. 

### `budget`

 Explicit bit-program instruction budget, before the fixed primitive overhead. 

### `command_eval`

 No node table is an input: runtime Q, arity, and a padded positive radix
suffice to physically produce every node record. 
