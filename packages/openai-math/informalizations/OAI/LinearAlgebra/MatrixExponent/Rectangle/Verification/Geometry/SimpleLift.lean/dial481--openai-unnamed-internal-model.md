---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Verification/Geometry/SimpleLift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Verification/Geometry/SimpleLift.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Verification/Geometry/SimpleLift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Equations with at most one product of affine forms 


# Covering correct products by conjunctions of accepting paths

For a given correct input, retain one path for each accepting seed.
Any input accepted by all of those paths has at least the same
accepting weight, so the strict gap forces it to be correct.


 # Defined division and nonzero tests as product equations 


# A polynomial system for one accepting path

Only nonzero tests and quotients introduce extra inverse variables.
Projecting away those variables recovers the original path on every
assignment of the inputs and registers.


 # Separating the matrix pair from the proposed product 

 # A system of affine equations with shared products and offsets 

 # Changing the coefficient field of the equations and their Jacobian 


# A simple solution specializing to an isolated one

Move the polynomial values along a ray whose direction is algebraically
independent over the original coefficients. Isolation supplies a component
on which the ray parameter varies. The values on this component are
algebraically independent over the original field, so the Jacobian is
invertible. Normalizing the curve gives a local ring for specialization.


 # The path equations with both input matrices fixed 


# Mixed derivatives of the verification equations

Subtract the Jacobian applied to the mixed derivatives of the unknowns.
The remainder is additive and vanishes on affine forms when the inputs
have vanishing mixed derivatives. Each shared product contributes two
products of first derivatives.



# Combining paths while sharing the same product claim

All path witnesses have disjoint names. One reserved variable permits
a test that a specified output coordinate differs from the true one.



# Isolating the correct product at algebraically independent inputs

A strict probability gap supplies a finite cover by conjunctions of
paths. Each conjunction excludes every false product even after
extending scalars. At least one conjunction is feasible generically.


 # Isolating a solution of one path by rational output measurements 

 # A square system using only the products from the original path 

### `jet`

 Fixing witnesses and measuring outputs adds only affine terms.
The rational combinations isolating the solution reuse every original
quadratic term, even when several equations need the same product. 
