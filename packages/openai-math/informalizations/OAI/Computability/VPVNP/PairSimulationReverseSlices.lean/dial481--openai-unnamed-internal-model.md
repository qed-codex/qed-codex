---
{
  "module": "OAI/Computability/VPVNP/PairSimulationReverseSlices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationReverseSlices.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationReverseSlices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading a subdivision slice from the new supply field

The frame stores the old-field offset first and the new-field offset second.
Recovering an old argument from a surviving supply field copies in the
opposite direction. The header reads the same three addresses in the same
order, then enters the ordinary private copy loop with the new field as source.


### `instruction`

 Exchange the two offset-add instructions. Register 0 is still the
private source cursor and register 2 the private destination cursor. 

### `Linked`

 The eleven assigned instructions implement reverse frame setup, adding the new offset to
the source and the old offset to the destination before copying a nonempty slice. 

### `FrameResult`

 The exact continuation of a slice copy in either direction. 

### `execute_stored_frame`

 Use only the three words of the resident frame. The first offset belongs
to the old field and the second to the new one. The selected direction determines
which is used as the private source offset. Empty frames need only their length. 

### `oriented_frame_words`

 Convert the three consecutive natural addresses of a fitted frame to native word
addresses. Empty records need no offset equalities. 

### `execute_frame`

 Reverse a completed source-major frame, copying from its new private field
back into its old private field at the recorded offset. 
