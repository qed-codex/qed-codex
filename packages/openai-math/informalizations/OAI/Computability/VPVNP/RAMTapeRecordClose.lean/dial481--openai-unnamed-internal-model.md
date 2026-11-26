---
{
  "module": "OAI/Computability/VPVNP/RAMTapeRecordClose.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeRecordClose.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeRecordClose.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Completing the serialized pre-sort block

Each unused record slot contributes five all-zero words. The remaining-slot
counter controls padding independently of the values in the accumulated
records. The last pass reverses the whole buffer once to expose records and
their word bits in the order consumed by the first sorting layer.


### `pad`

 Append one zero record for each unary mark left after probe emission. 

### `reverse`

 Pop the completed reverse buffer onto the output stack. 

### `close`

 Pad every unused slot with a zero record, then reverse the buffer to obtain the sorting
input in record order. 

### `close_run`

 Closing adds the exact prescribed suffix of zero bits. It clears the
slot counter and reverse buffer, and preserves the five field registers,
the zero template, and the empty scratch stack. 

### `serialized`

 The same byte sequence emitted by consecutive `appendRecord` calls. 

### `close_block`

 When the existing records followed by the vacant slots describe a
complete block, the output is its canonical sorting-exchange encoding. 
