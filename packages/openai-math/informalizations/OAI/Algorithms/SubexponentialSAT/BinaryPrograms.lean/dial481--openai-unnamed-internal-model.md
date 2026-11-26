---
{
  "module": "OAI/Algorithms/SubexponentialSAT/BinaryPrograms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BinaryPrograms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BinaryPrograms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-control programs for binary arithmetic

Operands, their widths, and moduli are data. None of the programs in this file
have a control-state set depending on an operand length or numeric parameter.


### `fastCarry`

 Carry generation using three gates after the shared input XOR. 

### `program`

 A constant finite program: it never inspects the numeric value or length
of an operand. Registers 0..7 are carry,a,b,present-a,present-b,t,u,v. 

### `run`

 A complete execution to the halted state, for arbitrary operand lengths. 

### `littleEndianProgram`

 The complete adder followed by an actual stack-transfer loop.  Its output
has the same little-endian orientation as its inputs. 

### `primitive_value`

 A primitive tape execution, with one fixed compilation factor. 

### `accumulate`

 The accumulator specification matched by the fixed-control multiplier. 

### `program`

 The six ports are multiplier, shifted multiplicand, accumulator, copy,
copy scratch, and reversed sum. Every instruction acts on Boolean data only. 

### `add_block`

 The adder is installed as literal instructions in this program's table. 

### `round`

 One full multiplier iteration, including all copy and arithmetic work. 

### `run`

 The complete fixed program computes the accumulator specification.  The
bound counts every executed Boolean instruction and every stack operation. 

### `primitive_value`

 The fixed-control multiplier also runs on the actual primitive tape
machine. Its polynomial bound contains no word-sized arithmetic operation. 
