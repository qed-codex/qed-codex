---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Routing/GeometrySharp.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Routing/GeometrySharp.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Routing/GeometrySharp.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform displacement from incidence

Average the plane sites over the incident planes at each line. The
projective estimate and the variance inequality then bound the mean
square deviation of these line sites by 1/18 of the line-plane energy.
The single-plane displacement estimate loses 160/9. Their product
80/81 is strictly less than one, so iteration gives a common fixed point.


### `contract`

 One simultaneous update, using two sets of barycenters. 

### `common_fixed`

 Summing the displacements of the contracting placements gives an
absolute bound, independent of the number of planes. 

### `uniform_displacement`

 Uniform displacement. The only group-specific inputs are generation,
nesting, and the affine partition action on each plane. 


# Variance survives adjoining a spectral site

The barycenter belongs to the closure of the finite geodesic terms.
Their costs are identical in any two realizations of the same prices.



# Generation by plane motions

A motion in a direct sum of subspaces factors into three motions along
the two summands. The factors act simultaneously across all instances.


### `PermSystem.motion_generate`

 Plane motions generate any group closed under the required factorizations. 

 Finite transport bounds at every block of every collision. 


# The limiting widths of collision blocks

The finite fusion terms have polynomially many energy patterns, so their
logarithmic overhead vanishes after normalization. Compactness gives a
single limit for every block, independent of the transport test site.


### `Saturation.collisions`

 The unit-mass sphere price profile implies the full collision
budget and the transport inequality on every block. 


# Bounded displacement for families of permutations

Here the group is the product of all the finite permutation groups. No
restriction on the computation of a permutation family is imposed.


### `permutation_displacement`

 Uniform displacement for arbitrary permutation families, conditional
on the two metric incidence inequalities. 


# Inputs to the finite detection theorem

Use the affine and projective links over an infinite extension of
the coefficient field. No extension is made to the actual tensors
in the local price tests.



# Sharp incidence estimates under a strict square saving

Points, lines and flags each carry their own uniform probability
measure. Regularity converts the sums over flags to these means.


### `SharpIncidence`

 The point barycenter serves both sets of sites. 

### `projective_of_saving`

 Points and lines of projective space over the finite field of
order `q`, in the characteristic of the coefficient field. 

### `affine_of_saving`

 Points in the affine plane of a finite extension and lines in
the `q+1` directions defined over the base field. 
