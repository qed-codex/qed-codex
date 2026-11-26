---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecCNFTupleOdometer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCNFTupleOdometer.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCNFTupleOdometer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-control increment of framed binary tuples

Tuple components are little-endian Boolean words carried by
`Encoding.encodeList id`. The finite table below skips framing bits and
increments only payload bits, with carry continuing into the next component.
Neither the number of components nor their widths enters the control table.


### `bumpWord`

 Fixed-width increment. The first component reports carry beyond the word. 

### `bumpWords`

 Carry travels through successive records in their encoded order. 

### `bumpWord_value`

 All arithmetic is on payload bits; overflow contributes exactly one modulus. 

### `program`

 Three registers hold the scanned bit, presence, and final overflow flag. 

### `frame_carry_trace`

 If a component is exhausted, scanning continues at the next record. 

### `frame_stop_runs`

 Once a zero payload bit is found, the finite program restores the entire
scanned prefix and returns without reading later payloads. 

### `list_runs`

 Full framed traversal. A pre-existing reversed prefix on scratch is also
restored, so this theorem composes directly with the record-entry transition. 

### `increment_runs`

 One complete invocation of the fixed table. The suffix is untouched and
the scratch stack is cleared. The bound counts actual bit-program instructions. 

### `increment_primitive`

 The verified compiler yields actual primitive-tape execution, with fixed
overhead independent of every tuple dimension and payload value. 

### `bumpWord_append`

 Concatenation transports carry, independently of the frame representation. 

### `bumpWords_flatten`

 The tuple odometer is exactly fixed-width increment of all payload bits. 

### `advance_before_last`

 Before the last bit-tuple, the counter advances by exactly one and does
not report overflow. This supports a rank argument for exhaustive traversal. 

### `overflow_at_last`

 The last bit-tuple resets all payload bits to value zero and reports
overflow. Record boundaries and every component width remain unchanged. 

### `increment_runs_width`

 A useful bound when each index record has at most w payload bits. 
