---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorAdvicePackStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdvicePackStep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdvicePackStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packing the evaluator's advice bit banks

The initial cursor of each output row writes zero to the destination word.
Each of its remaining cursors installs one low-endian bit if that bit lies
in the actual raw advice. The padding cursors leave the partial final word
intact. Every call makes at most three probes.


### `PackCode`

 A native advice-packing flow with 32 registers and five public operands. 

### `stride`

 Number of cursor positions per packed row, including the initial clear and one position per
source bit. 

### `total`

 Number of advice-packing cursor positions across all destination rows. 

### `row`

 Recover the packed row number from a linear packing cursor. 

### `column`

 Recover the position within a packing row, with zero reserved for clearing its destination. 

### `index`

 The zero-based raw advice bit index corresponding to a bit-installation cursor. 

### `dst`

 The packed destination word address for the current row. 

### `src`

 The raw advice bit address for the current bit-installation cursor. 

### `packedValue`

 The specified native shift and OR of the bit read and the accumulated destination. 

### `stepMemory`

 The memory effect of one packing cursor, clearing a new row, installing an in-range bit, or
skipping padding. 

### `stepBody`

 Public words in order are source bit base, destination word base, field
width, actual source length and number of destination rows. 

### `stepTable`

 The native call template implementing one advice-packing cursor step. 

### `stepEvents`

 The local ticks and probes of a packing step, selected by the row-clear, in-range bit, or
padding case. 

### `stepReport`

 The packing step's events and return state, closing at the end of the last row. 

### `step_exec`

 Every valid cursor produces the specified trace and final memory, with
the next cursor and total in the common closing registers. 

### `callFuel`

 At most 28 body instructions and two closing instructions. 

### `execute_step`

 Native execution rejects surplus choice bits. Every valid cursor with a
canonical source bit returns its single deterministic report. 

### `step_required`

 The source-range test is imposed only for data columns that read a real bit.
An invalid cursor or a nonbinary word read from that interval cannot exit. 

### `execute_step_iff`

 Exact successful reports on arbitrary raw memory and arbitrary choices,
including rejection of nonbinary source words and out-of-range cursors. 

### `stageBody`

 The linkable stage treats an empty bank as one accepting call at cursor zero. 

### `stageTable`

 The native advice-packing stage template, including the test for a zero row count. 

### `stageFuel`

 The 33-step private clock bound for a native advice-packing stage call. 

### `stageReport`

 Native report with the row-count test included in the event stream. 

### `execute_stage_iff`

 The linkable stage also checks the empty bank's initial cursor, and
rejects every surplus branch bit in both branches. 
