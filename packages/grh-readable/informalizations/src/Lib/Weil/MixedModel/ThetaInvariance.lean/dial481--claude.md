---
{
  "module": "src/Lib/Weil/MixedModel/ThetaInvariance.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/ThetaInvariance.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/ThetaInvariance.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Mixed model of the Weil representation: Levi intertwining and invariance of θ

This file proves that the slice map x ↦ f[x] = `D.slice x f` of a splitting `D` is continuous and
integrable on `𝔸^p`. Take `g` with `g k = k a`, `a ∈ GL_p(𝔸)`, acting as `g₀` on `V₀`. Then ev
ω(g) = χ_𝔸(det a)⁻¹ ω(g₀) ev, where ev is the zero term and χ_𝔸 = `New.chiAdelic`. The file then
proves that θ is invariant under the rational unitary group. When `V₀` is zero, the function
x ↦ f[x] plays the part of a vector of the Schrödinger model on `𝔸^p`; this identification is not
stated here, and the space L²(𝔸^p) is not used.

## Main definitions and results

* `New.Space.Splitting.zeroTerm_omega_levi`: on the Levi subgroup, ev ω(g) = χ_𝔸(det a)⁻¹ ω(g₀) ev.
  The modulus of the scalar comes from `New.Space.Splitting.integral_dataInner_slice`. Its phase
  comes from `New.Space.Splitting.exists_hyperbolic_levi_multiplier_nonneg`.
* `New.Space.theta_omega_ratEmbed`: θ is invariant under the rational unitary group, acting through
  `New.Space.ratEmbed` and `New.Space.ω`. On a split space two opposite parabolic subgroups fix θ
  and generate the group (`New.Space.theta_omega_ratEmbed_of_splitting`). The general case follows
  by doubling: `V ⊕ V⁻` is split, and `γ` acts on it as `(γ, 1)`.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to diag(s) at the infinite places and 1 at the finite places.
* `New.𝒮`: The Banach space 𝒮(V) of integrable functions c on 𝔸^n with c(x) = ∫ c(y)β(y,x)e(x−y) dy,
  under the L¹ norm; β is the adelic bicharacter and e the vacuum function `New.vacuumFn`.
* `New.Space.Splitting`: A decomposition V = (lE^p ⊕ kE^p) ⊥ ιV₀ over E: isotropic frames l, k with
  l*Jk = 1, an isometry ι from V₀ orthogonal to both, and rk V = rk V₀ + 2p.
* `New.WeilData`: Weil data on a stably unramified E. They consist of ȷ in E with ȷ = −ȷ̄, Im τȷ > 0
  for every τ in the CM type and (1 − ȷ⁻¹)/2 integral; a finite idele α for which the completed
  integers Ô are self-dual under (z, u) ↦ ψ_f(ȷαᾱzu); and a splitting character υ equal to −1 at
  uniformisers of the places w with w = w̄.
* `New.Space.Splitting.zeroTerm`, `New.Space.Splitting.slice` (in `Lib.Weil.MixedModel.ZeroTerm`):
  the zero term ev : 𝒮 V → 𝒮 V₀, the integral of `f (ι y + k b)` over `b ∈ 𝔸^p`, and the slice
  f[x] = ev(ϱ(l x) f).

## Relation to the literature

Known result: Schrödinger and mixed models of the Weil representation and the action of parabolic
subgroups. Here the groups are adelic unitary groups of spaces `New.Space` over a CM field with
`New.WeilData`, and the vectors have integrable coefficients instead of being Schwartz functions.
The representation is normalised by its vacuum coefficient, so the formulas for the parabolic
subgroup are proved rather than taken as the definition. Source: C. Mœglin, M.-F. Vignéras, J.-L.
Waldspurger, Correspondances de Howe sur un corps p-adique, LNM 1291, 1987; S. Kudla, Splitting
metaplectic covers of dual reductive pairs, Israel J. Math. 87 (1994) 361–401; A. Weil, Acta Math.
111 (1964) n° 16–19, 41.

Known result: Adelic Weil representation of a unitary group and the invariant theta functional. Here
the CM fields have enough roots of unity and carry a splitting character and a self-dual rank-one
lattice, and the Weil representation is built without a polarisation. Vectors are integrable
coefficients against a vacuum, the splitting is fixed by the vacuum coefficient, and the sign of the
finite cocycle comes from a congruence modulo 4. Source: A. Weil, Sur certains groupes d'opérateurs
unitaires, Acta Math. 111 (1964), n° 16-19 Thm 4, n° 41 Thm 6; S. Kudla, Splitting metaplectic
covers of dual reductive pairs, Israel J. Math. 87 (1994) 361-401; H. Reiter, Metaplectic Groups and
Segal Algebras, LNM 1382 (1989) (space of data, after H. Feichtinger, On a new Segal algebra,
Monatsh. Math. 92 (1981)); E. Zelenov, p-adic Heisenberg group and Maslov index, Comm. Math. Phys.
155 (1993) 489-502, Prop. 4 (cocycle of three lattices); Robinson and Rawnsley, Mem. AMS 410 (1989)
(real normalisation).



## Continuity and integrability of x ↦ f[x]

Integrability follows from the bound `New.Space.Splitting.tsum_enorm_slice_le` on sums over
`E^p` and from compactness of `𝔸^p / E^p`.


### `continuous_slice`

 For a Witt decomposition `D` of `V` as `(l E^p ⊕ k E^p) ⊥ ι V₀` over a CM field `E` with Weil
data, and any `f` in 𝒮(V), the slice `x ↦ D.slice x f` is a continuous map from 𝔸^p to 𝒮(V₀) with
its own topology. Here `D.slice x f` is the mixed-model value, namely the zero term along `k` of
`ϱ(l x) f`. 

### `integrable_slice`

 For a splitting of V over V₀ with p hyperbolic planes and f in 𝒮(V), the 𝒮(V₀)-valued
function x ↦ f[x] of the mixed model is integrable on 𝔸^p. 


## Intertwining on the parabolic subgroup

The zero term ev = `New.Space.Splitting.zeroTerm` : 𝒮 V → 𝒮 V₀ is taken along the isotropic frame
`k` of a splitting.

`New.weilMultiplier` is the multiplier Δ in the definition of `ω`. `dataInner` is the scalar product
on `𝒮`.


### `exists_hyperbolic_levi_multiplier_nonneg`

 For a in GL_p(𝔸) and x the point of the space `New.hyperbolicSpace` of p hyperbolic planes
(signs `hyperbolicSigns p`: +1 on the first p and −1 on the last p coordinates; x is (1, −1; 1,
1)/√2 at each infinite place and integral at the finite places), some g₁ in the adelic unitary group
has matrix x⁻¹ diag(a*⁻¹, a) x. Moreover Δ(g₁)υ(det a) is a nonnegative real number, where Δ is the
multiplier `weilMultiplier` and υ is the splitting character of the Weil data. 

### `integrable_dataInner_slice`

 Let `D` be a Witt decomposition V = (l E^p ⊕ k E^p) ⊥ i V₀, and for f in 𝒮(V) let
f[x] = `D.slice x f` in 𝒮(V₀) be its slice at x ∈ 𝔸^p. For f, f′ in 𝒮(V), the scalar product ⟨f[x],
f′[x]⟩ = ∫ conj(f[x]) f′[x] is integrable in x. 

### `integral_dataInner_slice`

 For a Witt splitting `D` of `V` over `V₀` with frames of `p` columns, let f[x] = `D.slice x f`
in 𝒮(V₀) be the slice at x ∈ 𝔸^p. There is a constant C with ∫ ⟨f[x], f′[x]⟩ dx = C⟨f, f′⟩ for all
f, f′ in 𝒮(V). The pairing on the left is `dataInner` of 𝒮(V₀) and on the right that of 𝒮(V). 

### `exists_zeroTerm_omega_eq_smul`

 Suppose g sends the frame k to k·a for some a in GL_p(𝔸), and g acts on the V₀-part as g₀. Then
there is a scalar c with ev(ω(g)f) = c·ω(g₀)(ev f) for all f in 𝒮(V), where ev is the zero term
`New.Space.Splitting.zeroTerm`. 

### `integral_comp_conjTranspose_mulVec`

 The push-forward of the volume under `x ↦ aᴴ x` is `|det a|⁻¹` times the volume: for continuous
F on 𝔸^p, the integral of F(aᴴ x) is |det a|⁻¹ times the integral of F. 

### `weilMultiplier_conj_levi`

 Let the group element k have as columns, reordered by e, those of the matrix of D's frames
times diag(x, 1) (`frameAt 1 1` is the matrix of the frames; x is the point of hyperbolic space),
and let g₁ have the matrix x⁻¹ diag(a*⁻¹, a) x. Then the conjugate by k of the Levi element of
(a, g₀) is block diagonal with blocks g₁, g₀, so its multiplier Δ is the product of theirs. 

### `eq_inv_chiAdelic_of_norm_sq_of_phase`

 A scalar c with |c|² = |det a| and c J conj(m) = I, for reals I > 0, J ≥ 0 and a complex m with
m υ(det a) ≥ 0, is χ_𝔸(det a)⁻¹. 

### `levi_mulVec_lAdelic_mulVec_conjTranspose_mulVec`

 The Levi element attached to `(a, g₀)` sends the vector `l aᴴ x` to `l x`. 

### `zeroTerm_omega_levi`

 For the Levi element `D.levi (a, g₀)` attached to `a ∈ GL_p(𝔸)` and `g₀` in the group of `V₀`,
one has ev ω(`D.levi (a, g₀)`) = χ_𝔸(det a)⁻¹ ω(g₀) ev. Here ev is the zero term
`New.Space.Splitting.zeroTerm`, and `χ_𝔸 = υ |·|^(-1/2)`. 

### `slice_omega_levi`

 The Levi element with parts `a` (on the isotropic frame) and `g₀` (on `V₀`) acts on the slices
`x ↦ D.slice x f` by the substitution `x ↦ aᴴ x`, the operator `ω(g₀)` on the values and the
factor `(chiAdelic a.det)⁻¹`. 

### `zeroTerm_omega`

 Let `D` split `V` as `(l E^p ⊕ k E^p) ⊥ ι V₀`, and let `g` satisfy gk = ka for a p×p adelic
matrix a whose determinant is the idele d. Suppose also that the V₀-block of g is g₀ in the adelic
group of V₀. Then ev(ω(g)f) = υ(d)⁻¹ |d|^{1/2} ω(g₀) ev(f) for all f, where ev is the zero term
along k, υ is the splitting character of the Weil data, and the scalar is the inverse of
χ_𝔸(d) = υ(d)|d|^{−1/2}. The V₀-block is `iCoord * g * iAdelic`, with `iAdelic` the adelic embedding
ι of V₀ and `iCoord` the projection to its coordinates. When V₀ is zero, this is the value at the
origin of the formula for the Siegel parabolic subgroup in the Schrödinger model. 

### `slice_omega_radicalElement_zero`

 For a Witt splitting `D` of `V` over `V₀` with frames of `p` columns and a hermitian adelic
`p × p` matrix `z`, consider the element `D.radicalElement 0 z` of the centre of the radical. It
fixes `k`, fixes `ι`, and sends `l` to `l − k j⁻¹ z`. Acting through the Weil representation `V.ω`,
it multiplies the slice `D.slice x f = ev(ϱ(lx) f)` in 𝒮(V₀) by the standard additive character at
`-xᴴ z x / 2`. 

 ## Invariance of θ under rational points 

### `thetaStabilizer`

 The subgroup of the rational unitary γ whose Weil operator ω(γ) fixes the theta functional of
V. 

### `theta_omega_ratEmbed_of_mul_k`

 Let V be split by D, with isotropic frames k, l and no middle part. A rational unitary γ that
maps the span of k to itself, γk = ka with a invertible over E, fixes the theta functional θ of V:
θ(ω(γ)f) = θ(f), where ω is the Weil representation and γ acts through the rational embedding. 

### `theta_omega_ratEmbed_of_splitting`

 If V has a splitting with no middle part, every point γ of the rational unitary group fixes the
theta functional θ under the Weil representation ω: θ(ω(γ)f) = θ(f). 

### `diagonalSplitting`

 The splitting without middle part of `V ⊕ V⁻`, with `V⁻` the space of the negative form, whose
frame `k` spans the diagonal `{(v, v)}` and whose frame `l` spans the antidiagonal `{(v, -v)}`. 

### `exists_theta_boxProd_eq_mul`

 For a datum y of a second space V′, the functional f ↦ θ(f ⊠ y) is a multiple of the theta
functional of V. Here θ is the theta functional of V ⊕ V′, and ⊠ = `New.Space.boxProd` is the
tensor product 𝒮(V) × 𝒮(V′) → 𝒮(V ⊕ V′) for the evident splitting of the coordinates. 

### `exists_theta_boxProd_ne_zero`

 The theta functional of V ⊕ V′ does not vanish on all products f ⊠ y (`New.Space.boxProd`) of
data f of V and y of V′. 

### `theta_omega_ratEmbed`

 The theta functional is invariant under rational points: θ(ω(γ)f) = θ(f) for every γ in the
rational unitary group of V and every f in 𝒮(V), where ω is the Weil representation.

A case of Weil's invariance of the theta distribution under rational points, for the unitary group
of a hermitian space V with a point, with the representation ω and the functional θ on 𝒮(V). 

### `omega_ratEmbed_apply`

 A rational point γ acts on a datum f, read as the function f(x) = θ(ϱ(x)f) of the adelic vector
x, by substitution: (ω(γ)f)(x) = f(γ⁻¹x). 
