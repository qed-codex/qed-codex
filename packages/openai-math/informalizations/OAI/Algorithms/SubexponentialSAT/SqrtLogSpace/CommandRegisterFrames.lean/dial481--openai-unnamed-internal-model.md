---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CommandRegisterFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CommandRegisterFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CommandRegisterFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Register frames derived from the actual finite instruction tables and
structured command syntax. These footprints describe code, not an assumed
semantic behavior of a callback. 

### `programWrites`

 All register destinations in a concrete finite instruction table. 

### `baseWrites`

 Base-command footprint uses the original concrete instruction for atoms. 

### `writes`

 Calls contribute their actual finite table; guards only read registers. 

### `eval_register_frame`

 Every actual execution preserves each register outside the static writes. 

### `relocate_writes`

 Relocation changes every destination by precisely the declared register map. 

### `compiled_writes`

 Compiling guards, sequencing and return jumps introduces no register writes. 

### `not_mem_clearProgram`

 These primitive loops can only write their explicit value/presence registers. 
