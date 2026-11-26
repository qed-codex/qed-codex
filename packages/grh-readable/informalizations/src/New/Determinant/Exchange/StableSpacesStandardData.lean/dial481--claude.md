---
{
  "module": "src/New/Determinant/Exchange/StableSpacesStandardData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/StableSpacesStandardData.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/StableSpacesStandardData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Criteria for a function with a matched function to lie in a stable space; vanishing of lifts

Let χ be tame (`New.TameLocalChar`), and let P be a GL_n(F)-stable space of Schwartz–Bruhat
functions on n × b matrices. Let Ψ be a locally constant function that has a matched function
(`New.AreMatched`). The file gives two criteria for Ψ ∈ P in terms of the standard data
`New.stdColDatum χ s`, the function y ↦ χ⁻¹(det s y) for integral y with det s y a unit of O, and 0
otherwise.

## Main definitions and results

* `New.Exchange.match_mem_of_stdColDatum`: if P contains a standard datum multiplied by an ℕ-valued
  function that is non-zero at a suitable point, then Ψ ∈ P; the proof averages over GL_n(O).
* `New.Exchange.IntegralFrame.match_mem_of_isPrimitiveMatrix_vanishing`: if a space M contains the
  shears of a standard datum and P contains what certain functionals kill in M, then Ψ ∈ P; a Gauss
  sum of the shears lies in P, and `New.Exchange.match_mem_of_stdColDatum` applies to it.
* `New.Exchange.IsEquivariantLift.shearInvariant_stdColDatum`: the partial means
  (`New.Space.Splitting.partialMean`) of the coefficients of the image of the standard datum of the
  frame are invariant under the local shears along one more isotropic line.
* `New.Exchange.IsSelfDualTestPair`, `New.Space.Splitting.VanishesAtSelfDual`: the pairs of an index
  and a Levi component at which vanishing at self-dual lattices is tested, and that vanishing.
* `New.Exchange.IsEquivariantLift.apply_eq_zero_of_areMatched`: `𝒟` vanishes on every locally
  constant datum with a matched function, once the image of the standard datum of the frame vanishes
  at self-dual lattices.

Notions from other files:
* `New.SemilocalField`: Conditions met by a finite product of non-archimedean local fields: a
  locally compact ring with Haar measure, compact open subring O of volume one, a topologically
  nilpotent invertible ϖ in O, and `New.IsValuationPair O`.
* `New.schwartzBruhat`: The space of locally constant, compactly supported complex functions that
  vanish outside a given set.
* `New.HasIntegralConductor`: The additive character ψ is continuous and has conductor O: ψ is
  trivial on tO exactly when t lies in O.
* `New.Exchange.IntegralFrame.stdDatum`: For a function G, the function equal to G(x·(K I)) at
  integral x and 0 elsewhere, with K and I two of the column blocks K, I, L of the frame.
* `New.Space.Splitting.partialMean`: the mean of a Fourier coefficient over the shifts of one more
  isotropic vector; `New.Space.Splitting.ShearInvariant` is its invariance under local shears.


 ## Stable spaces containing a standard datum 

### `IntegralFrame.exists_stdRowDatum_eq_stdDatum`

 Let χ be tame, let A be an integral frame (an integral basis of Fⁿ with column blocks L, K, I,
whose integral inverse has row blocks L', K', I'), and let σ order the n rows as L', K', I'. The row
datum `stdRowDatum σ χ A.dualL` sends x to χ⁻¹ of the determinant of the square matrix with rows L'
and x, ordered by σ, if that matrix is in GL_n(O), and to 0 otherwise. It equals c · χ⁻¹(det x (K
I)) at integral x with det x (K I) a unit of O, and 0 elsewhere, for a constant c of modulus 1. 

### `exists_pow_smul_add_eq`

 Let χ be tame (χ⁻¹ on the units of O is a primitive character of the finite ring O/ϖO) and let Ψ
be locally constant with a matched function Φ for χ over O (`AreMatched`: for k in GL_n(O), Φ at the
rows a of k⁻¹ is χ(det k) times Ψ at the columns b of k, in the order e, and both vanish
elsewhere). Then for some c, the function Ψ is invariant under translation by ϖ ^ c times integral
matrices. 

### `match_mul_stdColDatum_translate`

 Let χ be tame (χ⁻¹ on the units of O is a primitive character of the finite ring O/ϖO), let Φ be
a matched function of Ψ for χ over O (`AreMatched`: Φ at the rows a of k⁻¹ is χ(det k) times Ψ at
the columns b of k, for k in GL_n(O), the n indices being split as b ⊕ a by e, and both vanish
elsewhere), and let p = r · `stdColDatum χ s` with r an ℕ-valued function and s an integral matrix;
the standard datum `stdColDatum χ s` is χ⁻¹(det s y) at integral y with det s y a unit of O, and 0
elsewhere. Let x be integral with s x = 1, let Ψ be invariant under translation by ϖ ^ c times
integral matrices, and let d = ϖ ^ (-c) (1 - x (s - ϖ ^ c s)). Then Ψ(k⁻¹ x) p(d k y) =
|p(d k y)| Ψ(y) for k in GL_n(O). 

### `match_mem_of_stdColDatum`

 Let χ be tame and let P be a GL_n(F)-stable space of functions on n × b matrices that are
locally constant, compactly supported and zero outside a set U. Suppose that P contains
p = r · `stdColDatum χ s`, where `stdColDatum χ s` is the standard datum of the integral matrix s
(χ⁻¹(det s y) at integral y with det s y a unit of O, 0 elsewhere), and r is an ℕ-valued function
with r(x) ≠ 0 at an integral x with s x = 1. Then P contains every locally constant Ψ that has a
matched function Φ for χ over O (with the n indices split as b ⊕ a by e, Φ at the rows a of k⁻¹ is
χ(det k) times Ψ at the columns b of k, for k in GL_n(O), and both vanish elsewhere). 

### `IntegralFrame.stdColDatum_shear_of_isIntMatrix`

 An integral frame A is an integral n × n basis cut into column blocks K, I, L (K and L are
n × b), with integral inverse cut into row blocks K', I', L'; thus K' K = L' L = 1 and
K' L = L' K = 0. The shear y ↦ y + L z K' y by an integral z fixes the standard datum of K', which
is χ⁻¹(det K' y) at integral y with det K' y a unit of O, and 0 elsewhere. 

### `sum_mul_addChar_lift_eq_zero`

 Let π : O → R be a homomorphism to a finite ring, η a primitive character of R, φ a primitive
additive character of R with φ(π x) = ψ(ϖ⁻¹ x), and l a section of the reduction of matrices by π.
If η vanishes at the determinant of the reduction of T, then the sum over b × b matrices r over R of
η(det r) ψ(ϖ⁻¹ trace(T l(r))) is zero. 

### `invOnUnits_det_eq_resChar_det`

 For tame χ with reduction π and residue character η, and a matrix N over O, the value of χ⁻¹,
cut off to the units of O, at det N is η(det π(N)). 

### `IntegralFrame.stdColDatum_mul_sub_smul`

 Let χ be tame: there are a reduction π of O onto a finite ring with kernel ϖO and a primitive
character η of that ring with η ∘ π equal to χ⁻¹ on units and 0 on the rest of O. Let A be an
integral frame (an integral basis with column blocks K, I, L, whose integral inverse has row blocks
K', I', L'), so that L' L = 1 and K' L = 0. The standard datum `stdColDatum χ s` of a matrix s is
χ⁻¹(det s y) at integral y with det s y a unit of O, and 0 elsewhere. For r over O and x integral,
the standard datum of L' at L r K' x - ϖ x is η(det π(r)) times the standard datum of K' at x. 

### `IntegralFrame.match_mem_of_isPrimitiveMatrix_vanishing`

 Let χ be tame, let ψ have conductor O, and let P be a GL_n(F)-stable space of locally constant,
compactly supported functions on n × b matrices that vanish outside a set U. The standard datum of
K' is the function S₀(y) = χ⁻¹(det K' y) at integral y with det K' y a unit of O, 0 elsewhere, and S
z is its shear y ↦ S₀(y + L z K' y), with L a block of the integral frame A and K' a block of its
inverse. Let M be a space of functions that contains all S z (`h_shear_mem`). Suppose that P
contains every f ∈ M with Λ f = 0 for all matrices T and functionals Λ such that Λ(S z) = ψ(tr T z)
Λ(S₀) for all z, and Λ(S₀) = 0 in case T is primitive, that is, integral with an integral left
inverse; for the square matrix T this means T ∈ GL_b(O) (`h_kill`). Then P contains every locally
constant Ψ that has a matched function Φ for χ over O. 


## Vanishing of an equivariant lift on the data with a matched function

`New.Exchange.IsEquivariantLift` says that `𝒟` maps local data at the places `𝔠.ramifiedPlaces`
equivariantly to automorphic functions. `New.Space.Splitting.centreCoeff` is the Fourier coefficient
along the centre of the unipotent radical of the parabolic subgroup attached to a splitting
`New.Space.Splitting`. The standard datum of the frame of a splitting `D` is `New.stdColDatum` of
the dual block `dualL` of `adaptedFrame 𝔠.readsAt D`.


### `New.Exchange.IsEquivariantLift.apply_eq_zero_of_centreCoeff_eq_zero`

 Let `𝒟` be an equivariant lift on `M`: a linear map from functions of `m × b` matrices over the
completions at the ramified places `S = 𝔠.ramifiedPlaces` of the character `𝔠` to functions on
`U(X)` which, on the space `M` of locally constant compactly supported such functions, has
automorphic values, turns translation by the group at `S` into right translation up to a character
of the determinant, and has values right invariant under the standard level away from `S`. Let `D`
split `X` as `W₁` plus hyperbolic planes along `b` lines and be adapted (its adelic frame is
orthonormal at infinity and integral at the finite places; `adaptedFrame 𝔠.readsAt D` is this frame
read in the completions at `S`). Let `O` be the product of the rings of integers at `S`, and let
`Ψ₀ ∈ M` be the standard datum of the dual block `dualL` of that frame, the function
`y ↦ χ⁻¹(det (dualL y))` at integral `y` where this determinant is a unit, 0 elsewhere, with
`χ = 𝔠.semilocalChar`. Suppose that the Fourier coefficient `D.centreCoeff T` of `𝒟 Ψ₀` along the
centre of the unipotent radical of the parabolic of `D`, at a skew-hermitian index `T`, vanishes at
every point `(1, g)`, with `g` trivial at `S`, whenever `(invDifferentIdele E)⁻¹ • T` lies in
`GL_b(O)` at `S`. Then `𝒟` kills every locally constant datum `Ψ` that has a matched function
`Φ`. 

### `New.Exchange.SplitTameChar.isIntMatrix_glue_hermitian`

 Let `S` be the set of finite places outside `𝔠.ramifiedPlaces` and its conjugate and let `e` be
the idempotent adele `idemAdele S.conjClosure`, which is `1` on `S` and `0` elsewhere. If `P` is
integral at the places of `S` and their conjugates and the hermitian `Q` is integral at
`𝔠.ramifiedPlaces`, then `e • P + (1 - e) • Q` has integral finite part. 

### `New.Exchange.IsSelfDualTestPair`

 The pairs `(T, q)` of an index `T` and a point `q` of `GL_b(𝔸)` at which vanishing at self-dual
lattices is tested, for a hermitian space `V'` over the CM field `E` with form `V'.J`, signs `t'`
and adelic frame `V'.x`. Either (a) `T = V'.J` and `q = scaleIdele E • V'.x * Y` (`scaleIdele E` is
the idele of `WeilData E` that makes `Ô` self-dual), where the finite part of `Y` times some
`k ∈ GL_b(Ô)` is unitary for the form `1` (`U 1`), so that the columns of `V'.x * Y` span a lattice
that is self-dual for `T`; or (b) `T` is invertible and not of the form `aᴴ diag(t') a` at some
infinite place, and `q` is arbitrary. 

### `New.Space.Splitting.VanishesAtSelfDual`

 Let `D` be a splitting of the space `X` (indices `m`, signs `r`) as `W₁` (indices `n`, signs
`s`) plus hyperbolic planes along `b` lines. A function `f` on `U(X)` vanishes at self-dual lattices
if its Fourier coefficient along the centre of the unipotent radical of the parabolic of `D`, at the
index `j • T` (`j` is the fixed skew element of `WeilData E`), vanishes at each point
`D.radicalElement c z * D.levi (q, g)` of that parabolic (a radical element times the Levi element
of `q ∈ GL_b(𝔸)` and `g ∈ U(W₁)`) for which `(T, q)` is a test pair for `V'`
(`IsSelfDualTestPair`). 

### `New.Space.Splitting.centreCoeff_eq_zero_of_orthonormal`

 Let `D` be a splitting of `X` over `W₁` along `b` lines, let `j` be the fixed skew element of
`WeilData E` and `scaleIdele E` its idele that makes `Ô` self-dual. Let `f` be an automorphic
function that vanishes at self-dual lattices, tested on the pairs of a hermitian space `V'` with
Gram matrix `V'.J`, adelic frame `V'.x` and signs `t'`: its Fourier coefficient `D.centreCoeff`
along the centre of the unipotent radical, at the index `j • T`, vanishes at the points
`D.radicalElement c z * D.levi (q, g)` if (a) `T = V'.J` and `q = scaleIdele E • V'.x * Y`, where
the finite part of `Y` times some `k ∈ GL_b(Ô)` is unitary, or (b) `T` is invertible and at some
infinite place not of the form `aᴴ diag(t') a`. Let `det β ≠ 0`, and let the columns of `q * k`,
with `k ∈ GL_b(Ô)`, be orthonormal for `β` at the finite places. Then the coefficient at `j • β`
vanishes at `D.radicalElement l z * D.levi (scaleIdele E • q, g)`. 

### `New.Exchange.IsEquivariantLift.partialMean_shear`

 Let `𝒟` be an equivariant lift on `M` and let `ν ∈ U(X)` have matrix `1 + e u c - ē N`, with
`c u = 0`, `e` the idempotent of `𝔠.ramifiedPlaces` and `N` any matrix, so that `ν` is `1 + u c` at
`𝔠.ramifiedPlaces`. Let `A` split one isotropic line off `X`, leaving `W₀`, let `B` split `b` planes
off `W₀`, leaving `W`, and let `D` split `X` over `W₁`. For `Ψ ∈ M`, let `Ψ' y = Ψ (g y)`, with `g`
the component of `x⁻¹ ν x` at `𝔠.ramifiedPlaces`. Then `Ψ' ∈ M`, and the partial mean of `𝒟 Ψ'` at
`x` equals that of `𝒟 Ψ` at `ν⁻¹ x`. 

### `New.Exchange.IsEquivariantLift.exists_linear_partialMean`

 Let `𝒟` be an equivariant lift on `M`. Let `A` split one isotropic line off `X`, `B` split `b`
planes off what remains and `D` split `X` over `W₁`, and let the adelic isotropic frame `kAdelic` of
`D` be the image under the embedding `A.iAdelic` of that of `B`. At each point `x`, the map
`Ψ ↦ A.partialMean B D T (𝒟 Ψ) x` on `M` is the restriction of a linear form `L`, and `L` is
invariant on `M` under composition with `y ↦ y + u w l y` for all rows `w`. Here `u` and `l` are the
components at the ramified places of `x⁻¹ A.kAdelic` (the isotropic vector of `A`) and of
`D.lCoord x`. 

### `New.Exchange.IsEquivariantLift.shearInvariant_stdColDatum`

 Invariance under shears. Let `𝒟` be an equivariant lift on `M` and `f = 𝒟 Ψ₀`, where `Ψ₀ ∈ M` is
the standard datum of the adapted splitting `D` (frame orthonormal at infinity and integral at the
finite places): `y ↦ χ⁻¹(det (dualL y))` on integral `y` with unit determinant, 0 elsewhere, for the
dual block `dualL` of the frame of `D` read at the ramified places and `χ = 𝔠.semilocalChar`. Let
`A` split one isotropic line off `X`, leaving the sum `hyperbolicSum b W` of `b` hyperbolic planes
and `W`, so that the frame of `D` is the image under `A` of the frame of the tautological splitting
`removePlanes b W` of those planes (`hA`). Let `S` be the set of finite places outside
`𝔠.ramifiedPlaces` and its conjugate (`hS`), and let `g` fix the frame of `D` at all places outside
`S`. Then, for every `T`, the partial mean of `f` takes the same value at `g` and `ν * g`, for each
`ν` that is `1 + u c` at `𝔠.ramifiedPlaces` and `1` away from `𝔠.ramifiedPlaces` and its conjugate,
where `u` is the isotropic vector of `A` and `c u = 0`. 

### `New.Exchange.IsEquivariantLift.apply_eq_zero_of_areMatched`

 Self-dual lattices suffice. Let `𝒟` be an equivariant lift on `M` (a linear map from data at the
ramified places `S = 𝔠.ramifiedPlaces` to functions on `U(X)`, automorphic and `S`-equivariant on
`M`). Let `D` and `D₁` be adapted splittings of `X` over `W₁` along `b` lines and of `W₁` over `W`
along one line; the extra line `D₁` gives the shears under which the partial means are invariant.
Let `f = 𝒟 Ψ₀` for the standard datum `Ψ₀ ∈ M`: `y ↦ χ⁻¹(det (dualL y))` at integral `y` with unit
determinant, 0 elsewhere, for the dual block `dualL` of the frame of `D` read at `S` and
`χ = 𝔠.semilocalChar`. Suppose that `f` vanishes at self-dual lattices along `D`, tested on the
pairs of the hermitian space `V'` with form `V'.J`. Then `𝒟` maps to zero every locally constant
datum `Ψ` that has a matched function `Φ`. 
