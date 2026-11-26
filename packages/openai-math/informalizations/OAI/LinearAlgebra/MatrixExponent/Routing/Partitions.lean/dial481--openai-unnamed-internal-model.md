---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Routing/Partitions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Routing/Partitions.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Routing/Partitions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Routing permutations of a finite product

Peel off perfect matchings between the source and destination first coordinates.
Each matching becomes a row by permuting second coordinates before and after
the given permutation. This is an existence result without runtime bounds.


### `stays_inside`

 A bijection fixing the row of every point outside `s` preserves the
remaining rows as a set. 

### `perm_factor`

 Any permutation factors into permutations of columns, rows, then columns. 


# Centers for finite placements and bounded group orbits

Minimizing the common upper bound of a family of strongly convex
functions treats both the average and the largest squared distance.


### `minimize`

 Minimize a simultaneous upper bound. The midpoint estimate forces any
decreasing minimizing sequence to be Cauchy. 

### `Comparison.orbit`

 The center of a bounded orbit is fixed and within half the squared bound of
the starting point. The bound is on squared distances. 


# Matching independent partitions

The partition represented by `g` is the coset `g H` of the stabilizer of
the original partition. An independent pair `e, f` of lists can be matched
with a third list in two ways. The group-theoretic condition below is all
that the displacement estimate uses about matching.


### `Bridges`

 `v` fixes the `e`-partitions, `w` takes them to their `g`-translates,
and both take the `f`-partitions to the same third list. 


# Independent partition lists admit simultaneous matching

In each fiber write the address as a product of the first list of names
and the second list with its unused coordinates. Three-stage permutation
routing then gives the common third list needed in the displacement estimate.
The same argument works in a smaller group closed under this factorization.


### `bridges_of_factor`

 A factorization alternating between the two joint stabilizers produces
the two matches required for the displacement estimate. 

### `preserving`

 The permutations preserving each name, simultaneously for all instances. 

### `PermSystem`

 A family of permutation functions. An instance index determines the
address format, and a world supplies the input at every instance. Fixed
families and the three factors in a product chart must be available. 

### `pull`

 Require membership on every input. 

### `bridges_of_product`

 The joint names are coordinates on a product in each base fiber.
Unused coordinates may be included in either of the two factors. 


# Displacement on a single plane

We only need to match *pairs* of partitions. For at least half of the
ordered pairs the matching argument bounds the diameter of the orbit by
twice the pair distance. Squaring and averaging gives a diameter bound
in terms of the variance of the affine placement.


### `Incidence`

 The incidence estimate at `q ≥ 100` in flag-counting normalization. 

### `PlaneAction`

 Cosets for the affine point partitions and their projections along
each direction. `l` gives the affine line through a flag. 

### `PlaneAction.fixed`

 Given a point fixed by the base and one fixed by each direction, there
is a plane-fixed point controlled by the mean base-to-direction energy. 


# Successive geodesic means

The sample space is a full finite power. Conditioning on the tail of a
tuple reduces the mean squared error to a one-step variance computation.


### `sampleMean`

 Mean of an ordered tuple, read from its last entry to its first. 

### `sampleMean_error`

 The expected squared error of the sample mean is at most the variance
of one draw divided by the number of independent draws. 


# Incidence as inequalities in finitely many geodesic terms

Replace the barycenter by a random successive mean. Its mean squared
error is uniformly controlled by the second moment about any anchor.
The resulting tests are linear in squared distances. They pass through
uniform finite averages and pointwise limits without any choice of
compatible barycenters.


### `joint`

 Cost of moving both sides of the flag distribution to `z`. 


# Completing a table of squared distances on geodesic terms

The table need not separate terms. Metric completion identifies terms
of zero distance and extends both interpolation and the group action.


### `Table`

 Comparison and pseudometric laws on a table of squared distances. 

### `Table.realize`

 An invariant table gives an isometric action on a complete space. 
