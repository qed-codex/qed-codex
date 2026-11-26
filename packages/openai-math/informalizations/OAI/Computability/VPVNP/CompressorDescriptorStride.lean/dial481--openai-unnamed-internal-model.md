---
{
  "module": "OAI/Computability/VPVNP/CompressorDescriptorStride.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDescriptorStride.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDescriptorStride.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bootstrapping the runtime descriptor stride

The calendar multiplies the selected level number by a word stored immediately
before its directory. This deterministic burst reads the three coordinate
counts produced in the cursor parameter frame, computes the level stride,
and writes that single word. Only the pair workspace pointer is public.


### `singleCode`

 Evaluate the recipe's expressions, store the first field alone, and return
the next cursor. This form is used for the single stride word between the
active parameter frame and the directory. 

### `singleTable`

 Instruction template that evaluates a recipe, writes its selected field once, and returns
the advanced cursor. 

### `singleReport`

 Report for a single-field recipe burst, including evaluation, the external write, and the
successor state. 

### `calculation`

 Only the first field is emitted by the single-cell store. 

### `table`

 Public operand two of the live pair is the workspace base. 

### `report`

 Report of the level-stride calculation using the pair workspace pointer in public operand
two. 

### `cost`

 Instruction count of the fixed program that computes and publishes the runtime level
stride. 

### `native`

 Run the actual Fin 11 bootstrap table. The input frame is the output
of `CursorRAM.ParametersInit.frame_ready`. No field of the directory itself
is required on entry. 
