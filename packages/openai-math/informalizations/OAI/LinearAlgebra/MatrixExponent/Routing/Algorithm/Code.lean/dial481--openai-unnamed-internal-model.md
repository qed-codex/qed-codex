---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Routing/Algorithm/Code.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Routing/Algorithm/Code.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Routing/Algorithm/Code.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Deterministic straight-line word programs

A program contains its literal bits and words. A gate stores four bits.
The children of a tabulation are a finite array of programs, fixed before
evaluation. The evaluator materializes each result array once. The word
accounting uses pointers to immutable pairs and arrays.


### `tabulate`

 Materialize the child array, whose entries can then be read by index. 

### `charge`

 Charge each instruction once and each table slot once. 

### `advice`

 Reserve an opcode, literal/width fields, and child references in an
eight-word header. Each tabulation has one additional reference per child. 

### `scratch`

 A frame holds operands, result and continuation. Pairs can stay in
the frame. Tabulation allocates one extra result word per slot. 

### `time`

 Word cost with a fixed charge for dispatch, operations and frame
access. A table slot includes reading its child offset and writing its result. 

 # A permutation system with distinct exterior and channel widths 

### `PaddedSystem`

 The exterior and interior record lengths may be different. 

### `Correct`

 Transmission is counted in bits, including both ends of each link. 
