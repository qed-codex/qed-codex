---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderAllocated.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderAllocated.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderAllocated.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-capacity scans with a runtime field count

Each call reads the count from the descriptor and tests the current position
relative to the phase's first cursor. Occupied positions run the actual
payload copy or padding guard. An idle position advances the cursor without
reading the field offset or the packed header. The scheduling capacity can
therefore be public while the length of the occupied interval is private.


### `Parameters`

 Public operand indices identifying the first cursor, source-offset cell, destination base,
and runtime count for a bounded field scan. 

### `Parameters.firstCursor`

 Index of the public word from which the field-relative cursor is measured. 

### `Parameters.srcOffsetAddress`

 Index of the public address of the descriptor cell holding the packed source offset. 

### `Parameters.destinationBase`

 Index of the public destination base used to store copied field bits. 

### `Parameters.countAddress`

 Index of the public address of the field's live count word. 

### `block`

 Register 7 contains the successor on every normal return. 

### `table`

 The allocated-field worker table for either copying or padding-checking the selected packed
bit slot. 

### `position`

 The field-relative cursor obtained by subtracting the phase's first cursor. 

### `Active`

 The cursor lies within the occupied prefix specified by the live count word. 

### `bitAt`

 The selected slot bit read from the packed source word at the current field-relative
position. 

### `destination`

 The address to which an occupied payload bit is copied. 

### `Returns`

 The complete event log, including the count read, witnesses the effect on
memory and the cost of the successful call. 

### `copy_exec`

 An active payload call copies the selected bit and advances the cursor.
The four probes are count, offset, packed word, and destination. 

### `padding_exec`

 Occupied zero padding passes the guard and leaves memory unchanged. 

### `idle_exec`

 At every unoccupied position the count is the only external read. 

### `padding_rejects`

 No successful derivation can bypass a failing guard on an occupied
padding position, whatever the initial register file. 

### `exec_choices`

 Every successful execution, on any initial register file and memory,
consists entirely of deterministic instructions. 

### `native_of_returns`

 A successful block has the same effect in the native fixed table when
the allotted fuel includes its return instruction. 

### `native_report_of_returns`

 An arbitrary successful native report realizes the very same cursor,
memory effect and cost. This also accounts for surplus choice tapes and
arbitrary proposed fuel bounds. 

### `padding_native_rejects`

 Failing active padding rejects the native call for every choice tape and
fuel bound. 

### `report_successor`

 Every successful allocated cell, including an idle padding check, is
deterministic and advances the persistent cursor. 

### `report_frame`

 A report preserves the reserved tag under replay on every memory.
Only an active copy has a write, and it targets the current destination. 
