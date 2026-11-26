---
{
  "module": "OAI/Computability/VPVNP/SpectralGeometry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralGeometry.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralGeometry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Spectral wire geometry and compression estimates

In Theorem 4.2 of *VP and VNP differ over every field*, the unit cube's basis
vertices have total distance `√(j * (j - 1))` to their centroid, for a group
of size `j`. Equation (4.5) uses two such groups and charges the wire between
their centroids in proportion to its length `√(1/s + 1/t)`. Lemma 6.2 uses
the squared-distance CAT(0) inequality to reduce the weighted energy of the
six-party wire motif. Appendix A.3 obtains its endpoint-coupling bound by
splitting a two-row cost table and shrinking the range of its column gaps.


### `starLength`

 Total length of the star from the centroid to a group of basis vertices. 

### `starLength_split`

 Splitting the star at two centroids saves strictly more than half a unit
on the terminal wires, before paying for the wire between the centroids. 

### `balancedCut_strictGap`

 The strict gap between the star bound (4.4) and the leading term of (4.5).
The balance conditions say that each side contains at least one third of the
terminals. The inequality remains strict at the threshold `s + t = 18 * C²`. 

### `subsetCentroid`

 The centroid of the standard basis vertices indexed by a subset. 

### `basis_dist_subsetCentroid_sq`

 Distance from a standard basis vertex in a subset to that subset's centroid. 

### `subsetCentroid_star_length`

 Total terminal-to-centroid length of one side of the balanced layout. 

### `disjoint_subsetCentroids_inner`

 Disjoint sides of a cut have orthogonal centroids. 

### `disjoint_subsetCentroids_dist`

 The length of the wire joining the two side centroids in the balanced layout of (4.5). 

### `basisCentroid`

 Centroid of the standard basis vertices of the full cube. 

### `basisCentroid_minimizes`

 Among all centers, the centroid minimizes the total distance to the basis vertices. 

### `balancedLayout_strict`

 A balanced two-centroid layout has strictly less total weighted wire length
than the single-center layout, for every choice of the single center. The
terminal wires have unit cost and the wire between centroids has weight `C`. 

### `sixParty_energy`

 Lemma 6.2. The two demand edges are `ab` and `cd`. Each group of four
supply edges receives masses `8/31, 4/31, 40/93, 16/31`, totaling `4/3`. 

### `EndpointTable`

 A table on the endpoint choices of two intervals. `false` denotes the first endpoint. 

### `columnGap`

 The difference between the two rows in column `j`. 

### `gapMidpoint`

 With two columns the midpoint between the maximum and minimum gap is their average. 

### `splitTable`

 The `true` branch is the positive split and lowers entries of row zero. The negative
split lowers entries of row one. 

### `leafTable`

 Follow the specified sequence of positive and negative splits from the root table. 

### `leafTable_gapDifference`

 At a leaf the difference of the two column gaps is exactly the initial difference
multiplied by one half per split. 

### `leafTable_columnGap_mem`

 The gap in each column stays in the initial interval at every stage. 

### `EndpointCoupling`

 A joint distribution with endpoint marginals `(1-u,u)` and `(1-v,v)`. 

### `EndpointCoupling.mass`

 Joint mass at each pair of endpoints, with row and column sums prescribed by the two
  interpolation parameters. 

### `independentCoupling`

 Independent choices of the two endpoints. 

### `EndpointCoupling.cost`

 Expected value of the four entries under the coupling. 

### `coupling_cost_sub`

 Equal marginals force the signed difference of joint masses to be a multiple of the
alternating table. Only the difference of the two column gaps contributes to its cost. 

### `coupling_leaf_bound`

 The scalar coupling estimate at depth `path.length` in Appendix A.3. In particular
`ρ` can be the independent coupling, while `π` may be any coupling of the endpoints. 
