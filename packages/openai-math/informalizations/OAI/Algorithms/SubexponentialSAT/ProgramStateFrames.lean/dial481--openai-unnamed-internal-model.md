---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ProgramStateFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ProgramStateFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ProgramStateFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Reusable data projection and framing for genuine finite subroutine calls.
The projection/embedding functions specify states; executable code uses only
the fixed instruction-port relocation already proved by ProgramLinking. 

### `eval_call_from_state`

 A complete local run can be called directly from an arbitrary caller state. 

### `embedState_update_stack`

 One stack update in the local result becomes the same update at its
assigned caller port. This is an equality of state descriptions. 

### `liftCommand`

 Lift any fixed structured command by compiling and calling its finite
instruction table. The extra source instruction is its final return. 

### `Eval.final_unique`

 Different finite execution derivations of the same structured command
must have the same final data. The existing source port supplies a concrete
compiled machine, and determinism is inherited from its actual transition. 
