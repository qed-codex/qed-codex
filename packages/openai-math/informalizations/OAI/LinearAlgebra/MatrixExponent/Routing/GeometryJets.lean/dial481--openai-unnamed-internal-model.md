---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Routing/GeometryJets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Routing/GeometryJets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Routing/GeometryJets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selecting fusion terms by a common functional

After clearing poles a family is a polynomial of degree at most `N`.
The order at infinity is then `N - P.natDegree`. A single functional
annihilating the span of cheap tensors keeps the total order of the
first surviving coefficients over all collision charts at most `N`.
Energies are recorded in half-integer units.


### `select_fusions`

 Each local jet lies in the span of candidates costing at most twice
its order. If one value survives modulo `W`, select a surviving candidate
in every chart with a *joint* budget of twice the degree bound. 


# Secant widths and incidence energy

The unit-mass transport inequality in the proof of the secant bound gives a
width for each line, with a bound on the sum of their squares. Transport along
a short segment, followed by squared distance comparison, lets us use those
widths directly, without introducing angles or first variation.


### `secant_comparison`

 The transport bound controls the loss in the law of cosines, summed
over the points incident with a line. 

### `incidence_of_widths`

 Raw sums over flags. In a biregular graph the normalized left hand
side uses the uniform distribution on each class of vertices. 

### `SecantBound`

 The fused widths on the retained lines, after dropping the nonnegative
contributions of omitted secants. Here `n + 1` counts *all* secants
through each point. This is the input from the spectral spaces argument. 

### `regular_incidence`

 The projective degrees are `s = q+1`, `j = n+1`. For affine points
of order `Q` with `q+1` retained directions they are `s = n = Q`,
`j = q+1`. In both cases `q*n ≤ j*s`. 

 A slope in the base field, or the vertical direction. 

 Finite arrangements of affine points and their secants. 

### `Secants`

 Unit-mass conclusion of the secant argument, expressed with the
transport bounds for fused widths. `n+1` bounds the number of secants
through each marked point. 


# Deleting singleton blocks

The collision parameters are the secant directions and infinity.
For a singleton block testing its own site in the transport inequality
shows that its width pays at least the distance from the center.


### `CollisionBound`

 Input from the rational-function fusion argument for sphere forms.
Finite collision parameters use the negative of the slope. 


# Clearing all poles of the moving sphere form

A marked point (a,b) has moving position aX+bY. For each
pair of points remove its vanishing linear factor from the common
denominator. This gives a polynomial contraction kernel and works
over any coefficient algebra, including truncated local rings.


### `local_correlator`

 After factoring a common scalar, the local polynomial is the
normalized motion kernel at every finite order. 

 Reading polynomial coefficients from truncated local fusion identities. 

### `jets_of_fusion`

 The same scalar multiplies all coordinates, so after clearing the
denominator the jet still lies in the span of low energy terms. 
