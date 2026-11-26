---
{
  "module": "OAI/Computability/VPVNP/MatrixWire.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MatrixWire.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MatrixWire.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Matrix restrictions of a wire

A wire carries the summation index of a matrix factorization between its two
endpoints. Taking the rows or the columns as the factorization index bounds
the wire dimension by either local dimension in the split-star construction.


### `matrixTensor`

 Place the row and column indices of a matrix at the indicated parties. 

### `wire_restricts_matrixTensor_of_factorization`

 An exact factorization with inner index `Z` is obtained by acting with
its two factors at the respective ends of a `Z`-dimensional wire. 

### `wire_restricts_matrixTensor_left`

 Use the row index as the wire index and put the whole matrix at the column endpoint. 

### `wire_restricts_matrixTensor_right`

 Use the column index as the wire index and put the whole matrix at the row endpoint. 
