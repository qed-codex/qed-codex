---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/NativePackingBoundsTail.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/NativePackingBoundsTail.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/NativePackingBoundsTail.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounds for the actual packing tail

All sizes below come from the represented input and generated records.
There is no assumed runtime certificate: the cost estimates apply to the
same leftover and inverse budgets used by `PackingExecution.program_trace`.


### `type_word_length_le`

 Every type occurs in the actual generated type stream. 

### `context_snapshot`

 The initial leftover state is obtained from the proved extraction output. 

### `tail_budget_le`

 Both actual tail stages have a fixed fourth-degree bound in the vertex
count and the bytes of the generated type stream. 
