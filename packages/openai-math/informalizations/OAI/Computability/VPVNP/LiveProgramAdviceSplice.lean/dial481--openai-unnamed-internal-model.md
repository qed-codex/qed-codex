---
{
  "module": "OAI/Computability/VPVNP/LiveProgramAdviceSplice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramAdviceSplice.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramAdviceSplice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Returning native stages in the middle-group preparation

Every successful stage in this prefix transfers to another stage with
persistent cursor zero. Consecutive stage logs concatenate with their
actual external memory effects. The fixed frame initializer has one such
call, whose log includes the outer tag read and transfer write.


### `Returning`

 A verified deterministic prefix of a linked machine, including the
post-call cursor, memory image, and exact number of empty branch streams. 

### `returning_append`

 The memory seen by each suffix is exactly that returned by its predecessor. 

### `tagAddr`

 Word address of the outer stage tag used to splice a returning advice stage into the live
program. 

### `returning_frames`

 Execute the single frame-initialization call as stage 10 of the actual
live machine. The next dispatch sees stage 11 and the newly published operands. 
