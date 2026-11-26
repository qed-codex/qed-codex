---
{
  "module": "OAI/Computability/VPVNP/WalkEnergy.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WalkEnergy.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WalkEnergy.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Barycentric smoothing of a finite walk

Section 5.3 of *VP and VNP differ over every field* bounds the squared-distance
Poincaré constant of the Cesàro average of powers of a lazy walk. All energies
here multiply the paper's averages by the number of vertices. This common
factor cancels in the Poincaré inequality.


### `walkEnergy`

 Sum of squared lengths over the directed edges with the given weights. 

### `rowVariance`

 Row `i`'s mean squared distance from the previous configuration to its new center. 

### `walkEnergy_ge_variances`

 Repeated conditioning using the variance inequality in each row. The edge
energy of an `h`-step stationary walk pays for the displacement of its barycentric
iterate and for all the intermediate row variances (Section 5.3, page 18). 

### `walkEnergy_le_four_localEnergy`

 Comparison through each row's center for the lazy stochastic matrix in §5.3. 

### `pairVariance_le_displacement_variance`

 Comparison of pairwise squared distances through an intermediate configuration in §5.3. 

### `exists_walk_energy_le_average`

 Index selection in the CAT(0) walk averaging argument of Section 5.3.
The first half of the walk lengths pays for all the displacements. Each walk
in the second half pays for every energy in the first half. 

### `walk_poincare_coefficient`

 The scalar estimate converting the selected walk bound to the amplified
Poincaré coefficient `max 12 (48 * γ / t)` in Section 5.3. 

### `HasPoincareBound`

 Poincaré inequality in the normalization obtained by multiplying the paper's
variance and edge energy by the order of the graph. 

### `lazyWalk`

 Add a one-half probability of staying at the current vertex. 

### `cesaroWalk`

 Uniform mixture of lengths from one to `t`, inclusive. 

### `cesaroWalk_hasPoincareBound`

 The averaging estimate in Section 5.3. The Cesàro average of the first `2n`
lazy powers has a Poincaré bound independent of `γ` once the number of powers
is proportional to `γ`. Symmetry of the original matrix may be replaced by
stationarity of the uniform measure, expressed by its column sums. 
