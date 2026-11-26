---
{
  "module": "src/New/UpperBound/Objects/AuxiliaryPair.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/AuxiliaryPair.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/AuxiliaryPair.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Descent pairs: descent data for theta lifts to definite unitary groups

This file sets up the theta lift from U(W), with W of rank r, to the definite group U(V), with
V = `New.stdSpace` of rank n > r, and the descent from V to W. One structure, `New.DescentPair`,
holds the data: the places of the level, the space W, an embedding of the indices of its basis into
those of V, a numbering of its basis vectors, the numbers of columns k⁺ and k⁻, and a character of
U(1)(𝔸) with its weight and tame part. The level sits at two finite families of split places
(`New.LevelPlaces`): M, the chosen places `chosenPlace`, and Q, the places `twistPlace` of the
twist. The residue field at w is k_w = `New.ResField w`. The finite datum Ψ_bl ⊗ vac is a vector of
the Weil representation `New.pairWeil` on `Hom(W, V)`: the block datum Ψ_bl, a function of the
reductions of a matrix at M and Q, with the vacuum at the other finite places.

For a descent pair `O`, the character of the descent datum is `O.u1Char`, with weight `O.weight` and
tame part `O.tamePart`. The highest weight of the forms on V is `(O.columnCount, O.detExp)`, given
by numbers of columns. Vectors of the representation of this weight are written ξ, and forms on V
are written Ξ.

## Main definitions and results

* `New.DescentPair`: the data of a descent pair; `New.DescentPair.FormV`: its forms on V, with the
  action `New.DescentPair.formAction` of ∏_M GL_r and the Hecke polynomial
  `New.DescentPair.heckePolyOnForms`.
* `New.DescentPair.fockPoly`, `New.DescentPair.blockDatum`, `New.DescentPair.conjKernel`,
  `New.DescentPair.normalizedDescent`: the Fock polynomial of a vector, the finite datum Ψ_bl ⊗ vac,
  the conjugate theta kernel as a linear form on weight vectors, and the normalized descent from
  forms on V to functions on U(W)(𝔸).
* `New.DescentPair.blockDatum_eq_sum_modDatum`: Ψ_bl ⊗ vac is the sum of the translates of Ψ¹ ⊗ vac,
  with Ψ¹ = `New.DescentPair.identityBlockIndicator`, by lifts (`New.LevelPlaces.twistResidueLift`)
  of the inverses of the elements of `∏ GL(k_w)` over `Q` (`New.LevelPlaces.TwistGL`).
* `New.DescentPair.paramV`, `New.DescentPair.isHCParam_paramV`: the doubled parameter `l'` of the
  weight of forms on `V`.
* `New.DescentPair.FitsParams`: the data of a descent pair `O` are those of a parameter `l` on `W`
  and `l'` on `V`.
* `New.DescentPair.FitsParams.exists_isJointHarmonic`, `New.DescentPair.FitsParams.isEdge`: then the
  polynomial of the highest vector is a product of joint harmonics (staircases of minors), so it is
  an edge from `l` to `l'`.
* `New.DescentPair.normalizedDescent_eq_smul_star_lift_swap`: the normalized descent
  `New.DescentPair.normalizedDescent`, defined by a class sum, is a multiple of the descent by the
  datum of the highest vector, the conjugate of the transposed lift (`New.Space.lift` from `V` to
  `W`) of the conjugate form.

Notions from other files:
* `New.levelOf w H`: the subgroup of K₀ = `New.stdLevel` of the elements whose reductions at the
  places `w i` form an element of H.
* `New.levelSpace π K χ`: the vectors on which each k in K acts through π by the scalar χ(k).
* `New.HasHeckePolynomial π hw p y`: y is spherical at the split place w, and the Hecke polynomial
  at T acts on it by p(T).
* `New.IsJointHarmonic`: a nonzero polynomial that is highest, of the lowest K-types, for the row
  and the column actions and harmonic in both directions.

## Relation to the literature

See `Lib.Adelic.Unitary.CongruenceLevels` for sources.



## Descent pairs, their level and their lifts

Block 0 is the image of the embedding r ↪ n, block 1 the rest (`New.rangeParabolic`).

* `New.DescentPair.HasLiftHeckePolynomial`: a form on V has the Hecke polynomials of a lift of a
  given eigensystem.


### `LevelPlaces.ChosenGL`

 The finite group given by the product over the M-places w of GL_r of the residue field at w. 

 ### Levels at the places of M and Q 

### `firstBlockHom`

 The homomorphism sending (g_w) in ∏_M GL_r(k_w) to the family equal to diag(g_w, 1) at the
places of M and 1 at those of Q. 

### `firstBlockHom_apply_inl`

 At a place w of M the component of `firstBlockHom S u g` is diag(g_w, 1). 

### `firstBlockHom_apply_inr`

 At a place of Q the component of `firstBlockHom S u g` is 1. 

### `descentResidueLevel`

 The group of families in GL_n(k_w) that at the places of M fix the basis vectors indexed by u,
and at the places of Q preserve the span of the other basis vectors. 

### `mem_descentResidueLevel_iff`

 A family `g` lies in `New.descentResidueLevel S u` if and only if two conditions hold. First, at
each chosen place (`S.ChosenIndex`) it fixes the n × r inclusion matrix of `u`, whose columns are
the basis vectors indexed by `u`. Second, at each place of the twist (`S.TwistIndex`) it lies in the
opposite parabolic `New.rangeParabolic u`. 

### `firstBlockHom_conj_apply_inr`

 Conjugation by `firstBlockHom S u s` does not change the components of `x` at the places of the
twist, indexed by `S.TwistIndex`. 

### `firstBlockHom_conj_mem_descentResidueLevel`

 Conjugation by an element of the image of `New.firstBlockHom`, that is, by diag(s_w, 1) at the
places w of M (indexed by `S.ChosenIndex`) and 1 at those of Q (indexed by `S.TwistIndex`), maps
the level `New.descentResidueLevel` into itself. 

 ### Descent pairs and their forms on V 

### `DescentPair`

 A descent pair: places M and Q, a space W of rank r with an index `numbering` on its basis
vectors, an embedding of indices into n > r, column multiplicities k⁺ and k⁻, and a character
μ = `u1Char` whose tame part is trivial off M and Q. 

### `DescentPair.signs`

 The signs of the basis vectors of `W` at the infinite places. 

### `DescentPair.W`

 The hermitian space `W` of rank `r` with the given signs, as a `New.Space`. 

### `DescentPair.incl`

 The embedding of the index set of the basis of `W` in that of `V = I_n`. 

### `DescentPair.numbering`

 An index for each basis vector of `W`; under `New.DescentPair.FitsParams` it numbers the
  vectors within each sign. 

### `DescentPair.colsPlus`

 k⁺: the number of columns of height `i` of the partition at `τ` for the sign `1`, as a
  function of `τ` and `i`. 

### `DescentPair.colsMinus`

 k⁻: the number of columns of height `i` of the partition at `τ` for the sign `-1`, as a
  function of `τ` and `i`. 

### `DescentPair.u1Char`

 The character μ of `U(1)(𝔸)`, trivial on rational points. 

### `DescentPair.weight`

 The weight of `u1Char`, an integer for each infinite place. 

### `DescentPair.tamePart`

 The tame part of `u1Char`, a character ψ_w of the residue field for each finite place w. 

### `DescentPair.hasWeight`

 The character `u1Char` has weight `weight` and tame part `tamePart`. 

### `DescentPair.tame_eq_one`

 The tame part is trivial at every place other than the chosen places of `M` and `Q`. 

### `DescentPair.rank_lt`

 `W` has smaller rank than `V`: `r < n`. 

### `levelGroup`

 The level of the descent pair: the elements of K₀ whose reductions modulo the places of M fix
the basis vectors indexed by `incl`, and whose reductions modulo the places of Q preserve the span
of the other basis vectors. 

### `residueBlockDatum`

 The block datum Ψ_bl as a function of families X of residue matrices: it is the product over
w ∈ Q of ψ_w(det of the rows of X_w indexed by `incl`) if X_w is the inclusion matrix of `incl` at
every w in M, else 0. 

### `columnCount`

 The column numbers (τ, i) ↦ k⁺(τ, i) + k⁻(τ, n − i) of the highest weight of the forms on
V = I_n, with n the rank of V. 

### `detExp`

 For an infinite place τ, the integer −∑_{1 ≤ i < n} k⁻(τ, i), the power of the determinant in
the highest weight of the forms on V. 

### `residueLevelChar`

 The character of `New.descentResidueLevel` sending g to ∏_{w ∈ Q} ψ_w⁻¹(det g_{w,00}). Here
g_{w,00} is the diagonal block of the component of g at w on the basis vectors indexed by `incl`
(block 0 of `New.rangeParabolic`). It is multiplicative because these components are block
triangular. 

### `residueLevelChar_apply`

 `O.residueLevelChar g` is the product over the places w = `O.placeAt (inr i)` of Q of
`O.tamePart⁻¹` at w, applied to the determinant of the block of the component of g at w on the basis
vectors indexed by `O.incl`. 

### `residueLevelChar_firstBlockHom_conj`

 The character `New.DescentPair.residueLevelChar` is invariant under conjugation by the image of
`New.firstBlockHom`, as it only reads the components at the places of Q. 

### `levelChar`

 The character of `New.DescentPair.levelGroup` obtained by reduction modulo the places of M and Q
followed by `New.DescentPair.residueLevelChar`. 

### `FormV`

 Algebraic forms on V = I_n of weight (`O.columnCount`, `O.detExp`) whose level fixes the basis
vectors indexed by `incl` modulo the places of M and the span of the other basis vectors modulo the
places of Q, with character ∏_Q ψ_w⁻¹(det g₀₀), g₀₀ the diagonal block on `incl`. 

### `chosenGLRep`

 The representation of ∏_{w∈M} GL_r(k_w) on the vectors of π on which
`New.DescentPair.levelGroup` acts by `New.DescentPair.levelChar`. An element g acts by ∏_w ψ_w(det
g_w) times π of a lift of the family equal to diag(g_w, 1) at M and to 1 at Q. 

### `formAction`

 The representation `New.DescentPair.chosenGLRep` on right translation of algebraic forms
(`New.algFormRep`): the action of ∏_M GL_r(k_w) on the forms on V. 

 ### The theta kernel and the normalized descent 

### `tensorPoly`

 The linear map from V_{k⁺} ⊗ V_{k⁻}, seen as functions on pairs of indices of Weyl module bases
(`New.WeylIndex`: families of standard fillings over the places), to polynomials, sending a ⊗ b to
the product of the polynomials (`New.letterPoly`) of a in the Fock variables of the basis vectors of
W of sign 1 and of b in those of sign −1. The letter h of a filling stands for the sum of the
variables of the basis vectors of that sign with `O.numbering` equal to h. 

### `tensorPoly_vecMulVec`

 The value of `New.DescentPair.tensorPoly` at a pure tensor a ⊗ b, the vector with entry a_i b_j
at (i, j) (that is, `(vecMulVec b a).vec`), is the product of the polynomials (`New.letterPoly`) of
a and b in the variables of the positive, resp. negative, sign. 

### `fockPoly`

 The Fock polynomial of a vector: the linear map ξ ↦ P_ξ that applies the integer matrix of
`New.mixedCartan`, a chosen embedding of the module of weight
`mixedWeight n O.colsPlus O.colsMinus` into the tensor product of those of weights k⁺ and k⁻, and
reads the resulting tensor as a polynomial in the Fock variables by `New.DescentPair.tensorPoly`. 

### `charW`

 The character ν_W of U(1)(𝔸) attached to W: `upsilonU1` raised to the number r₋ of basis
vectors of W with sign −1. It belongs to the standard splitting character υ^{2r₋ − r} of W, with υ
the character of the Weil data. 

### `charV`

 The character ν_V = μ·υ^{⌊n/2⌋} of U(1)(𝔸) attached to V, for μ the character of the descent
pair, υ that of the Weil data and n the rank of V. For even n it belongs to the splitting character
of V that is the base change of μ (`New.Exchange.spaceChar_rankTwist`). 

### `pairThetaKernel`

 The theta kernel of the pair (W, I_n) of the descent pair, with the characters
`New.DescentPair.charW` and `New.DescentPair.charV`. 

### `blockDatum`

 The finite datum Ψ_bl ⊗ vac on Hom(W, I_n): the block datum `New.DescentPair.residueBlockDatum`
at the places of M and Q and the vacuum at the other finite places. It is the `New.vacuumDatum`, an
element of the finite part of the space of data, of the function of matrices modulo M²Q that applies
the block datum to their reductions at these places; reading it modulo MQ gives the same vector. 

### `fockDatum`

 The datum v_{P_ξ} ⊗ Ψ_bl ⊗ vac in 𝒮(Hom(W, V)): the Fock vector of the polynomial
P_ξ = `New.DescentPair.fockPoly` ξ tensored with the finite datum `New.DescentPair.blockDatum`. 

### `conjKernel`

 The linear form ξ ↦ conj θ(ω_{ν_W,ν_V}(g, h)(v_{P_ξ̄} ⊗ Ψ_bl ⊗ vac)) for g in U(W)(𝔸) and finite
h in U(V). Here ν_W = `O.charW`, ν_V = `O.charV`, and v_{P_ξ} is the Fock vector of the polynomial
P_ξ. 

### `normalizedDescent`

 The normalized descent, a linear map from forms Ξ on V to functions on U(W)(𝔸): θΞ(g) is the
class sum over h, for `New.DescentPair.levelGroup`, of `New.DescentPair.conjKernel` at g and h
applied to Ξ(h). 

 ### Hecke polynomials 

### `heckePolyOnForms`

 For split w with w, w̄ off M and Q, the operator H_w(X) = ∑_{i≤n} (−X)^i q^{i(i−1)/2} T_{w,i} on
the forms on V, with q the norm of w. 

### `heckePolyOnForms_eq_smul`

 Let w be split with w, w̄ off M and Q. If a form y on V, viewed as a function on the finite
points, is spherical at w and the Hecke polynomial at each T acts on it by p(T)
(`New.HasHeckePolynomial`), then `New.DescentPair.heckePolyOnForms` at X sends y to p(X) • y. 

### `rankDiff`

 The difference of ranks t = n − r = dim V − dim W of the descent pair. 

### `liftHeckeRoot`

 The complex number q^{1−n+r/2} υ(ϖ_w)^{r−2r₋}, with υ the character of the Weil data, q the
norm of w, ϖ_w the chosen uniformiser and r₋ the number of minus signs of W. 

### `HasLiftHeckePolynomial`

 At each split w with w, w̄ off M and Q, y is spherical with Hecke polynomial
∏_{l<n−r} (1 − q^l νT) · H_{z(w)}(q^{n−r} νT/ν'). Here q is the norm of w, H_{z(w)} is the rank r
polynomial `New.heckePolyEval` with eigenvalues z(w), and ν, ν' are the `New.AutChar.frobValue` of
the characters `O.charW`, `O.charV` in ranks r, n. 


## The block datum as a sum of translates, and the action of the level on it

In this section `n` indexes the basis of `W` and `n'` that of `V`.

* `New.DescentPair.identityBlockIndicator`: the function Ψ¹, which is Ψ_bl with the character of the
  determinant at each place of `Q` replaced by the indicator of the identity block.


### `LevelPlaces.TwistGL`

 The product of the groups GL_n(k_w) over the places w of Q, where k_w is the residue field at
w. 

### `instance : Fintype (S.TwistGL n)`

 The group ∏_{w ∈ Q} GL_n(k_w) is finite. 

### `LevelPlaces.twistResidue`

 For A in the product of GL_n(k_w) over Q, the family of residue matrices that is 1 at the places
of M and the inverse of the component of A at each place of Q. 

### `LevelPlaces.twistResidue_inl`

 The family `twistResidue A` is 1 at the places of M. 

### `LevelPlaces.twistResidue_inr`

 For an index `i : S.TwistIndex` of a place of the twist, the family `S.twistResidue A` at
`.inr i` is `(A i)⁻¹`, the inverse of the component of `A` at that place. 

### `LevelPlaces.twistResidueLift`

 For A in the product of GL_n(k_w) over Q, a chosen element of K₀ reducing to A⁻¹ at the
places in Q and to 1 at those in M. 

### `LevelPlaces.reduceFamily_twistResidueLift`

 The lift `twistResidueLift A` reduces to the family `twistResidue A`. 

### `LevelPlaces.reduceAt_twistResidueLift_inl`

 The lift `twistResidueLift A` reduces to 1 at each chosen place `S.placeAt (.inl i)`. 

### `LevelPlaces.reduceAt_twistResidueLift_inr`

 The lift `twistResidueLift A` reduces to `(A i)⁻¹` at each place of the twist
`S.placeAt (.inr i)`. 

### `DescentPair.identityBlockIndicator`

 The indicator Ψ¹ of the matrices `y` modulo `M Q` that reduce to the inclusion matrix of the
embedding of indices of the pair at the places of `M` and whose rows indexed by that embedding
reduce to the identity at the places of `Q`. 

### `DescentPair.charV_detFin_eq_prod`

 For `k` in `stdLevel E n` (integral finite points of U(W)), `O.charV` of `detFin O.signs k` is
the product over the places `O.placeAt i` of M and Q of `O.tamePart` at that place, applied to the
determinant of `stdLevel.reduceAt` of `k` there (k mod w). 

### `DescentPair.residueBlockDatum_eq_sum`

 Here M and Q are the families of places indexed by `O.ChosenIndex` and `O.TwistIndex`, ψ_w is
`O.tamePart w`, and Ψ_bl = `New.DescentPair.residueBlockDatum`. The value of Ψ_bl at a family `X` of
residue matrices is a sum over the families `A` of invertible matrices at `Q`. The term of `A` is
`∏ ψ_w (det A_w)` if `X` is the inclusion matrix at `M` and `A` consists of the rows of `X` indexed
by `O.incl`, and `0` if not. 

### `DescentPair.blockDatum_eq_sum_modDatum`

 The finite datum Ψ_bl ⊗ vac of a descent pair (W, V) is the sum, over A in ∏_{w ∈ Q} GL_n(k_w)
(Q indexed by `O.TwistIndex`, n the rank of W), of the datum Ψ¹ ⊗ vac, moved by the element
`New.LevelPlaces.twistResidueLift` A of U(W), a lift of A⁻¹. Here Ψ¹ =
`New.DescentPair.identityBlockIndicator` is the indicator of the matrices modulo MQ that reduce to
the inclusion matrix of `O.incl` at M and whose rows indexed by `O.incl` reduce to 1 at Q, and vac
is the vacuum at the other finite places. 

### `DescentPair.residueBlockDatum_inv_mul_mul`

 Here M and Q are the families of places indexed by `O.ChosenIndex` and `O.TwistIndex`, and ψ_w
is `O.tamePart w`. Let `k`, `k'` be families of invertible residue matrices of ranks `n`, `n'` and
`j` an element of `New.descentResidueLevel`, such that `k' = diag(k, 1) j` at `M` and `k' = j` at
`Q`. Replacing `X` by `k'⁻¹ X k` multiplies `New.DescentPair.residueBlockDatum` by
`New.DescentPair.residueLevelChar j`, the product over `Q` of ψ_w⁻¹ of the corner determinant of
`j`, times `∏ ψ_w (det k_w)` over `Q`. 

### `DescentPair.omega_blockDatum_eq_smul`

 Here M and Q are the places `O.chosenPlace` and those indexed by `O.TwistIndex`, and ψ_w is
`O.tamePart w`. Let `k`, `k'` lie in `stdLevel`. Suppose the reduction `reduceFamily O.placeAt k'`
is `firstBlockHom` of `reduceFamily O.chosenPlace k` times `j.val`. The element `j` lies in
`New.descentResidueLevel`, so it fixes the basis vectors indexed by `O.incl` at `M` and preserves
the span of the others at `Q`. Then the Weil action `O.pairThetaKernel.ω (k, k')` multiplies
Ψ_bl ⊗ vac = `O.blockDatum` by (∏ over `M` of ψ_w (det (k mod w)))⁻¹ times
`New.DescentPair.residueLevelChar j`. 


## The real datum and the normalized descent

This section starts from the real data of a descent pair `O : New.DescentPair` (a space `W` of rank
`r` with signs `O.signs`, and `V = I_n` definite of larger rank), whose Fock polynomials are
`New.DescentPair.fockPoly`.

Throughout, r₋ = `card {c // O.signs c = -1}` is the number of minus signs of `W`, k⁺ and k⁻ are
`O.colsPlus` and `O.colsMinus`, and P_ξ is `O.fockPoly ξ`.


### `paramV`

 The doubled parameter on `V`: at the place `w`, the entry at `i` is the entry of
`New.hcParameter` of the weight `(O.columnCount, O.detExp)` in rank `card n` at the position of `i`
in the numbering of `n`. 

### `isHCParam_paramV`

 `O.paramV` is twice the Harish-Chandra parameter of the weight `(O.columnCount, O.detExp)` of
forms on `V`, in the sense of `New.IsHCParam`. 

### `FitsParams`

 The doubled parameter l on W fits the descent pair O: it corresponds to l' = `O.paramV` on V
(`New.ParamsCorrespond`: at each infinite place the two satisfy the block rule `New.IsBlockRule` for
the weights), the numbering `O.numbering` lists the basis vectors of sign ±1 by decreasing ±l, and
k^± have no column higher than the number r_± of signs ±1. 

### `FitsParams.paramsCorrespond`

 The parameters `l` on `W` and `O.paramV` on `V` correspond, for the weights r₋ (the number of
  minus signs of `W`) and ⌊n/2⌋ plus `O.weight`, the weight of `O.u1Char`. 

### `FitsParams.numbering_eq`

 At every place the basis vectors `c` of each sign are numbered from `0` by decreasing
  `O.signs c * l w c`. 

### `FitsParams.colsPlus_eq_zero`

 `O.colsPlus τ i` vanishes when `i` exceeds the number r₊ of plus signs of `W`. 

### `FitsParams.colsMinus_eq_zero`

 `O.colsMinus τ i` vanishes when `i` exceeds the number r₋ of minus signs of `W`. 

 ### The action of the real points of `U(V)` 

### `_root_.New.fockRowSubst`

 The substitution of Fock variables by which y in the compact group U(n)(ℝ) acts on the rows: the
variable (τ, i, a) goes to ∑_j (y_τ)_{j i} X(τ, j, a) if the column a has sign s(a) = 1, and to
∑_j (y_τ⁻¹)_{i j} X(τ, j, a) otherwise. 

### `_root_.New.realPairWeil_one_polyVector`

 Let the pair be U(diag s) and the compact group U(n)(ℝ), so that the Fock variables have the
signs s (`New.realSigns` of `New.homSigns s 1`). In its real Weil representation `New.realPairWeil`
with first weight the number of negative signs of s and any second weight γ', (1, y) acts on the
Fock vector of a polynomial P by the substitution `New.fockRowSubst s y`. 

### `_root_.New.fockRowSubst_fockLetters`

 Let F be a polynomial in an array of variables with rows (τ, i) and columns h ∈ ℕ. Then
`New.fockLetters s ord c F` replaces the variable (τ, i, h) by the sum of the X(τ, i, a) with
s a = c and ord a = h. On it the substitution `New.fockRowSubst s y` is the substitution
(`New.rowSubst`) of yᵀ in the variables of F if c = 1, and of y⁻¹ otherwise. 

### `_root_.New.realPairWeil_fockLetters`

 If the first weight is the number of negative signs of s, then (1, y), y in the compact group
U(n)(ℝ), acts on the Fock vector of `New.fockLetters s ord c F` by substituting yᵀ in the variables
of F if c = 1, and y⁻¹ otherwise. 

### `fockRowSubst_tensorPoly`

 Let O be a descent pair with signs `O.signs` and column numbers k⁺ = `O.colsPlus` and
k⁻ = `O.colsMinus`. Let y lie in `GInf E 1`, the compact group U(n)(ℝ). Let v be a tensor in
V_{k⁺} ⊗ V_{k⁻}, given by its coordinates at pairs of indices of the Weyl module bases
(`New.WeylIndex`). The substitution `New.fockRowSubst O.signs y` sends the Fock polynomial
`O.tensorPoly v` of v to the polynomial of (S_{k⁺}(y) ⊗ S_{k⁻}(y⁻ᵀ)) v. Here S_k is the Schur matrix
`New.schur k`, the action on the Weyl module V_k. 

### `realPairWeil_fockPoly`

 In the real Weil representation `realPairWeil` of the descent pair `O`, with weight
`negCount O.signs` at every place and any weight `γ'`, a real point `y` of U(V) sends the Fock
vector of the polynomial `O.fockPoly (star ξ)` to that of `O.fockPoly (star (ρ(y)ξ))`. Here
ρ = `New.conjWeylRep` is the action through the conjugate matrices, by which algebraic forms
transform, so that conj(ρ(y)ξ) is the image of conj(ξ) under y. 

 ### Joint harmonics and the edge 

### `productOfMinors`

 The product of minors at the infinite place w. Order the rows by decreasing η·l', with
l' = `O.paramV w`, and the columns of sign η by `O.numbering`. It is the product over η = ±1 and
p < n of the minor (the determinant of `New.staircaseBlock`) on the first p rows and columns for η,
raised to the power k⁺(w, p) = `O.colsPlus w p` for η = 1 and k⁻(w, p) = `O.colsMinus w p` for
η = −1. 

### `decreasingPosition_paramV`

 For each place `w` and index `a`, the position `decreasingPosition` of `a` in `O.paramV w` (the
number of entries larger than the one at `a`) is `Fintype.equivFin n a`. Its position in
`-O.paramV w` is the reversed index `(Fintype.equivFin n a).rev`. 

### `fockPoly_highestVector`

 The Fock polynomial `O.fockPoly` of `highestVector O.columnCount O.paramV` (the highest vector
of weight `O.columnCount` for the parameter `O.paramV`) is the product over the infinite places w of
the products of minors `O.productOfMinors w`, each in the variables of w. 

### `FitsParams.isJointHighest_productOfMinors`

 If l fits O, consider the standard Fock dual pair on the variables n × r with signs 1 on the
rows and `O.signs` on the columns and weights r₋ (the number of minus signs) and
−(⌊n/2⌋ + `O.weight w`). For it the product of minors `O.productOfMinors w` is nonzero, harmonic on
both sides, and highest (`IsJointHighest`) for the rows, ordered by `O.paramV w`, of weight the
lowest K-type of this parameter, and for the columns, ordered by −l_w, of weight
`New.staircaseWeight`. 

### `FitsParams.lowestKType_eq_staircaseWeight`

 If l fits O, the lowest K-type of −l_w on W is `New.staircaseWeight`, the column weight of the
staircase, that is, of the product over both signs and all p < n of the leading p × p minors to the
powers k⁺(p) = `O.colsPlus w p` (sign 1) and k⁻(p) = `O.colsMinus w p` (sign −1), for the weight
−(⌊n/2⌋ + `O.weight w`). 

### `FitsParams.isJointHarmonic_productOfMinors`

 If l fits O, the product of minors at w is a joint harmonic for (V, W), with weights r₋ (the
number of minus signs of W) and −(⌊n/2⌋ + `O.weight w`) and parameters `O.paramV w` and −l_w. 

### `FitsParams.exists_isJointHarmonic`

 Let the parameter l fit O, let l' = `O.paramV`, let r₋ be the number of minus signs of W and
γ_w = ⌊n/2⌋ + `O.weight w`. There are polynomials Φ_w, one for each infinite place w, such that
Φ_w is a joint harmonic for (V, W) with weights r₋, −γ_w and parameters l'_w, −l_w, and the
polynomial `O.fockPoly` of the highest vector of l' is the product of the Φ_w, each in the variables
of w. Moreover, the lowest K-type of −l_w is `New.staircaseWeight`, the column weight of a product
of leading p × p minors of the two signs to the powers k⁺ = `O.colsPlus w` and k⁻ = `O.colsMinus w`.


### `FitsParams.isEdge`

 Suppose W has positive rank (`Nonempty r`) and l fits the descent pair O (`O.FitsParams l`). Let
v⁺ = `New.highestVector` for l' = `O.paramV`, and let P_{v⁺} be its polynomial `O.fockPoly`. Then
the Fock vector of P_{v⁺} is an edge from `New.typeKernel l O.signs` to `New.typeKernel O.paramV 1`.
Here `New.typeKernel` is the product over the infinite places of the discrete series kernels, and an
edge (`New.IsEdge`) is a half edge in both directions between two such kernels. 

 ### The descent as the conjugate of a lift 

### `omega_fockDatum_star`

 For a descent pair (W, V), x real in U(V) and k in the level of V, the Weil operator of (1, (x,
k)) of the theta kernel sends `O.fockDatum` at conj ξ to `O.levelChar k` times `O.fockDatum` at
conj(ρ(x)ξ), where ρ = `New.conjWeylRep`. 

### `conjKernel_equivariant`

 For rational γ in U(I_n) and k in the level, the kernel `New.DescentPair.conjKernel` with vector
c(k)ρ(γ)v at (g, γxk) equals that with vector v at (g, x). Here ρ = `New.Space.weightRep` and
c = `New.DescentPair.levelChar`. 

### `normalizedDescent_eq_smul_star_lift_swap`

 The normalized descent θΞ = `O.normalizedDescent Ξ`, for a form `Ξ : O.FormV` on V, equals
d · [`stdLevel` : `O.levelGroup`] times the descent of Ξ♮ from V to W by the datum
`O.fockDatum v⁺` = v_{P_{v⁺}} ⊗ `O.blockDatum`. Here d, the dimension of the Weyl module of
`O.columnCount`, is the number of elements of `WeylIndex n O.columnCount`. v⁺ is the highest vector
for `O.paramV`. Ξ♮ = `ofAlgForm O.paramV 1 Ξ` is the function g ↦ ⟨v⁺, ρ(g_∞⁻¹) Ξ(g_f)⟩ on U(V)(𝔸),
the signs 1 saying that V is definite. 


## Residue rings and level indices for the modulus of level places

`X.levelModulus 1` is the product of the places of `X : New.LevelPlaces E`; we consider its quotient
ring.


### `ker_reductionGL_eq`

 Let `X` be a choice of level places: the chosen places and the places of the twist. An element
of `stdLevel E N`, the stabiliser of the standard lattice in the finite adelic unitary group,
reduces to `1` modulo `X.levelModulus 1`, the product of all places of `X`, exactly if it reduces
to `1` modulo each place of `X`. 

### `card_levelModulus_residueRing`

 The quotient ring of `X.levelModulus e`, the modulus `M ^ e Q`, has as order the `e`-th power of
the product of the norms of the places of `M`, times the product of the norms of the places of
`Q`. 

### `card_GL_levelModulus`

 Let `R` be the residue ring of `X.levelModulus 1`, the modulus M·Q, where M and Q are the
products of the chosen places and of the places of the twist of X. Then the order of `GL N R` is the
level index `stdLevelIndex (levelOf X.placeAt ⊥)`, with ⊥ the trivial subgroup. 
