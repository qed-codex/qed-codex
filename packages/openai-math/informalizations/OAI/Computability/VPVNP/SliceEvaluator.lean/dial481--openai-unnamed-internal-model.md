---
{
  "module": "OAI/Computability/VPVNP/SliceEvaluator.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceEvaluator.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceEvaluator.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The path-counting evaluator on a finite geometric slice

For a nonempty finite zero set, the quotient by its vanishing ideal supplies the labels in
equation (8.2). A scan of the monomials through the point-count bound selects a basis
starting with the unit. The coordinate at this unit, followed by the constant coordinate in
a power basis of the slice field, gives the normalized functional. The number of accepting
matrix-index paths for each exponent vector reduces to the value of that functional.


### `exists_monomial_listing`

 Enumerate all exponent tuples of total degree at most `N`, with the zero tuple
first. Distinct tuples can give the same monomial value in the algebra. 

### `primeCoordinate`

 Constant coordinate of the prime-field power basis of the finite slice field. 

### `Presentation`

 The ordered monomial list, the retained independent entries, and the index of the unit. 

### `Presentation.lastIndex`

 Last valid index in the finite list of monomials used to choose a basis of the coordinate
  algebra. 

### `Presentation.listing`

 Enumerate the coordinate monomials through degree `N`, with the constant monomial in
  position zero. 

### `Presentation.basis`

 Basis of the coordinate algebra formed by retaining each listed monomial that increases
  the span of its predecessors. 

### `Presentation.unitIndex`

 Greedy basis index of the constant monomial one, used to extract its coordinate in the
  normalized functional. 

### `evaluator_for_listing`

 The selected basis of any listing of all bounded monomials beginning with one. 

### `Presentation.functional`

 Coordinate on the unit of the slice algebra followed by the constant coefficient in the
prime-field power basis of the slice field. 

### `Presentation.branchCount`

 Integer number of the evaluator's successful matrix-index paths. 

### `exists_sliceEvaluator`

 Given a finite nonempty slice, one basis and one normalized linear functional count
every exponent vector, at every input width, and the chosen labels solve all the equations.
The monomial listing has at most `(N + 1) ^ t` entries. 
