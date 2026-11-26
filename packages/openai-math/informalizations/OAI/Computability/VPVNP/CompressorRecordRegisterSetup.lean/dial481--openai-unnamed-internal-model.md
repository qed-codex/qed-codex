---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRegisterSetup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRegisterSetup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRegisterSetup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loading a finite family of operand expressions into live registers

The six input registers provide the five expression operands and the state operand.
Each expression is evaluated using the existing straight-line compiler in the same
scratch bank. Its result is copied to its own output register. All loads use the
current external memory. Neither memory changes and no branch bits are consumed.


### `scratchCount`

 Maximum number of temporary slots needed by any expression in the operand bank. 

### `regCount`

 Register count for the output bank, shared expression scratch, and one final fallback
register. 

### `output`

 The dedicated register holding the value of the expression at this index. 

### `scratch`

 Select a register after the outputs for an in-range scratch index, or the last register
otherwise. 

### `emit`

 Compile one operand expression into shared scratch and copy its value to its dedicated
output register. 

### `lines`

 Concatenate the expression evaluations and output copies in increasing operand-index order. 

### `instruction`

 Lower a recipe assignment to a private-machine instruction using the designated work
registers, input registers, and successor address. 

### `Linked`

 Every program address in the assignment list contains the specified lowered instruction
linked to the next address. 

### `execute_setup_trace`

 Execute the linked read-only setup on arbitrary live input registers. The static
code length bounds every probe and private step, independently of the field widths. 

### `execute_setup`

 Register and continuation postconditions of the native setup. 
