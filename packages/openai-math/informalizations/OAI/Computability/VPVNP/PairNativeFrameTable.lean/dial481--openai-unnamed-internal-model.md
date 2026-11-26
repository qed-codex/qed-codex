---
{
  "module": "OAI/Computability/VPVNP/PairNativeFrameTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeFrameTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeFrameTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Relocatable instruction rows for installing the terminal geometry frame

The arithmetic and its six external reads enter a chain of thirteen private
stores. The last two instructions hand the histogram base to the caller and
the cache base to the leaf's operand initializer.


### `fieldReg`

 Local source register for frame field `i`, with the twelve words occupying consecutive
registers 3 through 14. 

### `size`

 Number of instruction rows for a frame prelude and its 29-row installation tail. 

### `label`

 Program counter in the installation table corresponding to a label of the frame prelude. 

### `tail`

 Offset zero stores the frame pointer. Offsets 1 through 24 write the
twelve fields and advance the cursor. 

### `store`

 Address of the next field-store row, with index twelve denoting the histogram-pointer
handoff after all fields have been written. 

### `advance`

 Address of the unit cursor advance following frame field `i`, which transfers control to
the next store position. 

### `row`

 The caller supplies the continuation instruction at `tail 27`; the
rejecting flow exit is at `tail 28`. 
