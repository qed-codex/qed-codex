---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalLink.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalLink.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalLink.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The fixed eleven-operand terminal controller for compressed pairs

The entry word zero starts the descriptor bootstrap unconditionally. Every
continuation returns the marker one and writes its worker ordinal and full
persistent word into the terminal header. Thus an ordinary zero returned by
a worker is a valid local cursor. An accepting worker advances to the next
worker with local state zero, except at the final vertex stage, where it
accepts the whole terminal program.


### `Stage`

 The five successive workers in a compressed pair's terminal computation. 

### `bootstrap`

 The worker that publishes the terminal header. 

### `prefixRows`

 The worker that computes the prefix sums of final wire widths. 

### `traversalRows`

 The worker that writes role tags and child rows for the selected layers. 

### `sharedBits`

 The worker that chooses the final shared wire values. 

### `vertices`

 The worker that processes the final vertices in increasing ordinal order. 

### `next`

 The stage entered after this worker accepts, if another worker remains. 

### `registers`

 Fixed worker bank, sharing the low registers and retaining the complete
eleven-word live pair ABI in each relocated instruction. 

### `embedding`

 Place a worker's registers in the common register bank. 

### `component`

 Relocate a worker to the shared register bank, preserving its public operands. 

### `Label`

 Control locations for entry, stage comparisons, worker bodies and return instructions. 

### `codeSize`

 Number of instructions after placing the five workers and their dispatch code. 

### `labels`

 Number the controller and worker labels in their physical instruction order. 

### `enter`

 Address of an instruction in the terminal entry sequence. 

### `scan`

 Address of a stage-tag load or the exhausted-scan rejection. 

### `compare`

 Address of the comparison that selects a particular worker. 

### `bodyPC`

 Physical address of an instruction in the selected worker. 

### `storeTag`

 Address of the instruction that stages a tag for the next call. 

### `save`

 Address of a control-word write or the return to the host. 

### `ordinary`

 Physical index of a register used by the worker. 

### `extra`

 Physical index of a register reserved by the terminal controller. 

### `phaseAddress`

 Register containing the address of the stage-tag cell. 

### `savedAddress`

 Register containing the address of the saved worker state. 

### `stateValue`

 Register holding the persistent word supplied to the worker. 

### `phaseValue`

 Register holding the current or next stage tag. 

### `temporary`

 Register used in computing the header and comparing stage tags. 

### `unitReg`

 Register containing the continuation marker one. 

### `extras`

 Values of the six controller registers while the worker executes. 

### `bodyConfig`

 Relocate the worker's current instruction and registers, retaining its private memory. 

### `header`

 Address of the first of the 32 terminal-header words in the pair workspace. 

### `tagWord`

 Machine-word representation of the stage ordinal. 

### `bodyInstr`

 Translate a worker instruction, including restoration of its state and handling of its exit. 

### `literalWidth`

 A width sufficient for the controller literals and every worker literal. 

### `enterInstr`

 Compute header addresses, check the host marker and enter or resume the terminal program. 

### `saveInstr`

 Write the stage and worker state, then return the host continuation marker. 

### `instruction`

 The instruction assigned to each physical controller or worker label. 

### `linked`

 Static eleven-operand template linking the five relocated workers. 

### `table`

 Finite terminal table obtained from the supplied numerical worker tables. 

### `machine`

 Instantiate the terminal template at the host word width and public input. 
