---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorRecord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorRecord.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorRecord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Prepending a five-word successor record

The record fields are words 3 through 7 of the successor message. To
prepend them in increasing order, the machine visits them in decreasing
order. For each word it reverses the bits onto a scratch stack, then pops
them back to both the source and the record.


### `RecordPort`

 Ports used to prepend successor words three through seven to the saved record while
restoring the word stacks. 

### `prependCopy`

 Prepend the contents of one bit stack to another, preserving their order
and restoring the source. The temporary stack must start empty. 

### `prependCopy_runs`

 Each bit costs two instructions to save it and three to restore and copy it.
The two empty pops finish the scans. Only the destination changes. 

### `appendRecord`

 A fixed routine for the record payload, independent of the word width. 

### `appendRecord_runs`

 Each word costs two empty pops and five instructions per bit. All
source and scratch stacks return to their initial contents. 
