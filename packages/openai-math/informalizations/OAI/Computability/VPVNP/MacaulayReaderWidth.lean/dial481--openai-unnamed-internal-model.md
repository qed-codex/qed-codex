---
{
  "module": "OAI/Computability/VPVNP/MacaulayReaderWidth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayReaderWidth.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayReaderWidth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # A common word width for the physical matrix readers

The input row counts include both original equations and pins. The field
size can be bounded before the prime is chosen. The same width covers all
legal rows and columns, label shifts and Frobenius target comparisons.


### `ReaderPlan`

 Counts and upper bounds used to choose a single word width for Macaulay reads across the
allowed fields, rows and target operations. 

### `ReaderPlan.arity`

 Number of variables in the slice equations and their monomials. 

### `ReaderPlan.equations`

 Number of original equations before the affine pin rows. 

### `ReaderPlan.pins`

 Number of affine pin equations added to form the slice. 

### `ReaderPlan.degree`

 Upper bound supplied for the degrees of the defining equations. 

### `ReaderPlan.points`

 Upper bound supplied for the number of geometric points in the slice. 

### `ReaderPlan.order`

 Upper bound on the cardinality of the finite ground field. 

### `target`

 Degree bound for target monomials obtained by multiplying by a variable or applying
Frobenius. 

### `certificate`

 Uniform effective Nullstellensatz degree bound using the plan's equation and target
degrees. 

### `power`

 Upper bound on the Frobenius power used in radical membership queries. Its exponent is the
ceiling binary logarithm of the certificate bound. 

### `multiplier`

 Degree allowance for monomials multiplying the equations, including the powered target
degree. 

### `column`

 Degree allowance for the coefficient columns of all products of a multiplier with a
defining equation. 

### `source`

 Common degree bound for source monomials in both equation multiples and the appended
monomial rows. 

### `scale`

 Common upper bound on exponent scaling for ordinary, powered and Frobenius-target reads. 

### `pairWidth`

 Word width sufficient for the pair scan using the plan's largest source degree, column
degree, scale and marked coordinate. 

### `addressLimit`

 The dimensions can be bounded by the raw address ranges even though
the physical caller uses dense ordinals. 

### `addressBits`

 Bit width obtained by taking the ceiling binary logarithm of the plan's address limit. 

### `wordWidth`

 Common register width covering the input addresses, the row decoder's intermediate values
and the exponent scan. 

### `Covers`

 The slice query has field order at least two and fits the plan's bounds on field order,
equation degree and number of points. 

### `width_polynomial`

 The physical word width is bounded independently of the varying row
and column ordinals and the operation being queried. 
