---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentInputProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentInputProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentInputProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical input construction for sequential type assignment

All parameters are unary stack data. The fixed program constructs the one-hot
word alphabet, reads its actual first word, derives its packed view, and builds
the exact seed range and dimensions expected by `AssignmentInitProgram`.


### `Writes`

 A physical stage changes one public stack and restores the private bank.
The witness is an actual measured execution of its finite instruction table. 

### `command_eval_measured`

 The complete fixed producer, including concrete record extraction and
range generation. The only semantic witness chooses names for the actual
emitted word bytes; it is not supplied to the executable program. 

### `extent`

 Explicit data-size envelope, including generated arrays. It is assertion
notation only; no bound or table is passed to the machine. 

### `sizeBound`

 A closed bound containing only runtime parameter values and input size. 
