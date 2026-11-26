---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackRegister.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackRegister.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackRegister.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed bit-stack routines for register decision trees

Arithmetic instructions stage their two word operands before writeback. The
natural subtraction instruction tests for underflow and returns zero in that
case. Decisions compare two registers on the tape and execute one statically
specified branch.


### `Regs`

 Contents of `r` registers holding words of width `w`. 

### `Machine`

 A bit-stack routine on `r` register ports with no public input words. 

### `Arith.opcode`

 Translate a natural-arithmetic instruction to the corresponding binary word opcode. 

### `Arith.word`

 Width-bounded register semantics for natural operations. 

### `RegCode`

 Register programs built from literals, copies, arithmetic, sequencing, and equality tests. 

### `exec`

 Execute a register program on width-`w` words, saturating subtraction at zero. 

### `length`

 Weighted instruction count used to bound execution time, charging two units for arithmetic
and the longer arm of a test. 

### `compile`

 Compile a register program into a bit-stack routine, testing for underflow before a
subtraction. 

### `compile_runs`

 The compiled program is finite and independent of the operand width.
It returns the specified register bank within a quadratic per-instruction
bit-stack clock. 
