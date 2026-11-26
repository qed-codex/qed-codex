---
{
  "module": "OAI/Computability/VPVNP/JointLabelBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointLabelBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointLabelBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Degree and coefficient bounds for the joint integer equations

In §8.1, a parse contributing to a grammar equation contains one label per
vertex of a full ordered binary tree with `n` leaves. The integer constant
subtracted from its parse count comes from the clocked accepting paths. The
additional motif equations depend only on the fixed integral tensors.


### `acceptingCount_le`

 Every accepting path has its canonical string of clocked choices. 

### `grammarEquation_totalDegree_le`

 The designated query is homogeneous of degree `2n - 1` before
subtraction of its integer constant. 

### `parseExponent`

 An exponent bounding the parse count. The factors account for ordered
tree shapes, child states and terminal variables. 

### `grammarExponent`

 An exponent bounding the magnitude of any integer grammar coefficient. 

### `motifEquation_totalDegree_le`

 One matrix entry per party is multiplied by a constant tensor coordinate
in each summand of a base identity. 

### `motifHeight`

 The fixed integer coefficient height of all local motif equations. 

### `equations_totalDegree_le`

 The union of the two systems preserves the separate degree estimates. 

### `coefficientExponent`

 One exponent for the entire joint system at length `n`. 

### `polynomiallyBounded_coefficientExponent`

 The joint height exponent is a polynomial bound for each fixed circuit
size exponent and fixed motif system, uniformly in the equation and monomial. 

### `equations_coeff_size_le`

 The unsigned bit length of any coefficient is at most the common exponent plus one. 
