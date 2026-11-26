---
{
  "module": "OAI/Computability/VPVNP/PairTraversalRowExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalRowExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalRowExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing a descriptor row from its represented preimage list

The scan replaces identifiers by absolute child descriptor addresses. The
header routine then reads the stored count and publishes the pointer and count.
Both runs use the same external memory, with the header starting from the
writes actually emitted by the scan.


### `scanRegs`

 Registers at entry to the identifier scan. 

### `headerRegs`

 Registers at entry to the descriptor header routine. 

### `passMemory`

 The external memory after the identifier translation and the two header writes. 

### `NativePass`

 Two native runs, including their actual memory handoff, event costs,
and ordered children as read by the DFS. 

### `native_pass`

 Translate the represented source identifiers and publish the resulting row.
The count may overlap the source or either header cell: it is read before the
header writes, and the translation writes strictly above it. 
