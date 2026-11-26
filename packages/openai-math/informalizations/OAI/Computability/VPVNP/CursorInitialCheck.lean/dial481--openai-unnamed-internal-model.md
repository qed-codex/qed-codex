---
{
  "module": "OAI/Computability/VPVNP/CursorInitialCheck.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorInitialCheck.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorInitialCheck.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing an initial cursor vertex

The checker receives four contiguous bit vectors, the two outgoing and the
two incoming fields of its own vertex. It executes the local route tests
and runs the private site validator only at cursor zero. Its accepted bit
strings are exactly the initial choices used in the monomial path sum.


### `Buffers`

 Four contiguous vectors of arc bits, addressed within one vertex. 

### `readBuffer`

 Read one routing operand at its precomputed field offset. 

### `halfBuffers`

 Serialize the four independent half-wire vectors supplied at a vertex. 

### `incidentBuffer`

 Decode the validator input by addressing the selected arc at each
successor or sorting slot. 

### `initialAccept`

 Boolean acceptance on independently supplied half-wire indices. A valid
transit vertex consumes no private bits. 

### `initialAcceptEquiv`

 Acceptance on the serialized local buffers preserves the original
private path itself. It gives the singleton empty string at a valid transit
vertex and no strings at vertices failing a route or clamp check. 
