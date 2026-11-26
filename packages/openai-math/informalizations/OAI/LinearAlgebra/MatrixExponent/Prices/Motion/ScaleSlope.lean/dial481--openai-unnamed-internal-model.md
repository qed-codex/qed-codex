---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Prices/Motion/ScaleSlope.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Prices/Motion/ScaleSlope.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Prices/Motion/ScaleSlope.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A supporting slope for the displacement profile

Minimize the distance to the fixed set plus a small linear tilt. This
gives a supporting line of strictly negative slope at the chosen
radius without differentiating the distance to the moving fixed set.


### `RationalSecants`

 Convexity at rational triples is enough for decreasing profiles. 

### `Kink`

 Uniform two-sided little-o estimate at the onset of displacement. 

### `first_displacement`

 Each radius t selects a profile R t vanishing from that radius on.
Its earlier values bound the change in the projection distance f. 


# Finite realizations of geodesic expressions

Every finite set of expressions can be realized at one spectral point.
When a missing expression is added, all previously correct expressions
keep their original sites and prices.



# Completing a spectral placement

Pairwise distances of formal terms are independent of the finite model.
Use larger finite models to prove the triangle and comparison inequalities
for these distances, and pass to metric completion.



# Finite prices on geodesic terms

These constructions precede squared-distance comparison and metric
completion. In particular they can be used to establish comparison.



# Rescaled limits of spectral wire metrics

Take the ultralimit on sequences of bounded rescaled displacement.
Distance zero need not be quotiented out for wire tests or segments.

