---
{
  "module": "OAI/Computability/VPVNP/PrivateRAMRegisterOperands.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrivateRAMRegisterOperands.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrivateRAMRegisterOperands.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Lowering public-word operands inside a native subroutine

A virtual public word is supplied either by the enclosing machine's public data
or by a register initialized before entry. The subroutine keeps these registers
intact. A second copy of the host program counters executes the caller after
return, so its continuation may overwrite any operand or invoke the subroutine
again. Both executions produce the same report for every fuel and bit stream.


### `Operand`

 Source of a virtual public word, given by either a register index or an index into the
caller's public data. 

### `Operand.value`

 Read the word stored in the register or public-data slot named by an operand. 

### `translate`

 Relabel jump targets and compile public loads in a single pass. 

### `lower`

 Compile each virtual public load into a register copy or a physical public load according
to the operand assignment. 

### `mapPC`

 Apply a program-counter map to every continuation and jump target in an instruction. 

### `withPC`

 Construct a configuration with the supplied program counter and the given persistent word,
registers, and private memory. 

### `mapConfig`

 Apply a label map to the program counter of a RAM configuration. 

### `Agrees`

 The operand bank agrees with the semantic data on entry. 

### `enter`

 Embed a program label in the first copy of the instruction table, used for subroutine
entry. 

### `caller`

 Embed a program label in the second copy of the instruction table, used for the caller's
continuation. 

### `fold`

 Recover the original program label from its address in either copy of the instruction
table. 

### `enterConfig`

 Place a configuration at the corresponding label in the subroutine-entry copy of the
program. 

### `callerConfig`

 Place a configuration at the corresponding label in the caller's copy of the program. 

### `project`

 Recover a configuration of the original machine by folding its doubled program counter. 

### `shadow`

 The first copy uses the role's semantic rows and virtual data inside its
region. All remaining rows use physical public data and jump to caller PCs. 

### `destination`

 The register written by this instruction, including the destination
filled by a successful external read. 

### `reg_of_continuesTo`

 Every continuation preserves registers outside the instruction's
destination, for either choice and every possible read answer. 

### `execute_project`

 Projecting every continuation on an invariant set preserves the entire
external execution report at any fuel and on every choice stream. 

### `execute_caller`

 Once the role returns to a caller PC, the shadow runs the actual caller,
including later calls and writes to any of the formerly saved operands. 

### `callerConfig_project_of_pc`

 Project a returned configuration directly to the caller's program counter
space. All register and memory fields are kept verbatim. 

### `execute_enter`

 Every lowered step agrees with the virtual one until the role returns.
Only rows in the role are required to preserve the operand registers. 
