---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackCodegen.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackCodegen.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackCodegen.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed bit-stack compilation of Schur descriptor and child requests

A decision tree computes each of six result words from the immutable eight
inputs. Each test compiles its two expressions to separate scratch intervals.
The same scratch bank is reused for the selected subtree and the remaining
output words.


### `need`

 Scratch-register allowance for computing one output field, counting its leaf expressions
and both sides of every test. 

### `bits`

 Sum of expression weights used to bound the word width for one field of the dispatch tree. 

### `fieldCode`

 Compile the tests and leaves that compute a single output field into register instructions. 

### `scratch`

 Total scratch allowance obtained by summing the register requirements of all six output
fields. 

### `wordFactor`

 Sum of the six output fields' width factors for the compiled dispatcher. 

### `inReg`

 Inputs occupy slots zero through seven, and the result words occupy slots
eight through thirteen. The scratch interval starts at fourteen. 

### `outReg`

 Physical output register for field `i`, following the eight input registers. 

### `workReg`

 Scratch register at offset `i` from the end of the fourteen input and output registers,
indexed modulo the bank size. 

### `emitFields`

 Reuse one scratch bank while evaluating a finite sequence of output fields. 

### `physical`

 Compile the dispatch tree to a physical machine that emits all six output fields. 

### `physical_runs`

 The fixed compiled bit-stack program returns all six output words, while
preserving its eight input words. Its finite control and scratch count depend
only on the syntax of the decision tree. 
