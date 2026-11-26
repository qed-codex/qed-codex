---
{
  "module": "src/Lib/ClassField/GaloisCohomology/ShapiroCorestriction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GaloisCohomology/ShapiroCorestriction.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GaloisCohomology/ShapiroCorestriction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Shapiro's lemma, corestriction and reduction of H² statements to steps of prime index

Let `Γ` be a compact group, `U` an open subgroup and `M` a discrete `Γ`-module. `M.restrictTo U` is
`M` as a `U`-module, and `M.resH2 U` is restriction `H²(Γ, M) → H²(U, M)`. `M.funModule U` is the
module of functions `Γ ⧸ U → M` with `(g F) x = g (F (g⁻¹ x))`. The file proves the parts of
Shapiro's lemma that are needed, the norm from `U` on invariants with a projection formula for the
symbols `(χ, w)`, and the fact that a class in `H²` that dies on `U` is killed by `[Γ : U]`.

## Main definitions and results

* `New.DiscreteModule.shapiroZ1`, `New.DiscreteModule.shapiroH2`: restrict a cocycle to `U` and
  evaluate it at the coset `U`.
* `New.DiscreteModule.shapiro_H0`, `New.DiscreteModule.shapiro_H1`,
  `New.DiscreteModule.shapiroH2_injective`: the parts of Shapiro's lemma that are used. In degree
  zero, every `Γ`-invariant function is `x ↦ x.out y` for some `U`-invariant `y`. In degree one, a
  cocycle whose image is a coboundary is itself a coboundary. In degree two, the map is injective.
* `New.DiscreteModule.corestrictH0`: the norm from `U`.
  `New.DiscreteModule.cyclicClass_corestrictH0` gives the projection formula: if `α` restricts on
  `U` to `(χ|U, w)`, then `(χ, N w)` is `[Γ : U] α`.
* `New.DiscreteModule.mem_of_prime_step`: a class `α` in `H²(Γ, M)` lies in a subgroup `S` if it
  dies on an open normal subgroup `W` and the vanishing of `α - s` (some `s ∈ S`) can be lifted
  through normal steps of prime index. The proof climbs a chain of `l`-subgroups of a finite
  quotient `Γ ⧸ W`, as in Sylow's theorem.
* `New.DiscreteModule.HoldsCorestrictions`: a group of cocycles of `Γ` contains the coboundaries and
  corestrictions of a given group of cocycles of an open subgroup `U`; it is used in local duality.

Notions from other files:
* `New.cyclicClass`: The symbol (χ, w) = δχ ∪ w in H²(G,M) of a continuous character χ: G → ℚ/ℤ
  (`New.QZChar`) and an invariant w. It is the class of (g,h) ↦ carry(χ(g), χ(h))·w.
* `New.H2`: Continuous cohomology H²(G,M): continuous 2-cocycles of ρ modulo coboundaries of
  continuous 1-cochains.

## Relation to the literature

Known; see `Lib.ClassField.GaloisCohomology.KummerCyclicClasses` for sources.



## Shapiro's lemma, norms and corestriction for open subgroups

Corestriction on `H²` is not defined as a map. `New.DiscreteModule.mapH2_sum_eq_index_smul`
expresses corestriction after restriction through a class `β` with values in the functions
`Γ ⧸ U → M`. This class is summed over the cosets by `New.DiscreteModule.sum`.


### `New.QZChar.comap`

 For a continuous homomorphism φ: H → Γ, the additive map from continuous ℚ/ℤ-valued
characters of Γ to those of H, χ ↦ χ∘φ. 

### `New.QZChar.comap_apply`

 The character `χ ∘ φ`, as a homomorphism to `ℚ/ℤ`, takes the value `χ (φ h)` at `h`. 

### `New.QZChar.exists_ker_eq_of_isCyclic`

 An open normal subgroup `U` of the compact group `Γ` with cyclic quotient is the kernel of a
continuous character `Γ → ℚ/ℤ`. 

 ### The Shapiro maps and the norm 

### `funModule_apply_one`

 An element `u` of `U` fixes the coset `U`, so acting by `u` on a function `F : Γ ⧸ U → M`
and evaluating at the coset `U` gives `u` acting on the value `F U`. 

### `shapiroZ1`

 The Shapiro map on continuous 1-cocycles, Z¹(Γ, Fun(Γ/U, M)) → Z¹(U, M): restrict to U and
evaluate at the trivial coset. 

### `shapiroH2`

 The linear map H²(Γ, Fun(Γ/U,M)) → H²(U,M) given by restriction to U followed by evaluation
at the identity coset. 

### `corestrictH0`

 The norm of a U-invariant y of M: the sum of g·y over the cosets gU in Γ/U. 

 ### Shapiro's lemma 

### `exists_coset_section`

 A section of `Γ → Γ ⧸ U` adapted to `U`: for `U` open in `Γ` there is `s : Γ ⧸ U → Γ` that
sends the coset `U` to `1` (first clause), with `s x` in the coset `x` (second clause), and with
`(s x)⁻¹ g s (g⁻¹ x) ∈ U` for all `x` and `g` (third clause). 

### `shapiro_H0`

 Shapiro's lemma in degree zero. A `Γ`-invariant element `F` of the module of functions
`Γ ⧸ U → M` (an equivariant function) is `x ↦ x.out y` for some `U`-invariant `y` in `M`, where
`x.out` is the chosen representative of the coset `x`. This is the function summed in the norm
`New.DiscreteModule.corestrictH0`, so the sum of `F` is the norm of `y`. 

### `shapiro_H1`

 Shapiro's lemma in degree one, injectivity. If the restriction to `U` of a 1-cocycle `F` with
values in the functions `Γ ⧸ U → M`, evaluated at the coset `U`, is the coboundary of `m`, then
`F` is a coboundary. 

### `shapiroH2_injective`

 Shapiro's lemma in degree two, injectivity: for U open in the compact group Γ, the map
H²(Γ, Fun(Γ/U, M)) → H²(U, M), restriction followed by evaluation at the trivial coset, is
injective. 

 ### Corestriction and restriction of classes in `H²` 

### `mapH2_sum_eq_index_smul`

 Corestriction after restriction is multiplication by the index. If `β` is a class with values
in the functions `Γ ⧸ U → M` whose Shapiro image is the restriction of `α` to `U`, then summing
`β` over the cosets gives `[Γ : U] α`. 

### `cyclicClass_corestrictH0`

 The projection formula for symbols. Suppose `v` is the norm of the `U`-invariant `w`, and the
restriction of `α` to `U` is `(χ|U, w)`. Here `χ|U` is `QZChar.comap (subgroupIncl U) χ`, `χ`
composed with the inclusion `U → Γ`, and `H0` denotes invariants. Then `(χ, v)` is `[Γ : U] α`. 

### `index_smul_eq_zero_of_resH2`

 For Γ compact and U an open subgroup, a class in H²(Γ, M) whose restriction to U vanishes is
killed by the index [Γ : U]. 

### `resH2_cyclicClass_eq_zero_of_nsmul_eq`

 Let `w = k • r` be a `Γ`-invariant element of `M`, and `U` a subgroup of `Γ` that fixes `r`
and on which `k • χ` vanishes. Then the class `(χ, w) = δχ ∪ w` in `H²(Γ, M)` restricts to zero
on `U`. 

### `resH2_cyclicClass_eq_zero`

 `resH2_cyclicClass_eq_zero_of_nsmul_eq` with its two conditions on `U` (`U` fixes `r`, and
`k • χ` vanishes on `U`) joined in one hypothesis. 

 ## Reduction to steps of prime index and corestriction of cocycles 

### `HoldsCorestrictions`

 The group `Y ≤ Z¹(Γ, M)` of cocycles contains every coboundary and a corestriction of each
cocycle in `Y' ≤ Z¹(U, M)`, for an open subgroup `U` of `Γ`. 

### `HoldsCorestrictions.coboundary_mem`

 Every coboundary `g ↦ g m - m` lies in `Y`. 

### `HoldsCorestrictions.exists_corestriction`

 Each `y ∈ Y'` is the Shapiro image (restrict to `U`, evaluate at the trivial coset) of a
  cocycle `F` with values in the functions `Γ ⧸ U → M` whose sum over `Γ ⧸ U` lies in `Y`. 

### `resH2_subgroupOf_eq_zero_symm`

 If the restriction of `α` to `U ⊓ V`, seen as a subgroup of `V`, vanishes, then so does
its restriction to `U ⊓ V` seen as a subgroup of `U`. 

### `mem_of_prime_step`

 Let `S ≤ H²(Γ, M)`, and let `α` vanish on an open normal subgroup `W`. Suppose that for
all open `W ≤ V ≤ U` with `V` normal of prime index in `U`: if `α - s` vanishes on `V` for
some `s ∈ S`, then `α - s'` vanishes on `U` for some `s' ∈ S`. Then `α ∈ S`. 
