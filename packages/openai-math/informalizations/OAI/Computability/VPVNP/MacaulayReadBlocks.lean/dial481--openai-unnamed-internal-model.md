---
{
  "module": "OAI/Computability/VPVNP/MacaulayReadBlocks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayReadBlocks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayReadBlocks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Joining the three physical row blocks on the determinant engine's ABI

The first two blocks have product indices for an equation and its multiplier
monomial. The appended monomials have one index each. This proof combines the
three typed native reads without reconstructing a matrix or restricting its
queried row or column.


### `rowOf`

 Index the row for equation or affine pin `r` multiplied by monomial `o` in the augmented
matrix. 

### `appended`

 Index the powered monomial at suffix ordinal `o`, after all multiples of equations and
pins. 

### `BlockRun`

 All three local reads preserve the decoder and its coefficient advice. 

### `armCorrect_of_blocks`

 From one typed call for each row block, obtain the raw arm contract on
all addresses, with one common immutable coefficient bank. 
