---
{
  "module": "src/Lib/ClassField/Global/AlbertBrauerHasseNoether.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Global/AlbertBrauerHasseNoether.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Global/AlbertBrauerHasseNoether.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Real place symbols, the second inequality and Albert–Brauer–Hasse–Noether

Let `K` be a number field and let `Γ` act as the Galois group of `Ω/K`, where `Ω` (`New.Ω`) is the
algebraic closure of `ℚ`. The first section treats complex conjugations in `Γ` and the symbols of
totally positive elements of `K`. The second section proves the second inequality for a Galois
extension `L / K`; the proof compares Dirichlet densities of primes of degree one. In the last
section `L` is the field cut out by a character `χ` of `Γ`; it treats local norms and Artin symbols,
proves Hasse's norm theorem in prime degree when the real places of `K` stay real in `L` and deduces
the Albert–Brauer–Hasse–Noether theorem.

## Main definitions and results

* `New.IsTotallyPositive.exists_resH2_cyclicClass_eq_zero`: the symbol of a totally positive `x`
  restricts to zero on an open subgroup containing every complex conjugation.
* `New.second_inequality`: for `L / K` Galois, an open subgroup `W` of the finite ideles that
  contains the totally positive principal ideles and the norms from `L` has index at most `[L : K]`.
  Each of its cosets contains the uniformiser idele `ϖ_v` for infinitely many `v` of prime norm
  (`New.frequently_prime_uniformizer_div_mem_of_adeleNorm_mem`).
* `New.exists_hasPrimeDensity_addChar_uniformizer`: the values of a character `f` of the quotient by
  `W` at the `ϖ_v` have mean `1 - m` if `f` is trivial and `-m` otherwise, for some `m : ℕ`.
* `New.exists_localNorm_of_abelianLift_artinAt`: an element of a completion with trivial local
  symbol is a local norm.
* `New.albert_brauer_hasse_noether`: a class in H²(Γ, Ωˣ) is zero if it dies at every finite place
  and over a finite extension in which the real places stay real.

Notions from other files:
* `New.IsProGalois`: a profinite group acts on the Galois extension Ω/K as its Galois group, with
  open stabilisers.
* `New.QZChar.abelianLift`: The homomorphism induced by the continuous character χ on the
  topological abelianisation of Γ, with values in ℚ/ℤ written multiplicatively.
* `New.artinAt`: The local Artin map K_v^× → Γ^ab: the Artin map to the abelianised decomposition
  group of the chosen place above v, followed by the map induced by inclusion.

## Relation to the literature

Known result: Global class field theory, comprising Albert–Brauer–Hasse–Noether, reciprocity,
existence and norms. Only finite ideles are used, with real places handled by total positivity, and
existence is proved only for totally complex fields. Reciprocity starts from cyclotomic characters
of prime conductor, with the auxiliary character chosen by B. H. Neumann's covering lemma. Source:
J. S. Milne, Class Field Theory (v4.03, 2020), VI 4.9, VII 4–9, VIII 4; Tate, Global class field
theory, in Cassels–Fröhlich 1967, ch. VII; H. Hasse, Die Struktur der R. Brauerschen
Algebrenklassengruppe, Math. Ann. 107 (1933) (reciprocity from the sum formula).

See also `Lib.ClassField.Places.LocalFields` and `Lib.ClassField.HeckeL.ContinuationAtOne`.



## Symbols of totally positive elements at the real places

`New.IsComplexConj c` says that `c` acts as complex conjugation under some embedding of `Ω` in `ℂ`.
`New.cyclicClass _ χ w` is the class in `H²` of the cocycle `(g, h) ↦ carry (χ g) (χ h) • w`, which
stands for `δχ ∪ w`. For `w` coming from `x : Kˣ` with coefficients `Ωˣ`, it is the symbol `(χ, x)`.


### `Cohomology.isTotallyPositive_of_isTotallyComplex`

 In a totally complex field `K` every element `x` is totally positive (`New.IsTotallyPositive`:
`φ x > 0` for every ring homomorphism `φ : K →+* ℝ`), since there is no such `φ`. 

### `Cohomology.isReal_comp_algebraMap`

 Let `c` act on `Ω` as complex conjugation under the embedding `j : Ω →+* ℂ` (`hj`). Then `j`
restricted to `K` is a real embedding, since `c` fixes `K`. 

### `exists_isComplexConj`

 If the number field `K` has a real place `w`, some `c` in `Γ` acts on the field `Ω` (`New.Ω`,
the algebraic closure of `ℚ`) as complex conjugation (`New.IsComplexConj`: under some embedding
`j : Ω →+* ℂ`, `j (c • x)` is the complex conjugate of `j x`). 

### `IsComplexConj.mul_self`

 A complex conjugation `c` (`hc`) is an involution, as `Γ` acts faithfully on `Ω`. 

### `IsTotallyPositive.exists_resH2_cyclicClass_eq_zero`

 For a character `χ` of `Γ` and a totally positive `x : Kˣ` there is an open subgroup `U` that
(a) contains every complex conjugation (the real places of `K` stay real in its fixed field)
and (b) on which the symbol `(χ, x) ∈ H²(Γ, Ωˣ)` restricts to zero. Here `Ω` is the field `New.Ω`,
the algebraic closure of `ℚ`, on which `Γ` acts as the Galois group over `K`. 

### `IsComplexConj.false_of_isTotallyComplex`

 A totally complex field `K` has no complex conjugation `c` (`hc`) in `Γ`: it would give a real
embedding of `K`. 

### `IsComplexConj.cyclotomicCharMod_eq_neg_one`

 A complex conjugation `c` (`hc`) inverts the `N`-th roots of unity: the cyclotomic character
mod `N` (`New.cyclotomicCharMod`) is `-1` at `c`. Here `Ω` is the field `New.Ω`, the algebraic
closure of `ℚ`. 

### `IsComplexConj.cyclotomicChar_eq_neg_one`

 The `l`-adic cyclotomic character `New.cyclotomicChar` is `-1` at a complex conjugation `c`
(`hc`). 

 ## The second inequality and equidistribution of primes in norm cosets 

### `New.exists_mul_prod_eq_one`

 Let ψ and finitely many c_i be homomorphisms from a monoid to ℂ, with ψ(x) = 1 whenever no
c_i(x) is −1. Then ψ times the product of some of the c_i is trivial. 

### `New.exists_hasPrimeDensity_addChar_uniformizer`

 Let `W` be an open subgroup of the finite ideles (`hW_open`) containing the principal ideles of
the totally positive elements (`hW_pos`), and `f` a character of the quotient by `W`, written
additively (so `f = 0` is the trivial character). The mean of `f` at the uniformiser ideles
(`New.HasPrimeDensity`, Dirichlet density over the finite places) is `1 - m` if `f = 0` and `-m`
otherwise, for some natural number `m`. 

### `index_re_le_sum_of_hasPrimeDensity`

 Let `L / K` be Galois and `W` an open subgroup of finite index of the finite ideles of `K` that
contains the norms from `L` (`h_norm`). If each character `f` of the quotient by `W` has mean `d f`
at the uniformiser ideles, then the index of `W` is at most `Re (∑ f, [L : K] * d f)`. 

### `hasPrimeDensity_addChar_uniformizer_of_adeleNorm_mem`

 Let `L / K` be Galois and `W` an open subgroup of the finite ideles of `K` (`hW_open`) that
contains the totally positive principal ideles (`hW_pos`) and the norms from `L` (`h_norm`). A
character `f` of the quotient by `W` has mean `1` at the uniformiser ideles if it is trivial
(`f = 0`), and mean `0` otherwise. 

### `index_le_finrank_of_adeleNorm_mem`

 Let `L / K` be Galois and `W` an open subgroup of the finite ideles of `K` (`hW_open`) that
contains the totally positive principal ideles (`hW_pos`) and the norms from `L` (`h_norm`). Then
the index of `W` is at most `[L : K]`. 

### `New.frequently_prime_uniformizer_div_mem_of_adeleNorm_mem`

 Let `L / K` be Galois and `W` an open subgroup of the finite ideles of `K` (`hW_open`) that
contains the totally positive principal ideles (`hW_pos`) and the norms from `L` (`h_norm`). Then
every coset `a W` contains the uniformiser ideles of infinitely many primes `v` of prime norm
`v.q`. 

### `New.second_inequality`

 The second inequality of class field theory, with equidistribution. Let `L / K` be Galois and
`W` an open subgroup of the finite ideles of `K` (`hW_open`) containing the principal ideles of the
totally positive elements (`hW_pos`) and the norms of finite ideles of `L` (`h_norm`). Then (a)
`W` has finite index at most `[L : K]`, and (b) each coset `a W` contains the uniformiser ideles of
infinitely many primes of prime norm: `frequently_prime_uniformizer_div_mem_of_adeleNorm_mem`. 


## Albert–Brauer–Hasse–Noether with a stronger hypothesis at real places

Γ is the Galois group of an algebraic closure Ω of a number field K, and χ is a character of Γ
(`New.QZChar`). L is the field cut out by χ, that is, the fixed field of its kernel. The local
symbol of x at v is `New.QZChar.abelianLift χ (New.artinAt Γ v x)`, and `New.adeleNorm` is the
adelic norm.


### `map_adeleNorm_principalIdele`

 The adelic norm `New.adeleNorm K L` takes the principal idele of `x` in `Lˣ` to the principal
idele of the norm of `x`. 

### `adeleNorm_mem_closure`

 For a finite adele `y` of `L` and a finite place `v` of `K`, the `v`-component of the adelic
norm of `y` is a limit, in the completion of `K` at `v`, of norms of elements of `L`. 

### `abelianLift_artinAt_eq_one_of_mem_closure`

 Let the continuous character χ : Γ → ℚ/ℤ cut out the finite extension L of K, and let K_v be the
completion of K at the finite place v. If a unit u of K_v is a limit in K_v of norms from L to K,
then χ vanishes on the local Artin symbol `artinAt Γ v u`. When `u` is a component of the adelic
norm of a finite idele of L, the hypothesis is `adeleNorm_mem_closure`. 

### `abelianLift_artinMap_adeleNorm`

 The character χ kills the Artin symbol of the norm of every finite idele of the field L that it
cuts out. 

### `exists_localNorm_of_abelianLift_artinAt`

 The kernel of the local symbol consists of local norms. Let L be the field cut out by χ, let w
be a finite place of L over the place v = `w.below K` of K, and let x be a unit of the completion
K_v of K at v with `χ (artinAt Γ v x)` trivial. Then there is a unit y of the completion
`LocField w` of L at w whose local norm to K_v is x. 

### `relIndex_mul_index_sup`

 Let f : E → G be a homomorphism to a commutative group, J, N subgroups of G with f(E)·J = G,
and U = f⁻¹J. Then [G : f(E)(N ∩ J)] · [U : U ∩ f⁻¹N] = [J : J ∩ N]. 

### `relIndex_norm_unit_pow`

 Index of the norms among the `S`-units. Let `L / K` be Galois of prime degree `l`, `S` a finite
set of places of `K` containing the ramified ones such that the principal ideles and the ideles that
are units off `S` generate all ideles (`h_gen`), and `T` the places above `S`. Then
`([E_S : N E_T] * l) ^ (l - 1) * l ^ (#T + r_L) = (l ^ l) ^ (#S + r_K)`, with `[E_S : N E_T]` the
index of the norms of the `T`-units in the `S`-units and `r` the number of infinite places. 

### `isUnramifiedAtInfinitePlaces_of_mem_ker`

 If `χ` kills all complex conjugations, the real places stay real in the field `L` it cuts out:
`L / K` is unramified at the infinite places. 

### `card_range_abelianLift_comp_artinAt`

 Let `L / K` be Galois of prime degree `l`, cut out by `χ`. A finite place `v` of `K` either
splits into `l` places of `L`, and the local symbol `χ ∘ artinAt Γ v` takes one value, or has one
place above it, and the local symbol takes `l` values. In both cases
`#(range of the local symbol) ^ (l - 1) * l ^ #(places above v) = l ^ l`. 

### `localSymbols`

 The tuple of the local symbols `χ ∘ artinAt Γ v` at the places `v` of a finite set `S` of
finite places of `K`, as a homomorphism on the finite ideles of `K`; each symbol takes its values in
its range. 

### `relIndex_ker_localSymbols_pow_mul_pow`

 The local count in Hasse's norm theorem. Let `L / K` be Galois of prime degree `l`, cut out by
`χ`, and let `S` be a finite set of finite places of `K`, with a finite set `T` of places of `L`
above it (`hT`). Then the index `i` of the kernel of the local symbols at `S` in the ideles that
are units off `S` satisfies `i ^ (l - 1) * l ^ #T = (l ^ l) ^ #S`. 

### `exists_map_norm_eq_of_abelianLift_artinAt_eq_one`

 Hasse's norm theorem in prime degree. Let `L / K` be Galois of prime degree, cut out by `χ`, and
let `χ` kill every complex conjugation. If `x` in `Kˣ` has trivial local symbol
`χ (artinAt Γ v x)` at every finite place `v` of `K`, then `x` is the norm of some `z` in
`Lˣ`. 

### `albert_brauer_hasse_noether`

 Albert–Brauer–Hasse–Noether. Let α be a class in H²(Γ, Ωˣ), where Γ acts as the Galois group of
`New.Ω` (the algebraic closure of ℚ) over the number field K. If α restricts to zero on the
decomposition group of every place of Ω over a finite place of K (`h_dec`) and on an open subgroup
U of Γ containing all complex conjugations (`h_conj`, `h_res`: over an extension in which the real
places stay real), then α = 0. 
