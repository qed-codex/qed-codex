---
{
  "module": "src/New/OneLift/HeckeValues/CharacterLiftNorm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/CharacterLiftNorm.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/CharacterLiftNorm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The lift of a character and its squared norm as a Hecke L-value

Let `p = (ν, z)` be a critical pair (`New.Data.CriticalPair`) with `z ≥ 2` and `ϑ` a tame character
with set of places `Q`. The first section defines the lift `φ` of `ν ϑ` from `U(1)` to the definite
`U(2 z)`, a denominator for its values, and its normalized squared norm. The second section works
with any lift data `X` (`New.LValueData`) and the lift `X.trivialLift`, which differs from `φ` by
the scales of the vacuum and of the derivatives. For even rank `2 k ≥ 4` its squared norm is an
explicit multiple of the value at `k` of the partial Hecke `L`-function of `X.u1Char⁻¹`, where
`X.u1Char` is the character of the data.

## Main definitions and results

* `New.Data.CriticalPair.trivialLift`: the lift `φ` of `ν ϑ`, which is the lift for these data times
  `vacuumScale ^ card n` and `(π̄ * jetScale) ^ rowLengthSum`, where `π = D.piMBar`.
* `New.Data.CriticalPair.denomBound`: a denominator `n_ν` for the values of `φ`.
* `New.Data.CriticalPair.algPart`: the squared norm of `φ` divided by `N(Q) ^ (2 z - 1)`;
  `New.Data.CriticalPair.integralAlgebraicPart` is its multiple by
  `n_L = chosenGroupOrder * denomBound ^ 2`.
* `New.LValueData.trivialLift_eq_smul_thetaLift`: `X.trivialLift` is the theta lift of the constant
  function `1` times the index of the level of `U(1)`.
* `New.LValueData.hasLiftHeckePolynomial_trivialLift`: at split places off the level,
  `X.trivialLift` is spherical, with the Hecke polynomials of a lift of the trivial system
  (`New.DescentPair.HasLiftHeckePolynomial`).
* `New.LValueData.inner_thetaLift_constForm_self`: Rallis' inner product formula
  `New.SiegelWeil.IsSharp.petersson_lift_eq_integral` for the constant `1`. It gives the squared
  norm of the theta lift of `1` as a multiple of the sum of the coefficients of the vacuum.

Notions from other files:
* `New.Data.TameChar`: a character of `U(1)(𝔸)` of weight `0` whose tame part is supported on a
  finite set `Q` of places of norm prime to `D.M * D.N`, with `Q` disjoint from its conjugate.
* `New.LValueData`: two families of split places (`chosenPlace`, and `twistPlace` for `Q`), row
  lengths `rowLength`, and a character `u1Char` of `U(1)(𝔸)` whose tame part is trivial off these
  places.
* `New.LValueData.descentPair`: the descent datum (`New.DescentPair`) attached to the data. Its
  source is the definite line, and its weight has one row of length `rowLength τ` at each infinite
  place `τ`.
* `New.Parameters.vacuumScale`, `New.Parameters.jetScale`: the scaling factor of the vacuum, and the
  scale at which Taylor series of theta functions are taken.
* `New.Data.chosenGroupOrder`: a common multiple of the orders of the stabilisers in the class sums.
* `New.placeSign`: signs on the places of `E` whose Euler product at `k` is the value at `2 k` of
  the zeta function `ζ_F` of the maximal real subfield `F`, over which `E` is unramified.

## Relation to the literature

See `Lib.SiegelWeil.RallisInner.SharpData` for sources.


 ## The lift of a pair, its denominator and the algebraic part 

### `HasLiftRank`

 For the pair `p = (ν, z)`, the index set `n` has `2 z` elements, and `z ≥ 2`. 

### `HasEmptyRow`

 The pair `p = (ν, z)`, with `ν` of weight `-c`, has empty row: `c τ = z` at every infinite place
`τ`. Moreover the index set `n` has `2 z` elements, and `z ≥ 2`. 

### `rowLengthSum`

 The sum `∑ τ, (c τ - z)` of the row lengths of the pair `p = (ν, z)` with `ν` of weight `-c`. It
is the total order of the derivatives in the lift. 

### `denomBound`

 A denominator for the values of the lift: the number `n_ν = M ^ (4 f z) * (M d) ^ j`, where
`M = D.M`, `f = D.f` is the number of infinite places, `d = P.d`, and `j = p.rowLengthSum` is the
sum of the row lengths. 

### `lValueData`

 The lift data `New.LValueData` for the pair `p = (ν, z)` twisted by the tame character `ϑ`, when
`n` has `2 z ≥ 4` elements: the chosen places together with the set `Q` of `ϑ`, the row lengths
`c τ - z` and the character `ν ϑ`. 

### `trivialLift`

 The lift `φ` of `ν ϑ`, an algebraic form on the definite `U(n)` with the weight, level and level
character of the descent datum `(lValueData H ϑ).descentPair` (the space `New.DescentPair.FormV`).
It is the lift for the data `lValueData H ϑ`, multiplied by `vacuumScale ^ card n`, which makes the
vacuum integral, and by the power `rowLengthSum` of the scale `star piMBar * jetScale` of the
derivatives. Both scales are taken at `towerExp = D.towerExp`, the exponent that selects the field
`D.E = P.E towerExp`. 

### `algPart`

 The algebraic part `L^alg(z, ν ϑ) = ‖φ‖ ^ 2 / N(Q) ^ (2 z - 1)`, viewed in `ℂ`: the squared norm
of the lift `φ = trivialLift H ϑ`, divided by a power of the product `N(Q)` of the norms of the
places in the set `Q` of `ϑ`. 

### `integralAlgebraicPart`

 The multiple `n_L L^alg(z, ν ϑ)` of `algPart H ϑ` by the natural number
`n_L = chosenGroupOrder * denomBound ^ 2`. 


## The lift of the constant function and the squared norm

This section concerns the unscaled lift `New.LValueData.trivialLift` from `U(1)` to the definite
`U(n)`, for lift data `X`. Here `New.AutChar.L μ S` is the `L`-function of `x ↦ μ(x / x̄)` without
the factors at `S` and its conjugates, and `New.hookNumber` is the squared Fock norm of the highest
vector of a weight.


 ### The lift is a multiple of the theta lift of `1` 

### `LValueData.isForm_const_one`

 For lift data `X` let `W = X.descentPair.W` be the source of the theta lift: the standard
positive definite hermitian space of rank one over the CM field `E`, with adelic unitary group
`U(1) = G E X.descentPair.signs`. The constant function `1` on this group is a form of parameter
`0`: it is automorphic, bounded, and fixed by right convolution over the real points with
`typeKernel 0 X.descentPair.signs` if this kernel is integrable (`New.Space.IsForm`). 

### `LValueData.constForm`

 The constant function `1` as a form of parameter `0` on the source line of `X.descentPair`. 

### `LValueData.trivialLift_eq_smul_thetaLift`

 The lift `X.trivialLift` is the theta lift `Θ_W 1` of the constant function `1` on `U(1)`, times
the index of the principal level at the chosen places. 

### `LValueData.lift_fockDatum_const_one`

 For lift data `X` the target of the theta lift is the definite `U(n)`, with forms of weight
`mixedWeight n colsPlus colsMinus`: as `colsMinus = 0` and `colsPlus τ` has `X.rowLength τ` columns
of height `1`, it has the single row `X.rowLength τ` at each infinite place `τ`. Let `paramV` be the
doubled Harish-Chandra parameter of this weight and `highestVector` its highest weight vector in the
order that `paramV` gives to the basis.

The lift of the constant function `1` on adelic `U(1)` by the theta kernel `pairThetaKernel` of the
two spaces, at the datum `fockDatum` of the highest vector, is the function `ofAlgForm` on adelic
`U(n)` attached to the algebraic form `X.trivialLift`, divided by the index of the level
`X.chosenLevel` in the integral points of `U(1)`. 

### `LValueData.hasLiftHeckePolynomial_trivialLift`

 The lift `X.trivialLift` has the Hecke polynomials of a lift of the trivial system of
eigenvalues. That is, at a split place `w` of norm `q` with neither `w` nor `w̄` among the places of
`X`, it is spherical with Hecke polynomial `∏_{l < N - 1} (1 - q ^ l α T) * (1 - q ^ (N - 1) α β⁻¹
T)`. Here `N = card n`, and `α`, `β` are the values `New.AutChar.frobValue` at `w` of the characters
`charW`, `charV` of the descent datum `X.descentPair`, for the spaces of ranks `1` and `N`. 

 ### Indices, masses and the real integral 

### `LValueData.index_rangeParabolic_incl`

 Let `F` be the residue field at `w` and `i : n` the index given by the embedding
`X.descentPair.incl : Unit ↪ n`. The subgroup `rangeParabolic` of `GL n F`, the stabiliser of the
hyperplane spanned by the basis vectors other than the `i`-th, has index
`1 + q + ⋯ + q ^ (card n - 1)`, where `q = #F`. 

### `LValueData.index_stabilizer_inclMatrix_col`

 Let `F` be the residue field at `w`. The matrix `inclMatrix F X.descentPair.incl` has one
column, a standard basis vector of `F ^ n`. The index of its stabiliser in `GL n F` is the number
`#F ^ card n - 1` of non-zero vectors. 

### `fockPairing_rename_rename`

 The pairing `fockPairing ℂ P Q = P(∂) Q (0)` of two polynomials is unchanged when the variables
are renamed along an injective map. 

### `LValueData.fockPairing_fockPoly_highestVector`

 Let `X` be lift data and `κ = X.descentPair.columnCount` the weight with one row of length
`X.rowLength τ` at each infinite place `τ`. Let `η` be its highest weight vector, for the order of
the basis given by `paramV`, the doubled Harish-Chandra parameter of this weight, and let
`P = fockPoly η` be the polynomial in the coordinates of `Hom(W, V)` at the infinite places that
corresponds to `η`, with `W`, `V` the definite spaces of ranks `1` and `card n`. Then the squared
Fock norm `⟨P̄, P⟩` is the hook number, where `⟨P, Q⟩ = fockPairing ℂ P Q = P(∂) Q (0)`. 

### `natCard_GL_unit_resField`

 The group `GL Unit (ResField w)` of invertible 1×1 matrices over the residue field `ResField w`
at `w` has as many elements as the unit group `(ResField w)ˣ` of this field. 

### `LValueData.stdLevelIndex_chosenLevel`

 The index of the level `X.chosenLevel` in the integral points of `U(1)` is the product of the
numbers `q - 1` of units of the residue fields at the places `X.chosenPlace`. 

### `LValueData.relIndex_descentResidueLevel`

 For lift data `X` let `i` be the index that the embedding `X.descentPair.incl : Unit ↪ n` picks.
The group `descentResidueLevel` consists of the families in the `GL n k_w`, over the places `w` of
the data (`toLevelPlaces`), that fix the `i`-th basis vector at each `X.chosenPlace` and preserve
the span of the other basis vectors at each `X.twistPlace`. Its preimage `levelOf` under reduction
is the level of the forms on `U(n)`. Its index (`relIndex`) in the group `stdLevel E n` of integral
points has a factor `q ^ N - 1` at each place `X.chosenPlace`, where a vector is fixed, and
`1 + q + ⋯ + q ^ (N - 1)` at each place `X.twistPlace`, where a hyperplane is preserved. Here
`N = card n` and `q` is the norm of the place. 

### `LValueData.blockMeanSquare`

 The mean of `|Ψ|²` for the block datum `Ψ = X.descentPair.blockFn`, that is the proportion of
the columns in its support, written as an explicit product (see `blockMass_eq_blockMeanSquare_div`):
a factor `q ^ (-card n)` at each place `X.chosenPlace` and `(q - 1) / q` at each place
`X.twistPlace`, where `q` is the norm of the place. 

### `LValueData.blockMass_eq_blockMeanSquare_div`

 For lift data `X` the block datum `Ψ = X.descentPair.blockFn` is a function of the columns `x`
of length `card n` modulo the places of `X`: it is zero unless `x` reduces at each `X.chosenPlace`
to one fixed basis vector, and then it is the product over the `X.twistPlace` of the tame characters
at one fixed entry of `x`. The mass `X.descentPair.blockMass` is defined as the sum of `|Ψ x|²` over
these columns, divided by the number of columns and by the order of the product of the groups
`GL Unit k_w` at the places `X.chosenPlace`. It equals the product `X.blockMeanSquare` of `q ^ (-N)`
over the chosen places and `(q - 1) / q` over the twist places (`q` the norm of the place,
`N = card n`), divided by the index of `X.chosenLevel` in the integral points of `U(1)`. 

### `LValueData.isSharp_blockDatum`

 Let `F = X.descentPair.blockDatum` be the finite datum given by the function
`X.descentPair.blockFn` of columns modulo the places of `X` and by the vacuum at the other finite
places. Let `S₀` be the set of the places of `X` and their conjugates, and `J = X.chosenLevel`. Then
`F` is sharp for the action `ω` of `U(1)` with character `X.descentPair.charV`: it is a vacuum off
`S₀`, and at the finite points `g` integral off `S₀` the coefficient `⟨F, ω(g) F⟩` is `⟨F, F⟩ ≠ 0`
for `g ∈ J` and `0` otherwise. Its mass, `⟨F, F⟩` over the index of `J`, is the mean square
`X.blockMeanSquare` of the block datum over this index. 

### `LValueData.blockMeanSquare_mul_relIndex_mul_prod_eq_pow`

 A place of the lift data `X` of norm `q` enters the norm of the lift, besides the index of
`X.chosenLevel` at a chosen place, through three factors:
* its factor in `blockMeanSquare`, the mean square of the block datum: `q ^ (-N)` at a place
`X.chosenPlace` and `(q - 1) / q` at a place `X.twistPlace`, where `N = card n`;
* its factor in the index (`relIndex`) of the level of the forms on `U(n)` in the integral points
`stdLevel E n`.
* the factor `(1 - q ^ (-N))⁻¹` of `ζ_F(N)`, with `F` the real subfield.

So the product over all places of `X` is `N(Q) ^ (N - 1)`, with `N(Q)` the product of the norms of
the twist places. 

### `LValueData.integral_fockInner_realPairWeil`

 For lift data `X` let `v` be the Fock vector (`polyVector`) of the polynomial `fockPoly η` of
the highest weight vector `η` of the weight `X.descentPair.columnCount`, which has one row of length
`X.rowLength τ` at each infinite place `τ`; the basis is ordered by `paramV`, the doubled
Harish-Chandra parameter of this weight. Both hermitian spaces, `W` of rank `1` and that of rank
`card n`, are definite, so the signs `realSigns E (homSigns 1 1)` of the coordinates of the Fock
space are all `1`, and the real points `GInf E X.descentPair.signs` of `U(1)` are one circle for
each infinite place. Let `ω` be the real Weil representation `realPairWeil γ γ'` of `U(1) × U(n)`,
in which `(x, y)` acts by the Fock operator times `∏ τ, det (y τ) ^ γ τ * det (x τ) ^ (-γ' τ)`. Here
`γ = X.descentPair.detExp` is the power of the determinant in the weight of the forms on `U(n)`, and
`γ' τ = -X.rowLength τ`, so that `ω(x, 1)` fixes `v`. Then the integral over the real points `x` of
`U(1)` of `⟨v, ω(x, 1) v⟩` times the Petersson product `⟨1, 1⟩` on `W` is the hook number times the
volume of the adelic quotient `[U(1)]`, the total mass of `quotMeasure` of `stdSpace E Unit`. 

 ### The inner product formula, the Euler product and the norm 

### `LValueData.inner_thetaLift_constForm_self`

 The inner product formula for the constant function `1` on `U(1)`. Let `X` be lift data of rank
`N = card n > 2`. The squared norm of the lift of `1` is a product of six factors:
* the volumes of `[U(1)]` and `[U(n)]` divided by the index of `X.chosenLevel`;
* the dimension of the weight, the cardinality of the index set `WeylIndex` of a basis;
* its hook number, the squared Fock norm of its highest vector;
* the index of the level `levelOf descentResidueLevel` of `U(n)` in the integral points;
* `X.blockMeanSquare`, the product of `q ^ (-N)` over the chosen places and `(q - 1) / q` over the
  twist places, with `q` the norm of the place;
* the sum `vacuumSum` of the coefficients `(b(det g) * finMultiplier g ^ N)⁻¹` of the vacuum, with
  `b = charV = X.u1Char * upsilonU1 ^ (N / 2)` and `finMultiplier` the multiplier of the Weil
  representation. Here `g` runs over representatives of the finite points of `U(1)` modulo those
  integral at every place other than the places of `X` and their conjugates. 

### `eulerProd_placeSign_ne_zero`

 The Euler product `eulerProd placeSign` over the finite places of `E`, with the signs
`placeSign`, does not vanish at `k` for natural `k > 1`. If `E` is unramified over its maximal real
subfield `F` at the finite places, this product at `k` is `ζ_F(2 k)`. 

### `LValueData.eulerProd_indicator_placeSign`

 For lift data `X` let the rank be `card n = 2 * k` with `1 < k`. The function `placeSign` gives
`1` at a place fixed by complex conjugation and the two signs to the two places of a split pair, so
its Euler product `eulerProd placeSign k`, of the factors `(1 - placeSign w * q_w ^ (-k))⁻¹` over
the places `w` of `E`, is `ζ_F(2 k)` for the maximal real subfield `F` when `E` is unramified over
`F` at the finite places, which this lemma does not assume. Setting the signs to zero on
`X.places.conjClosure`, the places of `X` and their conjugates, omits these factors, and so
multiplies the product by `1 - q ^ (-card n)` for each place of `X` of norm `q`. 

### `LValueData.inner_trivialLift_self_eq_L`

 The squared norm of the lift `X.trivialLift`. Here `X` consists of chosen and twist places, row
lengths, and a character `μ = X.u1Char` of `U(1)(𝔸)` of weight `-(X.rowLength τ + k)` at each
infinite place `τ`, whose tame part is trivial off these places; `X.trivialLift` is the theta lift
to the definite `U(n)` of the constant `1` on `U(1)` for these data, times the index of
`X.chosenLevel`.

Let the rank be `2 * k` with `1 < k`. Let `C` be the product of the volumes of `[U(n)]` and
`[U(1)]`, divided by `ζ_F(2 k)`, the Euler product at `k` of the signs `placeSign` (`F` is the
maximal real subfield of `E`). Then `C ≠ 0`, and the squared norm is a product of six factors: `C`,
the product of the numbers `q - 1` of the places `X.chosenPlace`, the hook number of the weight
`X.descentPair.columnCount`, its dimension, the value `L(k)` and `N(Q) ^ (card n - 1)`. Here
`L = X.u1Char⁻¹.L X.places` is the `L`-function of the character `x ↦ μ(x / x̄)⁻¹` of `E`, without
the factors at the places of `X` and their conjugates, and `N(Q)` is the product of the norms of the
places `X.twistPlace`. 
