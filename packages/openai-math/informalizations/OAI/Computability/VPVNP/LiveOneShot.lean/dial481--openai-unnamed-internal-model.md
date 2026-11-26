---
{
  "module": "OAI/Computability/VPVNP/LiveOneShot.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveOneShot.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveOneShot.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Closing a single-call stage of the live program

The descriptor initializer ends by returning a word. At its stage boundary
this is a normal accepting exit that lets the linker select the next stage.
The instruction trace, bit consumption, memory probes, and required fuel
agree with the original call.


### `oneShot`

 Close the returning exits of a single-call native template so the enclosing linker can
advance after its first call. 

### `execute_oneShot`

 Executing the closed table changes every successful return to acceptance. 
