---
{
  "module": "src/Lib/Weil/DualPair/ThetaIntegrals.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/ThetaIntegrals.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/ThetaIntegrals.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Terms of theta kernels at rational matrices and basic laws of theta integrals

This file studies the theta kernel `New.pairTheta S T α β f` of a pair of hermitian spaces (S, T)
and the theta integral `New.Exchange.thetaIntegral S T α β f`, which is its integral over `[U(T)]`.
When S is split along an isotropic subspace (`New.Space.Splitting`), the terms of the kernel at
rational matrices are invariant under (x, h) ↦ (γ x, γ h) for rational γ in U(T). Some results
concern data with real part a Fock vector `v`, finite part `y ↦ φ (π y)` at the places `A` (where
`π` reads the components at `A`), and the vacuum elsewhere. For such data the file describes how the
two unitary groups act.

## Main definitions and results

* `New.Space.Splitting.exists_tsum_thetaTerm_le`: the terms are absolutely summable, with moderate
  growth in h.
* `New.Space.Splitting.exists_tsum_thetaTerm_schrodingerOp_le`: under a support condition on Ψ the
  sum of their absolute values is bounded in h.
* `New.Space.Splitting.hasIntegrableTerms_integrated_schrodingerOp`: so this sum is integrable over
  the adelic quotient of U(T) (`New.Space.Splitting.HasIntegrableTerms`).
* `New.Exchange.ReadsAt.pairWeil_localDatum_of_mem_stdLevel`, `New.Exchange.thetaIntegral_pairWeil`:
  how the two unitary groups act.
* `New.Exchange.IsTargetBounded`: a growth bound on the kernel, under which the integral is linear
  in the datum (`New.Exchange.exists_linear_thetaIntegral`) and automorphic
  (`New.Exchange.IsTargetBounded.isAutFunction_thetaIntegral`).
* `New.Exchange.ReadsAt.isTargetBounded`: the bound holds when `F ≠ 0`, `v` has all moments finite
  and `φ` is locally constant of compact support and vanishes off the right invertible matrices.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to the diagonal matrix of its signs at the infinite places and 1 at the finite places.
* `New.𝒮`: The Banach space 𝒮(V) of integrable functions c on 𝔸^n with c(x) = ∫ c(y)β(y,x)e(x−y) dy,
  under the L¹ norm; β is the adelic bicharacter and e the vacuum function `New.vacuumFn`.
* `New.pairWeil`: The action ω_{a,b}(g, h) = a(det h) b(det g)⁻¹ ω(x ↦ hxg⁻¹) on 𝒮(Hom(S, T)).
* `New.Space.integrated`, `New.Space.schrodingerOp`: The operators f ↦ v ⊗ f for a Fock vector v and
  f ↦ Ψ ⊗ f for a function Ψ on finite adelic vectors.

## Relation to the literature

Known; see `Lib.Weil.DualPair.ThetaLiftConvergence` for sources.



## Terms of the theta kernel at rational matrices

Let S be split along an isotropic subspace (`New.Space.Splitting`, with frames k, l and complement
i). For a rational matrix x, `New.Space.Splitting.thetaTerm` is the term θ((ω(g, h) f)[x]) of the
theta kernel of the pair (S, T), where the slice f ↦ f[x] is `New.Space.Splitting.homSlice`.


### `thetaTerm`

 For split S and a rational matrix x, the term θ((ω_{a,b}(g,h)f)[x]) of the theta kernel. Here
f[x] is the slice (`homSlice`) of f over the maps that send the isotropic frame `D.k` to x. 

### `HasIntegrableTerms`

 The function h ↦ ∑ₓ |thetaTerm(g, x, h) · y(h)|, summed over rational matrices x, has finite
integral for the measure `T.quotMeasure` of the adelic quotient of U(T). The weight y is an optional
argument; without it y = 1. 

### `thetaTerm_ratEmbed_mul`

 For a rational point γ of U(T), the term `New.Space.Splitting.thetaTerm` is unchanged when (x,
h) is replaced by (γ x, γ h). 

### `_root_.New.exists_mem_norm_pairWeil_le_mul_height_pow`

 For fixed g there are C and B such that every point h of U(T) has a rational translate γ h with
‖ω(g, γ h)‖ ≤ C ht(h)^B. 

### `exists_tsum_thetaTerm_le`

 Let `D` split `S` over `S₀` and fix g ∈ G E s. There are C and B such that for all f in the data
space 𝒮(Hom(S,T)) and all h ∈ G E s', the sum over rational n' × p matrices x of
|θ((ω_{a,b}(g,h)f)[x])| (`D.thetaTerm T a b f g x h`, with f[x] the slice of f over the maps sending
`D.k` to x) is at most |C| ‖f‖ ht(h)^B in [0, ∞]. Here ht = `T.height` is 1 over the first minimum,
cut off at 1, of T moved by h. 

### `theta_homSlice_rho_ratMap`

 If a rational map `y` from `S` to `T` kills the isotropic frame `D.k`, its Heisenberg operator
does not change the theta functional of the term (`homSlice`) of a rational matrix `x`. 

### `theta_homSlice_rho_ratMap_frame`

 The rational maps `z (c • (D.k | D.i))ᴴ S.J` kill the isotropic frame `D.k`, so their Heisenberg
operators do not change the theta functional of the term of a rational matrix `x`. 

### `_root_.New.Space.exists_smul_col_mem_latticeBall`

 A multiple of a rational matrix `c` by a nonzero integer has its columns in
`(S.move g).latticeBall Z` for some Z: their coordinates at the point of S moved by g are integral
at the finite places and of norm ≤ Z at the infinite places. 

### `_root_.New.Space.coordMatrix_mul_natCast_smul_ne_zero`

 If a nonzero rational column `x` of `T` is paired with a finite adelic map `y` whose restriction
to the columns of `c` at `g` is right invertible after a ring map `φ`, then the pairing (finite part
of `T.coordMatrix k x`)ᴴ · y · (finite part of `S.coordMatrix g (d • c)`) is nonzero for every
nonzero natural `d`. 

### `exists_tsum_thetaTerm_schrodingerOp_le`

 Let `D` split `S` over `S₀`, let `Ψ` be Schwartz–Bruhat above a set `P` of finite places
disjoint from its conjugate, and let `v` be a Fock vector whose moments `fockMoment N v` are all
finite. Suppose that for every y with Ψ y ≠ 0, the product y·c becomes right invertible after a ring
map `φ` from the finite adeles to a nonzero ring, where c is the finite part of the coordinates
g⁻¹x_S⁻¹(k | i) (x_S the point of S) of the frame `(D.k | D.i)` spanning the orthogonal complement
of `D.k`. Then for f = v ⊗ Ψ ⊗ vac = ∫ v(y) ϱ(y)(Ψ⊗ e) dy, with e the vacuum of 𝒮(Hom(S,T)), the sum
over rational n' × p matrices x of |θ((ω_{a,b}(g,k)f)[x])| (`thetaTerm`, f[x] the slice of f over
the maps sending `D.k` to x) is bounded uniformly in k ∈ G E s'. 

