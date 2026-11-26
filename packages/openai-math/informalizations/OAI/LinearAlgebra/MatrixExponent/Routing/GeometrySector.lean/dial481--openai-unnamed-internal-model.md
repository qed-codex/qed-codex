---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Routing/GeometrySector.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Routing/GeometrySector.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Routing/GeometrySector.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The metric consequence of shifted crossing

The two original wires connect opposite terminals. On either cut we
may move terminals to a pair of centers and connect those centers.
At least one cut must pay the full cost of the original wires.



# The parallelogram law from shifted crossing

There is no regularity assumption on the seminorm. The directional
savings on two cuts are estimated using a finite difference at an
approximate minimizer of `p (r • (z+w) + z) - r * p (z+w)`.


### `gain`

 The sum of the two directional savings approaches the norm of
the sum of the directions. 


# Geodesic sectors

Two rays from a common origin whose equal-time distances grow linearly
span an affine quadrant. Only Busemann convexity is used here.


### `exists_sector`

 Boundary values are preserved up to zero distance, since the
ambient metric need not separate points. 


# Four-terminal wire prices from shifted crossings

Each summand of the crossing moves to the two centers of its cut.
There its separated factorization costs a single wire. All placements
allow coincidences, including at the two centers.


### `shifted_metric`

 Remove the constant loss by using arbitrarily large shifted crossings. 
