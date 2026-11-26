---
{
  "module": "OAI/Computability/VPVNP/PairVertexStagePrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexStagePrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexStagePrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing and linking the argument stages of a nonleaf visit

A preparation block can read the locator retained in the following routine's register
bank and initialize a separate argument-reader bank. The same construction links the
child stage on both roles and the absorbed-field stage on a shrinking role.


### `Preparation`

 Fixed instructions transferring operands to a phase before it starts. 

### `Preparation.count`

 Number of instructions in the operand preparation that runs ahead of a phase and its
  continuation. 

### `Preparation.entry`

 Entry ordinal of the setup portion of the preparation. 

### `Preparation.row`

 Native instruction generator for the preparation under the supplied DFS, saved, local
  register, and continuation placements. 

### `size`

 Total instruction count after concatenating setup, prepared phase, and continuation body. 

### `registers`

 Total private registers in the combined phase and continuation, with separate banks for
each. 

### `setupPC`

 Relocate a setup instruction from the initial block of the combined table to the program
address supplied by the placement function. 

### `phasePC`

 Relocate an instruction of the prepared phase, adding the setup block length before
applying the program-address function. 

### `bodyPC`

 Relocate a body instruction, adding the lengths of the setup and phase blocks before
applying the program-address function. 

### `phaseRegs`

 Embed phase registers in the combined bank after the continuation's reserved registers. 

### `bodyRegs`

 Embed continuation-body registers in the leading portion of the combined bank. 

### `assemble`

 Prepare the phase's inputs, run it, and return directly into the next body. 

### `childPreparation`

 The old-level child header reader receives the popped node and the old field table
head from the locator. Its ordinal bank has its own registers. 

### `withChildren`

 Assemble the child argument preparation and the supplied located body into one vertex
segment. 
