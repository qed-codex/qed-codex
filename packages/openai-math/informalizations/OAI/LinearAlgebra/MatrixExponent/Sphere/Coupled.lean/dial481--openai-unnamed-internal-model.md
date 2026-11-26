---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/Coupled.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Coupled.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Coupled.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Laurent reconstruction for moving insertions

Use a common denominator. At a point with pole bound `d`, remove
`(X-z)^d` from the denominator. Coefficient `i` of the resulting regular
quotient is Laurent coefficient `i-d`. The reconstruction weights do not
depend on the numerator, so they act simultaneously on every tensor entry.


### `poles`

 Polynomial denominator for the specified bounds at distinct marks. 

### `jet`

 Coefficient of degree `i` in the regular quotient `p(z + X) / q(z + X)`. 

### `laurent`

 Formal expansion of the quotient `p/q` at `z`. 

### `dvd_of_jet`

 Multiplying by the invertible regular denominator preserves vanishing
of the first `n` coefficients. 

### `reconstruct_regular`

 More regular evaluations than the numerator degree suffice to recover
every linear coefficient, including every Laurent jet. 

### `recover_coefficient`

 Regular evaluations recover even a specified coefficient at a pole. 

### `reconstruct_jets`

 The initial jets jointly determine any bounded-degree numerator
when their total length exceeds the degree bound. 

### `orders`

 At seams keep orders through `-L`, at insertion marks through `-1`,
and at the designated collector through `g*L`. 

### `reconstruct_motion`

 The same Laurent reconstruction weights work for all numerators bounded
at infinity after division by the common denominator. 

 # Reading Laurent coefficients in the doubled collision coordinate 


# Coupled motion in two coordinates

The two parameters are `z^P` and `z`, with `P` a characteristic
power. Pole bounds make the convolution at each order a finite sum.


### `coupled_coeff`

 Convolve the two Laurent expansions. The first coordinate moves at
`p^l` times the order of the second. No choice of numerator enters the
summation range. 


# Two-site fusion

Specialize the cluster expansion to offsets zero and one. Pairing the
translated modes with the reversed output wedge gives the matrix entry
used in transposition at a seam.


### `collision`

 Two sites at `c` and `c + u²`, scaled by `u` to their doubled
energies to remove the pole. Spectators stay at fixed positions. 

### `fusion_expansion`

 Exact through degree `N-1`, with no invertibility assumption on two. 


# Moving one insertion on a sphere

The affine trajectories consist of the identity and the constant maps
to the stationary marks. Clearing the finite collisions gives a numerator
whose degree does not exceed the denominator degree.


### `atPoint`

 Place the moving insertion at an arbitrary extension-field point. 

### `eval_sphere_over`

 This specialization is valid even at a transcendental point over a
finite field. 


# Laurent coefficients of a moving insertion

At a collision with a stationary mark only the two incident blocks are
fused. All other marks are spectators. Remove their weight and the
regular denominator from the truncated polynomial identity.


### `triple`

 Stationary modes, moving modes, then spectators. 

### `coeff_fusion_truncated`

 Laurent coefficient at order `i - H`, with common pole bound `H`.
The degree `2*i` includes the fixed weight of the spectators. 

### `coeff_fusion`

 At Laurent order `j` the two colliding states fuse through precisely
doubled energy `energy a + energy x + 2*j`, independently of the spectators. 

### `recover_fusion`

 Reconstruct the fusion coefficient from regular evaluations. The
weights depend only on the marks, pole bound, and coefficient index. 
