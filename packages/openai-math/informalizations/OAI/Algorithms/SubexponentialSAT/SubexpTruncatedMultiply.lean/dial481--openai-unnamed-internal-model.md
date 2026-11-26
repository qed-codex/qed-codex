---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpTruncatedMultiply.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTruncatedMultiply.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTruncatedMultiply.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual fixed truncated-polynomial multiplication service. Its code
contains no size-dependent control or mathematical scalar callback. The
physical input layout supplies the stored modulus, reduction coefficients,
and scalar width; every coefficient operation is executed by the concrete
quartic service. 

### `command_value`

 This is an actual command execution contract. `BaseReady` describes the
stored arithmetic inputs and scratch cells, rather than assuming a scalar
result or a scalar runtime. 

### `program_value`

 The source program is fixed while D and the field data remain on its
stacks. The final halt is included in the displayed polynomial bound. 

### `primitive_value`

 The checked primitive compiler contributes one fixed multiplicative
constant, independent of the runtime dimensions and field parameters. 

### `result_correct`

 The exact encoded output of the preceding machine theorems denotes the
truncated polynomial product. 
