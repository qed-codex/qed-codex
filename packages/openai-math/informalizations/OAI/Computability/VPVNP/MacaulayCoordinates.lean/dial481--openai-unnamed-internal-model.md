---
{
  "module": "OAI/Computability/VPVNP/MacaulayCoordinates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayCoordinates.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayCoordinates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coordinates from the augmented Macaulay matrix

Appendix D puts the Macaulay rows first and then the powered monomial rows.
A greedy coordinate query in this order returns a representation of the target.
Discarding the coefficients of the Macaulay rows gives a representation in the
quotient by their span, hence a representation of the original polynomial on
the slice.


### `appendRows`

 Concatenate two lists of rows, retaining their column indexing. 

### `mem_appendRows_greedy_iff`

 A row in the appended block increases the prefix rank exactly when its
class in the quotient increases the span of the preceding appended rows. 

### `originalRowCoordinate`

 Query the coefficient assigned to an original row. Only a selected row
contributes a term to the sum over greedy basis indices. 

### `quotientCoordinate`

 The monomial coefficients, indexed by the second block of the augmented matrix. 

### `quotientCoordinate_reconstruct`

 The difference between the target and the combination of retained monomial
rows belongs to the span of the original Macaulay rows. 

### `quotientCoordinate_eq_mkQ`

 Equality in the quotient by the Macaulay row space after discarding its coordinates. 

### `indexedQuotientCoordinate`

 Reindex the coefficient columns and the Macaulay rows for an indexed
determinant query. The chosen order of the appended list is retained. 

### `poweredDifference_relation_iff`

 The D.1 row test for representing one polynomial by a linear combination of a list. 

### `poweredDifference_class_iff`

 The row criterion as an equality in the reduced coordinate algebra. 

### `macaulayCoordinateQuery`

 Query the coordinates of a polynomial from the Macaulay rows followed by
the powered rows of the supplied list. Both finite indexings of the Macaulay
matrix are explicit, so the query can use the paper's monomial order. 

### `macaulayCoordinateQuery_reconstruct`

 The determinant query on the actual Macaulay matrix reconstructs any target
class in the span of the queried polynomials. The degree hypothesis is the
effective weak Nullstellensatz bound used in D.1. 

### `macaulay_greedyIndex_iff`

 After the Macaulay prefix, exactly the greedy basis indices in the reduced
coordinate algebra are selected, in the given order of the polynomial list. 

### `macaulayCoordinateQuery_eq_zero`

 The coordinate query returns zero off the selected polynomial basis in
the reduced algebra, including for repeated or zero polynomial classes. 
