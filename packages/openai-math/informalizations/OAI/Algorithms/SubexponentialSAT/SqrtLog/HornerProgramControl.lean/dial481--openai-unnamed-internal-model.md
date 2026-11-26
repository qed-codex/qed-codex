---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HornerProgramControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HornerProgramControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HornerProgramControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed native streaming Horner control for arbitrary-width coefficient
representations. Arithmetic callbacks are finite commands with exact framed
traces. No loop bound or ring dimension occurs in the control table. 

### `takeCoefficient`

 Read one reversed coefficient cell from the reversed polynomial stream. 

### `iteration`

 240 accumulator; 246 stream; 247 point; 248 counter; 250 width.
241,244,245,251,252 are restored empty; all other stacks are framed. 
