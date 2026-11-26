---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CRTLocalProgramLoops.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CRTLocalProgramLoops.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CRTLocalProgramLoops.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed native loops used by independent-precision local Hermite CRT.

The arithmetic argument is a finite `Cmd`, never a semantic instruction.
`ServiceSpec` is the exact trace contract discharged by the native represented
ring/array callbacks. All iteration counts remain on runtime stack 246.


### `LowFrame`

 The shared arithmetic workspace is below the persistent CRT ports. 

### `ServiceSpec`

 Arithmetic consumes neither input. Its sole changed stack is output 244. 

### `replace`

 Replace a high persistent port by a preserving copy from another port. 
