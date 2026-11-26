---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ArithmeticExpressionProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ArithmeticExpressionProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ArithmeticExpressionProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed arithmetic expressions, compiled below to actual finite bit programs.
The only varying semantic input is the natural number represented by the input word. 

### `slots`

 All work allocation is determined by the fixed expression tree. 

### `command`

 Compiling a call depends only on the fixed child syntax and port layout. 

### `primitive_correct`

 The primitive simulation factor depends on the fixed expression program,
never on the input word or its numeric value. 

### `raw_input_correct`

 No prepared input configuration is required: the sole raw binary input
word starts on the program's designated input stack, with empty work stacks. 
