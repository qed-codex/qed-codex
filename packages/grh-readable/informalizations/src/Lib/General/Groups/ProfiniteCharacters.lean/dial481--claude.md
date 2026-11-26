---
{
  "module": "src/Lib/General/Groups/ProfiniteCharacters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Groups/ProfiniteCharacters.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Groups/ProfiniteCharacters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# ℚ/ℤ, characters of profinite groups, and extension of homomorphisms

`New.QZ` is `ℚ/ℤ` with the discrete topology, and a character of a profinite group `G`
(`New.QZChar G`) is a continuous homomorphism `G → ℚ/ℤ`. The file first proves elementary facts:
the exponential embedding of `ℚ/ℤ` into `ℂˣ`, the embedding of `ZMod n` into `ℚ/ℤ`, extension of
homomorphisms into divisible groups, and equality of the orders of a finite abelian group and its
dual. It then shows that characters separate points of the topological abelianisation of `G`, and
that additive maps from characters to `ℚ/ℤ` are evaluations at its points; these facts are used to
build Artin maps from their values on characters. `New.QZChar.abelianLift χ` denotes the map
induced by `χ` on the abelianisation, with values written multiplicatively.

## Main definitions and results

* `New.QZ.exists_extend`: for abelian groups, homomorphisms to a divisible group extend along any
  homomorphism whose kernel they kill.
* `New.card_hom_QZ`: a finite abelian group and its dual have the same order.
* `New.QZChar.mem_of_forall_abelianLift`, `New.QZChar.abelianization_ext`: characters separate a
  point from a closed subgroup of the abelianisation, and hence separate points.
* `New.QZChar.exists_hom_abelianLift_eq`: every additive map from characters to `ℚ/ℤ` is evaluation
  at a point of the abelianisation, in a form that is multiplicative in a parameter.
* `New.QZChar.continuous_iff_forall_isOpen_ker_comp`: a homomorphism from a commutative topological
  group to the abelianisation is continuous exactly when its composite with each character has open
  kernel.
* `New.exists_monoidHom_extend`, deduced from `New.QZ.exists_extend`: a homomorphism
  `θ` from a commutative group into a divisible commutative group, trivial on the preimage of a
  subgroup `H` under a homomorphism `f` of commutative groups, factors through `f` by a homomorphism
  trivial on `H`.

Notions from other files:
* `New.Z1 ρ`: the continuous 1-cocycles of `ρ`, that is the continuous `f : G → M` with
  `f (g h) = f g + ρ g (f h)`; `New.QZChar G` is the case of the trivial action on `ℚ/ℤ`.
* `New.QZChar.toHom χ`: the character `χ` as a group homomorphism to `ℚ/ℤ` written
  multiplicatively; `New.QZChar.ker χ` is its kernel.


 ## ℚ/ℤ, embeddings of ZMod n and duals of finite abelian groups 

### `Continuous.of_isOpen_ker`

 A homomorphism from a topological group to a topological monoid is continuous as soon as its
kernel is open. 

### `isAddTorsion`

 Every element of `ℚ/ℤ` has finite order. 

### `addOrderOf_mk_inv`

 For `n` positive, the class of `1 / n` in `ℚ/ℤ` has order `n`. 

### `mk_surjective`

 Every element of `ℚ/ℤ` is the class of a rational number. 

### `mk_eq_zero_iff`

 The class of a rational number in `ℚ/ℤ` is zero exactly when the number is an integer. 

### `expUnit`

 The group homomorphism from `ℚ/ℤ`, written multiplicatively, to `ℂˣ` sending the class of `x`
to `exp (2 π i x)`. 

### `coe_expUnit_ofAdd_mk`

 The value of `expUnit` at the class of a rational number `x` is `exp (2 π i x)`. 

### `expUnit_eq_one_iff`

 The homomorphism `expUnit : x ↦ exp (2 π i x)` from `ℚ/ℤ` to `ℂˣ` has trivial kernel. 

### `exists_extend`

 Let `A`, `B` and `W` be abelian groups with `W` divisible and `f : A →+ B` a homomorphism, not
necessarily injective. Every homomorphism `u : A →+ W` that kills the kernel of `f` is equal to
`v ∘ f` for some homomorphism `v : B →+ W`. 

### `eq_zero_of_forall_hom_eq_zero`

 An element of an abelian group that is killed by every homomorphism to `ℚ/ℤ` is zero. 

 ### The embedding of `ZMod n` 

### `ofZMod`

 For `n` nonzero, the additive homomorphism `ℤ/n → ℚ/ℤ` sending the class of `k` to the class
of `k / n`. 

### `ofZMod_apply`

 The embedding `ofZMod n` sends a residue `b` to the class in `ℚ/ℤ` of `b.val / n`, where
`b.val` is the representative of `b` below `n`. 

### `exists_ofZMod`

 An element of `ℚ/ℤ` killed by `n` is in the image of the embedding `ofZMod n` of `ℤ/n`. 

### `bijective_ofZMod_comp`

 If `A` is killed by `n`, composing with `New.QZ.ofZMod n` is a bijection from the
homomorphisms `A →+ ZMod n` to the homomorphisms `A →+ ℚ/ℤ`. 

 ### Duals of finite abelian groups 

### `card_hom_QZ`

 A finite abelian group `A` has exactly `#A` homomorphisms to `ℚ/ℤ`: its Pontryagin dual has
the same order as `A`. 

 ## Characters of a profinite group and its abelianisation 

### `ofZModCocycle`

 The additive map sending a continuous 1-cocycle of `G` with values in `ℤ/n` (trivial action)
to the character `G → ℚ/ℤ` obtained by composing with the embedding `ofZMod n`. 

### `isOpen_ker`

 The kernel of a character `χ : G → ℚ/ℤ` is open. 

### `exists_apply_ne_zero_of_notMem_ker`

 Let `G` be a nonarchimedean group and `f : G →* C` a homomorphism to a commutative group
with closed kernel. If `σ` is not in the kernel, some continuous character of `G` vanishes on
the kernel but not at `σ`. 

### `isOfFinAddOrder_of_compactSpace`

 A character `χ : G → ℚ/ℤ` of a compact group has finite order: it is killed by the index of
its open kernel. 

### `exists_eval_eq_on_finset`

 Let `G` be a compact group and `t` an additive map from the characters `G → ℚ/ℤ` to `ℚ/ℤ`. On
a finite set `S` of characters, `t` is evaluation at some point of `G`. 

### `exists_eval_eq`

 For a compact group `G`, an additive map `t` from the characters `G → ℚ/ℤ` to `ℚ/ℤ` is
evaluation at some point of `G`. 

 ### Duality for profinite groups 

### `mem_of_forall_abelianLift`

 Let `G` be profinite and `H` a closed subgroup of its topological abelianisation. An element
`σ` of the abelianisation lies in `H` if it is killed by every character `χ : G → ℚ/ℤ` that kills
`H`; here `abelianLift χ` is the map induced by `χ` on the abelianisation. 

### `abelianization_ext`

 For a profinite group `G`, two elements of the topological abelianisation are equal if the
map `abelianLift χ` induced by each character `χ : G → ℚ/ℤ` takes the same value on them. 

### `exists_hom_abelianLift_eq`

 The existence part of Pontryagin duality for a profinite group `G`: if `s` maps a group `X`
homomorphically to the additive maps from the characters of `G` to `ℚ/ℤ`, then some homomorphism
`f` from `X` to the topological abelianisation of `G` has `χ (f x) = s x χ` for all `χ` and `x`.
Here `abelianLift χ` is the map induced by `χ` on the abelianisation. 

### `continuous_iff_forall_isOpen_ker_comp`

 Let `G` be a profinite group and `C` a commutative topological group. A homomorphism `f` from
`C` to the topological abelianisation of `G` is continuous exactly when its composite with the map
`abelianLift χ` induced by each character `χ : G → ℚ/ℤ` has open kernel. 

 ## Extension of homomorphisms into a divisible group 

### `New.exists_monoidHom_extend`

 Let `A` and `G` be commutative groups, `C` a divisible commutative group, `f : A → G` a
homomorphism and `H` a subgroup of `G`. A homomorphism `θ : A → C` that is trivial at every `a` with
`f a ∈ H` factors as `χ ∘ f` for some homomorphism `χ : G → C` trivial on `H`. 
