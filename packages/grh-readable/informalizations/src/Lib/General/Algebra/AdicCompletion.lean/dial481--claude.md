---
{
  "module": "src/Lib/General/Algebra/AdicCompletion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/AdicCompletion.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/AdicCompletion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Adic completeness: p-adic tools, extension by continuity, topological bases

This file collects tools on adic completeness over a commutative ring. It covers normed fields over
`ℚ_[p]`, divisibility by powers of an element `π`, maps of adic completions, monoid actions by ring
endomorphisms, extension of linear maps by adic continuity, and topological bases. In the results on
topological bases, `I` is an ideal of `S`, often `I = (p, z)`, and `M` is an `S`-module. For
`c : New.Lift.AdicBasis I M`, the `c.b i` are its vectors and the `c.coord i` its coordinate forms.

## Main definitions and results

* `New.shiftDiff`: the operator `(x_j) ↦ (x_j - π x_{j+1})` on sequences. By
  `New.isPrecomplete_of_shiftDiff_surjective`, if it is onto for `π = x` and for `π = y`, then
  `(x, y)`-adic Cauchy sequences converge.
* `New.Adic.ringHom_ext_of_approx`: two ring maps `F`, `G` from `A` to a `p`-adically separated ring
  are equal if every element of `A` is congruent, modulo each power of `p`, to an element on which
  they agree.
* `New.adicMap`: a ring map that carries `I` into `J` induces a map of adic completions.
* `New.exists_adic_extension`: a linear map `g` into an `I`-adically complete module extends along a
  map `β` with dense image, if `β f ∈ I ^ (n + n) • ⊤` implies `g f ∈ I ^ n • ⊤` for all `n`.
* `New.Lift.exists_adicBasis`: an `I`-adic topological basis of `M` over `S` exists when
  `I = (p, z)` is maximal, `S` is `I`-adically complete, `p` is zero or injective on `M`, and `z` is
  injective on `M / p M`. It may be taken to contain given vectors independent modulo `I M`.
* `New.free_finite_of_rank_le`: over a ring `S` that is complete for a maximal ideal `(p, z)`, a
  separated module of finite rank on which `p, z` behave as a regular sequence (or `p = 0` and `z`
  is regular) is finite and free. The proof uses the topological basis of
  `New.Lift.exists_adicBasis`.

Notions of this file:
* `New.Lift.AdicBasis`: a topological basis of `M` over `S` for the `I`-adic topology: vectors `b i`
  whose finite combinations are dense, with linear forms `coord i` on `M` that read off the
  coefficients of a finite combination.

## Relation to the literature

Known; see `Lib.PadicComparison.Completion` for sources.



## p-adic normed fields and divisibility by powers of π

* `New.PadicField`: normed fields over `ℚ_[p]`. `New.norm_p_eq_inv` gives the norm of `p` there,
  and `Nat.Coprime.norm_natCast_eq_one` that of natural numbers prime to `p`.
* `New.valRingCp`: the ring of integers of `ℂ_p`, a valuation ring with fraction field `ℂ_p`.
* `New.pow_dvd_of_map`, `New.smodEq_span_pow_iff_dvd`, `New.eq_of_forall_pow_dvd_sub`,
  `New.isUnit_of_dvd_sub`: divisibility by powers of `π`, and its use in `π`-adically separated or
  complete rings.


### `ThePrime`

 The statement that p is prime, as a class that fixes the prime p in scope. 

 ### Normed fields over `ℚ_[p]` 

### `PadicField`

 A normed field F that is a normed algebra over Q_p, not necessarily complete; the prime p is
read off from F (an `outParam`). 

### `PadicIso`

 For a prime ℓ, a choice of ring isomorphism ιℓ from ℂ to the algebraic closure of Q_ℓ. 

### `PadicIso.ιℓ`

 A ring isomorphism from ℂ to the algebraic closure of ℚ_ℓ. 

### `PadicPlace`

 A p-adic place of ℂ: a choice of ring homomorphism ιₚ from ℂ to C_p. 

### `PadicPlace.ιₚ`

 A ring homomorphism from ℂ to ℂ_p. 

### `valRingCp`

 The ring of integers of `ℂ_p`: the elements of norm at most one. It has the same elements as
Mathlib's `PadicComplexInt p`; here membership is the inequality `‖x‖ ≤ 1` by definition. 

### `_root_.Nat.Coprime.norm_natCast_eq_one`

 A natural number prime to `p` has norm one in every normed field over `ℚ_[p]`. 

 ### Divisibility by powers and adic completeness 

### `pow_dvd_of_map`

 Let T map a commutative ring R to a commutative ring S with T(πa) = ϖT(a) for all a. Let ϖ be a
non-zero-divisor, and let ϖ ∣ T(a) imply π ∣ a for all a. Then ϖ^n ∣ T(x) implies π^n ∣ x. 

### `smodEq_span_pow_iff_dvd`

 In a commutative ring, x and y are congruent modulo the submodule (π)^n of the ring if and only
if π^n divides x − y. 

### `eq_of_forall_pow_dvd_sub`

 In a ring that is separated for `(π)`, two elements congruent modulo every power of `π` are
equal. 

### `isUnit_of_dvd_sub`

 In a ring that is complete for `(π)`, an element congruent to a unit modulo `π` is a unit. 

### `isAdicComplete_over_base`

 An `S`-algebra that is `p`-adically complete as a ring is `p`-adically complete as an
`S`-module. 

### `shiftDiff`

 The operator `(x_j) ↦ (x_j - π x_{j+1})` on sequences in an `R`-module `N`. 

### `isPrecomplete_of_shiftDiff_surjective`

 Let R be a commutative ring with elements x and y. Write `shiftDiff R π` for the operator
(a_j) ↦ (a_j − π a_{j+1}) on sequences in R. If it is surjective for π = x and for π = y, then R
is precomplete for the ideal (x, y): every (x, y)-adic Cauchy sequence has a limit. 

 ## Ring maps to a p-adically separated ring that agree on a dense set 

### `New.Adic.ringHom_ext_of_approx`

 Let `F` and `G` be ring maps from `A` to a `p`-adically separated ring `R`. If every element of
`A` is congruent, modulo each power of `p`, to an element on which `F` and `G` agree, then
`F = G`. 


## Maps of adic completions and monoid actions by ring endomorphisms

* `New.PrincipalCompletion R π`: the `π`-adic completion of a ring `R`.
* `New.Adic.pow_dvd_iff_evalₐ_eq_zero`, `New.Adic.exists_approx`, `New.Adic.pow_dvd_iff`,
  `New.Adic.eq_zero_of_forall_pow_dvd`: the `π`-adic completion of `R` in terms of divisibility by
  powers of `π`.
* `New.actionOfHoms`, `New.extendAction`, `New.locAction`, `New.wittAction`: an action of a monoid
  `M` by ring endomorphisms, from a multiplicative family, and its extension along a ring map, to a
  localisation and to Witt vectors.


### `adicMap`

 For a ring homomorphism f: R → S carrying the ideal I into J, the induced ring homomorphism
from the I-adic completion of R to the J-adic completion of S. 

### `evalₐ_adicMap`

 For a ring map `f : R → S` carrying the ideal `I` into `J`, the component of `adicMap f h x` in
`S / J ^ n` is the image of the component of `x` in `R / I ^ n`. 

### `adicMap_algebraMap`

 For a ring map `f : R → S` carrying `I` into `J`, the induced map `adicMap f h` of adic
completions sends the image of `x : R` to the image of `f x`. 

 ### Actions of a monoid by ring endomorphisms 

### `actionOfHoms`

 The action of a monoid M on a ring B by ring endomorphisms given by a family f(m) with f(1)
the identity and f(ab) = f(a)∘f(b). 

### `extendAction`

 The M-action on B given by endomorphisms f(m) compatible with the action on R along i: R →
B, when endomorphisms of B are determined on the image of i. 

### `locAction`

 The action of M on the localisation B of R away from x extending the action on R, given that
each m sends x to an element invertible in B. 

### `instance (priority`

 A ring action of `M` on `R` induces an action of `M` on the Witt vectors `WittVector p R`. Each
element acts by mapping Witt vector coordinates through its ring endomorphism of `R`. 

### `smul_algebraMap_eq_algebraMap_smul`

 Let `M` act on `A` and on the `A`-algebra `R`. If `m • (a • r) = (m • a) • (m • r)`, then the
algebra map `A → R` is equivariant. 

### `smulDistribClass_of_tower`

 In a tower `A → B → R` with actions of `M`, if the actions on `A` and `B` are compatible and
the map `B → R` is equivariant, then the actions on `A` and `R` are compatible. 

### `PrincipalCompletion.`

 The `π`-adic completion of a ring `R`: its completion at the principal ideal `(π)`. 

 ### The completion at a principal ideal 

### `pow_dvd_iff_evalₐ_eq_zero`

 For an element `π` of a commutative ring `R`, an element `x` of the `π`-adic completion
(`PrincipalCompletion R π`, that is `AdicCompletion (span {π}) R`) is divisible by the image of
`π ^ n` if and only if its image in `R / π ^ n` is zero. 

### `exists_approx`

 Every element of the `π`-adic completion is congruent modulo `π ^ n` to an element of `R`. 

### `pow_dvd_iff`

 For elements `π` and `y` of a commutative ring `R`, the image of `y` in the `π`-adic completion
`PrincipalCompletion R π` is divisible by the image of `π ^ n` if and only if `π ^ n ∣ y` in
`R`. 

### `isSMulRegular_completion`

 Let `X` be a module over a commutative ring `R`. If a natural number `n` acts injectively on
`X`, then it acts injectively on the `n`-adic completion of `X`. 


## Extension by adic continuity and topological bases over a (p, z)-adic ring

The basis of `New.Lift.exists_adicBasis` lifts a basis of `M / I M`. By
`New.comap_span_pow_smul_le`, used twice, a combination that lies in `(p ^ n, z ^ n) M` has its
coefficients in `(p ^ n, z ^ n)`. This gives continuity.


### `isHausdorff_of_injective_pi`

 A module that embeds linearly in a product of copies of an `I`-adically separated module is
`I`-adically separated. 

### `isAdicComplete_of_free`

 A finite free module over an `I`-adically complete ring is `I`-adically complete. 

### `exists_adic_extension`

 Let C be I-adically complete, β: F → M have I-adically dense image, and g: F → C satisfy
g(f) ∈ I^n C whenever β(f) ∈ I^{2n} M. Then g = G ∘ β for some S-linear G: M → C. 

### `mem_span_pair_smul_top`

 An element lies in `(a, b) M` if and only if it has the form `a • u + b • v`. 

### `comap_span_pow_smul_le`

 Let `β : F → M` be linear. Suppose that `β x ∈ (a, t) M` implies `x ∈ (a, t) F`, and that
`t • y ∈ a M` implies `y ∈ a M` or `t = 0`. Then `β x ∈ (t ^ n, a) M` implies
`x ∈ (t ^ n, a) F`. 

### `eq_zero_or_exists_pow_smul_eq`

 Suppose that `z • a ∈ p M` implies `a ∈ p M`, and that `p` is zero or acts injectively on `M`.
If `p • y ∈ z ^ n M`, then `p = 0` or `y ∈ z ^ n M`. 

### `Lift.AdicBasis.`

 A topological basis of `M` over `S` for the `I`-adic topology: vectors `b i` whose finite
combinations are dense, with linear forms `coord i` on `M` that read off the coefficients of a
finite combination. 

### `Lift.AdicBasis.Index`

 The index set of the basis. 

### `Lift.AdicBasis.b`

 The basis vectors in `M`. 

### `Lift.AdicBasis.coord`

 The coordinate forms. 

### `Lift.AdicBasis.dense`

 Finite combinations of the vectors `b i` are dense for the `I`-adic topology. 

### `Lift.AdicBasis.dual`

 The `i`-th coordinate form reads off the `i`-th coefficient of a finite combination. 

### `Lift.exists_adicBasis`

 Let `S` be `I`-adically complete for a maximal ideal `I = (p, z)`. Suppose that `z` is regular
on `M / p M` and that `p` is zero or regular on `M`. Then every set `t ⊆ M` whose elements have
linearly independent images in the `S / I`-vector space `M / I M` lies in the range of an `I`-adic
basis `c` of `M`. Such a basis is a family `c.b` whose finite `S`-combinations are `I`-adically
dense in `M`, with linear forms `c.coord i` on `M` that read off the coefficients of any finite
combination. 

 ## Finite freeness from a bound on the rank 

### `New.free_finite_of_rank_le`

 Let `S` be complete for the maximal ideal `I = (p, z)`, and let `M` be an `I`-adically separated
`S`-module of finite rank. Suppose that `p` is zero or acts injectively on `M` (`hp`), and that `z`
acts injectively on `M / p M` (`hz`). Then `M` is free and finitely generated. 


## The subgroup nX of multiples and the p-adic filtration

`New.Period.nsmulRange n X` is the subgroup `n X` of an abelian group `X`.


### `nsmulRange`

 The subgroup nX of an abelian group X, for a natural number n. 

### `nsmulRange.map_mem`

 A linear map carries the subgroup `n X` of multiples into `n Y`. 

### `nsmulRange.mem_span_pow_smul_top_iff`

 For a module X over a commutative ring S and natural numbers p and k, the submodule (p)^k · X is
the subgroup p^k X of multiples. 


## Approximation and membership through the coordinates of a basis

* `New.Lift.AdicBasis.mem_of_coord`, `New.Lift.AdicBasis.eq_zero_of_coord`: a submodule
  containing `I ^ n A` contains `y` if it contains every `c.coord i y • c.b i`. If `A` is
  `I`-adically separated, an element with all coordinates zero is zero.


### `coord_sub_mem_pow`

 For a topological basis `c` of `A` (vectors `c.b i` with coordinate forms `c.coord i`): if
`y - ∑ f_j • c.b j` lies in `I ^ n A` for a finitely supported `f`, then `c.coord i y - f i` lies
in `I ^ n` for every `i`. 

### `eventually_sub_sum_mem`

 For a topological basis `c` of `A`, every `y` in `A`, every `n`, and every large enough finite
set `F` of indices, `y - ∑_{i ∈ F} c.coord i y • c.b i` lies in `I ^ n A`. 

### `mem_of_coord`

 For a topological basis `c` of `A`, a submodule `P ⊇ I ^ n A` contains `y` if it contains every
`c.coord i y • c.b i`. 

### `eq_zero_of_coord`

 If `A` is `I`-adically separated, an element whose coordinates in a topological basis `c` are
all zero is zero. 


## Successive approximation in complete modules

* Two instances: `New.shiftDiff π` is injective on a `π`-adically separated module and surjective on
  a `π`-adically complete one.
* `New.exists_eq_pow_mul_of_not_forall_dvd`: an element that is not divisible by all powers of `π`
  is `π ^ n * c` with `c` not divisible by `π`.


### `instance [IsHausdorff (Ideal.span {π}) N] : Fact (shiftDiff N π).Injective`

 On a `π`-adically separated module, `(x_j) ↦ (x_j - π • x_{j+1})` is injective. 

### `instance [IsAdicComplete (Ideal.span {π}) N] : Fact (shiftDiff N π).Surjective`

 On a `π`-adically complete module, `(x_j) ↦ (x_j - π • x_{j+1})` is surjective. 

### `mem_range_of_approx`

 Successive approximation: let `New.shiftDiff`, the operator `(x_j) ↦ (x_j - π • x_{j+1})` on
sequences, be surjective for `π` on `N` and injective for `π'` on `M`. Let `f : N → M` be additive
with `f (π • n) = π' • f n`. If every `g x` has the form `f n + π' • g y`, then every `g x` lies in
the range of `f`. 

### `exists_eq_pow_mul_of_not_forall_dvd`

 An element that is not divisible by every power of `π` is `π ^ n * c` for some `n` and some
`c` not divisible by `π`. 
