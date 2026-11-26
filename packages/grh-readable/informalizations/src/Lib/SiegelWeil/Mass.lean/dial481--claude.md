---
{
  "module": "src/Lib/SiegelWeil/Mass.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Mass.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Mass.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Masses of definite hermitian lattices and ideal zeta bounds for adelic Gauss sums

The mass `New.mass E l` is the sum of `1 / #Aut` over the double cosets `Γ \ G_f / K₀` of the
definite space `New.stdSpace E (Fin l)`. Here `G_f` is the unitary group over the finite adeles, `Γ`
(`New.stdRatPoints`) its rational points, `K₀` (`New.stdLevel`) the stabiliser of the standard
lattice, and `New.classSum` the weighted sum over these double cosets. If `E` is stably unramified,
the class sum in rank `j + 1` of the number of vectors of norm `1` is the mass in rank `j`. The file
also bounds adelic Gauss sums, integrated over the characters, by a value of the ideal zeta function
of a ring.

## Main definitions and results

* `New.classSum_card_norm_one_eq_mass`: let `E` be stably unramified (`New.HasPrimitiveRoot5040`:
  `E` contains a primitive root of unity of order `5040`, so it is unramified over its maximal real
  subfield at all finite places). Then the class sum in rank `j + 1` of the number of lattice
  vectors of norm `1` is the mass in rank `j`.
* `New.idealZeta`: the sum ζ_R(s) of [R : I]^(−s) over the ideals I of finite index of a ring R.
* `New.lintegral_le_idealZeta_mul`: let ζ_R(μ) ≤ 2. An integral is at most ζ_R(μ)·V if almost every
  point x of the domain lies in some set S(I), for an ideal I of finite index, with
  [R : I]^μ · f(x) · (measure of S(I)) ≤ V, for the integrand f.
* `New.lintegral_gauss_sum_le_idealZeta`: if ζ_Ô(μ) ≤ 2 and 2(μ + 1) ≤ n, the integral over b of
  |∫_{Ô^n} ψ_f(b(w*w − Γ)/2) dw| is at most ζ_Ô(μ)·vol(Ô^n).

Notions from other files:
* `New.stdSpace`: the definite space `I_n`, the sum of `n` norms with its standard lattice.

## Relation to the literature

Part of a known result, the mass formula for unimodular hermitian lattices: masses in consecutive
ranks are compared through the class sums of norm one vectors. See
`Lib.SiegelWeil.OneVector.SiegelClassSum`.

Part of a known result, Siegel's formula for representing a number by a hermitian form, with
bounds on the local densities: the Gauss sums are bounded at all finite places at once, by sorting
the characters by their conductor ideal. See `Lib.SiegelWeil.OneVector.SiegelClassSum`.



## Positivity of masses and class sums of norm one vectors

Both class sums are computed by `New.classSum_card_orbit`, the second with Witt's theorem.


### `mem_stdRatPoints_iff`

 An element `g` of the finite adelic unitary group lies in `stdRatPoints`, the image of the
unitary group over `E`, if and only if all its matrix entries come from `E`. 

### `classSum_stdRatPoints_eq_mass`

 For a finite type `κ`, the class sum of `1` over the rational points of the standard definite
space of basis `κ` and the stabiliser `stdLevel E κ` of its standard lattice is the mass in rank
`card κ`, the class sum of `1` for the basis `Fin (card κ)`. 

### `mass_pos`

 For a CM field `E` and every `l`, the mass `mass E l` of the genus of `O_E^l` is positive. This
mass is the sum of `1/#(Γ ∩ g K₀ g⁻¹)` over the classes `Γ g K₀` in the finite adelic unitary group
of rank `l`, where `Γ` is the image of `U_l(E)` and `K₀` the stabiliser of `Ô^l`. 

### `normOneLatticeVectors`

 The vectors of norm `1` in the lattice of `g`: the `y` in `E^κ` with `star y ⬝ᵥ y = 1` that
`g⁻¹` maps into the integral lattice `Ô^κ`, for a finite adelic unitary matrix `g`. 

### `replicateCol_gram_eq_one`

 A vector of norm `1` is a column with Gram matrix `1` for the standard form. 

### `exists_mulVec_eq_of_star_dotProduct_eq_one`

 Witt's theorem for vectors: the unitary group over `E` moves any vector of norm `1` to any
other. 

### `exists_mem_stdLevel_mulVec_eq_of_norm_one`

 Witt's theorem for integral vectors, with `E` stably unramified: the stabiliser `stdLevel E κ`
of the standard lattice moves any integral vector of norm `1` to any other. 

### `image_normOneLatticeVectors_eq_orbit_inter`

 Let `e` be the last basis vector of `E^(j+1)` and `g` a finite adelic unitary matrix, with `E`
containing a primitive root of unity of order `5040` (`HasPrimitiveRoot5040`). The vectors of norm
`1` in the lattice of `g` (`normOneLatticeVectors`) have as image in the adelic vectors
`Γ e ∩ g K₀ e`, for the rational points `Γ` and the stabiliser `K₀` of the standard lattice. 

### `classSum_card_norm_one_eq_mass`

 Let `E` be a CM field containing a primitive root of unity of order `5040`
(`HasPrimitiveRoot5040`). Let `Γ` be the image of the rational unitary group `U_{j+1}(E)` in the
finite adelic unitary group `G_f`, and let `K₀ = stdLevel` be the stabiliser of the standard lattice
`Ô^(j+1)`. Summing over the double cosets `Γ g K₀`, with weights `1 / #(Γ ∩ g K₀ g⁻¹)`, the number
of `y` in `E^(j+1)` with `star y ⬝ᵥ y = 1` and `g⁻¹ y ∈ Ô^(j+1)` (`normOneLatticeVectors`) gives
`mass E j`, the same weighted count of classes in rank `j`. 


## Ideal zeta functions and integrals of adelic Gauss sums

`New.Ô` is the ring of integral finite adeles, `New.stdLattice` the lattice Ô^n, `New.ψf` the
standard additive character, and `New.volÔ` the volume of Ô.


### `idealZeta`

 The ideal zeta sum ∑ [R : I]^(−s) over the ideals I of finite index in R, for a natural
number s, with values in [0, ∞]. 

### `le_two_of_pow_le_ofReal`

 A number whose positive power is at most `1 + 2⁻¹ ^ e` is at most `2`. 

### `lintegral_le_idealZeta_mul`

 Summation over ideals: let `idealZeta R μ ≤ 2`. If almost every `x` in `s` lies in a set
`S I`, `I` an ideal of finite index, with `[R : I] ^ μ * f x * ρ (S I) ≤ V`, then the integral of
`f` over `s` is at most `idealZeta R μ * V`. 

### `characterKernel`

 The group of finite adeles `r` such that the character `v ↦ ψ_f(b r v)` of `Ô` is trivial. 

### `isOpen_characterKernel`

 The group `characterKernel b` of the `r` for which `v ↦ ψ_f(b r v)` is trivial on `Ô` is open:
it contains the preimage of `Ô` under multiplication by `b`. 

### `conductorIdeal`

 The largest ideal of `Ô` on which the character `v ↦ ψ_f(b v)` is trivial. 

### `cardQuot_conductorIdeal_ne_zero`

 The conductor ideal of a finite adele `b`, the largest ideal of `Ô` on which `v ↦ ψ_f(b v)` is
trivial, has finite index. 

### `gauss_sum_sq_le`

 Let `E` be a CM field. Take a self-adjoint finite adele `b`, a finite adele `Γ`, and
`I = conductorIdeal b`, the largest ideal of `Ô` on which `v ↦ ψ_f(b v)` is trivial. Then the Gauss
sum `G = ∫_{Ô^n} ψ_f(b (w* w - Γ) / 2) dw` satisfies
`[Ô : I] ^ card n * |G| ^ 2 ≤ (volÔ ^ card n) ^ 2`, where `ψ_f` is the standard additive character
of the finite adeles and `volÔ = 2^{r₂}/√|disc E|`. 

### `lintegral_gauss_sum_le_idealZeta`

 Let `E` be a CM field, and let `ζ_Ô(μ) = idealZeta (Ô E) μ = Σ_I [Ô : I]^(−μ)`, summed over the
ideals `I` of finite index in `Ô`. If `ζ_Ô(μ) ≤ 2` and the rank `card n` is at least `2 (μ + 1)`,
then for every finite adele `Γ` the lower integral over the self-adjoint finite adeles `b` (for the
volume under which each coset of `selfAdjointCodifferent E 1` has measure one) of
`|∫_{Ô^n} ψ_f(b (w* w - Γ) / 2) dw|` is at most `ζ_Ô(μ) · volÔ ^ card n`. Here `ψ_f` is the standard
additive character and `volÔ = 2^{r₂}/√|disc E|`. This is the convergence bound for the finite part
of the singular series. 

### `idealZeta_intAdeles_pow_le`

 For a number field `E` and natural numbers `u, v, n` with `n · [E : ℚ] ≤ 2^v`, the `n`-th power
of the ideal zeta sum `idealZeta (Ô E) (u + v + 4) = Σ_I [Ô : I]^(−(u+v+4))` is at most
`1 + 2^(−u)`. The sum runs over the ideals `I` of finite index in the integral finite adeles `Ô` of
`E`. 
