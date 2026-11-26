---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HornerProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HornerProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HornerProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact native evaluation of a dynamically sized dense polynomial. Input
coefficients are in increasing degree order. Every other persistent stack is
preserved; the input stream and runtime counter are consumed. 

### `command_run`

 This is a concrete finite-command execution statement, not an arithmetic
oracle. Its only component premises are exact execution contracts for the two
fixed native binary services. 

### `program_run`

 Compilation gives an actual fixed BitProgram with one final halt step. 
