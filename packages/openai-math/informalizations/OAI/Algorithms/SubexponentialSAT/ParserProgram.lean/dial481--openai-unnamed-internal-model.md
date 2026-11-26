---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ParserProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ParserProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ParserProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-control parsers for the canonical formula encoding

These programs operate on two Boolean stacks and two Boolean registers.
Stack 0 is input; stack 1 accumulates output. Register 0 holds the last data
bit and register 1 records whether the last pop succeeded. Thus register 1
is true on successful delimiter termination and false on malformed input.
All stated running times count actual `BitProgram.step` transitions.


### `natProgram`

 Five fixed labels suffice to decode an arbitrary unary natural field. 

### `nat_trace`

 The count is data on stack 1, rather than an input-dependent control state. 

### `nat_empty_reject`

 An incomplete natural field is detected, rather than accepted as zero. 

### `frameProgram`

 Seven fixed labels read escaped frames of arbitrary length. The payload
is reversed on the destination stack; a stack-transfer routine restores order. 

### `frame_trace`

 Exact measured execution of the actual parser, preserving the unused suffix. 

### `formula_header_trace`

 The formula's declared coordinate count is parsed by the same fixed program. 

### `frame_decoding_agreement`

 Frame parsing agrees with the project's pure decoder; this pairs the
syntax equality with an actual bounded execution certificate. 

### `nat_input_shape`

 A successful pure natural-field parse characterizes the consumed prefix. 

### `frame_input_shape`

 Successful frame parsing also identifies the exact consumed prefix. 

### `nat_trace_of_read`

 Actual execution agrees with every successful result of the pure decoder,
not just inputs presented syntactically as encoded values. 

 ## In-place removal of one escape frame 

### `restoreProgram`

 Move the reversed payload back onto the input stack. 

### `unframeProgram`

 Eleven fixed labels implement one complete in-place frame removal. 

### `unframe_trace`

 The linked finite table restores forward order and clears its scratch stack. 

### `unframe_complete_trace`

 The in-place decoder is a complete program on actual raw input, with
canonical output on its designated stack and every register/scratch stack clear. 

 The compiler turns the preceding actual instruction traces into actual
primitive tape executions. Each overhead below belongs to one fixed program. 

### `unframe_primitive_execution`

 A complete primitive-tape execution from the actual raw input tape. 
