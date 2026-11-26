---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsRowRecipe.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsRowRecipe.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsRowRecipe.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing a compressor worker row from a live level header

A recipe is a finite straight-line word program. It may read a public word,
the current level pointer carried in persistent state, or external memory
through any computed address. Its assignments finish before it writes the
destination row, so its values describe the input memory even when a row
overlaps cells used to compute it. Two additional registers hold the output
cursor and the constant one.


### `RHS`

 Read-only assignments in the straight-line source program. The native
two-bit immediates may be combined by arithmetic to build larger constants. 

### `Assign`

 One straight-line planner instruction that evaluates a read-only right-hand side and stores
its word in a specified register. 

### `Assign.dst`

 Register overwritten by this assignment before the next recipe line executes. 

### `Assign.rhs`

 Read-only operation that supplies the word assigned to the destination register. 

### `RHS.value`

 Compute an assignment's word from the public operands, persistent state, external memory
and current registers. 

### `RHS.event`

 The assignment's trace event, a memory read carrying its address and observed word for a
load, or one private tick for another operation. 

### `RHS.reads`

 Number of external reads charged for one right-hand side, one for a memory load and zero
for all register operations and inputs. 

### `evaluate`

 Execute the assignments in order against the same entry memory, returning the chronological
events and the final register values. 

### `Recipe`

 The selected registers specify both the destination and the full padded row. 

### `Recipe.lines`

 Straight-line assignments that compute the destination address and field values before
  any directory word is written. 

### `Recipe.dest`

 Register containing the address at which to write the first word of the directory row. 

### `Recipe.tag`

 Register containing the stage tag that selects the worker for this row. 

### `Recipe.start`

 Register containing the cursor passed to the worker on its first call. 

### `Recipe.stop`

 Register containing the exclusive stopping cursor for the worker's scan. 

### `Recipe.params`

 Registers containing the worker's parameter words in their padded directory order. 

### `Recipe.fields`

 Output registers in the order their contents are stored, starting with the tag and both
cursor bounds and ending with the parameter bank. 

### `Recipe.values`

 The register file obtained by running the recipe's assignments from zeroed registers on the
supplied public words, state and entry memory. 

### `Recipe.address`

 The computed destination address read from the final register file before row storage
begins. 

### `Recipe.words`

 The words written to the directory, read from the final registers in tag, start, stop and
parameter order. 

### `Recipe.code`

 Compile the assignments, write the fields to consecutive cells, and put the incoming state
plus one in the return register. 

### `Recipe.table`

 Native instruction template for publishing one recipe row and returning the advanced state. 

### `Recipe.report`

 Trace of the recipe's assignment events, pointer setup, consecutive row writes and state
advance, with return value `s + 1`. 

### `Recipe.reads`

 Total external reads performed by the computation lines before the row is written, counting
repeated loads separately. 

### `execute_row`

 Exact native execution, including the rejection of every nonempty branch stream. 

### `Recipe.acceptTable`

 One-shot version of the row publisher that accepts after the row is stored so the linked
launcher can take control. 

### `execute_accept`

 Single-row planners transfer to a statically linked launch stage on acceptance. 

### `row_stores`

 Every field is computed from entry memory. No disjointness between metadata
and the destination row is needed to install the result. 

### `sizeRecipe`

 The four consecutive live level-header words are the vertex count, degree,
replication factor, and directory row ordinal. Public word zero is the directory
base. The emitted row for tag one starts at zero and stops at the slot count. 

### `sizeRecipe_row`

 Native construction of the slot-scan row using four metadata reads and five
writes. The row's stop and operands are evaluated from the original header. 
