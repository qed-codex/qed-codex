---
{
  "module": "OAI/Computability/VPVNP/MacaulayLeafBudgets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayLeafBudgets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayLeafBudgets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Shared time and space budgets for the three Macaulay entry arms

The live bank includes the signed counter, mask and value tables, two
ordinal words, and a full residual exponent buffer. Exhaustive counting and
ordinal scans contribute to the clock. Their exponent does not contribute
to the stack-height bound.


### `live`

 Includes the packed extension-field result and the residual buffer. 

### `scalarTime`

 Common tick bound for signed equation evaluation, affine pin lookup and copying an encoded
scalar constant. 

### `armTime`

 Tick bound for both ordinal scans and the post-scan scalar computation and buffer cleanup
of a matrix-entry arm. 

### `armSpace`

 Stack bound for the selected entry arm, including the ordinal scans, temporary exponent
buffer and decoder allowance. 

### `readTime`

 Time bound for decoding a row, routing it to the appropriate entry arm and returning the
scalar. 

### `leaf_bounds`

 All local clocks and stack heights are charged using their respective
budgets. The signed-call time is the only exponential term besides the two
ordinal scans. 
