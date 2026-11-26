---
{
  "module": "OAI/Computability/VPVNP/EvaluatorProgramRawInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorProgramRawInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorProgramRawInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Advice and exponent fields on a single binary input

The parser loads four header fields and the callback payload from the advice
prefix. The suffix carries the runtime exponent vector and three copies of
its unary width for the converter and the two scheduler counters. Scratch
ports start empty without consuming any input.


### `fields`

 The parser's ordered ports depend only on the fixed callback register list. 

### `advice`

 Advice contains the fixed binary divisor, the dimensions which depend
on the label system, and the specified callback registers. 

### `runtime`

 The runtime input depends only on the width and the native exponent array. 

### `rawInput_eq`

 The advice bytes are independent of both the exponent values and their width. 

### `readTicks`

 The clock for loading the self-delimiting input fields, charging three instructions per
payload bit and one for each field terminator. 

### `readTicks_le`

 Each encoded data bit and field terminator costs at most two parser steps. 

### `withReader`

 Load the advice and exponents before calling the fixed physical machine. 
