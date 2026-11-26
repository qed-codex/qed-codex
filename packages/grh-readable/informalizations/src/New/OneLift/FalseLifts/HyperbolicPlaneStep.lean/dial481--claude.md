---
{
  "module": "src/New/OneLift/FalseLifts/HyperbolicPlaneStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/HyperbolicPlaneStep.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/HyperbolicPlaneStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Vanishing of theta descents from W to W plus hyperbolic planes

`New.SiegelWeil.DescentsVanish W V a S Y` says that all theta descents of a function `Y` on
`U(V)(𝔸)` to `U(W)(𝔸)` vanish. The descents are twisted by the character `a` of `U(1)`, with data
that are the vacuum at the places of `S` and their conjugates. This file proves the inductive step
`New.SiegelWeil.descentsVanish_add_planes`: the vanishing passes from `W` to `W'`, the sum of `W`
and hyperbolic planes, each plane multiplying `a` by `New.WeilData.upsilonU1`. This holds when `V`
is definite of large rank and `Y` is killed by a Hecke polynomial at a suitable point.

## Main definitions and results

* `New.SiegelWeil.descentsVanish_add_planes`: The inductive step of the tower of descents.
* `New.SiegelWeil.eq_zero_of_heckePolyOp_eq_zero`: Small roots: let `F` be a bounded function on
  the adelic unitary group of signs `t`, of rank `card m`, that is spherical at the split place
  `w` of norm `q`. If the Hecke polynomial at `w`, taken at a point `X` with
  `q ^ (card m + 1) * |X| ≤ 1`, kills `F`, then `F` is zero.

## The steps of the argument

* The inductive step `New.SiegelWeil.descentsVanish_add_planes`: the zero term contributes nothing
  (`New.SiegelWeil.DescentsVanish.integral_homSlice_eq_zero`), the rest is bounded
  (`New.SiegelWeil.exists_norm_theta_sub_zeroTerm_le`), the descent inherits a Hecke equation
  (`New.SiegelWeil.lift_eq_zero_of_heckePolyOp_eq_zero`), and its root is too small
  (`New.SiegelWeil.eq_zero_of_heckePolyOp_eq_zero`).

Notions from other files:
* `New.pairWeil`: the Weil representation of U(W) × U(V) on the data space 𝒮(Hom(W, V)), twisted by
  two characters of U(1); `New.Space.θ` is the theta functional on that space.
* `New.Space.projOn`: the projection whose fixed vectors are the data that are the vacuum at the
  places of a set `S` and their conjugates. For `S` the complement of the places of the level and
  their conjugates, these are the test vectors.
* `New.heckePolyOp`: the operator ∑ (−X)^i q^(i choose 2) T_{w,i}, q the order of the residue field
  at w; `New.sphericalAt π w` is the space of vectors spherical at w.
* `New.Space.Splitting`: `D : W'.Splitting W p` writes `W'` as `W` plus `card p` hyperbolic planes,
  with isotropic frame `D.k`; it is adapted (`IsBaseAdapted D`) if its adelic frames are orthonormal
  at the infinite and integral at the finite places. `D.homSource V` is the splitting of
  `Hom(W', V)` that it induces, `D.zeroTerm` is the constant term along the isotropic frame, and the
  slice `D.homSlice V x` is the zero term of the translate by `x`, a datum on `Hom(W, V)`.

## Relation to the literature

See `New.OneLift.FalseLifts.PeriodsOfFalseLifts` for related work.


### `eq_zero_of_heckePolyOp_eq_zero`

 Small roots: let `F` be a bounded function on the adelic unitary group of signs `t`, of rank
`card m`, that is spherical at the split place `w` of norm `q`. If the Hecke polynomial at `w`,
taken at a point `X` with `q ^ (card m + 1) * |X| ≤ 1`, kills `F`, then `F` is zero. 

### `lift_pairThetaKer_swap_apply`

 The descent of a function `Y` on `U(T)(𝔸)` to `U(S)(𝔸)` by the datum `φ` is the integral of `Y`
against the theta kernel of `φ` over the adelic quotient of `U(T)`. 

### `projOn_homSlice_zero`

 Let `D` be an adapted splitting of `W'` into `W` and hyperbolic planes: its adelic frames are
orthonormal at the infinite and integral at the finite places. If the datum `φ` on `Hom(W', V)` is
the vacuum at the places of `S`, then so is its slice `D.homSlice V 0 φ`, a datum on `Hom(W, V)`,
namely the zero term of `φ` along the isotropic frame. 

### `DescentsVanish.integral_homSlice_eq_zero`

 Let `D` split `W'` into `W` and `card p` hyperbolic planes, with adelic frames that are
orthonormal at the infinite and integral at the finite places (`IsBaseAdapted`). Suppose that the
integral of `Y` over the adelic quotient of `U(V)` against the theta kernel of the pair `W, V`,
twisted by `a (det h)`, is zero for every datum that is vacuum at `S` (`DescentsVanish`). Then for
such a datum `φ` on `Hom(W', V)` and every `g` in `U(W')(𝔸)`, the integral of `Y` against the zero
term of the kernel of `φ` is zero. 

### `norm_theta_sub_zeroTerm_le`

 Let `D` split one hyperbolic plane off `W'`, with isotropic vector `k`. The induced splitting
`D.homSource V` of `Hom(W', V)` has the adelic frame `kAdelic`, and `ϱ` is the action of
translations on data. The theta functional minus its zero term along that frame is, at `φ`, the
mean over `b` of `θ φ - θ (ϱ (kAdelic b) φ)`, so a bound `B` for these differences bounds it. 

### `theta_sub_zeroTerm_rho_ratMap`

 Let `D` split one hyperbolic plane off `W'`, with isotropic vector `k`. The theta functional
minus its zero term along `k` is invariant under the translations by the rational maps
`z kᴴ J`, where `J` is the matrix of `W'`. 

### `exists_col_k_mem_latticeBall`

 Let `D` split one hyperbolic plane off `W'`, with isotropic vector `k`. The height of a point
`g` is the inverse of the first minimum, cut off at `1`, of the space moved by `g` (`W'.move g`).
For every point `g` there is a rational `γ` such that, if that height exceeds `2`, then `k` lies in
the lattice of the space moved by `γ g` and has length at most `2 / height g` there. 

### `subspaceMean_theta_sub_zeroTerm_eq_zero`

 Let `D` split one hyperbolic plane off `W'`, with isotropic vector `k`, and let the columns `dⱼ`
of `d` be a basis of `V`. Let `θ₀` be the zero term of the theta functional `θ` along the isotropic
frame of `D.homSource V`, the splitting of `Hom(W', V)` induced by `D`, and let `ϱ` be the action by
translations on data. Then the mean of `(θ - θ₀) (ϱ u φ)` over the adelic points `u` of the span of
the maps `dⱼ ⟨k, ·⟩` (`rankOneMaps`), modulo the rational ones, is zero. 

### `exists_norm_theta_sub_zeroTerm_le`

 Let `D` split one hyperbolic plane off `W'`, and let `φ = v_P ⊗ Ψ ⊗ vac` be the datum made of
the Fock vector of a polynomial `P`, a function `Ψ` that is Schwartz–Bruhat at a set `A` of finite
places disjoint from its conjugate, and the vacuum at the other places. Twist the theta kernel by
`χ (det h)`, for any automorphic character `χ` of `U(1)`. After a rational translation `γ` of
`g ∈ U(W')(𝔸)`, the kernel of `φ` minus its zero term along the isotropic frame is bounded
uniformly in `g` and in `h ∈ U(V)(𝔸)`. 

### `DescentsVanish.bddAbove_lift`

 Let `D` be an adapted splitting of `W'` into `W` and one hyperbolic plane, and let `A` be a set
of finite places disjoint from its conjugate. If the descents of the automorphic function `Y` to
`W`, twisted by the character `a`, vanish for the data that are the vacuum off `A` and its
conjugate, then the descent of `Y` to `W'` by a datum `v_P ⊗ Ψ ⊗ vac` is bounded. This datum is the
vacuum `vacElem`, acted on by the function `Ψ`, Schwartz–Bruhat at `A` (`schrodingerOp`), and by the
Fock vector `v_P` of the polynomial `P` (`integrated`). 

### `norm_frobValue`

 The value `χ.frobValue m w`, which is `q ^ (card m / 2)` times the value at a uniformiser at
`w` of the Hecke character of `χ` for rank `card m`, has modulus `√q ^ card m`. 

### `qPochhammer_ne_zero`

 The product `∏_{i<k} (1 - q^i X)` is not zero if `1 < q` and `q^k |X| ≤ 1`. 

### `lift_eq_zero_of_heckePolyOp_eq_zero`

 Let the automorphic function `Y` be spherical at the split place `w` and killed by the Hecke
polynomial at `X`. Let the base change of `χ` be unramified and the datum `φ` vacuum at `star w`.
Let `W'` have rank `card m` and `V` rank `card m + k`. If `|X|` is at most `q^(-k - card m/2)` and
`q^(-card m - 1 - k/2)`, and the descent of `Y` to `W'` by `φ` (`lift` by the theta kernel
`pairThetaKer` twisted by `χ`) is bounded, then that descent is zero. 

### `DescentsVanish.of_isEmpty`

 With no plane to split off, the zero term is the whole kernel: if `W'` splits over `W` along an
empty frame and the descents of `Y` to `W` vanish, then so do those to `W'`. 

### `descentsVanish_add_planes`

 Let `Σ` consist of the places of `A` and their conjugates, and let the descents of the
automorphic function `Y` to `W`, twisted by the character `a`, by data that are vacuum off `Σ`
vanish. Let `w` be a split place off `Σ` with the base change of `a` unramified at `star w`. Let `Y`
be spherical at `w` and killed by the Hecke polynomial at a point `X` of modulus
`q^(1 - t' - r'/2)`, where `r'` is the rank of `W` and `r' + t'` that of `V`. If `W'` is `W` plus
`l = card p` hyperbolic planes and `r' + 2 l + 3 < t'`, then the descents of `Y` to `W'` twisted by
`a * upsilonU1 ^ l` vanish, with `upsilonU1` the restriction of the character `υ` of the Weil data
to norm-one ideles. 
