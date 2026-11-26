---
{
  "module": "OAI/Computability/VPVNP/RAMProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Elementary programs for the burst RAM

A fixed finite instruction table and finite public constants specify the private
word computation of a call in Lemma 10.1. Register operands and instruction
destinations are bounded indices into the fixed machine. Private and external
addresses are full words. Private memory and registers start at zero on each
call, while the persistent input is separately available to its instructions.


### `BinaryOp`

 Arithmetic uses reduction modulo the word modulus. Division and remainder
use Lean's natural-number conventions on a zero divisor. Shifts by at least
the word width have value zero. 

### `BinaryOp.eval`

 Evaluate a binary arithmetic or bitwise opcode on width-w words. Arithmetic results are
word-sized, and a shift by at least the word width yields zero. 

### `Instr`

 Each instruction has constant arity. The conditional tests and branch
choices designate two program counters; every other continuing instruction
designates one. 

### `Machine`

 Finite instruction table for a burst RAM call, with an entry counter and an indexed table
of public operand words. 

### `Machine.entry`

 Program counter at which every fresh call starts. 

### `Machine.code`

 Instruction fetched at each of the machine’s finite program counters. 

### `Machine.publicData`

 Public operand words addressed by the machine’s public-word load instructions. 

### `Config`

 Private RAM state within one call, consisting of its program counter, persistent input
word, registers, and addressable private memory. 

### `Config.pc`

 Program counter used to fetch the next instruction. 

### `Config.persistent`

 Incoming persistent state word available to state-word loads during the call. 

### `Config.reg`

 Private word stored in each of the call’s registers. 

### `Config.privateMem`

 Private word memory indexed by a word address and initialized to zero at call entry. 

### `Config.put`

 Write a value to the destination register and advance to the given program counter. 

### `Config.store`

 Write a word at a private-memory address and advance to the given program counter. 

### `Instr.run`

 Interpret one instruction as a local step, binary choice, external memory probe, return of
a persistent word, accepting halt, or rejection. 

### `Machine.program`

 Executable translation to the burst interpreter. Resetting the private
workspace is part of call entry in this machine model. 

### `Machine.step_read`

 The value returned by an external read is available to every later
instruction, in particular to the address operand of another probe. 

### `Machine.execute_dependent_reads`

 Two consecutive external reads can use the answer of the first as the
address of the second. This is the native execution rule on actual memory. 

### `Instr.wordWork`

 A conservative word-operation accounting for a dispatch: instruction
fetch and program-counter update, operand reads, one arithmetic operation
or comparison, and a destination write. Read/write probe logging and guess
bits are counted separately. 
