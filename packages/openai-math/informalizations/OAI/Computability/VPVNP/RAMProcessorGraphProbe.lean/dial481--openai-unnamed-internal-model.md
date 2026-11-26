---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorGraphProbe.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorGraphProbe.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorGraphProbe.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native graph transfers for reads, writes and call returns

At an external read the graph copies the old address, consumes a full guessed
word, and only then replaces the destination register. Writes copy both original
register values. Return and acceptance update the persistent state/status used
by the site's iteration test.


### `Snapshot.afterRead`

 The record stages the address from before the destination register was
assigned. Thus the address and destination may be the same register. 

### `Snapshot.afterWrite`

 Snapshot after decoding an external write, with the next instruction selected and the write
tag, source address and value staged for recording. 

### `Snapshot.afterReturn`

 Snapshot after a call returns the designated register as its persistent word and marks the
machine as running. 

### `Snapshot.afterAccept`

 Snapshot after acceptance, with the running flag cleared for the site's next iteration
test. 

### `read_run`

 Genuine path on the table from read dispatch to record emission. 

### `read_short`

 Short read guesses reach the literal rejecting table row. 
