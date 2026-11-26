---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordGreedyDirectory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordGreedyDirectory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordGreedyDirectory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Installing the greedy directory in external memory

After the first `k` calls, the first `k` mutable labels and the first `k`
records agree with the complete directory. The remaining words still have
their original values. In particular, each call sees the original control
words and both directed mate arrays.


### `prefixMemory`

 Memory after installing the first `k` indexed vertices. 

### `write_prefixMemory`

 One complete row write, including the zero label, advances the memory invariant. 

### `prefixMemory_outside`

 Partial installation preserves every word outside the walk allocation. 

### `prefixMemory_tables`

 The prefix writes preserve the two mate arrays supplied to the initializer. 

### `prefixMemory_controls`

 The low control words are readable throughout preparation. 

### `prepare_segment`

 Lift native vertex writes along the successive prefix memories. 

### `prepare_directory`

 The native initializer visits every vertex, returns its final cursor and installs the
complete directory. Calls include the control reads, the label and header writes,
and the probes used to obtain and store the operand pointers. 
