---
{
  "module": "src/New/Determinant/AuxiliaryForms/Turns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/Turns.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/Turns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Turning path data, and turns off the diagonal

A turn of a path replaces two sides of a square by the two other sides. The `m`-fold twist is `ϑ`,
the characters of the edges are built from `D.untwistedLiftChar j`, of weight `-D.liftWeight j`, and
the vertical edges, whose character carries a power of `ϑ`, go from `Y^i_j` to `Y^i_(j+1)` and from
`Ỹ^i_j` to `Ỹ^i_(j+1)`. The forms that move in the grid of the `Y` are conjugate forms.

## Main definitions and results

* `New.Data.Corner.IsTurn.exists_isPathDatum`: the match of a path datum, after a Fourier transform
  in the column of the line if the turn is on the diagonal, is a path datum.
* `New.Data.exists_squareLaw_grid_hasAbsUpToNormPower`: the exchange
  `New.Exchange.one_square_identity_of_isEdgeFamily` on a square of a grid, with a constant
  `κ / c ϑ` whose denominator has, up to a power of the norm, the absolute value
  `New.Data.turnRatio`.
* `New.Data.TransfersPeriods`: path data pass forwards, and proportionality of periods passes
  backwards.
* `New.Data.exists_transfersPeriods_off_diagonal`: a turn off the diagonal transfers periods.

Notions from other files:
* `New.Data.GridNode`: a triple `(z, a, b)`, the node `Y^a_b` if `z = false` and `Ỹ^b_a` if
  `z = true`. Its index set is `D.NodeIndex`, which is `D.GridIndex z a b`.
* `New.Data.EdgeTuple`: a matrix over the residue ring modulo `gridModulus ϑ` for each pair of
  nodes. The modulus is that of the twist `ϑ` times a power of the product of the chosen places. A
  `New.Data.NodeFamily` is an invertible matrix `g q` for each node `q`; it takes the matrix `S e`
  on an edge `e = (p, q)` to `(g q)⁻¹ * S e * g p`. It is admissible (`New.Data.IsAdmissibleFamily`)
  if at each of the two starting nodes it lies in the level of the node and at each node
  `(true, a, a)` it is `g ⊕ 1` for its element `g` at `(false, a, a)`.
* `New.Data.IsPathDatum N w`: a function of the matrices on the edges `w` that admissible families
  fix up to `edgeCharProd`, that vanishes unless the vertical edges carry split injective matrices,
  and whose values are sums of at most `N` roots of unity.
* `New.AreMatched`: matched functions, `Φ(x_γ) = χ(det γ) Ψ(y_γ)` with both supported on such
  matrices, `y_γ` being the first columns of `γ` and `x_γ` the last rows of `γ⁻¹`. The subring
  argument, here `⊤`, is where the entries of `γ` and `γ⁻¹` lie. `New.Exchange.matchOf` is the match
  of a function.
* `New.Exchange.SquareLaw` with constant `C`, for functions `L` and `L'` on matrices over a finite
  ring: `∑ Ψ L' = C ∑ Φ L` for all matched `Φ`, `Ψ`.



## Turning a path datum

A turn of a path replaces the edges `V' → W₁`, `Ṽ' → W₂` of a square by `W₁ → V`, `W₂ → Ṽ`, where
`Ṽ' = V'` and `Ṽ = V` unless the turn is on the diagonal, at which a line is added to both.

The form that crosses the square goes from `W₁` to `W₂`. For a turn at `V' = (i, j)` in the grid
of the `Y`, and on the diagonal, `W₁` is the corner `(i, j + 1)` and `W₂` the corner `(i + 1, j)`;
in the grid of the `Ỹ` it is the other way round. On the diagonal the line sits on the edges at
`W₂`. The blocks of `y` and `x` at `W₁`, `W₂` are `y₁`, `y₂` and `x₁`, `x₂`.


### `Corner`

 The nodes at a turn of a path. The old path has the edges `V' → W₁` and `Ṽ' → W₂`, the new one
has `W₁ → V` and `W₂ → Ṽ`. A node (`GridNode`) is a place `(z, a, b)` in one of the two grids, and
`D.NodeIndex` is the index set of its basis. The type `T` indexes what `Ṽ'` has beyond `V'` and
`Ṽ` beyond `V`: in the use off the diagonal it is empty, and on the diagonal it indexes one line. 

### `Corner.low`

 The node `V'` that the turn removes. 

### `Corner.lowExt`

 The node `Ṽ' = V' ⊕ T`. 

### `Corner.fst`

 The node `W₁`, kept by the turn and joined to `V'` and to `V`. 

### `Corner.snd`

 The node `W₂`, kept by the turn and joined to `Ṽ'` and to `Ṽ`. 

### `Corner.high`

 The node `V` that the turn adds. 

### `Corner.highExt`

 The node `Ṽ = V ⊕ T`. 

### `Corner.sndEquiv`

 The basis of `W₂` as it is numbered in the square. 

### `Corner.lowEquiv`

 The basis of `Ṽ'` is that of `V'` and `T`. 

### `Corner.highEquiv`

 The basis of `Ṽ` is that of `V` and `T`. 

### `oldEdges`

 The edges of the old path, `w` being those that the turn preserves. 

### `newEdges`

 The edges of the new path. 

### `char`

 The character `χ` for which the data on the two sides of the square are matched: the inverse of
the product of the characters `edgeChar` of the two old edges. It lives on the residue ring modulo
`gridModulus ϑ`, the modulus of the twist `ϑ` times a power of the chosen places. 

### `IsTurn`

 The conditions under which the corner is a turn of a path whose other edges are `w`, for the
twist `ϑ`. A family `g` of invertible matrices, one for each node, is admissible
(`IsAdmissibleFamily`) if it lies in the level at the two starting nodes and is `g ⊕ 1` on the
diagonal of the second grid, for its element `g` at the same place of the first. 

### `IsTurn.fst_ne_snd`

 The two kept nodes differ. 

### `IsTurn.ne_low_and_ne_lowExt`

 The removed nodes are not on the new edges. 

### `IsTurn.endpoints_notMem`

 The other edges avoid the removed nodes and do not end at the added ones. 

### `IsTurn.vertical`

 One old edge is vertical, and the new edge at the same kept node is not. 

### `IsTurn.edgeChar_fst`

 Opposite edges have the same character. 

### `IsTurn.edgeChar_snd`

 Opposite edges have the same character. 

### `IsTurn.apply_highExt`

 Only the group of `V` acts at `Ṽ`. 

### `IsTurn.exists_eq_low`

 The node `V'` is inner: any element `k` may act there, through `k ⊕ 1` at `Ṽ'`. 

### `oldMatrix`

 The matrix `y : V' → W₁ ⊕ W₂` read on the old edges. 

### `oldColumn`

 The column `v : T → W₂` read on the old edge at `Ṽ'`. 

### `newMatrix`

 The matrix `x : W₁ ⊕ W₂ → V` read on the new edges. 

### `newRow`

 The row `v' : W₂ → T` read on the new edge at `Ṽ`. 

### `oldTuple`

 The tuple with `y` and `v` on the old edges and the matrices of `S` elsewhere. 

### `newTuple`

 The tuple with `x` and `v'` on the new edges and the matrices of `S` elsewhere. 

### `columnFourier`

 The column Fourier transform `Ψ̂'(y, v') = ∑ v, ψ(v' v) Ψ'(y, v)` in the column `v` of the line,
where `ψ(v' v)` is the additive character `ψ` at the trace of `v' v` and the matrices on the other
edges are those of `S`. 

### `turned`

 The datum on the new path: the match for the character `c.char ϑ` of the column Fourier
transform of `Ψ'`, taken at the row `v'` and the matrix `x` that are read on the new edges of `S`.
The bijection `ε` identifies the indices of `V'` and `V` with those of `W₁ ⊕ W₂`. 

### `sndGL`

 The element of a family at `W₂`, in the basis of the square. 

### `sumGL`

 The element of a family on `W₁ ⊕ W₂`. 

### `sum_tuplesOn_oldEdges`

 Let the corner `c` be a turn, for the twist `ϑ`, of a path whose other edges are `w`. A sum over
the tuples on the old edges is a sum over three things, put together by `oldTuple`: a tuple `S` on
the preserved edges `w`, a matrix `y` on the old edges and a matrix `v` of type `Matrix B T`. Here
`tuplesOn ϑ w` is the set of tuples of matrices that are zero off `w`. 

### `sum_tuplesOn_newEdges`

 Let the corner `c` be a turn, for the twist `ϑ`, of a path whose other edges are `w`. A sum over
the tuples on the new edges is a sum over three things, put together by `newTuple`: a tuple `S` on
the preserved edges `w`, a matrix `v'` of type `Matrix T B` and a matrix `x` on the new edges. 

### `columnFourier_congr`

 The column Fourier transform of a path datum `Ψ'` on the old path depends on `S` only through
the matrices of the preserved edges `w`. 

### `columnFourier_tupleAction`

 Let the corner be a turn and `Ψ'` a path datum on the old path, let `g` be an admissible family
and let `k` be an invertible matrix at the removed node `c.low`. Then moving `S` by `g`, replacing
`v'` by `v' * c.sndGL g` and `y` by `(c.sumGL g)⁻¹ * y * k` changes the column Fourier transform
only by the characters of the edges at the determinants. 

### `hasLeftInv_of_columnFourier_ne_zero`

 If the column Fourier transform of a path datum `Ψ'` on the old path is nonzero at `(v', y)`,
then the blocks of rows of `y` that lie on vertical edges, and the matrices of `S` on the vertical
edges in `w`, have left inverses. 

### `newRow_tupleAction`

 An admissible family `g` moves the row `v'` read on the new edge at `Ṽ` only through its
element at `W₂`. 

### `newMatrix_tupleAction`

 Let the corner `c` be a turn (`hc`). An admissible family `g` acts on tuples by `tupleAction`.
This moves the matrix `c.newMatrix S` read on the new edges on the left by `(g c.high)⁻¹`, the
inverse of its element at the node `V = c.high`. It moves it on the right by `c.sumGL g`, its
element on `W₁ ⊕ W₂`. 

### `areMatched_columnFourier`

 Let the corner `c` be a turn (`hc`), `Ψ'` a path datum on the old edges (`hΨ'`) and `v'` a
matrix. Then the function `matchOf` of the column Fourier transform `c.columnFourier ψ Ψ' S v'` is
matched with this transform for the character `c.char ϑ`. 

### `turned_tupleAction`

 Let the corner `c` be a turn and `Ψ'` a path datum on the old path. The turned datum
`c.turned ε ψ Ψ'` is the match of the Fourier transform of `Ψ'` in the column of the line, read on
the new edges; `ε` is the bijection between the indices of the removed and added nodes and those of
the two kept nodes. It is fixed by the action of an admissible family `g` up to `edgeCharProd g` of
the edges of the new path: the product over the edges `(p, q)` of their characters at
`det (g q) / det (g p)`. 

 ### The turned datum and the sum over a square 

### `exists_turned_eq`

 Let the corner `c` be a turn (`hc`) and `Ψ'` a path datum on the old edges (`hΨ'`). If
`c.turned ε ψ Ψ' S` is nonzero, then there is an invertible matrix `γ` with
`c.newMatrix S = invLastRows ε γ`, the matrix on the new edges. For this `γ` the value
`c.turned ε ψ Ψ' S` is `χ(det γ)`, for `χ = c.char ϑ`, times `c.columnFourier ψ Ψ' S` taken at the
row `c.newRow S` and at `firstCols ε γ`. 

### `hasLeftInv_of_turned_ne_zero`

 Let the corner be a turn, `Ψ'` a path datum on the old path and `ε` the bijection between the
indices of the removed and added nodes and those of the two kept nodes, for which the turned datum
is formed. Where this datum is nonzero at `S`, the matrices of `S` on the vertical edges of the new
path have left inverses, as a path datum on the new path requires. 

### `isSumOfRootsOfUnity_turned`

 Let the corner `c` be a turn (`hc`) and `Ψ'` a path datum (`IsPathDatum`) on the old edges,
whose values are sums of at most `N` roots of unity. Then each value `c.turned ε ψ Ψ' S` of the
datum on the new path is a sum of roots of unity, at most `N` times the number of matrices in
`Matrix B T` over the residue ring. 

### `exists_isPathDatum`

 Turning a path datum: let the corner be a turn and let `Ψ'` be a path datum on the old path,
with at most `N` roots of unity in a value. Hold fixed the matrices of the preserved edges and take
the Fourier transform of `Ψ'` in the column of the line (`columnFourier`). For each row `v'` the
match of the transform is `Ψ(·, v')` for a path datum `Ψ` on the new path, and the bound for the
number of roots of unity in a value is multiplied by the number of column matrices `v`. 

### `sum_eq_of_squareLaw`

 The exchange on a square at which the path turns. The sum over the tuples on the old path
(`tuplesOn`) against `Ψ'` equals `C` times the sum over the tuples on the new path against a datum
`Ψ` that matches the column Fourier transform of `Ψ'`. The square law with constant `C` is given for
a family of pairs `L i, L' i`. The index `f S v'` may depend on the matrices of the preserved edges
`w` and on the row `v'`. 

 ## The exchange on a square of the grids 

### `turnRatio`

 The ratio of the turn at `(i, j)`: the product over `1 ≤ s ≤ D.t` of the ratios of Hecke values
at `s` of the character `untwistedLiftChar (i + 1) * untwistedLiftChar (j + 1)` at the twist
`ϑ ^ (j + 1)`. 

### `squarePair`

 The critical pair of a square: the character `ν = untwistedLiftChar (a + 1) * untwistedLiftChar
(b + 1)`, of weight `-(D.liftWeight (a + 1) + D.liftWeight (b + 1))`, with its tame part `tamePart`
and the integer `z = D.t`. In a critical pair (`D.CriticalPair`) minus the weight is at least `z`
and at most `4 * D.b` at every infinite place. 

### `isRamified_squarePair`

 The pair `squarePair ha hb` of the square `(a, b)` is ramified: its tame part is nontrivial
exactly at the chosen places. 

### `isRamifiedRatio_turnRatio`

 For `i, j < D.m` the ratio `turnRatio i j` of a turn is the product of the ratios of Hecke
values of a ramified critical pair at the powers `ϑ ^ (j + 1)` of the twists. 

### `card_gridIndex_square`

 The two pairs of opposite corners of a square of the grid `z` have the same sum of ranks. 

### `charOfTamePart_gridModulus_mul`

 The character of the residue ring with given tame parts is multiplicative in the tame parts. 

### `edgeChar_columnEdge_mul_rowEdge`

 The characters of the two edges at the node `(a, b)` of the grid `z` multiply to the character
with components `(squarePair ha hb).tamePart * ϑ.tamePart ^ n`, for `n = a + 1` if `z` and
`n = b + 1` otherwise. 

### `gridChar_mul_gridChar_eq_rankTwist`

 Let `a, b < D.m`, let `r` be the sum of the ranks of the corners `(a, b + 1)` and `(a + 1, b)`
of the grid `z`, and let `p`, `q` be index types with `card p + card q = r`. The character
`gridChar ϑ z a p` of the edges of the lifts times `gridChar ϑ (!z) b q`, that of the edges of the
transposed lifts, is `rankTwist` of the product `ν * ϑ.toAutChar ^ n` in the rank `r`. Here
`ν = (squarePair ha hb).character = D.untwistedLiftChar (a + 1) * D.untwistedLiftChar (b + 1)`, with
`D.untwistedLiftChar j` the untwisted character of the `j`-th lift, `ϑ.toAutChar` is the character
of the twist `ϑ`, and `n = a + 1` if `z`, `n = b + 1` otherwise. 

### `card_gridIndex_square_le`

 For the sum `W` of the corners `(a, b + 1)` and `(a + 1, b)` of the square, half the rank of
`W` minus its number of negative signs is at most `(squarePair ha hb).negWeight τ`, minus the
weight of the pair of the square at the infinite place `τ`. The signs are `D.gridSigns z 0`, those
of the nodes of the grid `z` (offset `0`). 

### `exists_squareLaw_grid_hasAbsUpToNormPower`

 Crossing the square `(a, b)` of the grid `z`, for `a, b < m`: there are a constant `κ`, a
bijection `σ` between the indices of the two pairs of opposite corners and numbers `c ϑ ≠ 0` with
the following property. Let `f` be a form at the node `(a, b + 1)` and `l` a functional on the forms
at the node `(a + 1, b)`. Then the values of `l` at the images of `f` through `(a + 1, b + 1)`, by a
lift and a transposed lift, each by a matrix modulo `gridModulus ϑ`, and through `(a, b)`, by a
transposed lift and a lift, satisfy the square law with constant `κ / c ϑ`; the constant `κ` may be
`0`. The character of the law is the inverse of the product of the characters `edgeChar` of the
edges from `(a, b)` to `(a, b + 1)` (`columnEdge`) and to `(a + 1, b)` (`rowEdge`). The numbers
`c ϑ` have absolute value `turnRatio` up to a constant and a power of the norm of the modulus of
`ϑ`. 


## Transfers of periods, and turns off the diagonal

The property that one turn provides, `New.Data.TransfersPeriods`, passes to composites of turns.


### `TransfersPeriods`

 The property of turns and their composites, for any two paths `Γ'`, `Γ`: path data `Ψ'` on `Γ'`
give path data `Ψ` on `Γ` with the bound for the number of roots of unity in a value multiplied by
`k`, and if `Ψ` is proportional to `Ξ`, then `Ψ'` is proportional to `Ξ / c`. A triple
(`D.PeriodTriple`) is a twist and two forms, one at the start of each half of a path; `Ψ` is
proportional to `Ξ` (`IsProportional`) if at each real point its period, a function of the
triples, is a multiple of `Ξ` by a number independent of the triple. 

### `TransfersPeriods.mono`

 A pair of paths that transfers periods with bound `k` also transfers them with every larger
bound `k'`. 

### `TransfersPeriods.trans`

 Period transfers compose: the bounds and the constants multiply. 

### `innerCorner`

 The corner at the node `(a, b)` of the grid `z`, for a turn off the diagonal. 

### `isTurn_innerCorner`

 Let `a < b < m`, let `z` select one of the two grids and let `ϑ` be any `m`-fold twist. If the
edges `w` avoid the node `(z, a, b)` and do not end at `(z, a + 1, b + 1)`, then the corner at
`(z, a, b)` is a turn of a path whose other edges are `w`: it meets the conditions
(`Corner.IsTurn`) for replacing the two sides of the square at `(z, a, b)` by the two sides at
`(z, a + 1, b + 1)`. 

### `edges_eq_oldEdges_innerCorner`

 If the half in the grid `z` of `Γ'` is `q`, the two sides through `(a, b)`, then `r`, the edges
of `Γ'` are these two sides and the edges of `q`, `r` and the other half. 

### `edges_update_eq_newEdges_innerCorner`

 If the half in the grid `z` is replaced by `q`, the two sides through `(a + 1, b + 1)`, then
`r`, the edges are these two sides and the edges of `q`, `r` and the other half. 

### `sum_formMap_eq_of_squareLaw`

 The exchange at the corner `(a, b)` of the grid `z`, for one twist `ϑ`. Let `q` be a grid path
from `(0, D.m)` to `(a, b + 1)` and `r` one from `(a + 1, b)` to a diagonal node `(k, k)`. Let the
corner be a turn of a path whose other edges `w` contain those of `q` and `r`, let `Ψ` match the
column Fourier transform of `Ψ'`, and let the square law hold with constant `C`. Carry a form `F`
at `(0, D.m)` along `q`, two sides of the square and `r`, and read it at `(k, k)` by functionals
`l S` that depend on the tuple `S` only through its matrices on `w`. Then the sum against `Ψ'`
through `(a, b)` is `C` times the sum against `Ψ` through `(a + 1, b + 1)`. 

### `exists_transfersPeriods_off_diagonal`

 Fix the data `D`, with `m = D.m`, let `a < b < m` and let `z` say which of the two halves of a
path is changed. A turn off the diagonal, at the corner `(a, b)` of that half, transfers periods
with bound `1` and nonzero numbers `c ϑ`, one for each `m`-fold twist `ϑ`, whose absolute value is,
up to a constant and a power of the norm of the modulus of `ϑ`, the ratio of Hecke values
`turnRatio` of the square (at `(b, a)` if `z`): the old half is `q`, the two sides through `(a, b)`,
then `r`, and the new half passes through `(a + 1, b + 1)` instead. 
