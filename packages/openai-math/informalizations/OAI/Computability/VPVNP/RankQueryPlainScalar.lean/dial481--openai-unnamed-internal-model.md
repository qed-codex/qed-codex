---
{
  "module": "OAI/Computability/VPVNP/RankQueryPlainScalar.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryPlainScalar.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryPlainScalar.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scalar-entry routine for an ordinary determinant

The Cramer minors of Appendix D.2 have constant entries in the polynomial
variable. At degree zero this routine reads the chosen entry once. At positive
degree it emits a zero scalar. Both arms restore the binary index bank and
apply the sign requested by the Schur factor.


### `readPorts`

 Route the Macaulay row and column inputs to the query registers and the entry result to the
scalar accumulator. 

### `degreeTest`

 Register six contains the zero word. The branch writes the degree-zero
indicator into output word zero, using the same bank as the Gram accessor. 

### `arm`

 Select the matrix-entry reader on tag one and the zero-scalar writer on every other tag. 

### `machine`

 Test the requested coefficient degree, read the entry or emit zero, then apply the
requested sign. 

### `entry`

 Regard a constant matrix as a polynomial matrix by putting each entry in degree zero. 

### `testClock`

 Step bound for testing the coefficient degree on binary words of width `w`. 

### `clock`

 Step budget for the degree test, scalar read or zero output, and sign adjustment. 

### `space`

 Stack-space budget for the degree test and scalar reader followed by sign adjustment. 
