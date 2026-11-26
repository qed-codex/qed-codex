---
{
  "module": "OAI/Computability/VPVNP/TensorFlattening.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorFlattening.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorFlattening.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Flattening across one tensor party

The row of the matrix is the basis index at the distinguished party and
the column consists of the basis indices at all other parties.


### `OtherBasis`

 Column indices for the flattening at party `a`. 

### `joinBasis`

 Combine one row index and one column index into a full tensor index. 

### `flattening`

 The matrix of a tensor across one party and its complement. 

### `flattening_rank_mono`

 Applying local maps multiplies the flattening on the left and the right.
The right-hand matrix combines the local maps on the complementary parties. 

### `flattening_product_rank`

 Parallel tensor factors flatten to the Kronecker product after regrouping
the two column index tuples. 

### `flattening_zero_rank`

 A zero coefficient array has zero flattening rank. 

### `flattening_unit_rank`

 Flattening the simple unit gives a one-by-one matrix of rank one. 
