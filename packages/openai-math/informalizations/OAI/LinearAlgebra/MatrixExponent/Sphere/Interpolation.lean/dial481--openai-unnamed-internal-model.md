---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/Interpolation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Interpolation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Interpolation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Translation of a contraction at a nilpotent parameter

The negative binomial expansion truncates because the parameter is nilpotent.
All coefficients are integral and the proof uses no division.


### `kernel_translate`

 Translation of the mode at the moving point against one fixed spectator. 


# The two binomial transforms at the middle site

Vandermonde's identity and a finite difference of a row of Pascal's
triangle give integral identities, valid also after reduction modulo two.


### `binom_difference`

 A signed difference raises the offset of the lower binomial index by one. 


# The three-point fermion kernel

The points are zero, one and infinity. The infinity pairing uses the
ordinary dual basis, with no factor of a square root of minus one.
`dual` denotes a triangular change of modes at the middle point.


### `energy`

 Twice the energy of a word of generators. 

### `pairing_lower`

 The reflected modes are integral combinations of modes of no greater
energy. Both binomial identities hold after reduction in any characteristic. 


# The sphere kernel and motion of one site

A mode contraction is polynomial in the reciprocal separation. For a
nilpotent displacement `u²`, the translated separation can be inverted
exactly by a finite geometric sum.


### `coeff_shifted`

 Expand the moving mode at the center, with its doubled-energy weight. 

### `shifted_add`

 Composing displacements of the reciprocal separation adds their offsets. 


# Interpolation at auxiliary marks

Clearing common denominators converts vanishing at the auxiliary marks to
a polynomial identity. Evaluating it at a pole of maximal order isolates
one coefficient. This argument works in every characteristic.


### `cauchy_span_degrees`

 The total pole order suffices, even if the bound varies by site. 

### `cauchy_span`

 Sufficiently many pole-free evaluations span all covectors on distinct
pairs of a pole and a mode. The bound on the number of points is polynomial. 
