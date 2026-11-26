---
{
  "module": "src/Lib/Adelic/AutomorphicForms/Cuspidality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/Cuspidality.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/Cuspidality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cuspidality bounds, unipotent reduction, rapid decay and finite dimension of forms

This file studies forms of type `e` (`New.Space.IsForm`) on the adelic unitary group of a hermitian
space `V`, for a cusp kernel `e` (`New.IsCuspKernel`). At a point with a short lattice vector,
short vectors span a cusp: a rational isotropic subspace whose radical is covered by its rational
points times a small real ball and a level. A bounded continuous function that is fixed by `e` and
invariant under the rational points of a unipotent radical, of finite covolume, has mean zero along
the radical (`New.Space.integral_unipotentRadical_eq_zero`, in
`Lib.Adelic.AutomorphicForms.UnipotentRadical`). The rational points are cocompact in the radical
of a rational isotropic subspace, so forms are cuspidal. Forms then decay faster than every power
of the height, and those of a fixed level span a finite-dimensional space.

## Main definitions and results

* `New.Space.exists_cuspFrame`: let `N ≠ 0` be a natural number in the different of `E`, `M ≠ 0` and
  `0 < δ ≤ 1`. If the first minimum is less than `(δ / (M κ²))ⁿ`, with `κ = New.cuspConst E n N`,
  short lattice vectors span a rational isotropic subspace `A ≠ 0` and its orthogonal
  (`New.Space.CuspFrame`), and `N_A` lies in `(Γ ∩ N_A) Z_δ J(M)` (`New.Space.RadicalCovered`),
  where `Z_δ` is the real ball of radius `δ` about `1` and `J(M)` is the principal level `M`.
* `New.Space.IsCuspidal`, `New.Space.IsForm.isCuspidal`: cuspidal functions; forms are cuspidal.
* `New.Space.IsCuspidal.norm_le_of_firstMinimum_lt`: at such a point `g`, a cuspidal function of
  level `M` is at most its oscillation under real right translations of size `δ`.
* `New.Space.exists_norm_mul_height_pow_le`, `New.Space.IsForm.mem_rapidFunctions`: forms decay
  faster than every power of the height, uniformly at a fixed level.
* `New.Space.finite_levelSpace`: the forms of a fixed level span a finite-dimensional space.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to diag(s) at the infinite places and 1 at the finite places (in the coordinates x⁻¹ X this
  form is the adelic matrix `stdForm E s`); `V.Γ` is its group of rational points in the adelic
  group G = G_∞ × G_f, and `V.move g` has the point xg.
* `New.realConv`, `New.Space.IsForm`: R(k)F(g) = ∫ k(x) F(gx) dx over G_∞ (`New.GInf`, one copy of
  U(diag s) for each infinite place of E), for k on G_∞ and F on G. For integrable e, a form of
  type e is a bounded automorphic function fixed by R(e). Here e is a cusp kernel
  (`New.IsCuspKernel`): a minimal idempotent for convolution on G_∞ that decays polynomially and
  is reproduced by a compactly supported function.
* `New.Space.height`: the height ht(g) = 1/λ, with λ the first minimum cut off at 1
  (`New.Space.firstMinimum`) of the moved space `V.move g`.
* `New.unipotentRadical` (in `Lib.Adelic.AutomorphicForms.UnipotentRadical`): the adelic unipotent
  radical of the stabiliser of the span of the columns of an isotropic matrix.
* `New.Reduction.radicalElem` (in `Lib.Adelic.AutomorphicForms.UnipotentRadical`): the matrix
  `1 + 2 (T - Tᴴ - Tᴴ J T) J`; for hermitian `J` and `T = w aᴴ` with `aᴴ J a = aᴴ J w = 0`, it
  preserves `J`, fixes `a` and acts trivially on `a^⊥ / a`.

## Relation to the literature

Known results: cusp forms decay rapidly, and those of a fixed type and level make up a space of
finite dimension. Here a form is a bounded function reproduced by an integrable minimal idempotent,
with no differential equation. Cuspidality is used as a bound by the oscillation along unipotent
orbits, with an explicit depth, and the cusp is spanned by the shortest vectors of a sorted
Minkowski basis.

Sources: A. Borel, Automorphic forms on reductive groups (Park City lectures), IAS/Park City Math.
Ser. 12 (2007) 7-39, sections 7.6-7.9 and 8.3-8.4; I. Satake, Caractérisation de l'espace des
Spitzenformen, Sém. H. Cartan 10 (1957/58), exp. 9 bis; R. Godement, Série de Poincaré et
Spitzenformen, ibid., exp. 10; R. Godement, The spectral
decomposition of cusp forms, Proc. Sympos. Pure Math. 9 (1966) 225-234; S. Miller and W. Schmid, On
the rapid decay of cuspidal automorphic forms, Adv. Math. 231 (2012), arXiv 1106.2149; G. Muić,
Smooth cuspidal automorphic forms and integrable discrete series, arXiv 1610.05483 (cuspidality
through N. Wallach, On the constant term of a square integrable automorphic form, 1984).


 ## The cusp of a point with a short vector; cuspidal functions 

### `cuspConst`

 The constant `κ = 8 f n · rd + 48 n⁶ f² N + 1` in the bound
`New.Space.IsForm.norm_le_of_firstMinimum_lt`, where `f` is the number of infinite places, `rd` the
root discriminant of `E`, and `N` a natural number (in the bound, a nonzero natural number in the
different of `E`). 

### `adelicCoords`

 The rational matrix `X` in the adelic coordinates `x⁻¹ X` given by the point `x` of `W`, in
which the form of `W` is `stdForm E s`. 

### `radical`

 The adelic unipotent radical `N_A` of the span `A` of the columns of the rational matrix `X`,
used for isotropic `A`. For `W = V.move g` it is `g⁻¹ N_A g`. 

### `RadicalCovered`

 The radical `N_A` of the span `A` of the columns of `X` lies in `(Γ ∩ N_A) Z_δ J`, where `Γ` is
the group of rational points of `W` and `Z_δ` is the real ball of radius `δ` about `1`.
For `W = V.move g` it reads `N_A g ⊆ (Γ ∩ N_A) g Z_δ J`, with `Γ` and `N_A` those of `V`. 

### `CuspFrame`

 A cusp of size `δ`: a non-zero rational isotropic subspace `A` such that `A` and `A^⊥` are
spanned by the columns of `X = isotropicCols` and of `Y = perpCols`, lattice vectors of lengths at
most `lengthX`, `lengthY` (`W.latticeBall l`: vectors of `W.baseLattice` whose `W.archCoords` have
norm at most `l`) with `lengthX * lengthY ≤ δ`. 

### `CuspFrame.isotropicCols`

 A matrix whose columns span `A`. 

### `CuspFrame.perpCols`

 A matrix whose columns span `A^⊥`. 

### `CuspFrame.lengthX`

 The bound for the lengths of the columns of `isotropicCols`. 

### `CuspFrame.lengthY`

 The bound for the lengths of the columns of `perpCols`. 

### `CuspFrame.ne_zero`

 `A` is not zero. 

### `CuspFrame.isotropic`

 `A` is isotropic. 

### `CuspFrame.orthogonal`

 The columns of `perpCols` lie in `A^⊥`. 

### `CuspFrame.spans`

 The columns of `perpCols` span `A^⊥`: a vector `v` orthogonal to `A` equals
  `perpCols *ᵥ e *ᵥ v`. 

### `CuspFrame.col_isotropicCols_mem`

 The columns of `isotropicCols` are lattice vectors of length at most `lengthX`. 

### `CuspFrame.col_perpCols_mem`

 The columns of `perpCols` are lattice vectors of length at most `lengthY`. 

### `CuspFrame.lengthX_le`

 The vectors that span `A` have the smaller bound. 

### `CuspFrame.length_mul_le`

 The product of the two bounds is at most `δ`. 

### `adelicCoords_gram`

 The standard pairing of the adelic coordinates of `X` and `Y` is their pairing `Xᴴ J Y` for the
form `J` of `W`. 

### `isIntBounded_adelicCoords`

 If the columns of `X` are lattice vectors of length at most `l`, the adelic coordinates of `X`
are integral at the finite places and of operator norm at most `n² l` at the infinite ones. 

### `ratEmbed_move`

 Moving the point of `V` by `g` conjugates the embedding of the rational points by `g`. 

### `mem_dilationGroup_of_ratEmbed_mem_radical`

 If a rational point `ν` of `U(J)` embeds into the adelic radical of the span `A` of the columns
of `X`, it fixes `A` and `A^⊥ / A` pointwise over `E`. 

### `exists_le_rev_and_mul_rev_lt`

 Pairing from both ends: if the square of a product of `k` real numbers is below `c ^ k` with
`0 ≤ c`, then at some pair of opposite indices `i`, `i.rev` with `m i ≤ m i.rev`, the two
numbers have a product below `c`. 

### `rank_of_apply_min`

 The square matrix whose rows, numbered by `e`, are the independent vectors `y 0, …, y j`, the
last one repeated, has rank `j + 1`. 

### `Space.exists_basis_prod_norm_le`

 Minkowski's basis of a space of rank `k`. Let `1 ≤ κ` and `8 f k · rd ≤ κ`, where `f` is the
number of infinite places and `rd` is the root discriminant of `E`. The lattice of `W` contains a
basis, ordered by length, whose lengths have product at most `κ ^ k`. 

### `Space.one_le_norm_mul_of_span_eq_top`

 If lattice vectors `y j` of length at most `r` span `E ^ n`, the length of every nonzero lattice
vector times `r` is at least `1`. 

### `Space.nonempty_cuspFrame`

 A short lattice vector gives a cusp. Let `W` be a space over the CM field `E` in dimension `n`.
Let `1 ≤ κ`, `0 ≤ θ * κ ≤ 1` and `8 f n · rd ≤ κ`, where `f` is the number of infinite places and
`rd` is the root discriminant of `E`. If the first minimum of `W` (cut off at `1`) is below `θ ^ n`,
there is a cusp of size `θ * κ` (`New.Space.CuspFrame`): a nonzero rational isotropic subspace `A`,
with `A` spanned by lattice vectors of length at most `x` and `A^⊥` spanned by lattice vectors of
length at most `y`, where `x * y ≤ θ * κ`. 

### `dist_le_and_mem_principalLevel_of_adeleMatrix_eq`

 If `T` is integral at the finite places and of operator norm at most `δ / (6 M)` at the infinite
ones, with `0 < δ ≤ 1`, a point `x` with matrix `radicalElem (stdForm E s) (M • T)`, where
`radicalElem J T = 1 + 2 (T - Tᴴ - Tᴴ J T) J`, has real part within `δ` of `1` and finite part in
the principal level `M`. 

### `exists_isIntBounded_sub_map`

 Every adelic matrix is near a rational matrix. If `N ≠ 0` lies in the different of `E`, there is
a rounding map `f : 𝔸 E → E` such that every matrix `c` differs from its entrywise rounding by a
matrix that is integral at the finite places and of operator norm at most `n² (2 r)² N` at the
infinite ones, `r` being the number of infinite places. 

### `Space.adelicCoords_mul_add_mul_eq_one`

 If `Y e + 2 M b Xᴴ J = 1` over `E`, so that the orthogonal of the columns of
`X` lies in the span of those of `Y`, the same relation holds for their images in the adelic frame
of `W`, in which the form is `stdForm E s`. 

### `Space.map_radicalElem`

 The rational matrix `radicalElem W.J (P Xᴴ)`, read in the adelic frame of `W`, is the element
`radicalElem` for the standard form with the adelic coordinates of `P` and `X` as parameters. 

### `Space.mem_Gamma_of_adeleMatrix_eq_radicalElem`

 Let `p` and `a` be the adelic coordinates of rational matrices `P` and `X`. A point `x` with
matrix `radicalElem (stdForm E s) (p aᴴ)` is a rational point of `W`. 

### `Space.exists_mem_Gamma_adeleMatrix_mul_eq_radicalElem`

 Reduction by a rational point. Let `Xᴴ J X = Xᴴ J Y = 0` and `Y e + 2 M b Xᴴ J = 1` over `E`,
so that the columns of `X` span an isotropic subspace `A` and those of `Y` span `A^⊥`, and let `a`,
`y` be the adelic coordinates of `X`, `Y`. Let `r` be any map from adelic to rational matrices (a
rounding). For `u` in the radical `N_A` there are adelic matrices `c`, `d` and a rational point `γ`
of `N_A` such that `γ u` is `radicalElem` of `M (y (c - r c) - a (d - r d)) aᴴ`. 

### `exists_orthogonal_one_sub`

 Some matrix `b` over `E` makes the columns of `1 - 2 b Xᴴ J` orthogonal to those of `X` for `J`:
take `2 b` to be a generalised inverse of `Xᴴ J`. 

### `Space.isCocompact_radical`

 Let `A` be a rational isotropic subspace of the hermitian space `W`, spanned by the columns of
`X`. The group `Γ ∩ N_A` of rational points is cocompact in the adelic unipotent radical `N_A`.

A case of the compactness of `N(F) \ N(𝔸)` for a unipotent group `N` over a number field `F`. 

### `Space.CuspFrame.radicalCovered`

 Reduction in the radical of a cusp. Let `N ≠ 0` lie in the different of `E`, let `M ≠ 0` and
`0 < δ ≤ 1`, and let `κ = New.cuspConst E n N = 8 f n · rd + 48 n⁶ f² N + 1` (`f` the number of
infinite places, `rd` the root discriminant of `E`). Let `A` be a cusp of `W` of size `δ / (M κ)`: a
nonzero rational isotropic subspace, spanned by the columns of `A.isotropicCols`, with `A` spanned
by lattice vectors of length at most `x` and `A^⊥` spanned by lattice vectors of length at most `y`,
where `x * y ≤ δ / (M κ)`. Then the radical `N_A` lies in `(Γ ∩ N_A) Z_δ K(M)`
(`New.Space.RadicalCovered`), where `Γ` is the group of rational points of `W`, `Z_δ` is the real
ball of radius `δ` about `1`, and `K(M)` is the principal level `M`. 

### `Space.exists_cuspFrame`

 A point with a short vector lies high in a cusp. Let `N ≠ 0` lie in the different of `E`, let
`M ≠ 0` and `0 < δ ≤ 1`. Suppose the first minimum (cut off at 1) of the lattice of `W` is less than
`(δ / (M κ²))ⁿ`, where `κ = New.cuspConst E n N`. Then there is a cusp `A` of size `δ` whose radical
`N_A` lies in `(Γ ∩ N_A) Z_δ J(M)`. Such a cusp is a nonzero rational isotropic subspace, spanned by
the columns of `A.isotropicCols`, with `A` and `A^⊥` spanned by lattice vectors of lengths at most
`a`, `b` where `a b ≤ δ`. Here `Γ` is the group of rational points of `W`, `Z_δ` is the real ball of
radius `δ` about `1` and `J(M)` is the principal level `M`. For `W = V.move g` this is the inclusion
`N_A g ⊆ (Γ ∩ N_A) g Z_δ J(M)`. 

### `Space.norm_le_of_oscillation`

 Let `A ≠ 0` be the rational isotropic subspace spanned by the columns of `X`, let `J` be a
compact open subgroup of `Gf E n` inside the standard level, called a level, and let
`N_A g ⊆ (Γ ∩ N_A) g Z_δ J` (`New.Space.RadicalCovered`), with `Z_δ` the real ball of radius `δ`
about `1`. A bounded continuous function `F` that is fixed by a cusp kernel `e` and by `J`, and left
invariant under the rational points of the radical `N_A`, is bounded at `g y`, for `y` real, by its
oscillation `D` on `g Z_δ y`. 

### `Space.IsCuspidal`

 A continuous function `F` on `Γ \ G`, with `Γ = V.Γ` the group of rational points, is cuspidal
if its constant terms vanish: the integral of `F (u g)` over `u ∈ (Γ ∩ N_A) \ N_A` is zero for every
point `g` and every rational isotropic subspace `A ≠ 0`, with unipotent radical `N_A`. 

### `Space.IsCuspidal.continuous`

 `F` is continuous. 

### `Space.IsCuspidal.rat_mul`

 `F` is left invariant under the rational points. 

### `Space.IsCuspidal.integral_eq_zero`

 The integral is written in the frame at `g`, over `v = g⁻¹ u g`, and `A` is spanned by the
  columns of `X`. It is taken against the quotient measure, which is finite because the quotient is
  compact (`New.Space.isCocompact_radical`). 

### `Space.fixesLeft_move`

 A function that is left invariant under the rational points of `V`, read in the frame at `g`, is
left invariant under the rational points of `V.move g`. 

### `Space.IsForm.isCuspidal`

 Let `e` be a cusp kernel of order `B` on `G_∞`: a minimal idempotent with ‖x‖^(B+1) e(x)
integrable, ‖x‖^B e(x) bounded, and α ∗ e = e for some continuous compactly supported α. Let `F` be
a form of type `e` for `V`, that is, a bounded automorphic function fixed by right convolution with
`e`. Then `F` is cuspidal: its constant terms along the unipotent radicals of nonzero rational
isotropic subspaces vanish. 

### `Space.IsCuspidal.norm_le_of_firstMinimum_lt`

 High in a cusp, a cuspidal function is bounded by its oscillation. Let `F` be a cuspidal
function of level `New.principalLevel n M` with `M ≠ 0`. Let `N ≠ 0` be a natural number in the
different of `E`, and let `0 < δ ≤ 1`. Suppose the first minimum of the lattice at `g` is less than
`(δ / (M κ²))ⁿ`, where `κ = New.cuspConst E n N`. If `‖F (g x) - F g‖ ≤ C` for every real `x` with
`dist x 1 ≤ δ`, then `‖F g‖ ≤ C`. 

### `Space.IsForm.norm_le_of_firstMinimum_lt`

 High in a cusp, a form is bounded by its oscillation. Let `F` be a form of type `e`, with `e` a
cusp kernel, and of principal level `M ≠ 0`. Let `N ≠ 0` lie in the different of `E`, and let
`0 < δ ≤ 1`. If the first minimum of the lattice at `g` is less than `(δ / (M κ²))ⁿ`, where
`κ = New.cuspConst E n N`, then `‖F g‖` is at most the oscillation `C` of `F` at `g` under real
right translations of size `δ`. 

 ## Rapid decay, finite dimension at each level, and projection to type `e` 

### `dist_conj_one_le`

 Conjugation by a real point `z` multiplies the distance to `1` by at most `‖z‖ ^ 2`, where `‖z‖`
is the product over the infinite places of the operator norms. 

### `prod_opNorm_mul_le`

 The product over the infinite places of the operator norms is submultiplicative. 

### `exists_norm_sub_le_half`

 Small oscillation. For a cusp kernel `e` and `j ≥ 0` there is `δ₀ > 0` with the following
property. If a bounded continuous function `f` is fixed by `e` and `|f (g v)| ≤ C ‖v‖ ^ j` for all
real `v`, where `‖v‖` is the product over the infinite places of the operator norms, then
`|f (g u) - f g| ≤ C / 2` for the real `u` within `δ₀` of `1`. 

### `exists_norm_le_of_radicalCovered`

 Rapid decay in a cusp. For a cusp kernel `e` and `j ≥ 0` there is `δ₀ > 0` with the following
property. Let `J` be a level, `W` a space, and let `A ≠ 0` be a rational isotropic subspace of it,
spanned by the columns of `X`, with `N_A g ⊆ (Γ ∩ N_A) g Z_δ J` (`New.Space.RadicalCovered`; `N_A`
is the unipotent radical, `Γ` the group of rational points, `Z_δ` the real ball of radius `δ` about
`1`). If a continuous function `f` bounded by `T` is left invariant under `Γ ∩ N_A` and fixed by
`J` and by `e`, then `|f g| ≤ (δ / δ₀) ^ j T`. 

### `exists_cuspFrame_of_height`

 For an open subgroup `J` there is `κ > 0` such that for every space `V` and point `g` there is
`δ > 0` with `δ ^ n = κ / V.height g` and, if `δ ≤ 1` (the height is at least `κ`), a cusp `A` of
size `δ` at `g` whose radical satisfies `N_A g ⊆ (Γ ∩ N_A) g Z_δ J` (`New.Space.RadicalCovered`). 

### `exists_norm_mul_height_pow_le`

 Forms of a fixed level decay uniformly against every power of the height. Let `e` be a cusp
kernel of order `B` (a minimal idempotent on `G_∞` with ‖x‖^(B+1) e(x) integrable, ‖x‖^B e(x)
bounded, and α ∗ e = e for some continuous compactly supported α), `K` an open subgroup of `G_f`,
and `A : ℕ`. Then there is `R` such that every form `F` of type `e` (bounded automorphic, fixed by
right convolution with `e`) that is right `K`-invariant and bounded by `c` has
`‖F g‖ * V.height g ^ A ≤ c * R` for all `g`, where `V.height g` is the reciprocal of the first
minimum, cut off at 1, of `V.move g`. 

### `IsForm.mem_rapidFunctions`

 Let `V` be a hermitian space over the CM field `E`, and let `e` be a cusp kernel of order `B` on
`G_∞`. Such a kernel is a minimal idempotent `e` such that (a) `‖x‖^(B+1) e(x)` is integrable, (b)
`α ∗ e = e` for some continuous compactly supported `α`, and (c) `‖x‖^B e(x)` is bounded, where
`‖x‖ = ∏_w ‖x_w‖`. Then every form `F` of type `e` for `V` (a bounded automorphic function on `G`
fixed by right convolution with `e`) lies in `V.rapidFunctions`, i.e. decays rapidly: `|F|` times
any power of the height is bounded. 

### `finite_levelSpace`

 Let `e` be a cusp kernel of order `B` on the archimedean unitary group `G_∞`: a minimal
idempotent with ‖x‖^(B+1) e(x) integrable, ‖x‖^B e(x) bounded, and α ∗ e = e for some continuous
compactly supported α. Let `K` be an open subgroup of the finite adelic unitary group `G_f`. Then
the forms of type `e` for `V` (bounded automorphic functions fixed by right convolution with `e`)
that are right invariant under `K` make up a finite-dimensional complex vector space. 

### `isForm_realConv`

 Let `e` be a cusp kernel of order `B` on `G_∞`: a minimal idempotent with ‖x‖^(B+1) e(x)
integrable, ‖x‖^B e(x) bounded, and α ∗ e = e for some continuous compactly supported α. Let `F` be
automorphic for `V` (continuous, left `Γ`-invariant, right invariant under an open subgroup of
`G_f`), with `x ↦ e(x) F(g (x, 1))` integrable for every `g`. Then the convolution `realConv e F`,
`g ↦ ∫ e(x) F(g x) dx`, is a form of type `e`: automorphic, bounded, and fixed by right convolution
with `e`. 
