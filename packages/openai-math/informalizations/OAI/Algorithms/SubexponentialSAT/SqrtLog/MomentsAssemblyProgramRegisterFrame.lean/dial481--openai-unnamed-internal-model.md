---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAssemblyProgramRegisterFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAssemblyProgramRegisterFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAssemblyProgramRegisterFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `command`

 The wide producer is the only component that can access registers16+.
The actual composition retains the caller's register frame whenever it does. 

### `dense_eval`

 Apply this to the same actual Eval witness used to compile the worker.
All caller registers16..23 (indeed16..39) are preserved. 

### `denseCommand_eval_framed`

 The concrete wide assembly and readout trace, with the register frame
required by the node worker. Compile this same Eval with compiled_halt_trace. 