### `hasIntegrableTerms_integrated_schrodingerOp`

 Let `D` split `S` over `S₀`, let `Ψ` be Schwartz–Bruhat above a set `P` of finite places
disjoint from its conjugate, and let `v` be a Fock vector whose moments `fockMoment N v` are all
finite. Suppose that whenever Ψ(y) ≠ 0, the product y·c becomes right invertible under a ring map φ:
𝔸_f → R ≠ 0, where c is the finite part of the coordinates g⁻¹x_S⁻¹(k | i) of the frame
`(D.k | D.i)`. Then for f = v ⊗ Ψ ⊗ vac = ∫ v(y) ϱ(y)(Ψ⊗ e) dy (e the vacuum of 𝒮(Hom(S,T))), the
function h ↦ ∑_ξ |θ((ω_{a,b}(g,h)f)[ξ])| has finite integral over the adelic quotient of U(T)
(`HasIntegrableTerms`), with ξ over rational n' × p matrices and f[ξ] the slice of f over the maps
sending `D.k` to ξ. 


## The theta integral: group actions, linearity and automorphy

`New.Exchange.IsSchwartzVector v` says that all moments of the Fock vector `v` are finite.
`New.schwartzBruhat U` is the space of locally constant functions with compact support that vanish
outside `U`.


### `map_evalPlaces_eq_atPlaces`

 The components at `P` of the matrix of `g`, entry by entry, form `atPlaces P g`. 

### `transpose_map_star_eq_atPlaces_inv`

 The components at `P` of the conjugate transpose of `g` are those of `g⁻¹`. 

### `atPlaces_star`

 The components at `P` of the conjugate transpose of `g` are those of `g⁻¹`. The components of
`g` at `P` form `atPlaces P g`. 

### `ReadsAt.isSchwartzBruhat`

 If `π` reads the components at `A` and `φ` is locally constant of compact support and
vanishes outside `U`, then `y ↦ φ (π y)` is Schwartz–Bruhat above `A`. 

 ### A growth bound, and linearity of the theta integral 

### `thetaLarge`

 The theta integral over [U(T)] of the datum `localDatum` with real part `v`, the function `Φ`
at the ramified places `𝔠.ramifiedPlaces` of the split tame character `𝔠`, and the vacuum elsewhere;
both characters are `rankTwist 𝔠.character⁻¹ n`, that is ν⁻¹υ^⌊n/2⌋ with n = rk S and υ restricted
to the norm-one ideles. 

### `IsTargetBounded`

 There are B and C with |θ^{S,T}_{α,β}(f)(g,h)| ≤ C·ht(g)^B for all characters α, β and all
g, h: polynomial growth in g, uniformly in h. 

### `exists_linear_thetaIntegral`

 On the data that satisfy `New.Exchange.IsTargetBounded` the theta integral agrees with a linear
map. 

### `instance : Nontrivial (LocProd 𝔠.ramifiedPlaces)`

 The product of the local fields at the nonempty set `𝔠.ramifiedPlaces` is nontrivial. 

 ### The action of the two unitary groups 

### `ReadsAt.pairWeil_localDatum_of_mem_stdLevel`

 Let `π` read the components at `A` and `φ` be locally constant of compact support. The datum
`localDatum S T v φ r` has real part `v`, finite part `y ↦ φ (π y)` at the places of `A` and the
vacuum elsewhere. A pair `(g, h)` of finite elements that stabilise the standard lattices moves
`φ` to `x ↦ φ (π(h⁻¹) * x * π(g))`, up to the scalar `α(det h) · β(det g)⁻¹`. 

### `thetaIntegral_pairWeil`

 Acting on the datum by a pair `p` translates the theta integral on the right by `p.1`; the
component `p.2` in the group integrated over has no effect. 

 ### Automorphy, and data that satisfy the growth bound 

### `IsTargetBounded.isAutFunction_thetaIntegral`

 Under `New.Exchange.IsTargetBounded` the theta integral is continuous and left invariant under
the rational points. 

### `ReadsAt.isTargetBounded`

 Let `π` read the components at `A` in a ring `F ≠ 0`. If `v` has all moments finite and `φ` is
locally constant of compact support and vanishes off the right invertible matrices, then the datum
`localDatum S T v φ r` (real part `v`, `y ↦ φ (π y)` at `A`, the vacuum elsewhere) satisfies
`New.Exchange.IsTargetBounded`. 
