---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CommandStackFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CommandStackFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CommandStackFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Stack frames derived from the actual finite instruction tables and
structured command syntax. These footprints describe code, not an assumed
semantic behavior of a callback. 

### `programWrites`

 All stack destinations in a concrete finite instruction table. 

### `baseWrites`

 Base-command footprint uses the original concrete instruction for atoms. 

### `writes`

 Calls contribute their actual finite table; guards only read registers. 

### `eval_stack_frame`

 Every actual execution preserves each stack outside the static writes. 

### `relocate_writes`

 Relocation changes every destination by precisely the declared stack map. 

### `compiled_writes`

 Compiling guards, sequencing and return jumps introduces no stack writes. 

### `not_mem_copyProgram`

 Copying temporarily pops its source, so all three ports are written. 
