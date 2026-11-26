---
{
  "module": "src/Lib/PadicHodge/BlochKato.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/BlochKato.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/BlochKato.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bloch–Kato crystalline cocycles: reduction modulo p^m, rank and vanishing

Let `T` be a finite free `ℤ_[p]`-module of rank d with an action `ρ` of a group Γ, and let
j = `𝒥.toGp`, given by the structure `𝒥 : New.Period.OverGp Γ p`, map Γ with open image of index n
to the absolute Galois group `New.Gp` of ℚ_p. The Bloch–Kato cocycles
Z_f(T) = `New.Period.crysCocycles ρ` are the maps Γ → T that become coboundaries over the period
ring B = `New.Period.Bmax`. χ = `New.Period.χ` is the cyclotomic character `New.cyclotomicGp`
composed with j. The file proves basic properties of Z_f(T), builds admissible extensions from
crystalline cocycles of potentially crystalline representations, studies reduction modulo p^m, and
computes the rank of Z_f(T) and its vanishing.

## Main definitions and results

* `New.Period.IsPotentiallyCrystalline.exists_hodge_basis`: for potentially crystalline T, in a
  ℤ_p-basis of T, an automorphism of B_dR^ι that makes the action of Γ coordinatewise and carries
  (B_dR^+)^ι to the lattice given by the jumps of T.
* `New.Period.extensionRep`, `New.Period.isAdmissible_extensionRep`: the extension of a trivial
  module by T given by cocycles in `New.Period.crysCocycles` is admissible along the same filter as
  T (`New.Period.IsAdmissible`).
* `New.Period.IsPotentiallyCrystalline.reducedCocycle`: for an equivariant additive map `q` from `T`
  to a discrete module `V` with kernel `p ^ m T`, the map sending a crystalline cocycle `c` to the
  continuous cocycle `q ∘ c`.
* `New.Period.crysCocycles.finrank_eq`: for potentially crystalline T, Z_f(T) is finitely generated
  over ℤ_p of rank d + n·(number of negative Hodge–Tate jumps).
* `New.Period.IsPotentiallyCrystalline.exists_coboundary_eq_smul`: for potentially crystalline T
  with positive jumps, Z_f(T) is torsion modulo coboundaries.
* `New.Period.crysCocycles.apply_eq_zero_of_cyclotomicGp`: let Γ act through χ^(−a) with a ≥ 0. Then
  crystalline cocycles vanish where the action is trivial. When a = 0 we also need j(s) to lie in
  inertia.

Notions from other files:
* `New.Period.IsPotentiallyCrystalline`: the elements of Bmax ⊗ T fixed by all g with j(g) near 1
  span Bmax ⊗ T over Bmax.
* `New.DiscreteModule`: A discrete Γ-module over R: an R-module with the discrete topology and a
  continuous R-linear action of the topological group Γ.
* `New.DiscreteModule.HoldsCorestrictions`: for a discrete Γ-module V, an open subgroup U of Γ and
  groups of cocycles Y′ ≤ Z¹(U, V) and Y ≤ Z¹(Γ, V), the group Y contains every coboundary and a
  corestriction of each y in Y′: there is a cocycle F with values in the functions Γ/U → V whose
  Shapiro image is y and whose sum over Γ/U lies in Y.
* `New.Period.jump`: The multiplicity of the Hodge–Tate jump u at γ: the dimension over Q̄_p (zero
  if infinite) of the γ-semilinear f : T → ℂ_p with f(gx) = χ(g)^(−u)·g f(x) for g near 1.

## Relation to the literature

Known result: Bloch–Kato finite local condition, rank formula. Here it is treated on cocycles of a
lattice in a potentially crystalline representation. The rank is counted from the fundamental exact
sequence. Local duality is not treated in this file, only the reduction of crystalline cocycles
modulo p^m. Source: S. Bloch, K. Kato, L-functions and Tamagawa numbers of motives, Grothendieck
Festschrift I (1990), Prop. 3.8, Cor. 3.8.4; J. Bellaïche, An introduction to the conjecture of
Bloch and Kato, Clay Summer School notes (2009), Prop. 2.8, Thm 2.1.



## Crystalline cocycles: functoriality, coboundaries and saturation

* `New.Period.crysCocycles.comp_mem`: an equivariant map carries crystalline cocycles to crystalline
  cocycles.
* `New.Period.crysCocycles.coboundary_mem`, `New.Period.crysCocycles.apply_mul`: `crysCocycles ρ`
  contains the coboundaries and, for `T` free over `ℤ_p`, consists of cocycles.
* `New.Period.crysCocycles.mem_of_smul_mem`: `crysCocycles ρ` is saturated in the maps Γ → T.


### `comp_mem`

 Functoriality: a ℤ_p-linear map `f : T → T'` with `f (ρ g x) = σ g (f x)` carries a crystalline
cocycle `c` of `ρ` to the crystalline cocycle `f ∘ c` of `σ`. 

### `coboundary_mem`

 The coboundary `g ↦ g x - x` of an element `x` of T is a crystalline cocycle. 

### `apply_mul`

 If T is free over Z_p, every c in `crysCocycles ρ` is a cocycle: c(gh) = c(g) + g·c(h) for all
g, h. 

### `mem_of_smul_mem`

 Saturation of Z_f(T) = `crysCocycles ρ`, the maps c : Γ → T that become coboundaries in Bmax ⊗ T
(1 ⊗ c g = (j(g) ⊗ ρ(g)) y − y for some y and all g, j : Γ → Gal(Q̄_p/Q_p) from `OverGp`): if a is a
non-zero element of ℤ_p and a·c lies in Z_f(T), then c lies in Z_f(T). 


## Hodge bases and cocycle extensions of potentially crystalline representations

* `New.Period.IsPotentiallyCrystalline.exists_hodge_basis`: a basis of B_dR ⊗ T adapted to the Hodge
  filtration in which the action of Γ is coordinatewise.
* `New.Period.extensionRep`, `New.Period.isAdmissible_extensionRep`,
  `New.Period.jump_extensionRep_le`: the extension of a trivial module by T given by crystalline
  cocycles is admissible, and its Hodge–Tate jumps u ≠ 0 are at most those of T.
* `New.Period.crysCocycles.eventually_eq_pow_smul`: a crystalline cocycle is divisible by p^m near
  1, for every m.


### `IsPotentiallyCrystalline.exists_hodge_basis`

 Hodge basis over B_dR. Let `j = toGp : Γ → Gal(Q̄_p/Q_p)` have open image, and let T be
potentially crystalline with a finite ℤ_p-basis e indexed by ι. There are integers k_i and a
ℤ_p-linear automorphism N of B_dR^ι such that: (a) the k_i, with multiplicity, are the Hodge–Tate
jumps of T over ℤ_p at the inclusion ℤ_p → ℂ_p; (b) N carries the action `coordAction ρ e g` of each
g on B_dR^ι (the matrix `repMatrix ρ e g` of ρ(g) in e, with j(g) acting on the entries), read
through e, to the coordinatewise action of j(g); (c) a vector b is the image under N of a vector
with coordinates in B_dR^+ if and only if each b_i lies in the Hodge filtration step t^(−k_i)
B_dR^+; (d) for some invertible matrix W over B_dR^+, with `hodgeMatrix W k` = W·diag(t^(k_i)) and t
the period `tUnit`, the matrix of ρ(g) in e times j(g) applied to `hodgeMatrix W k` equals
`hodgeMatrix W k`, for all g.

This is a case of the existence of bases adapted to the Hodge filtration (Brinon–Conrad 6.3.7). 

### `extensionRep`

 The representation g(y, c) = (ρ(g)y + a(c)(g), c) on T × C: the extension of the trivial
module C by T given by the crystalline cocycles a(c). Here `proj g` evaluates a map Γ → T at g. 

### `isAdmissible_extensionRep`

 Let `F` be a filter on `Γ`, and suppose `ρ` is admissible for `F`: the elements of `Bmax ⊗ T`
fixed by `j(g) ⊗ ρ(g)` for `F`-almost all `g` span `Bmax ⊗ T` over `Bmax`. Then the same holds, with
the same `F`, for `extensionRep a`, the representation `g(y, c) = (ρ(g) y + a(c)(g), c)` on `T × C`
given by an `R`-linear family `a` of crystalline cocycles. 

### `jump_extensionRep_le`

 Let T be free over ℤ_p and finite over R, let `a` be an R-linear family of crystalline cocycles,
and let γ : R → ℂ_p be a ℤ_p-algebra map. For every integer u ≠ 0, the multiplicity
`jump (extensionRep a) γ u` of the jump u of the extension of C by T is at most `jump ρ γ u`.

This is one inequality of the additivity of Hodge–Tate weights in exact sequences. 

### `crysCocycles.eventually_eq_pow_smul`

 Let `ρ` be a potentially crystalline representation of `Γ` on `T`, with `T` finite free over
ℤ_p, and let `c : Γ → T` lie in `crysCocycles ρ`, i.e. become a coboundary in `Bmax ⊗ T`. Then for
every `m`, `c g` lies in `p ^ m • T` for all `g` whose image under the structure map `j : Γ → Gp p`
is close enough to `1` (the filter `nearOne Γ`). 


## Crystalline cocycles modulo p^m: continuity and corestriction

In the main results of this section, `𝒥.toGp` is an open embedding and `T` is potentially
crystalline.


### `pPowMultiples`

 For a natural number m, the additive subgroup p^m T of T, the image of multiplication by p^m. 

### `index_pPowMultiples`

 If T is free of rank d over ℤ_p, the subgroup p^m T has index p^(md). 

### `zmodPowToUnits`

 The additive homomorphism from ℤ_p/p^m to the multiplicative group of Q̄_p, written additively,
that sends the class of a to ζ^a, where ζ is the primitive p^m-th root of unity chosen in
`New.rootPowHom`. 

### `map_cyclotomicGp_smul`

 An additive map `f` from a `ℤ_[p]`-module to the `p ^ n`-th roots of unity turns multiplication
by the cyclotomic character of `g` into the Galois action of `g`. 

### `crysCocycles.continuous_comp`

 Let j: Γ → G_p be an open embedding and T potentially crystalline, finite free over ℤ_p. For an
additive map q from T to an additive group with any topology, with values killed by p^m, and x in
`crysCocycles ρ`, the map q∘x is continuous. 

### `IsPotentiallyCrystalline.comp_mem_Z1`

 For an additive map `q : T → V` that is equivariant (`e`) and has kernel `p ^ m T` (`k`), the
reduction `q ∘ c` of a crystalline cocycle `c` is a continuous cocycle of `V`. Here `𝒥.toGp` is an
open embedding (`hj`) and `T` is potentially crystalline (`h`). 

### `IsPotentiallyCrystalline.reducedCocycle`

 For an additive map q: T → V that is equivariant (`e`) and has kernel p^m T (`k`), the additive
map sending a crystalline cocycle c to the continuous cocycle q∘c in Z¹(V). Here `𝒥.toGp` is an
open embedding (`hj`) and `T` is potentially crystalline (`h`). 

### `IsPotentiallyCrystalline.ker_reducedCocycle`

 The kernel of `New.Period.IsPotentiallyCrystalline.reducedCocycle` is `p ^ m` times the
crystalline cocycles: a crystalline cocycle that is `p ^ m` times a function is `p ^ m` times a
crystalline cocycle. Here `ρ` is the action of `Γ` on `T`, `q : T →+ V` maps to a discrete
`Γ`-module `V` over `S`, and it is equivariant (`e`) with kernel `p ^ m T` (`k`), `hj` says that
`𝒥.toGp` is an open embedding and `h` that `T` is potentially crystalline. 

### `IsPotentiallyCrystalline.holdsCorestrictions`

 Let `𝒥.toGp` be an open embedding, `T` potentially crystalline, `Γ` compact, `q : T → V`
equivariant and surjective with kernel `p ^ m T` and `U` an open subgroup of `Γ`. The reductions of
the crystalline cocycles of `Γ` contain all coboundaries of `V` and a corestriction of each
reduction of a crystalline cocycle of `U` (`New.DiscreteModule.HoldsCorestrictions`). 


## Bloch–Kato cocycles: rank, finiteness and vanishing

The rank comes from the fundamental exact sequence of p-adic periods.


### `rank_comap_eq_add`

 Rank–nullity for preimages: for a linear map e of modules over a domain and a submodule N of
the target, rk e⁻¹(N) = rk (N ∩ im e) + rk ker e. 

### `rank_eq_of_le_of_torsion`

 If the submodule A lies in B and every element of B has a nonzero multiple in A, then A and B
have the same rank. 

### `exists_pow_mul_coboundary_integral`

 If the coboundary `coboundaryMap (coordAction ρ ε) x` (g ↦ g x − x, with Γ acting on
`ι → BdRPlus` through the basis `ε` of `T`) of a vector `x` over `BdRPlus` has entries in `ℚ_[p]`,
one power of `p` makes all of them integral. 

### `crysCocycles.finite_and_finrank_eq_of_rank_eq`

 If the crystalline cocycles have rank `n` over ℤ_p, they form a finite ℤ_p-module of finite rank
`n`: the module is separated and torsion free, so a bound on its rank gives finite generation. 

### `frobEnd_algebraMap_padicInt`

 The Frobenius `φ` of `Bmax` fixes the `p`-adic integers. 

### `exists_padicInt_eq_pow_smul_of_frobEnd_eq`

 Bounded denominators. Let `Dy : Γ → ι → Bmax` have entries fixed by `φ` that, read in `BdR`,
are the coboundary of a vector `x` over `BdRPlus`. Then one power `p ^ s` makes all entries of
`Dy` integral `p`-adic numbers. 

### `rank_comap_coboundary_eq`

 The side of the coboundaries in the rank count of `New.Period.crysCocycles.finrank_eq`. In the
coordinates of a basis `ε` of `T`, let `D y = (g ↦ g y - y)` be the coboundary map on vectors over
`Bmax` and `incl` the map from functions `Γ → T` to functions `Γ → ι → Bmax`. The vectors `y` whose
coboundary `D y` comes from a function `Γ → T` form a module of rank `rk Z_f(T) + rk ker D`. 

### `rank_comap_frob_sub_prod_eq`

 The side of the fundamental exact sequence in the rank count of
`New.Period.crysCocycles.finrank_eq`. Let `k : ι → ℤ` and let `N` be a ℤ_p-linear automorphism of
`ι → BdR` that carries the vectors with entries in `BdRPlus` exactly onto the `b` with each `b i` in
`hodgeFil (-k i)`, as in (c) of `New.Period.IsPotentiallyCrystalline.exists_hodge_basis`; let `P` be
this image, `u` the map sending a vector over `Bmax` to `N` of its image in `ι → BdR`, and `w` the
inclusion of vectors over `K = localFieldOf Γ` into `ι → BdR`. For a ℤ_p-submodule `Z` of
`ι → Bmax`, the preimage of `Z × (range of w mod P)` under `Φ y = (φ y - y, u y mod P)`, with `φ`
the Frobenius acting entrywise, has ℤ_p-rank `rk Z + rk (K ^ d⁻) + rk (ℚ_p ^ ι)`, where `d⁻` is the
number of `i` with `k i < 0`. 

### `crysCocycles.finrank_eq`

 Bloch–Kato: for a potentially crystalline lattice `T` with Hodge–Tate jumps `J` (`hJ`: the jumps
with multiplicity of `T` over ℤ_p, `overZp ρ`, at the inclusion `ofId ℤ_[p] ℂ_[p]`), the crystalline
cocycles are finitely generated over ℤ_p of rank `d + n d⁻`. Here `d` is the rank of `T`, `n` is the
index of the image of `𝒥.toGp`, and `d⁻` is the number of negative jumps. 

### `crysCocycles.fg`

 If j: Γ → G_p is a homomorphism with open image and the R[Γ]-module T is finite free over
Z_p and potentially crystalline, then the R-module Z_f(T) of crystalline cocycles is
finitely generated. 

### `IsPotentiallyCrystalline.exists_coboundary_eq_smul`

 If `ρ` is potentially crystalline and all Hodge–Tate jumps of `ρ` (read over ℤ_p) are positive,
a crystalline cocycle `c` is torsion modulo coboundaries: there are `t ≠ 0` in ℤ_p and `x` in `T`
with `ρ g x - x = t • c g` for all `g`. 

### `crysCocycles.apply_eq_zero_of_cyclotomicGp`

 Let Γ act on T, finite free over ℤ_p, through χ^(−a) with a ≥ 0, where χ is the cyclotomic
character of Γ. A crystalline cocycle vanishes at every s with ρ(s) = 1, provided that, when a = 0,
j(s) = `toGp s` lies in inertia (`IsWeilPair (toGp s) 0`).

This is a consequence, on cocycles, of the Bloch–Kato computation of H¹_f of Tate twists. 
