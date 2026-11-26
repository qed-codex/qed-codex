---
{
  "module": "OAI/Computability/VPVNP/CompressorSelectedPayloadReadback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSelectedPayloadReadback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSelectedPayloadReadback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading selected role-specific payloads and successor pitches

The actual scheduled pass determines the type of its selected term.
A shrinking stage always has a successor pass, whose metadata publisher
writes the pitch needed to decode the new-state party operands.


### `Shrinking`

 Type of predicates relating a selected shrinking term, its tape, and memory at a specified
history level. 

### `Refreshing`

 Type of predicates relating a selected dyadic refresh term, its tape, and memory at a
specified history level. 

### `byOrigin`

 Dispatch the payload predicate on the pass's typed origin. The
constructor exposes the native choice and input state to the producer. 

### `Past.read_field`

 Read any field of an older selected level from its actual published
source record, even if the same level value occurs at multiple ordinals. 

### `shrink_successor_stride`

 The shrink's output-state pitch is read from the next actual pass's
native metadata packet, including across the final shrink of each block. 
