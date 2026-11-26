---
{
  "module": "OAI/Computability/VPVNP/NormRigidity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/NormRigidity.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/NormRigidity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Norm rigidity from the shifted crossing

The two flattening bounds in Theorem 3.1 give a geometric inequality on the
cost of placing the auxiliary wire endpoints. This file derives Lemma 3.2's
inner-product conclusion from that inequality. If the dual quadratic bound
fails at smooth points, both costs strictly decrease along suitable directions.
Dense differentiability of the norm supplies supporting functionals and extends
the estimate to arbitrary vectors.


### `norm_deriv_neg`

 The norm's derivative at the opposite vector is the opposite functional. 

### `eventually_lt_of_deriv_neg`

 A negative derivative at zero forces a decrease for every sufficiently
small positive step, without any derivative assumptions away from zero. 

### `weighted_norm_motion`

 A common movement of two endpoints decreases their weighted lengths even
after paying the linear cost for the new segment. 

### `exists_norm_derivative_approx`

 Norm derivatives approximate the norm from below in every direction. 

### `CrossingPlacement`

 The two crossing cuts use opposite partners at the terminal marked by `y`.
The central-wire costs are the two square roots in Theorem 3.1. 

### `crossing_descent_directions`

 A strict failure of the dual norm inequality yields simultaneous strict descent
directions for the two crossing costs. 

### `dual_bound_of_placement`

 A placement satisfying the crossing inequality forces the dual quadratic
estimate on any two derivatives of the norm, as in equation (3.1). 

### `parallelogram_le_of_dual_bound`

 The two dual combinations bound the weighted evaluations at `a + b` and `a - b`.
Approximate support functionals then give the upper half of the parallelogram law. 

### `parallelogram_of_dual_bound`

 Applying the upper parallelogram estimate to the sum and difference gives equality. 

### `innerProduct_of_dual_bound`

 The real norm comes from an inner product whenever its approximate support
functionals satisfy the dual estimate (3.1). 

### `innerProduct_of_placement`

 The geometric implication of Lemma 3.2. In a finite-dimensional real
space the two crossing placement costs force the given norm to be Euclidean. 

### `exponent_le_max_add_one`

 The cost of adding two tensor summands contributes at most one bit beyond
the larger base-two exponent. 

### `limit_le_max_of_two_powers`

 For two exponentially scaled wire costs, subadditivity implies that the
target rate is bounded by the larger limiting cost. 

### `crossingPlacement_cost_limit`

 The four-terminal wire inequality at a common realization scale. The
two original wires have terminal-to-terminal lengths `2*x0` and `2*y0`. In each placement
the terminal links have lengths `xp,yp` or `xm,ym` and the two centers have
distances `2*ep` and `2*em`. The two crossing ranks may have different exponential rates. 

### `FiniteCrossingCost`

 The spectral inequality for the two placements of a finite, integer crossing.
The shared scale belongs to the realization of the eight points. 

### `crossingPlacement_of_finiteCosts`

 Theorem 3.1 turns the finite wire-cost inequality at one common realization
scale into the two geometric placement costs of Lemma 3.2. 

### `exists_homothety_mem`

 A translate of one positive rescaling of a finite configuration lies
entirely in any prescribed nonempty open set. 

### `dist_homothety`

 A translated positive rescaling multiplies every pair distance by its scale. 

### `EightPointCrossingCost`

 The two possible placements use eight roles. Roles 0 and 1 are the endpoints
of the first wire, 2 and 3 those of the second wire, and the last four are the
two pairs of auxiliary centers. The distances may vanish between distinct roles. 

### `placement_of_local_costs`

 From scaled spectral costs on every finite configuration in an open set,
obtain the two placement inequalities on the whole normed space. 

### `innerProduct_of_local_costs`

 A finite-dimensional norm is Euclidean if some nonempty open set satisfies
the two finite crossing costs at a common scale for every eight-point configuration. 

### `eightPointCost_of_spectrum`

 A spectral point bounds the finite cost at any eight labelled tensor parties. 

### `norm_rigidity`

 Lemma 3.2. If each finite subset of a nonempty open set in a real normed
space is realized up to scale by spectral wires over the fixed field, the
space's norm comes from an inner product. The proof works in every finite
dimension, including the real normed planes of the lemma. 
