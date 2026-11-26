---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsController.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsController.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsController.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native controller for the compressor's directory of stages

Each directory row contains a worker tag, initial and exclusive final cursors,
and a padded bank of public operands. The controller snapshots the row before
writing the active frame. Its five public words are the frame base, directory
base, ordinal cell, row-count cell, and dispatch-tag cell.


### `PCs`

 Number of controller instruction addresses, including six load-and-store instructions for
each of the stop word and padded operand slots. 

### `Regs`

 Number of controller registers, including a snapshot register for the stop word and each
padded public operand. 

### `table`

 The program size depends only on the largest arity among the fixed worker tables. 

### `machine`

 The directory controller instantiated at the live word width with its five public workspace
addresses. 

### `rowBase`

 Modular address arithmetic of the native program. 

### `field`

 Read a directory or frame field at a word offset from the given source address. 

### `doneReport`

 The terminating controller report after reading the current ordinal and directory row
count. 

### `rowReport`

 Full transcript including the snapshot of the stop word and all padded operands. 

### `execute_row`

 The complete native directory-row call, at any sufficient cap and for any proposed stream. 

### `execute_done`

 An exhausted directory accepts immediately after reading the ordinal and row count. 

### `frameMemory`

 The memory after copying the selected row's exclusive stop and padded operands into the
active worker frame. 

### `after_row_outside`

 A worker-data word, a future directory word, or the row count is preserved when
it lies outside the frame and the two mutable control cells. 

### `after_row_frame`

 The first frame word is the exclusive stop. The remaining words are the
worker's padded parameter bank. All field values refer to the entry memory. 

### `rowBase_val`

 A directory fitting in the physical address space uses the ordinary row-major index. 

### `after_row_ordinal_val`

 When a row is present, advancing its ordinal never wraps around. 

### `execute_cap`

 For every cap, the controller succeeds exactly when the complete
deterministic transcript and its terminal instruction fit in that cap. 
