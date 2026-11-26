---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Face/Contact.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Face/Contact.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Face/Contact.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The diagonal inequality from integer rectangular bounds

The homogeneous quadratic inequalities extend from positive integer
weights to positive real weights by a common rescaling and a limit.


 # The unique contact price at the square 


# Positive spectral contact on a homogeneous tripod

Lengths on the three arms determine three wire distances. The common-label
rate is homogeneous and convex along each arm, with transport cost at
most one per unit distance. In reciprocal coordinates its excess over
the harmonic benchmark satisfies the regularity hypotheses of the
strong minimum principle.


### `Tripod`

 The properties of common-label rates on a homogeneous spectral tripod
used for propagation. 

### `Tripod.boundary`

 At one contact there is no defect. The directional comparison then
forces the full positive polar boundary into the spectrum. 

### `propagation_of_tripod`

 It is enough to realize the initial contact in one tripod where
the directional identity holds locally. 


# Contact at infinity from a sharp dual threshold

Normalize the sum of the two short arms to two. Testing the spectral
formula just above inner exponent one half forces these arms to converge
to one, the long arm to escape, and the *absolute* diagonal defect to vanish.


### `Escapes`

 Contact in the limit as one arm escapes to infinity. 

### `losses`

 Completing the square separates three nonnegative losses. 


# Approaching a reciprocal face

The star bound and convexity along an unbounded arm make the
diagonal rate minus the length nonincreasing along that arm.
In reciprocal coordinates this gives a limit at the open face.


### `StarTripod`

 A tripod whose common-label rate satisfies the star spanning-tree bound. 

 # Uniform estimates tangential to a reciprocal face 


# The positive face as a three-coordinate defect

Splitting one tangential coordinate into two equal-role coordinates
allows the interior strong minimum principle to be used unchanged.


 # Passing the directional integral comparison to a face 

### `Uniform`

 The constant stays bounded as the first reciprocal length tends to
zero while the other two range over a compact positive box. 


# Spectral contact at infinity

The localized rate estimate gives a zero at one point of a reciprocal
face. The strong minimum principle first propagates it tangentially;
normal comparison then gives a finite contact on the tripod.


### `Localized`

 Truncation of the long arm at length `x`, with short arms of
unit length. 

### `StarTripod.boundary_of_limit`

 A zero at infinity on a homogeneous tripod realizes the entire
positive polar boundary in the space of spectral prices. 

### `dual_of_localization`

 A localized tripod with uniform comparison is the remaining
geometric input for the strict dual saving. 
