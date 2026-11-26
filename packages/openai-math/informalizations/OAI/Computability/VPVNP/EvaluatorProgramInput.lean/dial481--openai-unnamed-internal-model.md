---
{
  "module": "OAI/Computability/VPVNP/EvaluatorProgramInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorProgramInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorProgramInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native input conversion and the finite-algebra evaluator

The row converter receives the binary exponent array in its native ascending,
little-endian order. Its digit output is the scheduler's table stack. This
allows traversal to start directly at column zero while preserving the
divisor, the unary width, and the callback's state.


### `Port`

 The packed binary input and its size counters, the division registers and the digit
scheduler's ports. 

### `radixPort`

 The radix converter writes its output directly onto the scheduler table. 

### `extend`

 Framing a scheduler bank retains the original divisor and row width.
All private conversion scratch is empty. 

### `initial`

 Place the binary exponent vector and dimensions on the input stacks. The
callback payload can contain its advice and its initial arithmetic registers. 

### `convert`

 The conversion code is independent of both runtime dimensions and the divisor. 

### `convertTicks`

 Instruction count for moving the binary exponent array to the converter and running its
radix-row routine. 

### `convert_runs`

 The packed table and the initial loop counters reach the scheduler together. 

### `run`

 Run a scheduler from the native exponent input. The state space of the
linked routine depends only on the fixed converter and scheduler programs. 

### `run_realizes`

 Any proved scheduler semantics now applies to the ascending binary input
array, with the exact verified radix conversion time added to the clock. 
