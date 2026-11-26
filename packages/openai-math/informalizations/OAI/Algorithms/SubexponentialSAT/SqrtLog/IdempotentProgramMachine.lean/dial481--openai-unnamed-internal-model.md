---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramMachine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed four-array Newton machine. Its native services perform full dynamic
vector arithmetic, operand copying, and target replacement. 

### `arithmeticService`

 This instruction dispatcher is fixed, independent of every ring parameter. 

### `arithmeticBudget`

 All scans, scalar operations, register copies, and call halts are included. 

### `registerArrayStep`

 One fully measured register update, ready to instantiate with either
native arithmetic service. All source ports may coincide with the target. 

### `newtonMachine_exact`

 No native arithmetic hypothesis remains in this theorem. The input carries
its cached table, constants, dimension/width data, and starting arrays. 

### `arithmeticBudget_polynomial`

 A fixed polynomial bound for one complete register operation. 
