---
{
  "module": "src/Lib/SiegelWeil/Tower/LineGaussSums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/LineGaussSums.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/LineGaussSums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Standard partners, shear invariance, Gauss sums along lines and coefficients of lifts

Let `s` be an integral `b × n` matrix over a semilocal field (`New.SemilocalField`) with compact
open subring `O`, and let `χ` be a character; where `χ` is tame (`TameLocalChar`), `invOnUnits χ` is
locally constant and `χ` has absolute value one on units of `O`. The file constructs the standard
pair of partners attached to `s`. Finally it describes the Fourier coefficients `H.centreCoeff T`
along a splitting `H` of a hermitian space `X` of an equivariant lift `𝒟`
(`New.Exchange.IsEquivariantLift`) on a space `M` of local data.

## Main definitions and results

* `New.stdColDatum`: `y ↦ χ⁻¹ (det (s y))` for integral `y` with `det (s y)` a unit of `O`, else
  zero.
* `New.stdRowDatum`: `x ↦ χ⁻¹ (det (s; x))` if `s` stacked on `x` lies in `GL_n(O)`, else zero.
* `New.areMatched_stdRowDatum_stdColDatum`: these two are partners (`New.AreMatched`): they are
  carried by the blocks of rows of `k⁻¹` and of columns of `k`, for `k ∈ GL_n(O)`, and their values
  there differ by the factor `χ (det k)`.
* `New.Exchange.map_shear_stdColDatum_eq`: if a linear form is invariant, on a space `M` of
  Schwartz–Bruhat functions, under the shears `y ↦ y + u z s y`, then it takes the same value on the
  standard datum `New.stdColDatum χ s` and on its composite with `y ↦ y + u r y`, when both lie in
  `M`, `s` is integral, `s u = 0` and `r u = 0`.
* `New.Exchange.exists_lineTerm_localDatum`: the operator `New.Exchange.lineTerm`, the term along a
  line split off each of two hermitian spaces, sends a standard datum for the large pair of spaces
  to a scalar times a standard datum for the small pair. The scalar at the adele `x` depends on
  `a = x κ⁻¹`, where κ is a fixed idele. It is zero unless `a` is integral outside `S ∪ S̄` and both
  `a` and `ϖ ā` are units of `O` at the set `S` of places where `χ` is read. Then it is
  `l β * γ * χ⁻¹(a) * χ(ϖ ā)`, where `l β` is a nonzero constant for each of the two terms `β` and
  `|γ|²` is the inverse of the order of the residue ring.
* `New.Exchange.IsEquivariantLift.exists_linear_centreCoeff`: the coefficient at a point is a linear
  functional of the datum. A shear of the datum by `z` along the centre of the radical multiplies it
  by the additive character at `S` of `tr (T_S z)`, where `T_S` is the component at `S` of the
  product of `T` with the inverse of the idele `invDifferentIdele E`.

Notions from other files:
* `New.SemilocalField`: Conditions met by a finite product of non-archimedean local fields: a
  locally compact ring with Haar measure, compact open subring O of volume one, a topologically
  nilpotent invertible ϖ in O, and `New.IsValuationPair O`.
* `New.schwartzBruhat`: The space of locally constant, compactly supported complex functions that
  vanish outside a given set.
* `New.invOnUnits`: `χ⁻¹` on the units of `O`, zero elsewhere.
* `New.Space.Splitting.centreCoeff`: `H.centreCoeff T D g` is the mean of
  `ψ (tr (T M)) * D (H.radicalCentre M * g)` over adelic matrices `M` modulo rational ones;
  `H.radicalCentre M` has matrix `1 + H.kAdelic * (M - Mᴴ) * H.lCoord`.
* `New.Exchange.SplitTameChar`: A character ν of the idele classes of norm one with positive weight
  at every infinite place, whose tame part is non-trivial exactly on a non-empty finite set S of
  places disjoint from its conjugate.

## Relation to the literature

Known; see `Lib.SiegelWeil.Tower.LargeSideConstantTerm` and
`Lib.SiegelWeil.SingularForms.UnimodularCoefficients` for sources.


 ## The standard pair of partners attached to an integral matrix 

 ### The standard functions 

### `stdColDatum`

 For a matrix `s` with rows indexed by `b`, the function sending an integral `y` with `det (s y)`
a unit of `O` to `χ⁻¹ (det (s y))`, and every other `y` to zero. 

### `stdRowDatum`

 The function sending `x` to `χ⁻¹` of the determinant of the square matrix with rows those of
`s` and `x`, ordered by `e`, if that matrix lies in `GL_n(O)`, and to zero otherwise. 

### `isPrimitiveMatrix_iff_int_and_unit_det`

 A square matrix over `F` is primitive over the compact open subring `O = SemilocalField.O` of
`F` (integral, with an integral left inverse) if and only if it is integral and its determinant is a
unit of `O`. 

### `_root_.Membership.mem.transpose_mem_schwartzBruhat`

 If `Ψ` is locally constant with compact support in the matrices with a left inverse, then
`y ↦ Ψ yᵀ` is locally constant with compact support in the matrices with a right inverse. 

### `schwartzBruhat.mem_of_support_isPrimitiveMatrix`

 A locally constant function that vanishes off the primitive matrices has compact support and
vanishes off the matrices with a left inverse. 

 ### Supports, and the identity of partners 

### `invOnUnits_eq_mul_of_unit`

 If `t` is a unit of `O`, then `invOnUnits χ x = χ t * invOnUnits χ (x * t)`: the element `x` is
a unit of `O` if and only if `x * t` is one. 

### `isIntMatrix_of_stdColDatum_ne_zero`

 If the standard datum of an integral `s` does not vanish at `y`, then `y` is integral and
`s * y` is primitive: integral, with an integral inverse. 

### `isPrimitiveMatrix_of_stdColDatum_ne_zero`

 The standard datum of an integral `s` vanishes off the primitive matrices. 

### `areMatched_stdRowDatum_stdColDatum`

 For integral `s`, the row datum `stdRowDatum e χ s` and the column datum `stdColDatum χ s` are
partners for `χ` over `O`. The row datum sends `x` to `χ⁻¹ (det (s; x))` (rows ordered by `e`) if
`(s; x)` lies in `GL_n(O)`, and to `0` otherwise. The column datum sends an integral `y` with
`det (s y)` a unit to `χ⁻¹ (det (s y))`, and every other `y` to `0`. Being partners means: they
vanish off the last rows `a` of `k⁻¹`, resp. the first columns `b` of `k`, for `k ∈ GL_n(O)`, and
the first at `invLastRows e k` is `χ (det k)` times the second at `firstCols e k`. 

 ### The tame case: local constancy and compact support 

### `stdColDatum_mem_schwartzBruhat`

 For tame `χ` and integral `s`, the standard datum `y ↦ χ⁻¹ (det (s y))` is locally constant with
compact support in the matrices that have a left inverse: it is a locally constant function cut off
by the clopen set of integral matrices, and it vanishes off the primitive ones. 

### `stdRowDatum_mem`

 For tame χ, the datum `stdRowDatum e χ s`, that is `x ↦ χ⁻¹ (det (s; x))`, is locally constant
with compact support in the matrices that have a right inverse. 

 ## Shear invariance of linear forms on the standard datum 

### `New.Exchange.map_shear_stdColDatum_eq`

 Let `F` be a semilocal field with integer ring `O`, and `χ` a multiplicative character of `F`.
Let `s` be a `b × n` matrix over `O`, and `u` a column and `r` a row with `s u = 0` and `r u = 0`.
`stdColDatum χ s` sends an integral `y` with `det (s y)` a unit of `O` to `χ⁻¹ (det (s y))`, and
every other `y` to `0`. Suppose the linear form `Λ` is invariant under all shears `y ↦ y + u z s y`
on a space `M` of locally constant, compactly supported functions vanishing outside `U`. Then `Λ`
takes the same value on `stdColDatum χ s` and on its composite with `y ↦ y + u r y`, when both lie
in `M`. 

 ## Terms along a line as Gauss sums 

### `frameMatrix`

 The matrix with rows indexed by `n' ≃ b ⊕ r'` and columns by `Unit ⊕ (b ⊕ r) ⊕ Unit`, where
`n ≃ b ⊕ r`: on the rows `b` it is `(0, (1 0), 0)` and on the rows `r'` it is `(K, (0 I), L)`. 

### `isPrimitiveMatrix_frameMatrix`

 For an integral frame `Q` (blocks `K`, `I`, `L` of columns with dual blocks of rows, integral
and inverse to each other), the matrix `frameMatrix σ' σ Q.K Q.L Q.I` is primitive: integral, with
an integral left inverse, which is built from the dual blocks. 

### `stdColDatum_one_mul_mul`

 If `G` is primitive (integral with an integral left inverse) and `P`, `R` are integral matrices
inverse to each other, then the standard datum `χ⁻¹ (det ·)` at `G * T * R` is the constant
`χ⁻¹ (det (R * G))` times its value at `T`. 

### `triangularForm`

 The matrix under the determinant of the datum, in the frames of the two isotropic lines. It is
block upper triangular; its diagonal blocks are `c`, the matrix with rows `p` and `y`, and the last
coordinate `z (.inr 0)` of `z`, in this order (`LineIndex n r` indexes coordinates by `n` and one
more coordinate, then by `r`, then one last coordinate) if `β = true` and in the opposite order if
`β = false`. 

### `mul_stdColDatum_triangularForm`

 The standard datum at `triangularForm σ β c p y z`, times `ε`, is a product over the coordinates
of `z` times the standard datum `stdRowDatum σ χ p y`. Each coordinate contributes the indicator
function of `O`; the last one has the further factor `ε * χ⁻¹(c) * χ⁻¹(z i)` on units. 

### `ite_isIntegralUnit_eq_ite_invOnUnits_div`

 The quotient `invOnUnits χ x / invOnUnits χ y` is `χ⁻¹(x) χ(y)` if `x` and `y` are units of
`O`. Otherwise it is `0`, as its numerator or its denominator is `0`. The lemma states this under
a further condition `q`. 

### `stdRowDatum_frameAt_lineTermSplitting`

 In the frame of `lineTermSplitting A X β` (the matrix `frameAt` of its basis, with coordinates
indexed by `LineIndex n r` and by `r × n`), at the point with line coordinate `a` and other
coordinates `z` and `y`, the standard datum of `p * I'` equals `stdColDatum χ 1` (`χ⁻¹ det` if
integral with unit determinant, else `0`) at the product of `G` (built by `σ'`, `σ` from the frame
of `X`), the block triangular matrix `triangularForm` and the inverse frame `R` of `A`. 

### `exists_lineTerm_localDatum`

 Let `A` and `X` be adapted splittings of a hyperbolic plane off `W'` and `V'`, leaving `W` and
`V`. `lineTerm A X β x` maps data on `Hom(W', V')` to data on `Hom(W, V)`, and `β` picks one of two
models. A datum `localDatum W' V' v Φ rd` has real part `v` (in the Fock space `PairFock`). At a set
`S` of places it is `Φ`, read through `π` into the semilocal field `F` (subring `O`, element `ϖ`),
and elsewhere it is the vacuum. `stdRowDatum σ χ p y` is `χ⁻¹ det` of the rows of `p` and `y`
ordered by `σ` if that matrix is in `GL(O)`, else `0`. There are nonzero constants `l β` such that
for every tame `χ` there is a number `γ` with (a) `|γ|²` the inverse of the order of the residue
ring and (b) the following. The term at `x = scaleIdele E * a` (a fixed idele times `a`) maps the
datum with real part `v` and, at `S`, `stdRowDatum σ' χ (p * I')` (`I'` reads the coordinates of `W`
in the frame of `A`) to a scalar times the datum with real part `lineTermReal A X β a.1 v` and, at
`S`, `stdRowDatum σ χ p`. Here `a.1` and `a.2` are the infinite and finite parts of `a`. The scalar
is `l β * γ * χ⁻¹(a) * χ(ϖ ā)`, read at `S`, if `a.2` is integral at every finite place outside `S`
and its conjugate and both `a` and `ϖ ā` are units of `O` at `S`; otherwise it is `0`. 


## Fourier coefficients of an equivariant lift as functionals of the datum

Here `S = 𝔠.ramifiedPlaces`, and `componentsAt 𝔠` takes the components of an adele at `S`.

* `New.Exchange.IsEquivariantLift.apply_shear`: translation by an element supported on `S ∪ S̄` that
  is a shear at `S` corresponds to a shear of the datum.


### `components_of_mat_eq_one_add`

 An element of the adelic unitary group with matrix `1 + (e C - ē C')`, where `e` is the
idempotent of `S`, is trivial at infinity, is supported on `S ∪ S̄` and has component `1 + C`
at `S`. 

### `apply_shear`

 Let `𝒟` be an equivariant lift on `M` and let `ν` in the unitary group have matrix
`1 + e c k - ē B` (`e` the idempotent of `S`), so that it is `1 + c k` at `S`, with `k c = 0`.
Shearing a datum in `M` by the components at `S` (`componentsAt`) of `x⁻¹ ν x` keeps it in `M`, and
the lift of the sheared datum at `y x` is the lift of the datum at `y ν⁻¹ x`. 

### `centreCoeff_shear`

 Let `𝒟` be an equivariant lift on `M` and let `ν` in the unitary group have matrix
`1 + e c k - ē B` (`e` the idempotent of `S`), so that it is `1 + c k` at `S`, with `k c = 0`.
Shearing a datum in `M` by the components at `S` (`componentsAt`) of `x⁻¹ ν x` keeps it in `M` and
moves the point at which the Fourier coefficient `H.centreCoeff T` of its lift is taken from
`ν⁻¹ x` to `x`. 

### `exists_linear_centreCoeff`

 Let `𝒟` be an equivariant lift on `M` (functions of `m × b` matrices over the completions at the
ramified places `S` of `𝔠`) to functions on the unitary group of `X`, and let `H` split `X` over
`X₀`. Fix `T` a `p × p` matrix over `E`. (a) At each point `x`, the `T`-th Fourier coefficient
`Ψ ↦ H.centreCoeff T (𝒟 Ψ) x` along the centre of the radical of `H` is, on `M`, the restriction of
a linear functional `L`. Here `H.kAdelic` is the adelic frame of the isotropic subspace of `H` and
`H.lCoord` its conjugate transpose times the form, a matrix of coordinates. (b) The shear of `Ψ` by
`z` along this frame at `x` stays in `M` and multiplies `L Ψ` by `ψ_S (tr (T_S z))`, with `ψ_S` the
additive character at `S` and `T_S` the matrix of components at `S` of `δ⁻¹ T`, where `δ` is the
idele `invDifferentIdele E`. 

### `comp_mul_mem_ker`

 If `𝒟` is an equivariant lift on `M` (automorphic values, equivariant for translations at `S`),
the data in `M` that `𝒟` kills are stable under translation by invertible matrices over the
completions at `S`. 
