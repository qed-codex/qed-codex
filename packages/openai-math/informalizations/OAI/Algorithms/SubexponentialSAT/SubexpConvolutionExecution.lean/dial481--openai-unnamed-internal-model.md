---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpConvolutionExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual finite-program execution of the padded triangular convolution.
The generic local pair contract is instantiated separately by the concrete
quartic multiplier and persistent-cell update service. 

### `convolutionBudget_quartic_le`

 The concrete pair service yields a fixed-degree polynomial in the
runtime array dimension and coefficient width, including the final halt. 

### `convolutionBudget_parameter_le`

 Polynomial parameter envelopes can be substituted directly into the
actual convolution budget; both growing dimensions remain explicit. 

### `command_run`

 The whole nested-loop command consumes the left input and row counter,
retains the right input and scalar frame, and writes the computed output. 

### `initialized_command_run`

 Specialization to an actual zero-initialized D-cell output array. 

### `compiled_command_run`

 The actual compiled finite table includes its final halt instruction. 

### `primitive_command_run`

 Primitive-machine execution is obtained from the verified compiler, with
its fixed per-program overhead displayed rather than treated as one step. 

### `callAt`

 Relocate the one fixed convolution program into a larger caller. 

### `callAt_run`

 The local run can be used from an arbitrary caller state. Its untouched
frame is retained by `embedState`; the subroutine return is charged. 
