---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorRAMScheduleData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMScheduleData.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMScheduleData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scheduled cell operands in the actual live configuration memory

The noninitial call numbers enumerate first the old cells of tape one and
then the old cells of tape two. Reconstructing the private registers from
each call number supplies exactly the operands required by the cell test.


### `cellCursor`

 The one-based persistent call cursor for a selected tape and cell. 

### `exists_unique_visit`

 Every noninitial call below the accepting cursor visits exactly one
tape and cell. 

### `window`

 The literal selected tape, including the canonical blank tapes at halts. 

### `bank`

 Reconstruct the register bank used by the elementary cell fragment. 

### `baseOf`

 The start address of the selected tape window within a serialized configuration. 

### `writeAddr`

 The instruction-scratch address of the proposed write symbol for the selected tape. 

### `scheduled_tape_data`

 Every actual scheduled register bank refers to the right tape cells,
source and target states, and the instruction fields saved in scratch. 
