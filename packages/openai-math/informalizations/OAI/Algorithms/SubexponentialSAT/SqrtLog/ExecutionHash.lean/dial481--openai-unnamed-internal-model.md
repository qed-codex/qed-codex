---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/ExecutionHash.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ExecutionHash.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ExecutionHash.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The concrete native sparse-hash controller, including alphabet expansion,
unary control construction and candidate generation.  The remaining service
contract is an actual bit-machine evaluation of each candidate's mass; it is
not an arithmetic oracle or a unit-cost semantic callback. 

### `command_eval`

 All hypotheses about mass concern physical executions on reachable-size
matrices. The context frame only contains registers/stacks outside the fixed
setup layout, so a formula and ring context remain available to the service. 

### `decoded_result`

 The decoded returned matrix is exactly the semantic greedy run whenever
the paid mass service's bit scores have their specified numeric values. This
decoding is a correctness statement, not a free machine operation. 

### `primitive_run`

 Any proved execution of the complete command compiles to the same fixed
primitive machine. In particular, no varying alphabet size, P or K enters
the instruction table. 
