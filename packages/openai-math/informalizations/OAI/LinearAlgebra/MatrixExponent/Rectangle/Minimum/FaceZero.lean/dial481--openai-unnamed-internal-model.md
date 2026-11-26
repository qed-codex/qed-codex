---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Minimum/FaceZero.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Minimum/FaceZero.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Minimum/FaceZero.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Finite secants of a semiconvex defect along one ray 

### `Semiconvex.shift`

 Before subtracting the value at zero, the translated increment may
be negative. The subtracted increment is bounded below by a linear error. 

### `Semiconvex.envelope`

 One number controls the change near zero and gives a lower bound at
all larger arguments. No derivative at zero is needed. 


# Semiconvexity in reciprocal coordinates

Convexity and the one-sided transport bound make `D(r) + r` convex
and nondecreasing. A quadratic correction then absorbs the negative
reciprocal term left over after composition.


### `convex_quadratic_reciprocal`

 The difference of successive slopes has the sign of
`C * (a+x) * (a+y) * (a+z) + K`. 


# Translation of a truncated directional integral

After shifting the variable the interval loses a short prefix but gains a
nonnegative tail. On the overlap, the gain in the kernel is at least
`a / t^2`. A linear lower estimate for the defect thus gives a logarithmic gain.



# Dilation at a zero of the defect

A fixed interval of positive mass forces a strict decrease under dilation.
Continuity at zero controls the mass added below the lower cutoff.


 # The cost of translating a single coordinate 

### `increment`

 The logarithmic gain at intermediate distances pays for the possible
increase in the defect when the path switches coordinates. 


# Coordinate rays and radial paths in the positive orthant

Only *differences* of truncated directional integrals are needed.
Thus the common singular subtraction in the directional identity
cancels, even when the defect is positive at an intermediate point.


### `Comparison`

 The local directional comparison, in truncated form. 

### `path`

 First enlarge coordinate 0, then 1, then 2. 

 # Passing a directional comparison to a limiting face 

### `compare_limit`

 A common estimate near zero and an inverse-square tail let the
limiting comparison pass to a reciprocal face. 


# From a vanishing face to an interior zero

Compare the normal and tangential ray integrals on the same truncated
interval. Near zero their difference is bounded below by transport.
At infinity the tangential kernel has an integrable inverse-square bound.
On any fixed interval away from zero its integral vanishes in the face limit.


### `face_zero`

 A vanishing face and a uniform directional comparison up to that
face give a zero at a finite positive triple. 


# From directional potentials to price comparison

The derivative along a ray from an axis gives the defect. Inverting the
ray parameter converts the derivative to the kernel of the truncated
integral. Differences of the primitives have limits at both endpoints.


### `HasPotential`

 The comparison of axis limits is locally uniform in the
sense that one constant works throughout the positive box. 

 # Comparing a radial dilation with three coordinate increments 
