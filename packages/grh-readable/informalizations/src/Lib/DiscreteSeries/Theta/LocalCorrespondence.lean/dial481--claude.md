---
{
  "module": "src/Lib/DiscreteSeries/Theta/LocalCorrespondence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Theta/LocalCorrespondence.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Theta/LocalCorrespondence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Existence of joint harmonics, Howe's argument and the local theta correspondence

This file works in the polynomial (Fock) model of a dual pair of unitary groups. For matching
parameters, a joint harmonic is built as a product of minors along layers. For an oscillator pair,
the projection of a joint harmonic by the discrete series kernel is then nonzero, is fixed by
`π'(f)` for functions `f` that reproduce the kernel of the second group, and generates all projected
polynomial vectors under bump functions of the second group.

## Main definitions and results

* `New.IsLayering`: finitely many layers, each a list of rows paired with columns, of weight `ν`.
* `New.IsMatch.isLayering`: for matching parameters (`New.IsMatch`) the sets of variables
  `New.FockDualPair.Layer` are layers of weight `New.HCParam.lowestKType l`.
* `New.IsMatch.exists_isJointHarmonic`: hence a joint harmonic (`New.IsJointHarmonic`) exists.
* `New.IsJointHarmonic.howe_argument`: in the polynomial (Fock) model with its row action
  `T.oscRows` and column action `T.swap.oscRows`, a subspace that is stable under the columns,
  contains a joint harmonic (`New.IsJointHarmonic`) and contains certain images of the row operators
  is the whole space.
* `New.OscillatorPair.re_inner_integratedRep_pos`: for a joint harmonic `Φ` and `Φ₁ = π(e_λ) Φ`,
  with `e_λ` the discrete series kernel, `⟨Φ, Φ₁⟩` has positive real part.
* `New.OscillatorPair.integratedRep_integratedRep_eq_self`: `π'(f) Φ₁ = Φ₁` for every `f` of
  suitable decay that reproduces `e_λ'`; the proof compares the Casimir operators of the two groups
  on `Φ` and uses `New.integratedRep_fix_of_isKHighest`.
* `New.OscillatorPair.exists_bump_integratedRep_eq`: every `π(e_λ) P` is obtained from `Φ₁` by a
  bump function of the second group; the proof rests on `New.IsJointHarmonic.howe_argument`.

Notions from other files:
* `New.HCParam.IsKHighest`: each matrix unit `E a a` acts on `x` by `ν a`, and `x` is killed by the
  compact raising operators, the `E a b` with `ε a = ε b` and `l b < l a`.
* `New.IsJointHarmonic`: `l` and `l'` match (`New.IsMatch`), and `Φ ≠ 0` is highest for rows and
  columns, of the weights of the two lowest `K`-types, and harmonic along rows and columns.
* `New.OscillatorPair`: two commuting oscillator representations on one Fock space, one acting on
  the rows and one on the columns.
* `New.pairSign`: the sign `σ * ε r * ε' c` of the variable in row `r` and column `c`, with
  `σ = T.globalSign`; `T.varSign (r, c)` is this sign.
* `New.FockDualPair.IsMatchedPair`: the row `r` is matched with the column `c`: with `n = card R`,
  `n' = card C`, `γ = T.rowShift`, `γ' = T.columnShift` and `a = l r - 2γ + n'`, one
  has `a = -(l' c - 2γ' + n)` and `|n - n'| < σ * ε r * ε' c * a`.
* `New.HCParam.lowestKType`: the integer vector Λ = λ+ρ−2ρ_c for a parameter l = 2λ, the highest
  weight of the lowest K-type.

## Relation to the literature

Known result: Theta correspondence of discrete series for real unitary dual pairs, with joint
harmonics. Only matched parameters with large gaps on Fock space are treated. The joint harmonic
exists and is unique up to scalar, and its projection is fixed by the partner's `π'(f)` for every
`f` of suitable decay that reproduces the partner's discrete series kernel. The projection of every
polynomial vector is a compactly supported smoothing, under the second group, of the projected joint
harmonic. Source: J.-S. Li, Theta lifting for unitary representations with nonzero cohomology, Duke
Math. J. 61 (1990) 913-937; R. Howe, Transcending classical invariant theory, J. Amer. Math. Soc. 2
(1989); A. Paul, First occurrence for the dual pairs (U(p,q), U(r,s)), Canad. J. Math. 51 (1999)
636-657, Theorem 2.7.



## Products of minors along layers and existence of joint harmonics

Existence of joint harmonics in the Fock model `T` of a dual pair of unitary groups. Polynomials in
the variables `X (T.varEquiv (r, c))` carry two actions. `New.FockDualPair.oscRows` is an action of
`gl R` (rows `r`, signs `ε`). `New.FockDualPair.vacuumWeight` is the weight of the vacuum `1`.
`New.FockDualPair.IsTermwiseHarmonic` forbids, in a monomial, two variables in one column from rows
of opposite signs; for `T.swap` it is the same with rows and columns exchanged.

A matched pair (row `r`, column `c`) occurs in `|New.FockDualPair.relWeight l r|` layers, one at
each level below that number. The signs cut the variables into four quadrants; the layers of one
pair of signs are nested and give the leading minors of that quadrant.


### `derivation_apply_prod`

 A derivation of a polynomial ring sends a finite product to the sum of the products in which
one factor is replaced by its derivative. 

### `derivation_prod_det`

 If a derivation `D` acts on the columns of each matrix `M t` of polynomials through the matrix
`N t` (column `i` goes to `∑ j, N t i j •` column `j`), then it multiplies `∏ t, det (M t)` by
the sum of the traces of the `N t`. 

### `IsLayering`

 Finitely many layers `t`, each pairing distinct rows `ρ t` with columns `κ t`. Layers that share
a row have columns of one sign. With each of its rows a layer contains all rows of the same sign as
that row that lie further out in `l` than it, in the direction given by the sign
`New.FockDualPair.varSign` of its variable in that layer. The total weight is `ν`. 

### `IsLayering.injective`

 The rows of a layer are distinct. 

### `IsLayering.sign_eq`

 Two layers (possibly the same) that share a row have all their columns of one sign. 

### `IsLayering.closed`

 A layer with the row `ρ t i` has every row `r` of the same sign with `l r > l (ρ t i)` if
  `New.FockDualPair.varSign` is `1` at `(ρ t i, κ t i)`, with `l r < l (ρ t i)` if it is `-1`. 

### `IsLayering.weight_eq`

 The weight `ν r` is that of the vacuum plus the signs `New.FockDualPair.varSign` at the pairs
  `(r, κ t i)`, over all `(t, i)` with row `ρ t i = r`. 

### `IsLayering.polarisation_prod_det`

 Let `(ρ, κ)` be layers and let `P` be the product of their minors, with the matrices transposed.
If `a = b`, or `a` has the sign of `b` and lies further out than `b` in the direction `s`, then the
polarisation `∑ X (a, c) * ∂P/∂X (b, c)`, over the columns `c` where the variable `(b, c)` has sign
`s`, is `P` times the number of `(t, i)` with `ρ t i = a = b` and `T.varSign (b, κ t i) = s`. 

### `IsLayering.isKHighest_and_isTermwiseHarmonic`

 Let `(ρ, κ)` be a layering of weight `ν` for `l`: finitely many layers `t`, each pairing
distinct rows `ρ t` with columns `κ t`, such that layers sharing a row have columns of one sign,
each layer contains with each of its rows all rows of the same sign lying further out in `l` in the
direction of the sign of its variable, and the total weight is `ν`. The product `P` over `t` of the
minors of the variables with rows `ρ t` and columns `κ t`, written here with the transposed
matrices, is `K`-highest of weight `ν` for the row action `T.oscRows` and `l`. Also, no monomial of
`P` has two variables in one row whose columns have opposite signs. 

### `IsLayering.isJointHighest_prod_det`

 Let `(ρ, κ)` be layers of weight `ν` for the rows and `(κ, ρ)` layers of weight `ν'` for the
columns. Then the product over `t` of the minors of the variables with rows `ρ t` and columns `κ t`
is nonzero, highest of weight `ν` for the rows and `ν'` for the columns, and harmonic both ways. 

### `IsLayering.isJointHighest_of_eq_prod_det`

 Version of `IsLayering.isJointHighest_prod_det` for a polynomial `P` that is given as the
product of the minors: `P` is nonzero, highest of weight `ν` for the rows and `ν'` for the columns,
and harmonic both ways. 

### `IsMatch.exists_isMatchedPair_of_relWeight_ne_zero`

 Let the parameters `l` and `l'` match: each row and each column is either matched, that is, its
centred parameter (`l r - 2 γ + card C` for a row) is large and opposite to that of its partner, or
has a small one. Then a row `r` of nonzero weight `T.relWeight l r` (the lowest `K`-type relative to
the vacuum) is matched with a column `c`, and the weight has the sign of the variable `(r, c)`. 

### `IsMatch.exists_isMatchedPair_of_outer`

 Let the row `r` be matched with the column `c` and have nonzero weight `T.relWeight l r`. A row
`r'` of the same sign that lies further out in `l`, in the direction of the sign of the variable
`(r, c)`, is matched with a column of the sign of `c`, and its weight is at least as large in
absolute value. 

### `Layer`

 The layer `t` for the heights `w` of the variables. Here `t` is a level below the largest height
together with a pair of signs. The layer consists of the variables of height above that level whose
signs `(ε r, ε' c)`, for row `r` and column `c`, are sent to that pair by `s`. 

### `layerRow`

 The row of a variable of the layer `t`. 

### `layerCol`

 The column of a variable of the layer `t`. 

### `IsMatch.isLayering`

 Let `l = 2λ`, `l' = 2λ'` match (`IsMatch`): with `n = card R` and `n' = card C` both have gap
`500(n+n')³`, and with `ξ r = λ r − γ + n'/2` and `ξ' c = λ' c − γ' + n/2`, rows and columns pair
off as `ξ r = −ξ' c` with `σ ε r ε' c ξ r > |n−n'|/2`, the rest having small `|ξ|`. Let the height
`w` of the variable of `(r, c)` be `|T.relWeight l r|` (row-`r` entry of the lowest `K`-type minus
the vacuum weight) if `(r, c)` is matched, and `0` otherwise. Then the layers, with rows
`T.layerRow s w` and columns `T.layerCol s w`, form an `IsLayering` of weight `l.lowestKType`. The
permutation `s` of the pairs of signs lets the rows and the columns use the same layers. 

### `IsMatch.exists_isJointHarmonic`

 If the parameters `l = 2λ`, `l' = 2λ'` match, there is a joint harmonic. With `n = card R` and
`n' = card C`, matching means that both have gap `500(n+n')³`, and the entries
`ξ r = λ r − γ + n'/2`, `ξ' c = λ' c − γ' + n/2` pair off as `ξ r = −ξ' c` with
`σ ε r ε' c ξ r > |n−n'|/2`, the rest having small `|ξ|`. A joint harmonic is a nonzero polynomial
that is highest of weights `New.HCParam.lowestKType l` for the rows and
`New.HCParam.lowestKType l'` for the columns, and satisfies `New.FockDualPair.IsTermwiseHarmonic`
along columns and along rows (for `T` and `T.swap`).

This is the existence part of the known correspondence of discrete series by joint harmonics. 


## Howe's argument in Fock space

The proof is an induction on the degree with the Fischer inner product, ending in the uniqueness of
the joint harmonic.


### `New.Fischer.fockLaplacian_eq_zero_of_pderiv_eq_zero`

 For rows `a` and `b` with `ε a ≠ ε b`: if row `b` of `Q` has no variable of sign `1`, or row `a`
has none of sign `-1`, then the Laplacian `T.fockLaplacian a b` kills `Q`. It is a sum, over the
columns `c` with `T.varSign (a, c) = -1`, of terms built from `∂/∂X(a,c) ∂/∂X(b,c)`. 

### `New.IsMatch.centredParam_lt_or_lt`

 For matched parameters (each row is matched with a column or has a small centred parameter) and
`l b ≤ l a`, the centred parameter `l b - 2γ + card C` of row `b` is below `card R - card C` or that
of row `a` is above `card C - card R`. 

### `New.Fischer.perpInDegree_ne_bot`

 If `G` does not contain all polynomials of degree at most `j`, then some nonzero one of them is
orthogonal to those in `G` for the Fischer inner product. 

### `New.IsMatch.pderiv_eq_zero_of_lt_centredParam`

 Let `Q` be highest of the weight `Λ` of the lowest `K`-type for the rows and harmonic for the
columns (each `T.swap.fockLaplacian c d` with `ε' c ≠ ε' d` kills `Q`). If `s` times the centred
parameter `l r - 2γ + card C` of row `r` exceeds `card C - card R`, then `Q` has no variable of sign
`-s` in that row. 

### `New.IsJointHarmonic.howe_argument`

 Howe's argument: a column-stable subspace that contains a joint harmonic and the images (a)–(c)
below is the whole space.

Let `Φ` be a joint harmonic of the dual pair `T`, that is, a nonzero polynomial, highest of the
weights of the lowest `K`-types and harmonic for rows and columns. Let `G` be a space of polynomials
that is stable under the action `T.swap.oscRows` on the columns and contains `Φ`. Write `ρ` for the
action `T.oscRows` on the rows and `Λ` for `l.lowestKType`. Suppose that `G` contains
(a) `ρ X P` for every matrix `X` and every highest vector `P` of a weight `ν` with `ν - Λ` outside
`l.rootCone`, the cone of the positive roots,
(b) the images of the `E b a` with `ε a = ε b` and `l b < l a`,
(c) the images of the `E a a - Λ a`.
Then `G` is the whole space. 


## The projected joint harmonic and the local theta correspondence

The analytic part of the local theta correspondence. Let `π`, `π'` be an oscillator pair on Fock
space (`New.OscillatorPair`), `Φ` a joint harmonic of parameters `l`, `l'`
(`New.IsJointHarmonic`), and `Φ₁ = π(e_λ) Φ`, where `π(f) = ∫ f g • π g` is
`New.integratedRep π f`, `e_λ` is `New.HCParam.dsKernel l` (the signs come from the type of `l`),
and a polynomial is read as a vector of Fock space by `New.Fock.polyVector`.

The results are stated for the projection `π(e_λ)` of the first group, which acts on the rows; those
for the second group follow by `New.OscillatorPair.swap`. To work with `-λ` in place of `λ`, apply
them to the parameters `-l` and `-l'`; the kernel `e_{-λ}` is the conjugate of `e_λ`.


### `swap`

 Let `T` be the data of a dual pair in Fock space: a sign `T.globalSign`, integers `T.rowShift`
and `T.columnShift`, and variables indexed by `R × C`, with `R` and `C` nonempty. If `π` of `U(ε)`
and `π'` of `U(ε')` form an oscillator pair for `T` (two commuting oscillator representations on
one Fock space, `π` on the rows and `π'` on the columns), then `π'` and `π` form an oscillator pair
for `T.swap`. `T.swap` exchanges rows and columns, has sign `-T.globalSign`, row shift
`T.columnShift` and column shift `T.rowShift`. 

### `map_integratedRep_dsKernel`

 The operator `π(e_λ)` commutes with the action of the second group. 

### `isDerivedAction_integratedRep`

 Along the map `P ↦ π(e_λ) P` from polynomials to Fock space, the representation `π'` of the
second group has the column action `T.swap.oscRows` as its derived action. 

### `re_inner_integratedRep_pos`

 For an oscillator pair π, π' on Fock space and a joint harmonic Φ of parameters `l = 2λ` and
`l' = 2λ'`, the real part of ⟨Φ, π(e_λ)Φ⟩ is positive. Here `π(e_λ)` is the operator `∫ e_λ g • π g`
of the discrete series kernel `e_λ` (`New.HCParam.dsKernel`). 

### `integratedRep_integratedRep_eq_self`

 Let `Φ` be a joint harmonic (nonzero, highest of the lowest `K`-types and harmonic on both
sides) of an oscillator pair `π`, `π'` (commuting oscillator representations) and `f` a function on
the second group such that `g ↦ f g ‖g‖ ^ card I` is integrable and `f * e_λ' = e_λ'`, where `e_λ`
and `e_λ'` are the discrete series kernels of the parameters `l` and `l'`. Then the operator `π'(f)`
fixes `π(e_λ) Φ`. This applies to `f = e_λ'` and to bump functions that reproduce `e_λ'`. 

### `integratedRep_oscRows_eq_zero`

 If `Q` is highest of a weight `ν` with `ν - Λ` outside the cone of the positive roots, where `Λ`
is the lowest `K`-type of `l`, then `π(e_λ)` kills every derivative `Y Q` of `Q` along the rows. 

### `exists_bump_integratedRep_eq`

 Let `π`, `π'` be an oscillator pair for `T`: commuting representations of `U(ε)` and `U(ε')` on
one Fock space, acting on the rows and columns. Let `R`, `C` be nonempty. Let `Φ` be a joint
harmonic: `l`, `l'` match, and `Φ ≠ 0` is `K`-highest of the lowest `K`-type weights and termwise
harmonic for `T` and `T.swap`. Then for every polynomial `P` there is a smooth compactly supported
`α` on the second group (an element of `Bumps ε'`) with `π(e_λ) P = π'(α') π(e_λ) Φ`, where
`α' g = α g⁻¹` and `e_λ` is the discrete series kernel. The inversion is the convention of
`DiscreteSeries.smear`; `α'` is again smooth with compact support.

This smoothing statement is used in place of Howe's duality theorem for real unitary pairs (R. Howe,
Transcending classical invariant theory). It is proved by Howe's argument
(`New.IsJointHarmonic.howe_argument`) instead of through irreducibility. 
