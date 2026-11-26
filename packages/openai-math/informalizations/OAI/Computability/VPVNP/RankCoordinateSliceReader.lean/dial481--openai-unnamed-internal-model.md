---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateSliceReader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSliceReader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSliceReader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Native Cramer reader for a finite reduced slice algebra

The varying data are the replacement row and target monomial for a particular
pair of basis ordinals. The two determinant tables and the enclosing reader
are fixed throughout the quantification over both ordinals.


### `order`

 The rank of the appended equation and monomial rows, hence the common order of both Cramer
minors. 

### `Staged`

 Data presented by the rank selectors and root initializer for one live
query. Both matrix readers have the same physical ABI as the determinant. 

### `Staged.denominator`

 The encoded square matrix whose determinant is the denominator for this coordinate query. 

### `Staged.numerator`

 The encoded square matrix with the selected row replaced by the operation's target row. 

### `Staged.denReady`

 Condition on the auxiliary stacks from which the denominator entry routine can run. 

### `Staged.numReady`

 Condition on the auxiliary stacks from which the numerator entry routine can run. 

### `Staged.work`

 Private host stacks after preparation, containing both determinant inputs and the
  arithmetic frame. 

### `Staged.denAux`

 Auxiliary Gram-engine stacks prepared for the denominator matrix. 

### `Staged.numAux`

 Auxiliary Gram-engine stacks prepared for the numerator matrix with its replacement row. 

### `Staged.ticks`

 Number of machine ticks taken to prepare the two determinant inputs for this live query. 

### `core_step`

 The native core returns the next-coordinate scalar for either operation. 

### `entry_reader`

 Entrywise form used directly by the evaluator's two callback contracts. 
