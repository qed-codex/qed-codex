---
{
  "module": "OAI/Computability/VPVNP/LiveProgramPieces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPieces.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPieces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Linking native components with length-computable public operands

Each piece has its own register and operand count. The single finite native
table shares registers, and numbers the disjoint operand rows by a concrete
finite equivalence. Its sole additional operand is the outer tag address.


### `LiteralPrefix`

 The processor may read its own literal prefix when constructing the primed
strings. Supplying these two parsed values avoids embedding its code in itself. 

### `LiteralPrefix.length`

 Length in bits of the processor's literal program prefix as read from its input. 

### `LiteralPrefix.value`

 Packed natural number representing the bits of that literal program prefix. 

### `InputOperand`

 Source of one public operand, chosen from a geometry expression, the literal prefix length,
or its packed word. 

### `InputOperand.eval`

 Evaluate an operand using the supplied geometry and the two parsed literal-prefix values. 

### `Piece`

 A native component with a finite instruction table, register and operand counts, and a
source for each public operand. 

### `Piece.pcs`

 Number of program-counter positions in this component's instruction table. 

### `Piece.regs`

 Number of ordinary registers addressed by this component's instructions. 

### `Piece.count`

 Number of public operand positions in the component. 

### `Piece.table`

 The component's burst-RAM template at its specified instruction, register, and operand
  counts. 

### `Piece.operands`

 Select the source of each public word supplied to the component. 

### `Piece.ofTable`

 Package a native table whose public operands are all evaluated from geometry expressions. 

### `regs`

 Size of the shared ordinary register bank, given by the largest component register count. 

### `count`

 Total length of the public operand bank obtained by concatenating the component operand
rows. 

### `regEmbedding`

 Embed a component's register in the shared bank at the same numerical index. 

### `operandEmbedding`

 Number a component's local operand in the disjoint union of all component operand rows. 

### `table`

 Relocate a component's ordinary registers and public operands into the shared banks. 

### `program`

 Link the relocated component tables using the prescribed successor for each accepting stage
exit. 

### `bank`

 Look up the operand source belonging to a flattened component and operand index. 

### `operand`

 Append the geometry expression for the linker's stage-tag address to the component operand
bank. 

### `word`

 Evaluate a public operand and encode its natural value as a word at the geometry's RAM
width. 

### `publicData`

 Encode every linked public operand, including the final stage-tag address, for the given
geometry and literal prefix. 

### `machine`

 Instantiate the linked native table at the geometry's word width with the evaluated public
bank. 

### `component`

 Instantiate the individual component using its own public operand row at the same geometry
and literal prefix. 

### `data_eq`

 The physical processor can evaluate the flattened bank without receiving
any extra header contents or choices in its startup registers. 

### `component_eq`

 Operand relocation is invisible to native execution in each selected stage. 

### `execute_component`

 Every successful original native call appears in the linked machine on
precisely its own bit string, with the prescribed tag effect and bounded overhead. 

### `paths_eq`

 Exact replay for every choice stream, including rejection and calls after
termination. The per-stage semantics in this replay are native templates. 
