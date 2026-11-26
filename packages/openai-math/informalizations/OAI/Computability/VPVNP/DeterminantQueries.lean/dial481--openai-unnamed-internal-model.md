---
{
  "module": "OAI/Computability/VPVNP/DeterminantQueries.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DeterminantQueries.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DeterminantQueries.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing matrix rank by querying a weighted determinant

The Appendix D.2 rank algorithm scans bidegrees in the reverse characteristic
polynomial of the weighted Gram matrix. A fixed degree in a Gram entry reads
at most two scalar entries of the original matrix. The Schur coefficient query
then evaluates the entire determinant at a single bidegree. The proofs cover
empty matrices, rank zero, and characteristic two.


### `weightedGramEntryCoeff`

 A tagged Gram entry has at most one contributing column in each degree. 

### `streamMaximum`

 Scan a consecutive interval and return its maximum score, or zero if empty. 

### `rankPolynomial_coeff_natDegree_le`

 The inner degree at outer degree `u` is at most `u(n+m)`. 

### `scanRank`

 Recover rank by scanning scalar bidegree queries. The scans include both
endpoints and keep only the current indices and maximum degree. 

### `rankQuery`

 Rank computed by querying scalar coefficients of the weighted Gram determinant. 
