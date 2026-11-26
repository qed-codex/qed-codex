---
{
  "module": "OAI/Computability/VPVNP/PairShrinkHiddenCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native loop control for absorbed shrinking fields

The public row count and ordered ID array are read from external memory.
Each ID selects one fixed-stride private slot; only the term's actual bit
width is guessed and written. Registers 0–4 are the private field mover.


### `Control`

 Instruction labels for initializing the owner's scan, testing its remaining count,
addressing the current private slot, and advancing to the next dense ID. 

### `widthRegs`

 The term width reader's input pointer, term parameters, and outputs.
Its register six retains the actual dense hidden ID on completion. 

### `guessRegs`

 Embed the five registers of the private bit-guessing loop as registers 0 through 4 of the
absorbed-field scan. 

### `control`

 Emit the scan instruction at a control label, with supplied entry addresses for reading the
width, guessing the bits, and leaving the scan. 

### `ControlLinked`

 The machine contains each scan control instruction at its assigned program counter with the
given registers and jump targets. 

### `Args`

 Addresses and layout choices for one packed owner. The caller can
place the private slots at any base separated from its other scratch. 

### `Args.termBase`

 External word address of the first selected motif term record. 

### `Args.termStride`

 Distance in external words between the starts of consecutive motif term records. 

### `Args.layout`

 The surviving layout of the selected terms. The width reader uses the opposite layout for
  absorbed fields. 

### `Args.selectorBits`

 Number of selector bits contributed to a hidden field by each repetition of its term. 

### `Args.scratchBase`

 First private word address in the array of slots for guessed hidden fields. 

### `Args.slotStride`

 Distance in private words between slots for consecutive dense hidden-field IDs. 

### `Args.countBase`

 External base address of the table giving the number of hidden fields for each packed
  owner. 

### `Args.owner`

 Ordinal of the packed site whose count and ordered row of hidden-field IDs the scan
  reads. 

### `Args.rowBase`

 External address where the array of owners' ordered hidden-field ID rows begins. 

### `Args.rowStride`

 Distance in external words from one packed owner's ID row to the next. 

### `Args.row`

 Start address of this owner's external ID row, computed as the row base plus the owner
ordinal times the row stride. 

### `Args.slot`

 Start address of the private bit slot for a dense hidden-field ID, computed as the scratch
base plus the ID times the slot stride. 

### `Inputs`

 The ten designated input registers hold the term parameters, private slot geometry, owner
ordinal, and external count and row addresses required by the scan. 

### `Ready`

 The scan inputs are loaded, and registers 3 and 21 hold the constants one and zero for the
loop counter and guard. 

### `scratch`

 All modifications after the initial constant rows. 

### `Frame`

 The two configurations agree on every register outside the scan's embedded scratch
registers. 
