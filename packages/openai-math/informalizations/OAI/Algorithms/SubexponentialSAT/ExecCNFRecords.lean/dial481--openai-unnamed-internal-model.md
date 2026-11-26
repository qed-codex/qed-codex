---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecCNFRecords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCNFRecords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCNFRecords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-control skipping of framed CNF records

The program below has three Boolean registers, one Boolean stack, and eleven
fixed labels. It consumes an escaped frame or one tagged list item without
materializing the payload. The payload may itself encode a list of literals,
a clause, or a more deeply nested record. Every bound is proved for actual
`BitProgram.step` traces, rather than assigned to a semantic list operation.


### `regs`

 Registers 0, 1, 2 hold the last bit, presence flag, and item-found flag. 

### `skipProgram`

 Entry 0 reads a tagged list item; entry 4 reads a raw escape frame. 

### `frame_trace`

 Raw-frame entry consumes exactly one frame and preserves the entire suffix. 

### `record_trace`

 Public entry skips one tagged record, reporting that an item was present. 

### `list_end_trace`

 End-of-list is distinct from a successfully skipped record. 

### `empty_reject`

 Missing input is rejected by the presence flag, rather than read as a delimiter. 

### `record_runsIn_length`

 Linear actual-step bound in the encoded input length; no payload-size oracle. 

### `frame_runsIn_length`

 Frame-entry cost is likewise linear in the actual encoded bytes/bits. 

### `list_cons_trace`

 Each list item can contain an arbitrarily nested encoding. 

### `clause_record_trace`

 In particular, skip a whole clause whose payload is a framed list of naturals. 

### `frame_read_agrees`

 The decoded clause suffix agrees with the actual record traversal. 

### `ports`

 Source, destination and scratch are fixed ports 0, 1 and 2. 

### `captureProgram`

 Capture the raw bits of one frame or tagged record in reverse on scratch.
Destination port 1 is untouched. 

### `restoreCapturedProgram`

 Restore the captured word to forward order on the destination port. 

### `copyProgram`

 Sixteen fixed labels copy a whole raw record while consuming only that
record at the source. Its source suffix and old destination are preserved. 

### `copy_record_trace`

 Copy a tagged record in original encoded order; scratch is restored empty. 

### `copy_frame_trace`

 Raw-frame entry 4 copies a frame, including its escapes and delimiter. 
