---
{
  "module": "OAI/Computability/VPVNP/PairSimulationShrinkMapImage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkMapImage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkMapImage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The shrinking node's resident map loop in one finite instruction bank

The count reader and each item reader feed the actual grid and party chains.
Their targets are the lowered, descriptor-writing map handlers. Successful
entries return to the common row increment; exhausting the row reaches the
role continuation. All emitted instructions use the live five-bit literal format.


### `demandOrder`

 Exactly the order of the grid numbers written by the selected-term worker. 

### `Address`

 Instruction labels for the resident readers, loop, dispatcher, map handlers, and reject row. 

### `Registers`

 The eleven header registers have their resident reader roles. The extra
zero register serves the ordinal dispatcher and lies outside that reader bank. 

### `Registers.header`

 Placement of the eleven reader registers in the shared bank. 

### `Registers.zero`

 Shared register used for zero by the grid and party dispatcher. 

### `inputPC`

 Machine address of an instruction in the resident header or item reader. 

### `casePC`

 Machine address of a grid or party dispatch instruction. 

### `handlerPC`

 Machine address of a descriptor writer or map instruction in the handler family. 

### `loopPC`

 Machine address of the cursor test (`false`) or increment (`true`). 

### `badPC`

 Reject address for a grid or party ordinal outside the dispatch table. 

### `headerReg`

 Physical register assignment for the eleven resident reader registers. 

### `cases`

 Dispatches the grid and party ordinals read from an item to its descriptor writer. 

### `loop`

 Tests the reader's cursor against the end of the row and advances it after each handler. 

### `text`

 Five-bit instructions for one resident map row scan, including all dispatch targets. 

### `linked`

 Placing the one fixed table supplies the four program links and the
complete handler family rows, with no condition on the external memory. 

### `locations`

 Numbering of the complete resident-map portion, independent of the input length. 

### `sharedRegs`

 Embeds the role's shared registers into the segment's numbered register bank. 

### `mapRegs`

 Embeds the handlers' private registers into the segment's numbered register bank. 

### `segment`

 A segment compatible with the final-vertex image. The caller's level
and packed-site inputs are its header registers zero and one. 

### `segment_rows`

 Recover the typed opcode rows inside any installation of this whole segment. 
