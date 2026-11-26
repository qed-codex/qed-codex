---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ComputablePackingSplit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ComputablePackingSplit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ComputablePackingSplit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computable coordinate splitting for an explicit packing

The inverse uses a finite sum of equality-tested coordinate copies, followed
by a residual-coordinate lookup. None of the definitions chooses a basis or
uses classical choice. Finite types, embeddings, and coordinate values are
inputs; this is not a Turing-machine cost theorem.


### `scatter`

 Finite scatter along an explicit injection. 

### `Leftover`

 The coordinates absent from the supplied packing. 

### `leftoverExtend`

 Copy a residual coordinate when it is absent from the embedding, and
return zero on every packed coordinate. Range membership is a finite search. 

### `uncurryLinear`

 Computable conversion between curried block coordinates and pair coordinates. 

### `assemble`

 Assemble the packed blocks and the residual coordinates by finite copying. 

### `split`

 An executable coordinate split for a supplied block embedding.
The forward map restricts; the inverse uses `assemble`, with no chosen basis. 

### `split_symm_apply_eq_sum`

 The executable inverse formula, down to the finite equality-tested sum. 
