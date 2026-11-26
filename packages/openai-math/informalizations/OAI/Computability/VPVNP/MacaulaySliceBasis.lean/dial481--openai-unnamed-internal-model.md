---
{
  "module": "OAI/Computability/VPVNP/MacaulaySliceBasis.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulaySliceBasis.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulaySliceBasis.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Numeric basis queries for a finite reduced slice

For an indexed system of equations and a known bound on the finite geometric
zero set, these are the dimension, monomial basis ordinals and matrix entries
from Lemma 8.2. The field cardinality is a numeric input. Correctness uses the
proved effective weak Nullstellensatz and equality of the coefficient routine
with the coefficients of the defining equations.


### `QueryData`

 Numeric input to the finite-slice queries. 

### `QueryData.fieldOrder`

 Numeric cardinality of the finite ground field used in the Frobenius queries. 

### `QueryData.degreeBound`

 Supplied upper bound on the total degrees of the indexed defining equations. 

### `QueryData.pointBound`

 Supplied bound on the number of geometric points, also used to enumerate candidate basis
  monomials. 

### `QueryData.getCoeff`

 Look up the coefficient of an exponent tuple in an indexed defining equation. 

### `targetDegree`

 Maximum degree of any target monomial in a multiplication or Frobenius query. 

### `certificateDegree`

 Effective Nullstellensatz certificate degree used to bound the radical membership
computation for the target monomials. 

### `powerExponent`

 Ceiling logarithm of the certificate degree in base the ground-field order, giving the
number of Frobenius iterations. 

### `power`

 Power to which the candidate monomials are raised for the radical membership test. 

### `multiplierDegree`

 Degree bound for multipliers in the Macaulay equation rows, obtained by adding the
certificate degree to the powered target degree. 

### `columnDegree`

 Maximum total degree indexed by the columns, allowing a multiplier times any defining
equation. 

### `equations`

 Coefficient matrix of all bounded monomial multiples of the defining equations, with
entries read from the supplied coefficient lookup. 

### `monomials`

 Coefficient rows of the powered candidate monomials, indexed by their original ordinals up
to the point bound. 

### `dimension`

 Rank gained by appending the powered monomial rows to the equation matrix. For a presented
finite slice this computes its reduced coordinate algebra dimension. 

### `basisIndex`

 Return the original monomial ordinal for a given position among the rows selected greedily
after the equation rows. 

### `Operation`

 The two linear transformations queried in Lemma 8.2. 

### `target`

 Exponent tuple after multiplying by the selected variable or raising the monomial to the
ground-field order. 

### `matrixEntry`

 Matrix column `j`, row `i`, in dense basis coordinates. 

### `Presents`

 Agreement of the numerical field order, degree bound and entry oracle with the equations. 

### `points`

 Common zero set of the defining equations in the extension field. 

### `quotientMap`

 Send a polynomial over the ground field to its class modulo the vanishing ideal of the
common zero set. 

### `listing`

 Enumerate the classes of candidate monomials in the reduced coordinate algebra using dense
monomial ordinals. 

### `exists_basis`

 The matrix-rank algorithm actually indexes a basis of the reduced
coordinate algebra. Its first vector is the unit for a nonempty slice. 

### `dimension_eq`

 The size returned by the two rank queries is the reduced algebra dimension. 

### `coordinate_eq_repr`

 Any monomial of degree at most the target-degree bound has the coordinates
returned by the row algorithm, restricted to dense basis ordinals. 

### `Operation.apply`

 Multiply by one coordinate or apply the ground-field cardinality power. 

### `matrixEntry_eq_repr`

 The actual matrix-entry routine returns the coefficient of multiplying
the `j`-th basis monomial by a label or raising it to the field cardinality. 

### `finite_slice_coordinate_queries`

 Lemma 8.2's basis, dimension and coordinate values for the indexed finite
slice. The query functions take the scalar coefficient algorithm as input. 
