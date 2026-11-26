---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateRegisters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateRegisters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateRegisters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Register arithmetic for a physical prefix-rank query

The control holds the cursor, one, target ordinal, returned rank and inclusive
prefix length in five binary words. It forms the inclusive length before every
rank call and compares the returned word with the ordinal. Other ports remain
available to the matrix and rank subroutines.


### `Port`

 The five prefix-rank registers alongside the scalar reader's auxiliary bank. 

### `words`

 Initialize the cursor, constant one, requested ordinal, returned rank, and inclusive prefix
length. 

### `bank`

 Mount the five binary words and the prefix reader's auxiliary state in their disjoint
banks. 

### `rankTest`

 The prefix-length input is register four, and the rank output is register three.
Only this subcall depends on the matrix representation. 

### `machine`

 Starting at cursor zero, ask for the rank through the current row and advance until that
rank exceeds the requested zero-based ordinal. The cursor then identifies the corresponding
greedy pivot row. 

### `arithmeticBound`

 Step allowance for one register addition, used both to form the inclusive prefix length and
to advance the cursor. Each use contributes separately to the prefix-scan bound. 

### `rankAt`

 Numeric rank of a prefix, with saturation only for out-of-range indices,
which the machine never reaches. 

### `machine_runs`

 The only remaining call contract is the rank of a supplied prefix. All index
arithmetic and comparisons are physical routines, independent of the matrix shape. 
