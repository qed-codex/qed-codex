---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationEmitProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationEmitProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationEmitProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Native emission of the positive part of a shifted coefficient array.
The dimensions and the singleton support mask are runtime data. The constant
cell is consumed without emission; all later cells are framed, including zero
coefficients. No normalization or arithmetic oracle is used. 

### `keyMap`

 Swapping the key helper's mask port protects the caller's beta on220. 

### `readCoefficient`

 Take one forward fixed-width cell and reverse it for the framed emitter. 

### `step_run`

 Each iteration consumes one actual coefficient and restores all temporary
cells except the incremented unary exponent; beta and all other masters stay. 

### `emitted`

 Exact order of the raw native accumulator: later degrees are prepended.
This deliberately retains zero coefficients; normalization is a separate job. 

### `dropConstant`

 The first cell is the node value, not a positive-Z coefficient. 

### `command_run`

 Complete fixed-control array-to-dictionary producer. All scratch and the
consumed source are cleared; every other input stack is literally preserved. 

### `entries`

 Exact mathematical record list, before the native prepend reversal. 

### `full_array_output`

 The runtime loop emits exactly the previously specified positive-Z list,
with only the documented prepend reversal. It never emits the constant cell. 

### `coefficientArray_run`

 Closed typed producer contract for the exact input/output array ABI. 

### `compiled_budget_polynomial`

 Uniform bit-program transition bound, including the compiled return instruction. 
