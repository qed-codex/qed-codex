---
{
  "module": "OAI/Computability/VPVNP/ParseGrammar.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseGrammar.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseGrammar.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Graded parse tables for arithmetic circuits

Section 8.1 of *VP and VNP differ over every field* uses an ordered binary grammar to
record a homogeneous component of a circuit output. Here the layer index `d : Fin n`
represents degree `d.val + 1`. Each production has its own scalar, including a separate
scalar for each choice of terminal variable.


### `ParseGrammar`

 Scalar labels on all terminals and ordered binary productions through degree `n`. 

### `ParseGrammar.terminal`

 The scalar weight for emitting terminal variable `v` from state `h` in degree one. 

### `ParseGrammar.binary`

 The scalar weight for a binary production at layer `d`, given its parent state, split and
  ordered child states. 

### `leftDegree`

 Layer of the left child at split `b`. Its degree is `b.val + 1`. 

### `rightDegree`

 Layer of the right child. Its degree is the remaining `d.val - b.val`. 

### `eval`

 Evaluate a grammar state as a formal polynomial by multiplying the two ordered
children of each binary production and summing over all productions. 

### `eval_eq_of_recurrence`

 The recursive evaluation agrees with every state table that satisfies the grammar
equations, simultaneously for all states and positive degrees through `n`. 

### `eval_isHomogeneous`

 Every state polynomial is homogeneous in the input variables of its declared degree. 

### `weight`

 Multiply the terminal and internal scalar labels occurring in this ordered parse. 

### `eval_eq_sum`

 Expansion of the state polynomial as a sum over the actual ordered parse trees.
The multiplicative terminal monomial reads the leaves in their left-to-right order. 

### `eval₂_eq_sum`

 Evaluate the parse expansion with arbitrary terminal values and a change of scalars. 
