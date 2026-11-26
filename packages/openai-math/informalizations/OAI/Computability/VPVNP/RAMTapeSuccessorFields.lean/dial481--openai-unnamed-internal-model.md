---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Splitting the successor wire on the physical incident tape

One unary width stack supplies a count for each of the eight words. After each
word, the reader restores this count and reverses the saved bits into their
destination stack, preserving the least-significant-bit-first representation.


### `WordPort`

 Stacks for extracting one fixed-width word from the incident bit stream. 

### `Phase`

 Control states for collecting a word, restoring its unary width, and rejecting an exhausted
incident stream. 

### `wordCode`

 Read one field of the width given in unary, then restore its markers for the next field. 

### `word_runs`

 Extract the given word in its original order, restoring its unary width. 

### `Port`

 Shared input, width, and scratch stacks and the eight individual successor word stacks. 

### `indices`

 The indices of the eight words are fixed in the finite control. 

### `result`

 After reading, the next field starts at the top of the input stack. The
public width and the scratch stack have their original contents. 

### `read`

 The eight-word program is independent of the bit width and of all wire values. 

### `read_runs`

 Read an arbitrary successor field, including noncanonical encodings. The
same instruction count applies to every input with the public field lengths. 

### `raw_eq_flatten`

 The physical input tape is the row-major concatenation of fixed-width fields. 

### `raw_eq_flatten_words`

 Decoding the word array preserves every bit, including for malformed successor messages. 

### `read_raw_runs`

 Specialization to a successor wire in the serial transcript. 

### `incident_prefix`

 The incident stack exposes its send field, then its receive field, then
the unchanged sorting wires. This includes both zero-clamped boundary fields. 
