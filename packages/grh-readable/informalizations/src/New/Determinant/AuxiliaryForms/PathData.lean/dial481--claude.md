---
{
  "module": "src/New/Determinant/AuxiliaryForms/PathData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/PathData.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/PathData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Moduli, spaces, moves, path data and periods on the two grids

This file sets up the two grids of hermitian spaces attached to admissible data `D` and an `m`-fold
twist `ϑ`. A node is a triple `(z, a, b)`: the space `Y^a_b` for `z = false` and `Ỹ^b_a` for
`z = true`. The element `ϖ = π_M = New.Data.piM`, of norm `M`, generates the product of the chosen
places, and Q is the product of the places of `ϑ`. This file defines the moduli of the grids, the
spaces, characters, levels and moves at the nodes and edges, then functions on tuples of matrices
and the periods formed with them.

## Main definitions and results

* `New.Data.gridModulus`: the modulus `𝔪 = 𝔟 Q` with `𝔟 = ϖ ^ D.natB`. For the twist `1` it is `𝔟`
  (`New.Data.gridModulus_one_ideal`).
* `New.Data.liftMove`, `New.Data.transposedMove`: the theta lift `(a, b) → (a + 1, b)` and the
  transposed lift `(a, b + 1) → (a, b)` with a single matrix as finite datum.
* `New.Data.IsPathDatum`: functions of a matrix per edge of a path that are equivariant at the inner
  nodes and under the level `𝔟` at `Ỹ^m_0`, vanish unless the vertical edges (those whose character
  carries the twist) carry split injective matrices, and take sums of few roots of unity as values.
* `New.Data.gridPeriod`, `New.Data.IsProportional`: the period of path data, and the relation
  `Ψ ∝ Ξ`.

Notions from other files:
* `New.Modulus`: a nonzero ideal of O_E prime to its complex conjugate.
* `New.Data.MFoldTwist`: a twist ϑ whose tame part has ψ_wⁿ non-trivial for all w in Q and
  1 ≤ n ≤ m.
* `New.Data.GridIndex`, `New.Data.gridSigns`, `New.Data.gridParam`: the index set of a basis, the
  signs of the hermitian form and twice the parameter of the type at a node with an offset o; the
  grids have o = 0.
* `New.Exchange.IsEdgeFamily`: a family of characters over two pairs of conjugate cuspidal types
  which, with a polynomial, form an edge for the real Weil representation.



## The moduli and levels of the grids

* `New.Data.triangleModulus`: the modulus of the transposed lifts between the nodes `(0, b)`, whose
  datum is the indicator of an inclusion matrix: `𝔪₀ = ϖ Q` in grid `Y` and `𝔟 = ϖ ^ D.natB` in
  grid `Ỹ`. It divides the grid modulus (`New.Data.gridModulus_ideal_le_triangleModulus_ideal`).


### `instNeZeroNatB`

 `D.natB` is nonzero. 

### `gridLevelGen`

 The element `ϖ ^ D.natB` of the ring of integers of `E`, with `ϖ = D.piM` the generator of
the product of the chosen places. 

### `gridModulus`

 The modulus `ϖ^{natB} Q` of the twist `ϑ`: the product of the chosen places to the power
`D.natB`, times the product of the places of `ϑ`. 

### `triangleTwist`

 The twist whose places divide `New.Data.triangleModulus`: `ϑ` in the grid `false`, the trivial
twist in the grid `true`. 

### `triangleExponent`

 The exponent of the chosen places in `New.Data.triangleModulus`: `1` in the grid `false`,
`D.natB` in the grid `true`. 

### `instNeZeroTriangleExponent`

 The exponent `D.triangleExponent z` is nonzero in both grids. 

### `triangleModulus`

 The modulus at the nodes `(0, b)` of grid `z` (the triangle of that grid), used for the
transposed lifts `New.Data.pointTransposedLift` between them: `𝔪₀ = ϖ Q`, with `Q` the product of
the places of `ϑ`, if `z` is false, and `𝔟 = ϖ ^ D.natB` if `z` is true. Here `ϖ = D.piM`. 

### `gridModulus_ideal_le_triangleModulus_ideal`

 Let `ϑ` be an `m`-fold twist, `Q` the product of its places, `ϖ = D.piM` the generator of the
product of the chosen places, and `b = D.natB ≥ 1`. The triangle modulus of grid `z`, which is
`ϖ Q` for `z = false` (grid `Y`) and `ϖ ^ b` for `z = true` (grid `Ỹ`), divides the grid modulus
`ϖ ^ b Q`; this is stated as an inclusion of ideals. 

### `reduceToTriangle`

 Reduction from the residue ring of `New.Data.gridModulus` = ϖ^b Q to that of
`New.Data.triangleModulus`, which is ϖQ for z false and ϖ^b for z true, with b = `D.natB`. 


## Spaces, characters, levels and moves of the two grids

The node `(false, a, b)` is `Y^a_b`, the node `(true, a, b)` is `Ỹ^b_a`, and `Y^0_j` is the space
`Y_j`. Throughout, `ϖ` generates the product of the chosen places, `𝔟 = ϖ ^ D.natB`, and Q is the
product of the places of the twist ϑ.


 ### Spaces, types, characters and levels 

### `gridSpace`

 The hermitian spaces at the nodes `(z, i, j)` with offset `o`: the triangles are `i = 0` and the
grids `o = 0`. For `o = 0` they are `Y_j` along the first column of grid `Y` and `Y₀` plus a line
at the corner of grid `Ỹ`. At `i = j = 0` offset `o` multiplies the space by `(-1) ^ o`. All other
spaces are orthogonal sums of lines with the signs `gridSigns`. 

### `gridKernel`

 The pair of kernels of the types at a node: at `false` that of the parameter `gridParam` and at
`true` that of its negative. 

### `GridForm`

 The forms of the kernel `gridKernel` at `true` at a node, that is of the parameter `-gridParam`:
conjugate forms in grid `Y`, and forms in grid `Ỹ`, whose `gridParam` carries the opposite sign. 

### `gridChar`

 The character of U(1)(𝔸) of an edge of index `l` at an end of index type `n`. Write
`μ = D.untwistedLiftChar (l + 1)`, so that `D.liftChar ξ (l + 1) = μ ξ` for a tame character `ξ`,
and `υ = WeilData.upsilonU1` for the splitting character restricted to the norm-one ideles. For a
vertical edge (`c = true`) the character is `μ ϑ ^ (l + 1) υ ^ ⌊card n / 2⌋`. For a horizontal edge
(`c = false`) it is `μ υ ^ ⌈card n / 2⌉`, without twist. 

### `gridTamePart`

 The tame part of `gridChar`: that of `liftChar` with the twist `ϑ ^ (l + 1)` if `c`, and with
the trivial twist otherwise. 

### `triangleGLCard`

 The order of the general linear group of the node `(0, n)` modulo `triangleModulus z ϑ`. 

### `GridNode`

 The nodes of the two grids: `(false, i, j)` is the space `Y^i_j` of grid `Y`, and
`(true, i, j)` is the space `Ỹ^j_i` of grid `Ỹ`. 

### `NodeIndex`

 The index set of a node. 

### `nodeLevel`

 The level at node p, a subgroup of GL over the residue ring of 𝔪 = 𝔟Q: trivial at the nodes
(false, 0, b), that is at Y_b = Y^{0}_{b}, and the kernel of reduction modulo 𝔟 elsewhere. 

### `levelIndex`

 The index of the level `New.Data.nodeLevel` at node (a, b) of grid z in the general linear
group, as a complex number. 

### `gridLevelForms`

 The forms of level `𝔟`, the principal level of `New.Data.gridLevelGen`, at the node
`(true, 0, i)`, the space `Ỹ^i_0`. For `i = m` these are the forms at the start of every path. 

 ### Edges and identifications of spaces 

### `isConjKernelPair_gridKernel`

 At a node with i, j ≤ m the two types with kernels `New.Data.gridKernel` are cuspidal and
complex conjugates of each other. 

### `gridChar_hasWeight`

 The character `New.Data.gridChar` has weight `D.gridWeight c l n`, which is the exponent of `υ`
in it (`⌊card n / 2⌋` or `⌈card n / 2⌉`) minus `D.liftWeight (l + 1)`. Its tame part
`New.Data.gridTamePart` is the family of residue characters `ω ^ (l + 1)`, `ω = D.chiMLocal`, times
the tame part of `ϑ ^ (l + 1)` if `c` is true. 

### `isEdgeFamily_grid_succ_left`

 The step from the node `(i, j)` to `(i + 1, j)` of grid `z`, for `i + 1, j ≤ m` and a family
`ϑ x` of `m`-fold twists, is an edge family (`IsEdgeFamily`). The real Schwartz datum is the Fock
vector of `gridHarmonic`, a harmonic polynomial that is a highest weight vector for the lowest
`K`-types of both parameters. 

### `isEdgeFamily_grid_succ_right`

 The step from the node `(i, j)` to `(i, j + 1)` of grid `z`, for `i, j + 1 ≤ m` and a family
`ϑ x` of `m`-fold twists, is an edge family (`IsEdgeFamily`). 

### `gridSpace_diag`

 For j ≤ m, the space Ỹ^{j}_{j} equals the orthogonal sum of Y^{j}_{j} and the standard line of
sign (−1)^j, with the basis relabelled by the bijection `New.Data.gridDiagEquiv`. 

### `gridSpace_subdiag`

 The hermitian space `Ỹ^{j+1}_j` is the node `(j, j + 1)` of the grid `true`, and `Y^{j+1}_j` is
the node `(j + 1, j)` of the grid `false`; the first argument `0` of `gridSpace` is the offset,
which is `0` on the grids. There is a bijection `τ` of their basis indices that keeps the signs
`gridSigns` of the hermitian forms and such that `Ỹ^{j+1}_j` is `Y^{j+1}_j` with its basis
relabelled along `τ⁻¹`. 

 ### Transposed lifts and lifts 

### `pointTransposedLift`

 The transposed lift, from forms at `(0, b + 1)` to forms at `(0, b)` of grid z, with the datum
`New.Exchange.pointDatum` (the indicator of the inclusion matrix), times the cardinality
`triangleGLCard z ϑ b`. 

### `transposedChain`

 The composite of the transposed lifts `New.Data.pointTransposedLift` of grid z from the node
`(0, m)` to `(0, b)`: the identity for `b = m`, and zero by convention for `b > m`. It takes
conjugate forms from `Y_m` to `Y_b` in grid `Y`, and forms from `Ỹ^m_0` to `Ỹ^b_0` in grid `Ỹ`. 

### `transposedMove`

 The transposed theta lift (`New.Exchange.modTransposedLift`) from forms at `(a, b + 1)` to forms
at `(a, b)` in grid `z`, for the characters `gridChar ϑ (!z) b`. Its Schwartz datum is the indicator
of the matrix `y` modulo `𝔪` at the finite places, and at the infinite places it is given by the
joint harmonic polynomial `gridHarmonic` of the two nodes. 

### `liftMove`

 The theta lift (`New.Exchange.modLift`) from forms at `(a, b)` to forms at `(a + 1, b)` in grid
`z`, for the characters `gridChar ϑ z a`. Its Schwartz datum is the indicator of the matrix `y`
modulo `𝔪` at the finite places, and at the infinite places it is given by the joint harmonic
polynomial `gridHarmonic` of the two nodes. 

### `gridChar_det`

 Let `k` lie in `stdLevel D.E n'`, the stabiliser of the standard lattice in the finite adelic
unitary group of index type `n'`. The pair `(1, k)` is the point of the adelic unitary group of
signs `s` with real part `1` and finite part `k`, and `G.det` is its determinant. The character
`gridChar ϑ c l n` of U(1)(𝔸) at this determinant is `∏_{w ∣ 𝔪} ψ_w(det k mod w)`. Here
`𝔪 = gridModulus ϑ` is the product of the chosen places to the power `D.natB` times the product of
the places of the twist `ϑ`. The family `ψ = gridTamePart ϑ c l` of characters of the residue
fields is `ω ^ (l + 1)`, times the tame part of `ϑ ^ (l + 1)` if `c` is true, where
`ω = D.chiMLocal` is a fixed family that is trivial outside the chosen places. The index type `n`
of the character is unrelated to `n'` and does not affect the value. 

### `levelIndex_eq_card_GL_untwisted`

 Let `𝔪 = 𝔟 Q` be the grid modulus of the twist `ϑ`, with `𝔟 = ϖ ^ D.natB` the grid modulus of
the trivial twist, and let `n` be the basis index set of the node `(z, a, b)`. The number
`levelIndex ϑ z a b` is the index in `GL_n(O_E / 𝔪)` of the level `nodeLevel` of the node. In the
grid `Ỹ` (`z = true`), and in the grid `Y` for `a ≠ 0`, this level is the kernel of reduction modulo
`𝔟`, and the index is the order of `GL_n(O_E / 𝔟)`. 


## Path data and periods on the two grids

Tuples of matrices modulo `𝔪` on the edges of a path, path data, the maps on forms along a path,
and periods with the relation `Ψ ∝ Ξ`. The groups of integral points act through their quotients,
the invertible matrices modulo `𝔪`.


### `IsSumOfRootsOfUnity`

 `z` is a sum of at most `N` roots of unity. 

### `sum`

 A sum over a finite type `X` of numbers that are sums of at most `N` roots of unity is a sum of
at most `card X * N` roots of unity. 

### `mul_mem_nsmul`

 Let `z` be a sum of at most `N` roots of unity. If a set contains `0` and all multiples of `a`
by roots of unity, then `z * a` is a sum of `N` of its elements. 

### `EdgeTuple`

 A matrix modulo `𝔪` for each pair of nodes, where `𝔪` is `New.Data.gridModulus` of the twist
`ϑ`. 

### `NodeFamily`

 An invertible matrix modulo `𝔪` for each node. 

### `IsVerticalEdge`

 The vertical edges, whose character carries the twist: from `p` to `q` the first index changes
if `p` is in the grid of the `Ỹ`, and stays if it is in that of the `Y`. 

### `edgeChar`

 The character modulo `𝔪` of an edge `e = ((z, a, b), (z', a', b'))`: the character of the tame
part `New.Data.gridTamePart`, with the twist if the edge is vertical, at the index that changes
along the edge (`b` if `a = a'`, else `a`). 

### `tuplesOn`

 The tuples of matrices, one for each edge in `w`, extended by zero to the other pairs. 

### `edgeMatrixCountBound`

 A bound for the number of matrices of an edge between nodes with indices at most `D.m`: the
order of the residue ring of `𝔪` to the power `(2 * D.n D.m) ^ 2`, where `2 * D.n D.m` bounds the
ranks of such nodes. 

### `vectorCountBound`

 A bound for the number of column vectors modulo `𝔪` of a space of the grids at indices at most
`D.m`. 

### `IsAdmissibleFamily`

 The families that must fix a path datum. At the ends `Y^0_m` and `Ỹ^m_0` the element lies in the
level of the node (which is trivial modulo `𝔪` at `Y^0_m`), at `Ỹ^a_a` it is `g ⊕ 1` for the element
`g` at `Y^a_a`, and elsewhere it is free. 

### `tupleAction`

 The action of a family `g` of invertible matrices at the nodes on tuples: the matrix at the edge
from `p` to `q` becomes `(g q)⁻¹ * S (p, q) * g p`. 

### `edgeCharProd`

 The factor in the action on functions of the matrices of the edges `w`: the product over the
edges from `p` to `q` of the characters `New.Data.edgeChar` at `det (g q) / det (g p)`. 

### `IsPathDatum`

 A function `Ψ` of tuples of matrices is a path datum for a set `w` of edges if it depends on the
matrices at `w` only, is fixed by the action of admissible families twisted by the characters of the
edges (`New.Data.edgeCharProd`), vanishes unless the vertical edges carry matrices with left
inverses, and has as values sums of at most `N` roots of unity. 

### `IsPathDatum.dependsOn`

 `Ψ` is a function of the matrices of the edges in `w`. 

### `IsPathDatum.invariant`

 (i) Admissible families fix `Ψ`, up to the factor `New.Data.edgeCharProd`. 

### `IsPathDatum.hasLeftInv`

 (ii) `Ψ` vanishes unless the matrices of the vertical edges are split injective. 

### `IsPathDatum.isSumOfRootsOfUnity`

 (iii) The values of `Ψ` are sums of at most `N` roots of unity. 

### `edgeCharProd_mul`

 The factor `New.Data.edgeCharProd` of the edge characters is multiplicative in the family of
invertible matrices. 

### `tupleAction_mul`

 The action `New.Data.tupleAction` on tuples is a right action. 

### `sum_tuplesOn_insert`

 Let `edges` be a finite set of pairs of nodes and `e` a pair not in it; `tuplesOn ϑ edges` is
the set of tuples of matrices modulo `𝔪 = gridModulus ϑ` that vanish outside `edges`. A sum over
the tuples on `insert e edges` is a sum over the tuples on `edges` and over the matrix at `e`. 

### `sum_tuplesOn_tupleAction`

 A sum over the tuples supported on `w` does not change when each tuple is moved by a family of
invertible matrices at the nodes. 

### `IsPathDatum.sum_tupleAction`

 For a path datum `Ψ` for the edges `w` and an admissible family `g`, the sum over
`S ∈ tuplesOn ϑ w` of `Ψ S * f (tupleAction g S)` equals `edgeCharProd g w` times the sum of
`Ψ S * f S`. 

### `card_matrix_le_edgeMatrixCountBound`

 For nodes `p` and `q` whose indices `p.2` and `q.2` are at most `(D.m, D.m)`, the number of
matrices from `NodeIndex q` to `NodeIndex p` (rows indexed by `p`, columns by `q`) over the residue
ring of `𝔪 = gridModulus ϑ` is at most `edgeMatrixCountBound ϑ`, the order of that residue ring to
the power `(2 * D.n D.m) ^ 2`. 

### `card_tuplesOn_le`

 If the ends of the edges in `w` have indices at most `D.m`, there are at most
`edgeMatrixCountBound ϑ ^ #w` tuples supported on `w`. 

### `columnEdge`

 The edge from `(a, b)` to `(a, b + 1)` in the grid `z`: the vertical edge `Y^a_b → Y^a_(b+1)`
or the horizontal edge `Ỹ^b_a → Ỹ^(b+1)_a`. 

### `rowEdge`

 The edge from `(a, b)` to `(a + 1, b)` in the grid `z`: the horizontal edge `Y^a_b → Y^(a+1)_b`
or the vertical edge `Ỹ^b_a → Ỹ^b_(a+1)`. 

### `edges`

 The edges in the grid `z` of a monotone path from the node `(a₀, b₀)` to `(a, b)`: a step `down`
from `(a, b + 1)` to `(a, b)` gives `columnEdge z a b`, and a step `right` from `(a, b)` to
`(a + 1, b)` gives `rowEdge z a b`. 

### `formMap`

 The composite of the maps by the matrices of `S` along a path in the grid `z`: a transposed lift
when the second index drops, a lift when the first index grows. It moves conjugate forms in the grid
of the `Y` and forms in the grid of the `Ỹ`. 

### `formMap_append`

 The map on forms along a concatenation of two paths is the composite of the two maps. 

### `formMap_congr`

 The map on forms along a path depends only on the matrices at the edges of the path. 

### `eq_and_le_of_mem_edges`

 Both ends of an edge `(u, v)` of a path from `(a₀, b₀)` to `(a, b)` lie in the grid `z` of the
path and in the rectangle spanned by its ends: the pairs of indices satisfy
`(a₀, b) ≤ u.2 ≤ v.2 ≤ (a, b₀)` in the componentwise order. 

### `card_edges_le`

 A path from `(a₀, b₀)` to `(a, b)` has at most `(a - a₀) + (b₀ - b)` edges, stated without
subtraction. 

### `TwoGridPath.edges`

 The edges of a path `Γ` through the two grids: those of its halves `Γ.half z`, each a path in
the grid `z` from the node `(0, m)` to the diagonal node `(Γ.diagonalIndex, Γ.diagonalIndex)`. 

### `card_tuplesOn_edges_le`

 A path `Γ` through the two grids `Y` and `Ỹ` has at most `2 * D.m` edges. So there are at most
`edgeMatrixCountBound ϑ ^ (2 * D.m)` tuples `tuplesOn ϑ Γ.edges`, which carry a matrix on each edge
of `Γ` and are zero elsewhere. 

### `diagonalPeriodForm`

 The period of a conjugate form on `Y^j_j` and a form on `Ỹ^j_j` along `U(Y^j_j) → U(Ỹ^j_j)`. The
second form is translated by a real point `g` of `U(Ỹ^j_j)` and, on the added line, by the `j`-th
power of `New.Modulus.flipScalar`, the finite idele `ū / u` with `u` a fixed multiple of the chosen
idele generating `𝔪 = gridModulus ϑ`. 

### `PeriodTriple`

 A twist, a conjugate form on `Y_m` and a form on `Ỹ^m_0`, of any levels. 

### `gridPeriod`

 The period `I(Ψ; g)` on the path `Γ`, as a function of a triple `x = (ϑ, y', φ)` of a twist, a
conjugate form on `Y_m` and a form on `Ỹ^m_0`: the sum over the tuples `S` on `Γ` of `Ψ_ϑ(S)` times
the pairing of the images of `y'` and `φ` along the two halves of `Γ`, which end at the diagonal
nodes `(l, l)`, `l = Γ.diagonalIndex`. Here `g` is a real point of `U(Ỹ^l_l)`. 

### `IsProportional`

 The relation `Ψ ∝ Ξ`: at each real point `g` the period `New.Data.gridPeriod` of `Ψ` is a
multiple of `Ξ` by a number that depends neither on the twist nor on the forms. 
