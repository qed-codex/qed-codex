---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed native program for one primed pair

The absolute cursor is tested against the end of the two input rectangles,
then against the end of the site parses. In a site block, division computes
the row and remainder distinguishes a mark clear, root initialization, or
node visit. The final region reads and compares one histogram entry per call.
Four private registers hold the cursor, its successor, the call count, and a
phase boundary outside the operand ranges of the embedded routines.


### `Code`

 Structured control flow for the combined counter using 52 private registers and 34 public
operands. 

### `Reg`

 Register indices in the combined counter, including the four registers reserved beyond the
input assembler. 

### `Pub`

 Indices of the input, parser and schedule operands in the combined public-word vector. 

### `inputReg`

 Identify each of the 48 input-assembler registers with the same-numbered combined register. 

### `parserReg`

 Identify each of the sixteen parser registers with the same-numbered combined register. 

### `inputPub`

 Place the sixteen assembler operands at the beginning of the combined public-word vector. 

### `parserPub`

 Place the fourteen parser operands after the assembler operands in the combined public-word
vector. 

### `stackPub`

 Address a stack-parser operand through the parser's block in the combined public-word
vector. 

### `inputRegs`

 Injective register placement used to link the input-assembly code into the combined
counter. 

### `parserRegs`

 Injective register placement used to link the parser and its administrative routines into
the combined counter. 

### `input`

 The whole body is finite and independent of every pair-specific header. 

### `node`

 The grammar-node visit routine installed on the combined registers and stack-parser
operands. 

### `clear`

 The mark-clearing routine installed in the combined parser code. 

### `init`

 The root-frame initialization routine installed in the combined parser code. 

### `compare`

 The nominated-versus-accumulated production count check installed in the combined parser
code. 

### `rowSetup`

 Register 51 contains the end of the assembly calls on entering this block.
The quotient is the zero-based row number and the remainder is the in-row cursor. 

### `site`

 Decode the site and local slot from the cursor and invoke mark clearing, root setup or the
grammar-node visit. 

### `afterInputs`

 Dispatch post-assembly cursors to a site parse or, after the site region ends, a histogram
comparison. 

### `dispatchSetup`

 Load the current cursor from persistent state, compute its successor and read the total and
input-assembly boundaries. 

### `body`

 Execute one scheduled counter call by dispatching its absolute cursor to the input or
post-assembly code. 

### `table`

 A single table is instantiated at every `n`, degree/state range, group pair
and nomination. It returns register 49, or accepts when that equals register 50. 

### `publicWords`

 Operand table for the common program. Input parameters, parser parameters,
and four schedule bounds occupy consecutive fixed slots. 
