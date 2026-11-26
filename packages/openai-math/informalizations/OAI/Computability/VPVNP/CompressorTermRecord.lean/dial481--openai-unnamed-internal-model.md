---
{
  "module": "OAI/Computability/VPVNP/CompressorTermRecord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTermRecord.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTermRecord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Constructing a motif term descriptor in external memory

A local demand record supplies the widths. A sequence of fixed native calls
writes the selected rounded-grid row and repetition count, followed by one
word per admitted supply coordinate. Every transition carries just the
previous return word and the post-call memory.


### `saveFlow`

 A returned row number or repetition word is stored in its descriptor cell.
The second public word is the cursor passed to the next native call. 

### `save`

 Run the native store that saves the incoming value at `target` and returns `next` for the
following call. 

### `saved`

 Exact four-event report of the single-cell save, including the return word for the next
call. 

### `headers`

 Read the actual demands, select and store the grid row, read the same
demand words for the repetition count, then store it next to the row. 

### `withHeaders`

 Generated descriptor headers use adjacent external words. 

### `run`

 Execute the five descriptor calls and keep their reports in order. The
payload call reads its own repetition word from the preceding record cell. 

### `recordMemory`

 The descriptor memory image contains precisely the two headers and the
selected integer vector. All other external addresses retain their input. 

### `recordMemory_fields`

 Read the physical fields of a term record. The layout is the rounded-grid
index, the repetition count, and then the outer supply coordinates in order. 

### `recordMemory_supply`

 The stored words read back as the original natural widths in every
admitted block. This is the integer readout needed by the supply-width pass. 

### `run_spec`

 The native term phase produces exactly one external-memory descriptor for
each stream admitted by the motif. The two headers, every payload word, all
five reports and the probe allowance are accounted for on each admitted path. 
