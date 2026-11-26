---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackSchur.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackSchur.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackSchur.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Stack execution of the Schur determinant product

The query tags implement the balanced product of Schur factors, the two degree
convolutions inside one factor, and the power of its trailing principal
submatrix. The only matrix reads are individual scalar coefficients.


### `map`

 Relabel both child queries of every product term while preserving scalar leaves. 

### `Block`

 A contiguous interval of Schur factors, stored by its start and its length. 

### `Block.start`

 First factor index in the contiguous block used by the balanced Schur product. 

### `Block.count`

 Number of consecutive Schur factors in the block. 

### `lower`

 Initial half of a block, containing the first `count / 2` factors. 

### `upper`

 Remaining half of a block, starting immediately after its initial half. 

### `Limit`

 Natural numbers from zero through the inclusive bound `b`. 

### `TailIndex`

 Local indices of the principal submatrix strictly after pivot `a`. 

### `lowDegree`

 Embed the first part of a coefficient-degree split into the original degree range. 

### `highDegree`

 Complementary degree `q - d` of a coefficient convolution. 

### `predBy`

 Subtract `k` from a bounded natural degree, saturating at zero. 

### `tailIndex`

 Translate a local tail index to its index in the original matrix after pivot `a`. 

### `Entry`

 Scalar coefficient reader indexed by matrix row, matrix column, and polynomial degree. 

### `tailEntry`

 Restrict the coefficient reader to the trailing principal submatrix after pivot `a`. 

### `SchurKey`

 The query tags and their numeric fields. `inner` handles the convolution of
the leading row with a matrix power, and `outer` multiplies by the trailing
column with the negative sign of the Schur factor. 

### `K`

 Schur query keys with fixed matrix order and two bounded coefficient degrees. 

### `unitCoeff`

 Bivariate coefficient of the constant polynomial one, supported at bidegree `(0,0)`. 

### `factorCoeff`

 Coefficient at `(u,z)` of the Schur factor for pivot `a`, using the unit factor after the
last pivot. 

### `innerCoeff`

 Degree-`z` convolution of a pivot-row entry and an entry of the `h`th power of the trailing
submatrix. 

### `outerCoeff`

 Degree-`z` convolution of the inner Schur product and the negated entry returning from the
tail to the pivot column. 

### `value`

 Scalar specified by a Schur query, from a product of factors down to an individual matrix
coefficient. 

### `node`

 Expand a Schur query into a scalar leaf or the indexed products that make up its next
coefficient convolution. 

### `program`

 Stack program evaluating Schur queries by expanding their product nodes and reading scalar
leaves. 

### `root`

 Initial query for coefficient `(u,z)` of the determinant pencil, taking the Schur product
over all `n` factors. 
