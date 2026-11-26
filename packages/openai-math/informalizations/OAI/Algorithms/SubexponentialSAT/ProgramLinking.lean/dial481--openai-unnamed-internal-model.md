---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ProgramLinking.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ProgramLinking.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ProgramLinking.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite program relocation and linking

Every linked block is an instruction table inside one finite program.  A block's
halt can be replaced by a jump to a caller-specified continuation.  The proofs
below transfer actual instruction traces, including that final instruction, and
preserve all ambient registers and stacks outside the block's assigned ports.

The finite sizes and maps are fixed when the linked program is constructed; they
do not inspect the unbounded input stacks.


### `relocateInstr`

 Relocate all finite references, optionally replacing halt by a return jump. 

### `embedCfg`

 A mathematical embedding into the caller's frame.  The executable program
does not evaluate this function: it uses the finite relocated instruction table. 

### `execInstr_relocate`

 Relocation commutes with every instruction, even when read value/presence
registers alias.  Injective port maps preserve exactly the source aliases. 

### `CodeEmbedding`

 Code agreement is an ordinary equality of actual finite table entries. 

### `relocate_trace`

 Complete block traces transfer with exactly the same number of steps.
In particular a source halt is the target's actual return-jump instruction. 

### `liftProgram`

 Install a standalone program on a larger port set, keeping its labels. 

### `relocate_trace_before_halt`

 A trace ending at an active label has not executed any halt instruction.
Thus the target may give all source halt labels an arbitrary continuation body. 

### `relocate_trace_to_exit`

 Designated-exit version: the exit's instruction can be replaced without
charging a step until the caller actually executes that instruction. 

 ## Concrete disjoint linking 

### `linkInto`

 Install two finite tables in disjoint label ranges.  The first block's halts
jump to the second block's entry; the second block's halts stop the program.
Register and stack assignments can share ports between the two blocks. 

### `linkInto_trace`

 Linking with port assignments uses a checked equality at the shared data
boundary.  Both source traces execute inside the concrete table above. 

### `relabelCfg`

 Only change the finite program counter, keeping all data verbatim. 

### `enter`

 Start another finite table with the current register and stack contents. 

### `link`

 Sequential composition when both blocks already use the same port set. 

### `link_trace`

 No dispatcher or subroutine oracle is added: the replaced halt itself is
the one-step return jump, so the composed trace length is exactly the sum. 

### `link_complete_trace`

 End-to-end sequential execution from raw program input to canonical output.
The second routine starts with the first routine's actual data, not a reset. 
