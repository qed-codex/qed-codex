---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Verification/Geometry/Cuts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Verification/Geometry/Cuts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Verification/Geometry/Cuts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Localizing a normalized affine parameter line

A point of a larger subring selects the prime on the normalization.
If the inverse of an element of the larger ring belongs to the
localization, clearing its denominator and evaluating at the point
shows that its numerator is also invertible there.


 # Extending rational points to the integral closure 

### `extend_point`

 Every rational point of the subalgebra extends over its integral closure. 

 # A branch of the deformation curve at the prescribed point 

### `exists_branch`

 Normalize over the parameter, then choose the prime below a point
on the integral closure of the affine algebra. This works even when
the original point is singular. 

 # Isolation at a rational point of affine space 

 # Rational cuts avoiding finitely many minimal primes 


# Isolating a point by rational combinations of given equations

One cut removes all positive-dimensional components through the
chosen point. The length of every chain remaining below it drops
by at least one. Applied to the zero ideal this gives a square
system of equations.


 # Transferring isolation to extended coefficients and to separate coordinates 

### `point_le`

 Every ideal fixing all coordinates contains the evaluation kernel. 

### `Isolated.map`

 An isolated rational point remains isolated under a field extension. 

### `difference`

 Equality of a repeated coordinate with its value in the reference block. 

### `Isolated.separate`

 Replace a shared block of coordinates by separate copies, imposing equality to one copy. 

 # Height of a rational point by successively evaluating its coordinates 


# Perturbing a square system at an isolated point

Add one variable and subtract a multiple of it from each equation.
No minimal prime through the given point can contain the new variable.
Otherwise isolation in the original fiber forces that prime to equal
the maximal ideal, whose height exceeds the number of equations.


 # The function field of a component of the perturbed system 


# Isolation from finite witness fibers and a unique common output

Each coordinate has finitely many possible values. Its split
annihilating polynomial belongs to every prime over the equations.
At the specified point only one linear factor can vanish.

