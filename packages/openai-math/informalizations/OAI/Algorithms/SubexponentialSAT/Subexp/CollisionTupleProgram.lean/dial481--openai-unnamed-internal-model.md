---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/CollisionTupleProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/CollisionTupleProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/CollisionTupleProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Streaming collisions from framed runtime tuples

The current word array and selected read plans are preserved. Each parsed
tuple is appended to the current array by actual transfer/copy routines, then
the fixed collision callback gathers the two types and emits one bit.


### `state`

 Parser flags are false/true/false during a callback. All low registers are
scratch of the collision program. 

### `validPayload`

 This schema only describes the serialized tuple's row widths and the
validity of the two numeric plans. It places no condition on the answer bit. 

### `command_eval`

 Every framed tuple is parsed and processed by the fixed callback. The
result is the reverse visit-order leaf stream, suitable for unary tallying. 
