---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorGuard.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorGuard.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorGuard.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rejecting malformed successor fields

The field reader produces separate validity bits for the send and receive.
The guard consumes those bits, continues only when both are true, and
otherwise halts with rejection. This instruction table can be linked directly
to the processor's call loop.


### `GuardState`

 States for testing the send and receive verdicts and halting on a failed test. 

### `guard`

 Consume the send verdict followed by the receive verdict, continuing only if both are
present and true. 

### `checked`

 Read the two successor fields and then guard the continuation with both validity bits. 

### `guardResult`

 Pop the send and receive verdict stacks after a successful guard. 

### `checked_allStops_of_read`

 The third guard instruction suffices even when the second validity bit
is false and the explicit rejecting halt must still execute. 
