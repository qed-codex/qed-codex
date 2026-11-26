---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapEntryProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapEntryProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapEntryProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The linked instruction blocks of one grouped map entry

The program uses one selector directory and fixed matrix bank at a chosen grid
point and party. The width guards and histogram scan share the same machine.


### `Program`

 Locations of the fixed instructions and registers used by the four phases. 

### `Program.selector`

 The selector directory scan and decoder for the block. 

### `Program.bank`

 Registers and public ports for the matrix rows at grid point `z` and party `j`. 

### `Program.loc`

 Machine instruction address assigned to each bank address. 

### `Program.edgeOrder`

 Order in which the width guard checks the supply edges. 

### `Program.expected`

 Register holding the expected total width for each edge. 

### `Program.guardTemp`

 Register compared with itself at the end of the width guard. 

### `Program.guardPC`

 Machine instruction addresses of the width comparisons. 

### `Program.histPC`

 Instruction addresses of the histogram scan. 

### `Program.histReg`

 Machine registers used by the histogram scan. 

### `Program.done`

 Continuation after the histogram scan finishes. 

### `Program.bad`

 Rejection address shared by the selector, row driver and width guard. 

### `driver`

 The matrix row driver at the instruction addresses assigned by `P.loc`. 

### `guardCode`

 Compare each accumulated edge offset with its expected width in `P.edgeOrder`. 

### `Linked`

 Instruction links for the common machine, including the shared rejection target. 

### `SelectorSaved`

 An exterior register survives the selector directory walk and decoder. 

### `Separate`

 The row bank, width targets and histogram operands can all be prepared
before entering the selector walk. Only the row bank uses the row scratch words. 

### `Public`

 The fixed code bits and matrix keys use the live word size. The two
selector phases share the same ordinal for each selector. 
