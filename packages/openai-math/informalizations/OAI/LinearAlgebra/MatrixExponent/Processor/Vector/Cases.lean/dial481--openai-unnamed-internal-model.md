---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Processor/Vector/Cases.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Processor/Vector/Cases.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Processor/Vector/Cases.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Simultaneous arithmetic on valid inputs

The same circuit handles every setting in the indicated domain.
Registers are interpreted modulo their capacity. Only comparisons and
indirect reads need hypotheses about the sizes of their operands.


### `unary`

 A fixed unary table may be evaluated on every register at once. 

 # Routing lanes to one of two computations by a fixed partition 

### `casesOn`

 Both stages may use every lane. Empty index sets need no dummy input. 

 # Indirect reads through fixed finite lookup tables 

### `fetch`

 A fixed indexing of the possible requests suffices. It is not
necessary to compute an inverse table from the input data. 

 # Converting circuits on named bits into packed word arrays 

 # Row sums of small square arrays of channel lengths 

 # Loading bits into word lanes and checking simultaneous assertions 


# Static tables indexed by two smaller keys

A worker number and a local record number can jointly index a table
even when the record is used many times. The product of the two key
ranges must fit in the shared array.


 # Changing the input and the lane indexing of a packed computation 

### `remap`

 Renumber a packed domain by any static function. 

 # Returning named Boolean results from a packed calculation 

### `output`

 If the register in each lane represents a bit, any fixed naming
of the requested bits can be used for the output of the circuit. 
