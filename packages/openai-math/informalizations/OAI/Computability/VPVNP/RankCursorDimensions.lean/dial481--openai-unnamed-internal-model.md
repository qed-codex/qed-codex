---
{
  "module": "OAI/Computability/VPVNP/RankCursorDimensions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorDimensions.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorDimensions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Initializing a rank scan from the two binary matrix dimensions

Register one supplies the row count and register three supplies the column
count. The machine adds and multiplies them to compute the inner scan bound
`(n + m) * n`. The preceding logarithm pass initializes the balanced Schur
depth from the row-count word.


### `dimensionRegs`

 The two physical dimension words supplied by the caller. 

### `startRegs`

 Cursor registers after computing the inner index and its bound as the word product `(n + m)
* n` in `w`-bit arithmetic. The outer register holds the word for `n`. 

### `initializeDimensions`

 Prepare the balanced-product depth from the row count and compute the inner scan bound from
the two dimension registers. 

### `startupClock`

 Step bound for computing the logarithmic depth and initializing the dimension registers
before the first rank query. 

### `startupSpace`

 Stack-height bound during rank initialization, accounting for the work bank, the w-bit
registers, and the existing flag stack. 

### `initialize_bounded`

 From encoded row and column counts, prepare the cursor and Schur root
constants and return the correct initial cursor registers. 
