---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackExpressions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackExpressions.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackExpressions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Compiling the arithmetic expressions of a Schur query

Each syntax node receives one fixed scratch register. Disjoint intervals
serve the two subexpressions. The proofs track the result register and show
that registers outside the assigned interval retain their values.


### `nodes`

 Number of nodes in an expression tree, used to allocate disjoint scratch slots for its
subexpressions. 

### `Fits`

 All intermediate natural-number results fit the register width. 

### `compile`

 Compile an expression into register code that writes its value to the scratch slot at
`start`. 

### `preserves`

 The compilation never writes outside the finite register interval
assigned to this expression. 

### `compile_correct`

 Interpreting a compiled expression reads the eight input words and
writes exactly its natural value to the first scratch register. 

### `weight`

 A syntax-dependent coefficient in the linear word-width bound. 

### `fits_weight`

 A width linear in the input bit bound suffices for any fixed expression. 
