---
{
  "module": "OAI/Computability/VPVNP/CompressorPayloadWrite.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPayloadWrite.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPayloadWrite.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Writing the selected motif payload to descriptor memory

The incoming persistent word gives the base of a contiguous descriptor. The
admission block receives the prepared registers of the motif choice reader.
After admission, the write block copies every supply coordinate, in order,
from its retained register to an external memory word.


### `overlay`

 Replace a contiguous slice of external memory with the given words. 

### `writeSlots`

 The cursor and its increment use registers 0 and 1. Each coordinate costs
one external write and one cursor increment. The terminal copy provides a
continuation even for a motif with empty supply. 

### `writePayload`

 Instructions that take the descriptor base from persistent state and write every retained
supply coordinate to its slot. 

### `chooseAndStore`

 A single linked table admits a motif vector and writes it at the persistent
base address. 

### `writeEvents`

 Exact events of the write block, including the two setup instructions. 

### `Admitted`

 The arithmetic input contract of the admission reader. Zero repetitions
produce the unit descriptor, whose coordinates are all zero. 

### `payloadBits`

 Choice stream for the payload, empty on the forced branch and otherwise the ordered word
encoding of the supply vector. 

### `admissionSteps`

 Number of admission steps for the forced branch or the full word-by-word vector choice, as
selected by the prepared registers. 

### `chooseAndStore_execute`

 Exact execution of the linked admission and emission code. It hands the
next native instruction its original bit suffix and the updated external
memory. The probe count is exactly the number of supply coordinates. 

### `template_store_iff`

 Appending the writer preserves exactly the complete bit streams of the
standalone admission template. The additional budget is its exact native
step count. The assertion holds at every admission budget. 
