---
{
  "module": "OAI/Computability/VPVNP/PairSimulationAnchorDecode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationAnchorDecode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationAnchorDecode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native scan of the anchor's selector sequence

A vertex call reads selectors from the high end of the anchor wire and
writes each decoded ordinal in its original copy position. Its control
table is independent of the repetition count. The output cells may be on
either side of the input slice.


### `fieldRegs`

 The first six registers of the loop belong to the padded field reader. 

### `Program`

 Registers 6 and 7 are the descending output cursor and its lower bound.
Register 8 contains the fixed selector width. 

### `Program.xs`

 Selectors in the order tested by the lookup. 

### `Program.key`

 Public port of each selector's encoded tag. 

### `Program.name`

 Public port of the ordinal stored after a successful lookup. 

### `Program.reg`

 Nine registers for the reader, cursor pair and selector width. 

### `Program.pc`

 Control locations for the five outer loop instructions. 

### `Program.reader`

 Control locations of the padded bit-field reader. 

### `Program.label`

 Physical location of each instruction in the fixed lookup table. 

### `Program.done`

 Continuation after all selectors have been written. 

### `Program.bad`

 Failure continuation for an unused selector code. 

### `selector`

 Lookup flow for the field reader's raw tag. 

### `instruction`

 Test the cursor, prepare the descending field read, and store its ordinal. 

### `Linked`

 All links for the five outer rows, the padded reader and the fixed selector table. 

### `Ready`

 Input register and private slice invariant with n remaining copies. 

### `Frame`

 Only the designated scratch registers and output interval may change. 

### `Outcome`

 The partial scan either decoded all remaining positions, or hit a
particular unused selector code. 

### `visitCap`

 Native bound for the control, reading, decoding and store of one anchor copy. 

### `loop`

 The physical loop scans the remaining n slots. A successful suffix is
kept in its original positions while the lower-index slots are filled. 

### `native`

 Every decoded ordinal is available at dest+i when the complete anchor
sequence is valid. An unused code transfers control to the bad exit. The
cap also holds for a rejection partway through the scan. 

### `native_reject`

 An invalid sequence rejects the genuine interpreter on every branch
stream, for every amount of fuel. 
