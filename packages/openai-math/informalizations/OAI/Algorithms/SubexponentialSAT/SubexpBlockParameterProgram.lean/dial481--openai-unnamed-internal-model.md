---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpBlockParameterProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpBlockParameterProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpBlockParameterProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual block-size and block-threshold arithmetic

The three input words contain `s`, `delta`, and `Q`.  The width `k` is part
of the fixed code.  Seven high stacks are a reusable empty work bank; the
fifteen low stacks retain inputs, constants, and computed intermediate words.
Every arithmetic operation below invokes a proved finite Boolean program.


### `command`

 The code depends on the fixed clause width, and not on any input number. 

### `powerBound`

 A polynomial bound in the numerical exponent and the actual input widths. 

### `Output`

 The returned low-word file records the actual words produced by the code.
No canonical-padding convention is required. 

### `length_estimates`

 Pure length arithmetic is checked independently of the execution witnesses. 

### `command_eval`

 Closed execution of the block-parameter stage, including constant loading,
exponentiation, and all threshold products. 

### `run_value`

 The same stage as a concrete finite instruction trace. 

### `primitive_execution`

 The fixed compiler also realizes this multiword stage on a primitive tape.
Its input configuration is explicit so a caller can retain a larger frame. 
