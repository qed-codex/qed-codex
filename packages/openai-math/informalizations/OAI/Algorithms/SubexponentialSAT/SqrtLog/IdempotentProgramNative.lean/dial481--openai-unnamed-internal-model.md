---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed native Newton control, conditional only on explicitly supplied native
array-operation services. Each service hypothesis requires a real `Eval` of a
fixed finite command. The iteration count is stack data, not generated control.
This module does not claim that the array-service obligations are discharged. 

### `nativeNewtonLoop`

 This command's finite syntax is independent of `t` and of `clog 2 t`. 

### `nativeNewtonLoop_correct`

 Once the three array services and source-preserving register copies have
native proofs, all Newton iteration/control work is already a genuine native
trace with an explicit bit-counter overhead. 

### `nativeNewtonLoop_runs`

 Compiling the fixed loop adds one actual halt instruction. 

### `nativeNewtonLoop_exact`

 Strong form: the fixed native loop implements the exact functional array
state, not only its image under a semantic decoder. 
