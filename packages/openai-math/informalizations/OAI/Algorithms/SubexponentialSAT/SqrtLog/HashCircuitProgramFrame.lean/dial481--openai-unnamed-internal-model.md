---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed caller framing for the native sparse-hash interpreter. Low ports
0--55 are reserved for arithmetic. Literal lookup uses 56--62, leaving the
clause, row and constant accumulators physically untouched. 

### `fetchLiteral_eval`

 A caller may keep arbitrary arithmetic data, source records and accumulators
outside the seven lookup stacks. The run includes the subroutine return. 

### `rowRegisters`

 The weighted record opener consumes50 and writes original clause bytes47
and reversed flat weight49. Ports41,59,60 are scratch shared with lookup. 

### `rowFrame_stack`

 All clause/row accumulator stacks are outside the opener's scratch set. 
