---
{
  "module": "OAI/Computability/VPVNP/EvaluatorInputBank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorInputBank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorInputBank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loading evaluator advice and exponents from a binary input

Each fixed port receives a separate field. A zero tag ends the field and a one
tag precedes a payload bit. Sending payloads in reverse order puts the original
lists on their stacks with one push per bit. The parser's finite control is
fixed by the ordered port names, independently of field lengths.


### `fieldBits`

 A self-delimiting raw input field. 

### `Phase`

 Finite control for reading tagged input fields and pushing each payload bit onto its named
stack. 

### `readField`

 Port `none` contains the raw input. All output ports have the form
`some k`, so reading a field never overwrites an unread input bit. 

### `frame`

 Place the raw stream on the input stack and a bank on the output stacks. 

### `readField_runs`

 Reading one field consumes its terminator and leaves the next field at
the top of the input. It uses three instructions per bit and one for the tag. 

### `reader`

 The ordered fields are fixed when the input parser is compiled. 

### `rawInput`

 Raw binary serialization of the selected ports, in their specified order. 

### `load_input_runs`

 From the raw input alone, restore the complete named evaluator bank.
Advice fields and runtime exponent fields have independent data and lengths. 

### `load_selected_runs`

 Initially empty scratch stacks need no fields in the raw stream. 

### `rawInput_append`

 Encoding the advice block and the exponent block separately concatenates
their raw streams; changing an exponent does not change any advice field. 
