---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticAccumulatePorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticAccumulatePorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticAccumulatePorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Operand and advice ports of the evaluator's multiply-and-add call

The two saved factors are copied onto private streams for the multiplication.
The resulting product then serves as the consumable operand of vector addition.
The original factors and the field advice remain available to the caller.


### `External`

 Caller ports for the two factors, the running accumulator, and the field parameters used to
add their product. 

### `Private`

 Private work ports for multiplication, addition, the two operand copies, and the temporary
stack used to copy them. 

### `Port`

 The full stack interface for adding a product to an extension-field accumulator. 

### `external`

 Populate the caller's field-advice ports, the two packed factors, and the packed
accumulator. 

### `workspace`

 At a call boundary all private stacks are empty. The intermediate frames
below name the two private streams that hold the copied operands and product. 

### `clean`

 Entry and return state with the caller's stacks installed and all multiplication workspace
empty. 

### `multiplyPorts`

 Connect the field multiplier to the private copies of the factors and the caller's field
advice. 

### `addPorts`

 Connect the coefficientwise adder to the private product stream and the caller's
accumulator. 

### `stage`

 Copy the saved left and returned right factors onto the two private multiplication stacks. 
