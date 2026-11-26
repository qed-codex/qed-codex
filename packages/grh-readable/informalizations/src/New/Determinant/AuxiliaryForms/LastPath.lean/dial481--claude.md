---
{
  "module": "src/New/Determinant/AuxiliaryForms/LastPath.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/LastPath.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/LastPath.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The branching pairing and the periods on the last path

On the last path all spaces are positive definite. Forms are read as algebraic forms on the groups
`New.stdSpace`, and theta lifts become algebraic. Branching from `GL (n + 1)` to `GL n` for
interlacing parameters is an integral pairing with explicit bounds, so a period over the smaller
definite group is a constant times an integral of this pairing over the finite points. This gives
the finite sum `Ξ = New.Data.lastPathPeriod` to which all periods on the last path are proportional.
This is part of the construction of spanning forms on `U(Y_0)` with integral twisted lifts and
bounded conjugates; the denominators and the conjugates of `Ξ` are bounded in
`New.Determinant.AuxiliaryForms.SpanningForms`. The prefix `lastPath` of a name refers to the
last path, which consists of the edges between the nodes `(z, j, m)`, `j ≤ m`.

## Main definitions and results

* `New.Exchange.IsBranchingPairing`: an integer matrix whose pairing is equivariant for block
  matrices, is bounded, and computes the period of two algebraic forms over the smaller definite
  group as a constant times the integral of the pairing of their values at finite points.
* `New.Exchange.exists_isBranchingPairing`: such a matrix exists. It is the branching matrix of
  `New.exists_branching_matrix` followed by the duality of `New.exists_isDualPairing_of_isHCParam`.
* `New.Data.exists_lastPathPeriod_mem_smul_norm_le`: for a path datum, `Ξ` is a sum of a controlled
  number of terms, each with the bound that holds for the pairings of the vectors reached by the
  lifts.
* `New.Data.isProportional_lastPathPeriod`: every period on the last path is a constant times `Ξ`
  divided by the index of the level `J(𝔪₀)` on `Y_m`, which differs from the index of `J(𝔪)` by a
  constant factor.

Notions from other files:
* `New.IsHCParam`: `l` lists twice the Harish-Chandra parameter of the weight `(κ, e)`, in some
  order; `κ` counts the columns of each height and `e` is the exponent of the determinant.
* `New.ofAlgForm`: the function g ↦ ⟨v⁺, ρ(g_∞⁻¹) φ(g_f)⟩ on the adelic group attached to an
  algebraic form φ, with v⁺ = `New.highestVector` for the parameter.
* `New.classIntegral`: the integral over Γ \ G of a smooth left Γ-invariant function, for the Haar
  measure that gives the level K volume 1, written as a sum over classes.
* `New.StdClasses`: the double cosets of G_f by its rational points on the left and a level K on
  the right.
* `New.Data`: the admissible data `D` for the fixed parameters `P`. They give the CM field `D.E`,
  its infinite places `D.Φ` and the number `m = D.m` of lifts in the chain.
* `New.Data.gridSpace`: the Hermitian space at the node `(z, i, j)`, for the offset `0`. It is
  `Y^i_j` if `z = false` and `Ỹ^j_i` if `z = true`, and `Y_j = Y^0_j`.
* Moduli of a twist `ϑ` with places `Q`, where `ϖ = D.piM` and `b = D.natB`: `𝔪 = ϖ ^ b Q`
  (`New.Data.gridModulus`), `𝔪₀ = ϖ Q` and `𝔟 = ϖ ^ b` (`New.Data.triangleModulus`). The level
  `J(𝔞)` consists of the integral finite points that reduce to `1` modulo `𝔞`.


 ## Branching pairing of interlacing weights of GL(n+1) and GL(n) 

### `diagramWeight_eq_add_succ`

 Row `i` of the diagram in rank `N` exceeds row `i + 1` by the number `κ τ (i + 1)` of columns
of height `i + 1`, if `i + 1 < N`. 

### `diagramWeight_eq_zero_of_le_succ`

 With the constant bound `N`, `diagramWeight` vanishes at `(τ, i)` whenever `N ≤ i + 1`. Only
columns of height `h < N` count, and no such `h` has `i < h`. 

### `add_diagramWeight_mem_Icc_of_interlace`

 Let `l'` list twice the Harish-Chandra parameter of the weight `(κ, e)` of `GL n'` and `l` that
of the weight `(κ₀, e₀)` of `GL n`, where `#n' = #n + 1`. If `l` and `l'` interlace, then the
highest weights interlace: entry `q` of the highest weight of `(κ₀, e₀)` lies between the entries
`q + 1` and `q` of that of `(κ, e)`. An entry is the exponent of the determinant plus a row length
`diagramWeight`. 

### `boxes_le_boxes_of_interlace`

 Suppose that at each place `w : Φ` the highest weight of `(κ₀, e₀)` for `GL n` interlaces that
of `(κ, e)` for `GL n'`, where `#n' = #n + 1`. Here `boxes κ N` is the total over all places of the
boxes in the columns of height less than `N`: the sum of `h * κ w h` over `w : Φ` and `h < N`. Then
`κ₀` has, in this total, at most as many boxes in columns of height below `#n` as `κ` has in columns
of height below `#n'`. 

### `exists_add_eq_of_interlace`

 If the highest weight of `(κ₀, e₀)` in rank `N > 0` interlaces that of `(κ, e)` in rank `N + 1`,
then `κ₀` arises from `κ` by removing a horizontal strip: of the `κ τ q` columns of height `q`,
`γ τ q` lose a box and `κ₁ τ q` keep theirs, and the columns of height `N` that keep their box are
added to the exponent of the determinant. 

### `norm_dotProduct_mulVec_le_of_isDualPairing`

 Cauchy–Schwarz for a duality pairing. Let the integer matrix `A` be a duality (`IsDualPairing`)
between the weights `(κ', e')` and `(κ, e)` of `GL n` for the doubled Harish-Chandra parameter `l`:
its pairing `v' ⬝ᵥ A *ᵥ v` of coordinate vectors of the two Weyl modules is invariant under `GL n`,
and pairing with `v` is the Hermitian product with a vector of the same Gram norm as `v`. Then the
pairing is bounded by the product of the Gram norms, the square roots of `weylNormSq`. 

### `IsBranchingPairing`

 The properties of a branching pairing over the CM field `E`. Here `(κ, e)` is a weight of
`GL n'` (column multiplicities and exponents of the determinant at the infinite places of `E`) with
doubled Harish-Chandra parameter `l'`, and `(κ', e')` is a weight of the smaller group `GL n` with
doubled parameter `-l`. The bijection `σ` adds one index to `n`, compatibly with the signs `s`, `r`
and `t` of the Hermitian forms. The integer matrix `B` pairs coordinate vectors `v'`, `v` of the two
Weyl modules (indexed by `WeylIndex`, with the action `weylRep`) to `v' ⬝ᵥ B *ᵥ v`. The properties
are that this pairing is equivariant for block matrices, is bounded in the Gram norms, and computes
periods: an integral over the rank-`n` adelic group of a product of two algebraic forms, read as
functions, is a constant times an integral over finite points of the pairing of their values. 

### `IsBranchingPairing.exists_equivariant`

 The pairing is invariant under a unitary matrix `g` acting on the left and `diag (g, u)` on
  the right, up to `∏ τ, det (f τ u) ^ N τ`, where the exponents `N τ` are bounded. 

### `IsBranchingPairing.norm_le`

 If `M` bounds the number of boxes of `κ`, the pairing is at most `(M ^ M) ^ 3` times the
  product of the Gram norms. 

### `IsBranchingPairing.exists_integral_eq`

 The pairing gives the periods over the group of rank `n`. Read algebraic forms `η`, `φ` as
  functions on the adelic groups by `ofAlgForm`. For each real point `g` there is a constant `c`
  with this property. Let `V` be standard (`IsStd`: all signs are `1` and its point is the
  identity). The integral of `η(x) φ(diag (x, u) g)` over the adelic quotient of `V` is `c` over
  the index `stdLevelIndex K = [K₀ : K ∩ K₀]` of the level `K` in the integral points `K₀`, times
  the integral (`classIntegral`) of the pairing of `η(h)` and `φ(diag (h, u))` over the finite
  points `h` modulo the rational points. 

### `exists_isBranchingPairing`

 Let `(κ, e)` be a weight of `GL n'`, `#n' = #n + 1` by the bijection `σ`, with doubled
Harish-Chandra parameter `l'`. Let `(κ', e')` be a weight of the smaller group `GL n` with doubled
parameter `-l`, where `l` and `l'` interlace, and let all signs be `1`, so that the unitary groups
are definite. Then there is an integer matrix `B` that is a branching pairing. 

### `le_div_two_add_of_paramsCorrespond`

 Let the doubled parameters `l` and `l'` of definite groups (all signs `1`) of ranks `#n < #n'`
correspond under a theta lift with exponents `γ`, `γ'` (`ParamsCorrespond`). This includes that at
each place `w` the shifted entries `l' w j - 2 γ w + #n` are the shifted entries
`l w i - 2 γ' w + #n'` together with a block of `#n' - #n` numbers centred at `0`, and that the
sign of a common entry is determined by the signs of the spaces. Then
`γ' w ≤ l w i / 2 + #n / 2` for every entry of `l`, in integer division, since every shifted entry
of `l` exceeds `#n' - #n`. 


## The last path: weights, levels, kernels and the finite sum

On the last path all spaces are positive definite. Its two halves run through the nodes `(z, j, m)`,
`j ≤ m`, which are the spaces `Y^j_m` and `Ỹ^m_j`.


### `LastPathIndex`

 The index type of the space at the node `(z, j, m)` of the last path, which is `Y^j_m` if
`z = false` and `Ỹ^m_j` if `z = true`. Here `D` is a choice of admissible data for the parameters
`P`, `m = D.m` is the number of lifts, and `GridIndex` indexes the coordinates at a node. 

### `exists_isLiftWeight_isHCParam`

 Let `D` be admissible data, with `m = D.m` lifts and with `D.Φ` the infinite places of the CM
field `D.E`. Fix a half `z` of the last path, through the nodes `(z, i, m)`: the Hermitian spaces
`Y^i_m` for `z = false` and `Ỹ^m_i` for `z = true`. For the edge from `i` to `i + 1`, let
`gridWeight z i n` be the weight of its character at the end with index type `n`. Along this half
every new block of the parameter lies below all old entries. So there are column multiplicities
`κ` and exponents `e i` of the determinant with three properties.
* `IsLiftWeight`: the rank grows from `i` to `i + 1`, no column has height strictly between the two
  ranks, and `e i` is the weight at the upper end plus the number of columns whose height is the
  rank at `i`.
* The weight at the lower end is `e (i + 1)`.
* For `i ≤ m` the weight `(κ, e i)` has the doubled Harish-Chandra parameter `-gridParam z 0 i m`
  of the forms moved along this half (the offset `0` selects the grids): conjugate forms on `Y^i_m`
  and forms on `Ỹ^m_i`. 

### `lastPathColumns`

 The column multiplicities of the weights along the half `z` of the last path. 

### `lastPathDetExp`

 The exponents of the determinant in the weights along the half `z` of the last path. 

### `isLiftWeight_lastPathColumns`

 The weight at the node `(z, j, m)` goes up to the rank of the node `(z, j + 1, m)`, along the
weight at the upper end of the character of the edge between them. 

### `gridWeight_eq_lastPathDetExp`

 The weight at the lower end of the character of the edge from `(z, j, m)` to `(z, j + 1, m)` is
the exponent of the determinant at `(z, j + 1, m)`. 

### `isHCParam_lastPathColumns`

 For `j ≤ m`, the weight at the node `(z, j, m)` has the doubled Harish-Chandra parameter
`-gridParam z 0 j m`. 

### `LastPathVector`

 The space of values of the algebraic forms at the node `(z, j, m)`. 

### `LastPathForm`

 Algebraic forms at the node `(z, j, m)`, of the weight given by `lastPathColumns` and
`lastPathDetExp`. 

### `LastPathFiniteDatum`

 Finite data for the theta lift along the edge from `(z, j, m)` to `(z, j + 1, m)`. In the space
of data on the matrices (`hom`) between the standard spaces of the two ranks, this is the span
(`finitePart`) of the translates of the vacuum under the finite Heisenberg operators. 

### `lastPathBranching`

 An integer matrix, chosen from `exists_isBranchingPairing`, that is a branching pairing between
the weight of the conjugate forms on `Y^m_m` (the node `(false, m, m)`) and the weight of the forms
on `Ỹ^m_m` (the node `(true, m, m)`). Its properties are stated in
`isBranchingPairing_lastPathBranching`. 

### `isBranchingPairing_lastPathBranching`

 The matrix `lastPathBranching` is a branching pairing for the weights and parameters at the
nodes `(true, m, m)` and `(false, m, m)`. 

### `lastPathPairing`

 The bilinear pairing `(v', v) ↦ v' ⬝ᵥ B *ᵥ v` of the matrix `B = D.lastPathBranching`. 

### `exists_lastPathBranching_equivariant`

 Let `D` be admissible data with `m = D.m` lifts and infinite places `D.Φ`. The weights on
`Y^m_m` (`false`) and `Ỹ^m_m` (`true`) have column multiplicities `lastPathColumns` and exponents of
the determinant `lastPathDetExp`; the integer matrix `B = lastPathBranching` pairs their Weyl
modules by `v' ⬝ᵥ B *ᵥ v`. There are integers `N τ` with two properties. Let `f τ : S →+* R` be
homomorphisms, one for each place `τ`, from a commutative star ring to a field of characteristic
zero, and let unitary matrices over `S` act through them (`weylRep`). Moving `v'` by `g` and `v` by
`diag (g, u)` multiplies the pairing by `∏ τ, det (f τ u) ^ N τ`. Also `|N τ|` is at most the number
of boxes of the weight on `Ỹ^m_m` plus the absolute value of its exponent of the determinant at
`τ`. 

### `norm_dotProduct_lastPathBranching_mulVec_le`

 If `M` bounds the number of boxes of the weight at `(true, m, m)`, then
`‖v' ⬝ᵥ lastPathBranching *ᵥ v‖` is at most `(M ^ M) ^ 3 * √(weylNormSq v') * √(weylNormSq v)`, i.e.
`(M ^ M) ^ 3` times the product of the Gram norms of `v'` and `v`. 

### `exists_integral_eq_lastPathPairing`

 The period at `(m, m)`. For a real point `g` of `Ỹ^m_m` there is a constant `c` with the
following property. Read algebraic forms `η`, `φ` as functions on the adelic groups by `ofAlgForm`.
The integral of `η(x) φ(diag (x, u) g)` over the adelic quotient of a standard space `V` of the rank
of `Y^m_m` is `c` over the index of the level `K` times the integral (`classIntegral`) of the
branching pairing of `η(h)` and `φ(diag (h, u))` over the finite points `h` modulo the rational
points. 

### `isStd_gridSpace_last`

 The spaces of the last path are standard positive definite spaces. 

### `lastPathToAlgForm`

 Forms at the outer end `(z, 0, m)` of a half of the last path, as algebraic forms. 

### `card_lastPathIndex_le`

 The rank at the node `(z, j, m)` with `j ≤ m` is at most `2 n_m`, twice the rank `n_m = D.n m`
in the sequence `n_j = k + j (t + 1)` of the data. 

### `natAbs_lastPathDetExp_le`

 At the node `(z, j, m)` with `j ≤ m` the exponents of the determinant are at most `⌈20 b⌉` in
absolute value, where `b = D.b` is the large weight of the data. 

### `boxes_lastPathColumns_le_natB_mul`

 At the node `(z, j, m)` with `j ≤ m`, the number of boxes of the weight `D.lastPathColumns z` is
at most `b r ^ 4`, where `b` is `D.natB` and `r` is `D.r`. 

### `lastPathLevel`

 The level at the node `(z, j, m)` of the last path, inside `Gf D.E (D.LastPathIndex z j)`: the
integral points whose reduction modulo `𝔪 = gridModulus ϑ` lies in `nodeLevel`, which is trivial on
`Y_m` (the node `(false, 0, m)`) and elsewhere the kernel of the reduction modulo the part `𝔟` of
`𝔪` that does not depend on the twist `ϑ`. So it is `J(𝔪)` on `Y_m` and `J(𝔟)` on the other spaces,
where `J(𝔞)` consists of the integral points that reduce to `1` modulo `𝔞`. 

### `lastPathLevel_le_principalLevel`

 For every twist `ϑ`, the level `lastPathLevel ϑ z j` at the node `(z, j, m)` of the last path
lies in the principal level `J(𝔟)`, the integral points that reduce to `1` modulo `𝔟`. Here `𝔟` is
generated by `D.gridLevelGen = ϖ ^ D.natB`, with `ϖ = D.piM`. It is the part of the modulus
`𝔪 = 𝔟 Q` of `ϑ` that does not depend on the places `Q` of `ϑ`. 

### `gridChar_hasWeight_lastPathDetExp`

 The character at the lower end of the edge from `(z, j, m)` to `(z, j + 1, m)` has as its weight
the exponent of the determinant at `(z, j + 1, m)`. Its tame part, the family of characters of the
residue fields that gives it on integral finite points, is `gridTamePart ϑ z j`. 

### `lastPathKernel`

 The theta kernel of the edge from `(z, j, m)` to `(z, j + 1, m)`, for the characters `gridChar`
at the two ends and the level at `(z, j, m)`. The derivatives in the Taylor series of the theta
functions are scaled by the constant `jetScale` of the field `D.E = P.E D.towerExp`. 

### `lastPathBlockPoint`

 The point `diag (h, u ^ m)` of `Ỹ^m_m` for a finite point `h` of `Y^m_m`, where `u` is the
scalar `flipScalar` of the modulus `𝔪`, acting on the line. 

### `FixedByOuterLevels`

 The two forms have the levels at the outer ends of the last path: `J(𝔪)` for the conjugate form
`y false` on `Y_m` and `J(𝔟)` for the form `y true` on `Ỹ^m_0`. 

### `lastPathEdgeDatum`

 The finite datum of an edge of the last path: the indicator of the matrix of the edge, on the
vacuum scaled by a power of `vacuumScale`. 

### `lastPathChain`

 The algebraic form of `F` on the outer node `(z, 0, m)`, lifted along the first `j` edges of the
half `z` of the last path with the data that the tuple `S` gives. 

### `lastPathPeriod`

 The finite sum `Ξ` on the last path. An `EdgeTuple` is a matrix modulo `𝔪` for each pair of
nodes, and `tuplesOn` lists the tuples `S` that vanish off the edges of the last path. For each such
`S` the two chains of lifts of `y false` and `y true` are paired and integrated over the finite
points of `Y^m_m` modulo the rational points; `Ξ` is the sum of these integrals against `Ψ S`. 


## The last path: the sum over classes

The invariance of a path datum makes the integrand of the sum `Ξ = lastPathPeriod` invariant under
the levels, in each variable. These levels are sufficiently small, so `Ξ` is a plain sum over tuples
of classes.


### `edges_last`

 The edges of the last path are those of the row `m` in both grids. 

### `edgeCharProd_last`

 For a family `g` of invertible matrices at the nodes, the product `edgeCharProd g` of the
characters of the edges of the last path splits into one factor for each of these edges. 

### `lastPathKernel_omega_lastPathEdgeDatum`

 Let `g` be a family of invertible matrices modulo `gridModulus ϑ` at the nodes. Let the integral
points `u`, `u'` reduce modulo `gridModulus ϑ` to the values of `g` at the ends `(z, j, m)`,
`(z, j + 1, m)` of the edge `rowEdge z j D.m` of the last path. For a tuple `S` of matrices on the
edges, `tupleAction g S` has the matrix `(g q)⁻¹ * S (p, q) * g p` on the edge from `p` to `q`. Then
the action `ω` of `(u, u')` for `lastPathKernel ϑ z j` takes the datum `lastPathEdgeDatum` of
`tupleAction g S` on this edge to that of `S`, times `edgeCharProd g`, the value of the character of
the edge. 

### `IsPathDatum.sum_lastPathPairing_omega_invariant`

 Let `Ψ` be a path datum: a function of the matrices on the edges, fixed by admissible families
up to the characters of the edges, with sums of roots of unity as values. Let `a` be a family of
elements of the levels along the last path with `a true m = diag (a false m, 1)`. Then moving the
data of all lifts by `a` does not change the sum against `Ψ` of the pairings of linear images `β`,
`β'` of the two tensors `pure` of data. 

### `lastPathPairing_lastPathChain_mem_smoothInvariants`

 Let `S` be a tuple of matrices on the edges, which gives the data of the lifts, and let
`y false`, `y true` be forms at the outer ends of the last path. Lift both forms `m = D.m` times
along the last path (`lastPathChain`), to `Y^m_m` and `Ỹ^m_m`. Consider the function that sends a
finite point `h` of `Y^m_m` to the branching pairing `lastPathPairing` of the value of the first
lift at `h` and the value of the second lift at `lastPathBlockPoint ϑ h`. It lies in
`smoothInvariants stdRatPoints`: it is smooth and left invariant under the rational points. 

### `IsPathDatum.sum_lastPathPairing_mul_level`

 Let `Ψ` be a path datum (`IsPathDatum N`) for the edges of the last path `TwoGridPath.last D.m`.
It is a function of tuples `S` of matrices modulo `𝔪 = gridModulus ϑ` on those edges. Let the forms
`y false`, `y true` have the levels at the outer ends of the path. For each `S`, lift both forms
`m = D.m` times with the data given by `S` (`lastPathChain`). Pair (`D.lastPathPairing`) the values
of the lifts at a finite point `g` of `Y^m_m` and at the block point `lastPathBlockPoint ϑ g` of
`Ỹ^m_m`. The sum over `S` of `Ψ S` times this pairing does not change if `g` is replaced by `g * u`.
Here `u` is an integral point whose reduction modulo `𝔪` lies in the level
`nodeLevel ϑ (false, D.m, D.m)` at `Y^m_m`. 

### `exists_lastPathPeriod_mem_smul_norm_le`

 Let `Ψ` be a path datum whose values are sums of at most `N` roots of unity, and let the forms
`y` have the levels at the outer ends. Let `σ` be a homomorphism from `ℂ` to a normed field. Let
`IsReached z j g v` be a property of a vector `v` at a finite point `g` of the node `(z, j, m)`,
such as membership in a set that contains all vectors reached by the lifts: it holds at `j = 0` for
the values of the two forms and is preserved by the kernels. Suppose that `‖σ (M * a)‖ ≤ R`, for a
fixed number `M`, for each pairing `a` of vectors with this property at corresponding points `g` and
`lastPathBlockPoint g` of `Y^m_m` and `Ỹ^m_m`.

Then the sum `Ξ = lastPathPeriod Ψ y` over the last path is a sum of numbers with this bound. The
number of summands is `L` times the product of the numbers of classes (`StdClasses`) of the
`2 * m + 1` levels that occur, for some `L ≤ N * edgeMatrixCountBound ^ (2 * m)`. 


## The last path: the periods

On the last path the lifts are multiples of algebraic lifts, and the period over `U(Y^m_m)` is a
multiple of the branching pairing.


### `exists_gridPathMap_eq_ofAlgForm_smul_lastPathChain`

 Let `D` be admissible data with `m = D.m` lifts, let `z` be a half of the last path, through
the nodes `(z, i, m)`, and let `j ≤ m`. Here `GridPath.row m j` is the path along the first `j`
edges of this half, from the node `(z, 0, m)` to `(z, j, m)`, and its map `formMap` is the composite
of the theta lifts along these edges, for the data given by a tuple `S` of matrices on the
edges. There is a constant `c` such that, for every twist `ϑ`, tuple `S` and form `F` at
`(z, 0, m)`, the function of the lifted form is that given by `ofAlgForm` from `c` times the ratio
of the indices of the levels at the two ends (`levelIndex`) times the algebraic chain of lifts
`lastPathChain S z j F`. 

### `isProportional_lastPathPeriod`

 Let `Ψ` be a family of functions on edge tuples, one for each twist. At each real point `g`
there is a number `β` such that, for every twist `ϑ`, conjugate form `y` on `Y_m` and form `φ` on
`Ỹ^m_0`, the period of `Ψ` on the last path at `g` is `β` times the sum `lastPathPeriod (Ψ ϑ)` at
`(y, φ)` divided by `triangleGLCard false ϑ m`. This last number is the order of the general linear
group of the rank of `Y_m` modulo `𝔪₀ = ϖ Q`, with `ϖ = D.piM` and `Q` the product of the places of
`ϑ`. 
