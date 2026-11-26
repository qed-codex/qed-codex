---
{
  "module": "src/Lib/ClassField/GaloisCohomology/TateIndexFormula.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GaloisCohomology/TateIndexFormula.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GaloisCohomology/TateIndexFormula.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coker/ker indices and Tate's index formula for cyclic actions of prime order

For a map `f` of abelian groups, `New.cokerKerIndex f` is the rational number `#coker f / #ker f`.
`(l : End ℤ A)` denotes multiplication by the natural number `l` on `A`. The file gives counting
tools for this index and for equivariant maps into finite projective `𝔽_l[Δ]`-modules.

## Main definitions and results

* `New.cokerKerIndex`: the rational number `#coker f / #ker f`; it is `0` if either group is
  infinite, so `cokerKerIndex f ≠ 0` says that both are finite.
* `New.cokerKerIndex_natCast_eq_of_ne_zero`: the index of `l` is unchanged under maps with finite
  kernel and cokernel.
* `New.card_hom_lattice_eq_card_equivariant`: `A / torsion` and a finite `Δ`-set `Z` have equally
  many equivariant maps to a finite projective `𝔽_l[Δ]`-module. This needs `A` finitely generated,
  of rank at most `#Z`, and with an equivariant map `A → ℝ^Z` whose image spans `ℝ^Z`.
* `New.Tate.index_formula`: computes the index of the norm group in the fixed points of an
  automorphism `σ` with `σ ^ l = 1`, `l` prime, from the indices of multiplication by `l`. It
  assumes that the kernel of the norm is the image of `σ - 1`, and it takes the place of the
  Herbrand quotient.
* `New.tate_index_formula_norm`: `New.Tate.index_formula` for a Galois-stable subgroup `U` of `Lˣ`
  with `H¹(Gal(L/K), U) = 0`, where `L / K` is Galois of prime degree. The hypothesis `hH1` gives
  this vanishing through Hilbert's Theorem 90.

## Relation to the literature

Known; see `Lib.ClassField.GreenbergWiles.CocycleCounts` and
`Lib.ClassField.GaloisCohomology.KummerCyclicClasses` for sources.


 ## The coker/ker index and equivariant maps from lattices to projective modules 

### `cokerKerIndex`

 For a linear map f : A → B, the rational number #coker f / #ker f; it is 0 if either group
is infinite. 

### `cokerKerIndex_comp`

 (a) The index of `g ∘ f` is `#coker g * ([B : I ⊔ N] / #(I ⊓ N)) / #ker f`, where
`I = f.range` and `N = g.ker`. (b) If one of the indices of `f` and `g` is nonzero, the index
of `g ∘ f` is their product. 

### `cokerKerIndex_mul_of_exact`

 For a short exact sequence `0 → A → B → C → 0` of abelian groups given by `f` and `g`, let
q_X = #(X/lX) / #X[l] be the rational cokernel-over-kernel index of multiplication by `l` on X,
taken to be 0 if either group is infinite. If q_A ≠ 0, meaning A/lA and A[l] are both finite, then
q_B = q_A · q_C. 

### `cokerKerIndex_natCast_eq_of_ne_zero`

 If `f : A → B` has finite kernel and cokernel, then `#(A/lA) / #A[l] = #(B/lB) / #B[l]`, each
side read as `0` when one of its groups is infinite. 

### `cokerKerIndex_natCast_eq_pow_finrank`

 On a finitely generated abelian group `A`, multiplication by `l ≠ 0` has index
`#(A / l A) / #A[l] = l ^ rank A`. 

### `cokerKerIndex_natCast_ne_zero`

 On a finitely generated abelian group `A`, multiplication by `l ≠ 0` has finite kernel and
cokernel: its index is nonzero. 

### `cokerKerIndex_eq_pow_finrank`

 On a finitely generated abelian group `A`, multiplication by `l ≠ 0` has nonzero index
`#(A / l A) / #A[l] = l ^ rank A`: the two clauses are `New.cokerKerIndex_natCast_ne_zero` and
`New.cokerKerIndex_natCast_eq_pow_finrank`. 

### `card_invariants_linHom`

 Let `L` be a free `ℤ`-module of finite rank with basis `b` and `Δ`-action `ρ`, and `V` an
`𝔽_l`-space (`l` prime) with basis `c` and `Δ`-action `σ`. If `τ` satisfies
`∑ g, σ g ∘ τ ∘ σ g⁻¹ = id` (`hτ`), the averaging operator `π f = ∑ g, σ g ∘ τ ∘ f ∘ ρ g⁻¹` projects
`Hom(L, V)` onto the equivariant maps. So their number is `l ^ m`, with `m` the multiplicity of `1`
as a root modulo `l` of the characteristic polynomial of an integral lift of `π`, built from the
transposed matrices of `ρ g⁻¹` and integral lifts `T g` of the matrices of `σ g ∘ τ`. 

### `charpoly_sum_kronecker_eq_of_perm`

 Let `Δ` act on the lattice `L` by `ρ` and suppose that some real basis `γ` of `Hom(L, ℝ)` is
permuted as `Δ` permutes `Z`. For integral matrices `T g`, the sum of the Kronecker products of
the transposed matrices of `ρ g⁻¹` with `T g` then has the same characteristic polynomial as the
same sum for the permutation representation on `ℤ[Z]`. 

### `card_hom_lattice_eq_card_equivariant`

 Let the finite `𝔽_l[Δ]`-module `V` be projective in Higman's sense: some additive `τ` has
`∑ g, g τ g⁻¹ = 1`. Let `A` be a finitely generated `ℤ[Δ]`-module of rank at most `#Z` with real
linear forms `Λ z` that are linearly independent over `ℝ` and permuted by `Δ` as `Z` is. Then there
are as many equivariant maps `A → V` that kill torsion as equivariant maps `Z → V`. The proof lifts
the averaging projector to an integral matrix and reads its characteristic polynomial over `ℝ`. 

 ## Tate's index formula for a cyclic action of prime order 

### `New.Tate.index_formula`

 Tate's index formula. Let `l` be prime, let `σ ^ l = 1` on `B`, let the sequence
`C → B → B → C` with maps `j`, `σ - 1`, `s` be exact with `j` injective, and let `s ∘ j = l`. So
`C` is the group of fixed points of `σ`, and `s` plays the role of the norm. With
`q_A = #(A/lA) / #A[l]` (`cokerKerIndex` of `l`) and `q_C ≠ 0`, one has
`[C : s B] ^ (l - 1) * q_B = q_C ^ l`. 

 ## Tate's index formula for the norm in an extension of prime degree 

### `New.tate_index_formula_norm`

 Tate's index formula for the norm `N` of a Galois extension `L / K` of prime degree `l`.
Let `U ≤ Lˣ` be Galois-stable, `V = U ∩ Kˣ`, and suppose that every Galois-fixed class of
`Lˣ / U` comes from `Kˣ` (by Hilbert 90 this says `H¹(Gal(L/K), U) = 0`). With
`q_A = #(A / A ^ l) / #A[l]` and `q_V ≠ 0`, one has `[V : N U] ^ (l - 1) * q_U = q_V ^ l`. 
