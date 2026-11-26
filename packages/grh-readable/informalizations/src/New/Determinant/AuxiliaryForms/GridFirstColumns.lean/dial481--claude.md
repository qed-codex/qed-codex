---
{
  "module": "src/New/Determinant/AuxiliaryForms/GridFirstColumns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/GridFirstColumns.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/GridFirstColumns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Periods on the diagonal and path data on the first path

The first path goes from `Ỹ^m_0` to `Ỹ^0_0 = Y₀ ⊕ E ẽ₀` and from `Y₀` to `Y_m`. Its spaces are the
nodes `(z, 0, i)`, the first columns of the two grids: `(false, 0, i)` is `Y_i` and `(true, 0, i)`
is `Ỹ^i_0`. A form on `Ỹ^m_0` and a conjugate form on `Y_m` move down these columns by transposed
lifts and meet at `i = 0`. The product `Ψ¹` of the point data of the edges computes the period of
the two iterated transposed lifts `New.Data.transposedChain`. The sum `Ψ⁰` of the translates of
`Ψ¹`, weighted by the characters of the edges, is a path datum, and its period is the number of
translates times that of `Ψ¹`.

## Main definitions and results

* `New.Data.exists_petersson_eq_diagonalPeriodForm`: the period with a form on `Ỹ^0_0`, as a
  functional of the form on `Y₀`, is a Petersson product.
* `New.Data.diagonalPeriodForm_tupleAction`: translating the matrices by a family that is `1` at
  the ends and `diag(g, 1)` at `(0, 0)` of the `Ỹ`, `g` being its member at `(0, 0)` of the `Y`,
  multiplies the period by the characters of the edges.
* `New.Data.firstPointDatum`, `New.Data.firstPathDatum`: the functions `Ψ¹` and `Ψ⁰`.
* `New.Data.exists_isPathDatum_diagonalPeriodForm_eq`: the period of the iterated transposed lifts
  is a constant times the period of path data on the first path.

Notions from other files:
* `New.Data.triangleModulus`: the modulus `𝔪₀ = π_M Q` for the chain of the `Y` and `𝔟 = π_M ^ b`
  for that of the `Ỹ`, with `π_M = D.piM`. `New.Data.gridModulus` is `𝔪 = 𝔟Q`, where `Q` comes
  from the twist `ϑ`. `New.Data.triangleGLCard` is the index `n_𝔪₀(Y_i)` or `n_𝔟(Ỹ^i_0)`.
* `New.Data.levelIndex`: the index of the level `New.Data.nodeLevel` at a node, which is the level
  `𝔪` at the `Y_i` and the level `𝔟` elsewhere.
* `New.Data.diagonalPeriodForm`: the period of a conjugate form on `Y^j_j` and a form on `Ỹ^j_j`
  along the embedding of unitary groups, shifted on the line by a scalar from the twist, at a real
  point.
* `New.Data.EdgeTuple`: a matrix modulo `𝔪` for each pair of nodes. A `NodeFamily` of invertible
  matrices acts on it by `New.Data.tupleAction`; `New.Data.edgeCharProd` is the product of the
  characters of the edges at the determinants of such a family.
* `New.GridPath.formMap`: the composite of the maps by the matrices of a tuple along a path.



## Periods on the diagonal and translates along the first column

The period of a conjugate form on `Y^j_j` and a form on `Ỹ^j_j` does not see a common translation.


### `finMean_isUnit_indicator`

 The mean of the indicator of the invertible matrices over a finite ring is the share of
invertible matrices. 

### `disjoint_edges_column`

 The edges of a first column in the two grids are disjoint. 

### `instance (D : Data P) (ϑ : D.MFoldTwist) : IsLocalHom (reduceToTriangle ϑ false)`

 Reduction modulo `𝔪₀ = π_M Q` from the residue ring of `𝔪 = 𝔟Q` (`reduceToTriangle ϑ false`, for
the grid of the `Y`) is a local homomorphism, because the two moduli have the same primes. 

### `exists_triangleGLCard_eq_mul_levelIndex`

 Let `π_M = D.piM`, let `Q` be the product of the places of a twist `ϑ`, and put `𝔪₀ = π_M Q` and
`𝔪 = π_M ^ D.natB * Q` (`gridModulus ϑ`). For the space `Y_j` at the node `(false, 0, j)`, the order
`triangleGLCard false ϑ j` of `GL(Y_j)` modulo `𝔪₀` is a number `C`, the same for all `ϑ`, times
`levelIndex ϑ false 0 j`. 

### `diagonalPeriodForm_formRep`

 The period of a conjugate form `y` on `Y^j_j` (grid `false`) and a form `φ` on `Ỹ^j_j` (grid
`true`) at the real point `g` does not change when `y` is translated by a finite adelic point `u` of
the unitary group and `φ` by the block matrix `diag(u, 1)`. 

### `formRep_block_one_eq_self`

 Let `𝔟` be `D.gridLevelGen = D.piM ^ D.natB`. A form `φ` in `D.gridLevelForms 0`, that is of
level `𝔟` on `Ỹ^0_0`, is fixed under `formRep` by the block matrix
`U.block (D.gridDiagEquiv 0) (u, 1)`, written `diag(u, 1)`, for every `u` on `Y₀` in
`principalLevel` of `𝔟`. 

### `gridKernel_zero_true_eq_star`

 At the node `Y^0_0` of grid `Y`, the kernel `gridKernel false 0 0 true`, that of the conjugate
forms `GridForm false 0 0`, is the complex conjugate (`star`) of `gridKernel false 0 0 false`, the
kernel of the forms on `Y^0_0`. 

### `exists_petersson_eq_diagonalPeriodForm`

 The period with a form `φ` on `Ỹ^0_0`, as a functional of the forms `y` on `Y₀`, is a Petersson
product. The chosen places are the prime divisors of `π_M = D.piM`, and `J_M = D.chosenLevel` is the
group of integral points that reduce to `1` at them. The family `(D.levelPlaces ϑ).placeAt` adds the
places of the modulus `Q` of a twist `ϑ`, so its level `levelOf … ⊥` is the level `𝔪₀ = π_M Q`. The
space `gridLevelForms 0` consists of the forms on `Ỹ^0_0` of principal level `𝔟 = π_M ^ D.natB`. At
a real point `g` there is a linear map `periodRepr` from it to the forms on `Y₀` of level `J_M` such
that, for every `ϑ` and every form `y` on `Y₀` of level `𝔪₀`, the Petersson product of `y` and
`periodRepr φ` is the period at `g` of the conjugate of `y` and `φ`. 

### `formRep_formMap_column_tupleAction`

 Put `m = D.m` and `𝔪 = gridModulus ϑ`. Let `S` be a tuple of matrices modulo `𝔪`, one for each
pair of nodes, and `F` a form at the end `(z, 0, m)` of the first column. Let the family `g` of
invertible matrices modulo `𝔪` be `1` at that end, and let `k` be an integral lift of `g (z, 0, b)`,
equal to `1` if `b = m`. Translate `S` by `g`, map `F` down the column to `(z, 0, b)` by `formMap`,
and translate the image on the right by `k`. The result is the image of `F` for `S` times
`edgeCharProd g`, the product over the edges from `p` to `q` of the column of their characters at
`det (g q) / det (g p)`. 

### `diagonalPeriodForm_tupleAction`

 Let `g` be a family of invertible matrices modulo `gridModulus ϑ`, one at each node, that is `1`
at the ends `(z, 0, D.m)` of both first columns and is the block matrix `diag(g (false, 0, 0), 1)`
at `(true, 0, 0)`. Map a conjugate form `y'` on `Y_m` and a form `φ` on `Ỹ^m_0` down these columns
by the matrices `S`, and take the period at the real point `gInf`. Replacing the matrix from `p` to
`q` by `(g q)⁻¹ * S (p, q) * g p` multiplies this period by `edgeCharProd`, the product over the
edges of both columns of their characters at `det (g q) / det (g p)`. 


## Path data on the first path

The product `Ψ¹` of the point data of the edges is symmetrized to the path datum `Ψ⁰`, the sum of
its translates.


### `sum_tuplesOn_union`

 For a set `w` of pairs of nodes, `tuplesOn ϑ w` is the set of tuples of matrices modulo
`gridModulus ϑ`, one for each pair of nodes, that are zero outside `w`. A tuple on the union of
disjoint sets `w` and `w'` is glued by `Finset.piecewise` from a tuple on `w` and one on `w'`, so a
sum over tuples on the union is a double sum. 

### `edges_column`

 The edges of the column from `(0, m)` down to `(0, b)` in the grid `z` are those from `(0, i)`
to `(0, i + 1)` with `b ≤ i < m`. 

### `mem_edges_first`

 An edge lies on the first path exactly when it is an edge of the first column of a grid. 

 ### The point data 

### `edgePointDatum`

 The point datum of the edge from `(0, b)` to `(0, b + 1)`, regarded modulo `𝔪`: the
indicator of the matrices that reduce to the standard inclusion modulo `𝔪₀` in the grid of the
`Y` and modulo `𝔟` in that of the `Ỹ`. 

### `columnPointDatum`

 The product of the point data `edgePointDatum` of the edges from `(0, b)` to `(0, m)` in the
grid `z`, at the matrices of `S`: the indicator that each of these matrices reduces to the standard
inclusion modulo `triangleModulus z ϑ`. 

### `firstPointDatum`

 The product `Ψ¹` of the point data of the edges of the first path. 

### `columnPointDatum_congr`

 The product of the point data from `(0, b)` to `(0, m)` depends only on the matrices of the
edges between these two nodes. 

### `isSumOfRootsOfUnity_firstPointDatum`

 A value of `Ψ¹` is `0` or `1`, so it is a sum of at most one root of unity. 

### `hasLeftInv_of_edgePointDatum_ne_zero`

 Let `y` be a matrix modulo `𝔪 = gridModulus ϑ` from the space `Y_b` at the node `(false, 0, b)`
to `Y_(b+1)`. If `edgePointDatum false b y` is nonzero, that is, `y` reduces to the standard
inclusion modulo `𝔪₀ = triangleModulus false ϑ`, then `y` has a left inverse modulo `𝔪`, because
`𝔪₀` and `𝔪` have the same primes. 

 ### The period 

### `pointTransposedLift_eq_sum`

 Both `pointTransposedLift` and `transposedMove y` are transposed theta lifts from forms at
`(0, b + 1)` to forms at `(0, b)` of the grid `z`. The datum of the first is the indicator of the
inclusion matrix modulo `triangleModulus z ϑ`, scaled by the order `triangleGLCard z ϑ b`; that of
the second is the indicator of the single matrix `y` modulo `𝔪`. The first is `triangleGLCard z ϑ b`
times the sum of the second over `y`, weighted by the point datum `edgePointDatum` of the edge. 

### `transposedChain_eq_sum`

 Let `b ≤ m = D.m` and take the first column of the grid `z` from `(0, m)` down to `(0, b)`. With
`π_M = D.piM`, `𝔟 = π_M ^ D.natB` and `Q` the product of the places of `ϑ`, the modulus
`triangleModulus z ϑ` is `π_M Q` for `false` and `𝔟` for `true`, and `triangleGLCard z ϑ i` is the
order of `GL` of the node `(0, i)` modulo it. The composite `transposedChain ϑ z b` of the
transposed theta lifts `pointTransposedLift` along the column is the product of these orders,
`b ≤ i < m`, times a sum over the tuples `S` of matrices modulo `𝔪 = 𝔟Q` on its edges: the composite
`formMap` of the transposed lifts whose data are the single matrices of `S`, weighted by the
indicator `columnPointDatum z b S` that each matrix reduces to the standard inclusion modulo
`triangleModulus z ϑ`. 

### `transposedChain_one_true_eq_transposedChain`

 In the grid of the `Ỹ` the iterated transposed lifts `transposedChain` along the first column do
not depend on the twist. 

### `pairing_transposedChain_eq_sum`

 Let `ϑ` be an m-fold twist (`MFoldTwist`), `y'` a conjugate form on `Y_m` and `φ` a form on
`Ỹ^m_0`. Move them to `Y₀` and `Ỹ^0_0` by `transposedChain`, the composites of transposed theta
lifts down the first columns of the two grids `Y` (`false`) and `Ỹ` (`true`). The pairing of the
images by a bilinear form `B` equals a product times a sum. The product runs over `i < D.m` and both
grids `z` of `triangleGLCard z ϑ i`, the order of `GL` at the node `(z, 0, i)` modulo
`triangleModulus z ϑ`. The sum runs over the tuples `S ∈ tuplesOn ϑ` of matrices on the edges of the
first path `TwoGridPath.first D.m`, which goes down both first columns. Its term is
`firstPointDatum S`, the indicator that each matrix reduces to the standard inclusion modulo
`triangleModulus z ϑ`, times `B` of the two forms mapped down the columns by `S` (`formMap`). 

 ### Invariance 

### `map_eq_one_and_edgeChar_eq_one_of_mem_nodeLevel`

 Let `k` be an invertible matrix modulo `gridModulus ϑ = 𝔟Q` in the level `nodeLevel` at a node
`(z, 0, i)` of the first column: the trivial subgroup for `z = false`, the kernel of reduction
modulo `𝔟` for `z = true`. Then `k` reduces to `1` under `reduceToTriangle ϑ z`, the reduction
modulo `π_M Q` for `z = false` and modulo `𝔟` for `z = true`, and for any `b` the character
`edgeChar` of the edge from `(z, 0, b)` to `(z, 0, b + 1)` is `1` at the determinant of `k`. 

### `firstPointDatum_invariant`

 Let `g` be a family of invertible matrices modulo `gridModulus ϑ`, one at each node, whose
members on the first path (the nodes `(z, 0, i)`, `i ≤ D.m`) lie in `nodeLevel`: they are `1` for
`z = false` and `1` modulo `D.piM ^ D.natB` for `z = true`. Then `g` fixes `Ψ¹ = firstPointDatum`,
the indicator that each matrix of the path reduces to the standard inclusion, under the action on
functions of tuples: the matrix from `p` to `q` becomes `(g q)⁻¹ * S (p, q) * g p`, and the value
is multiplied by the product of the characters of the edges at `det (g q) / det (g p)`. 

### `fintypeQuotientNodeLevel`

 The cosets of the level `nodeLevel` at a node form a finite type. 

### `LevelCosets`

 A coset of the level `nodeLevel` for each of the spaces `Y_i` and `Ỹ^i_0` with `i < m`: of the
level `𝔪` at `Y_i` and of the level `𝔟` at `Ỹ^i_0`. 

### `LevelCosets.out`

 Representatives of the cosets `x`, extended by `1` to the other spaces. 

### `LevelCosets.family`

 The family by which the cosets `x` translate: the representatives, except that `Ỹ^0_0`
moves with `Y^0_0`. 

### `firstPathDatum`

 The sum `Ψ⁰` of the translates of `Ψ¹` over the coset families, each weighted by the
characters of the edges. The coset at `Ỹ^0_0` does not act, so each translate is counted a constant
number of times. 

### `firstPathDatum_invariant`

 Let `g` be an admissible family of invertible matrices modulo `gridModulus ϑ`: it is `1` at
`(false, 0, D.m)`, is `1` modulo `D.piM ^ D.natB` at `(true, 0, D.m)`, and at `(true, a, a)` is the
block sum of `g (false, a, a)` with `1`. Then `g` fixes `Ψ⁰ = firstPathDatum ϑ` under translation
of the matrices (`tupleAction`) followed by multiplication by the product `edgeCharProd` of the
characters of the edges, because `Ψ⁰` is the sum of the translates of the indicator
`firstPointDatum` over cosets of the levels `nodeLevel`, and `g` permutes these cosets. 

### `card_levelCosets_le`

 The number of coset families `LevelCosets ϑ` is at most `edgeMatrixCountBound ϑ ^ (2 * D.m)`.
`edgeMatrixCountBound ϑ` bounds the number of matrices modulo `gridModulus ϑ` of an edge between
nodes of index at most `D.m`. 

### `isPathDatum_firstPathDatum`

 Put `m = D.m`. The function `Ψ⁰ = firstPathDatum ϑ`, the weighted sum of the translates of the
indicator `firstPointDatum`, is a path datum on the first path, the edges from `(z, 0, i)` to
`(z, 0, i + 1)` with `i < m`. Its values are sums of at most `N ^ (2 m)` roots of unity, where
`N = edgeMatrixCountBound ϑ` bounds the number of matrices modulo `gridModulus ϑ` between two nodes
with indices at most `m`. 

### `sum_firstPathDatum_mul`

 For a tuple `S` of matrices let `periodAt S` be the period, for the twist `ϑ` and at the real
point `gInf`, of the images under `formMap S` down the first columns of a conjugate form `y'` on
`Y_m` and a form `φ` on `Ỹ^m_0`. The sum of `periodAt` over the tuples on the first path weighted by
`Ψ⁰` is the cardinality of `LevelCosets ϑ` times the sum weighted by `Ψ¹`, because every translate
of `Ψ¹` gives the same sum. 

### `card_levelCosets_eq`

 The number of coset families `LevelCosets` is the product of the indices `levelIndex` of the
levels of the nodes `(0, i)` in the grid of the `Y` and of the orders `triangleGLCard` in that of
the `Ỹ`, over `i < m`. 

### `exists_diagonalPeriodForm_transposedChain_eq`

 Let `y'` be a conjugate form on `Y_m`, `φ` a form on `Ỹ^m_0`, and `g` a real point of the
unitary group of `Ỹ^0_0`. Move `y'` and `φ` down the first columns by the composites
`transposedChain` of transposed theta lifts, `y'` at the twist `ϑ` and `φ` at the trivial twist `1`.
The period at `g` of the images is a constant, independent of `ϑ`, times `gridPeriod` of
`Ψ⁰ = firstPathDatum` at `(ϑ, y', φ)`: the sum over the tuples `S` on the first path of `Ψ⁰ ϑ S`
times the period at `g` of the images of `y'` and `φ` under the matrices of `S`. 

### `exists_isPathDatum_diagonalPeriodForm_eq`

 Put `m = D.m`; the first path `TwoGridPath.first m` consists of the edges from `(z, 0, i)` to
`(z, 0, i + 1)` with `i < m`. There are a constant `C` and, for each `m`-fold twist `ϑ`, a path
datum `Ψ ϑ` on the first path. They satisfy the following for a conjugate form `y'` on `Y^0_m`, a
form `φ` on `Ỹ^m_0` (`GridForm true 0 m`) and a point `g` of the archimedean unitary group `GInf` of
`Ỹ^0_0`. Move `y'` and `φ` down the first columns by the composites `transposedChain` of transposed
theta lifts, `y'` at `ϑ` and `φ` at the trivial twist `1`. The period `diagonalPeriodForm` at `g` of
the images is `C` times `gridPeriod`: the sum over the tuples `S` on the first path of `Ψ ϑ S` times
the period at `g` of the images of `y'` and `φ` under the matrices of `S`. 
