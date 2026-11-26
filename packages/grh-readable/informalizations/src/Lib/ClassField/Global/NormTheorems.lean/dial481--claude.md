---
{
  "module": "src/Lib/ClassField/Global/NormTheorems.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Global/NormTheorems.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Global/NormTheorems.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Surjectivity of the Artin map, Hasse's norm theorem and norm groups of cyclic extensions

Global class field theory for cyclic extensions of a number field `K`, deduced from the reciprocity
law, the second inequality `New.second_inequality` and `New.albert_brauer_hasse_noether`.

* `New.artinMap_surjective`: the Artin map from the finite ideles onto `Γ^ab` is surjective.
* `New.exists_isProGalois_ker_of_isCyclic`: a cyclic extension `L/K` is cut out by a character.
* `New.hasse_norm`: Hasse's norm theorem, for totally positive elements.
* `New.index_ker_abelianLift_comp_artinMap`, `New.abelianLift_artinMap_eq_one_iff`: if `χ` cuts out
  `L`, the kernel of `χ ∘ artinMap` has index `[L : K]` and consists of totally positive elements of
  `Kˣ` times norms from `L`.

Notions from other files:
* `New.Ω` is an algebraic closure of `ℚ`, and `New.EmbeddedNumberField K` is a number field `K`
  with an embedding in `Ω`. `New.IsProGalois Γ K Ω` says that `Γ` is the profinite Galois group of
  `Ω/K`.
* `New.artinMap Γ` is the global Artin map from the finite ideles `(𝔸f K)ˣ` of `K` to the
  topological abelianisation `Γ^ab` of `Γ`, chosen so that a character takes at `artinMap Γ a` the
  product of its values at the local Artin symbols of the components of `a`.
* A `χ : New.QZChar Γ` is a continuous character `Γ → ℚ/ℤ`; `New.QZChar.toHom χ` and
  `New.QZChar.abelianLift χ` are its multiplicative forms on `Γ` and `Γ^ab`. "`χ` cuts out `L`" is
  the instance `IsProGalois (ker χ) L Ω`, with `New.QZChar.ker`.
* `New.IsTotallyPositive x`: every ring homomorphism `K → ℝ` sends `x` to a positive number.

## Relation to the literature

Known; see `Lib.ClassField.Global.AlbertBrauerHasseNoether` for sources.


### `isClosed_range_artinMap`

 The image of the global Artin map from the finite ideles of `K` to `Γ^ab` is closed. 

### `artinMap_surjective`

 The global Artin map from the finite ideles of `K` to the topological abelianisation `Γ^ab` of
the absolute Galois group `Γ` of `K` is surjective.

A consequence of Artin's global reciprocity law. 

### `exists_isProGalois_ker_of_isCyclic`

 Let L/K be a cyclic extension of number fields inside an algebraic closure Ω of ℚ. There is
a continuous character χ : Gal(Ω/K) → ℚ/ℤ whose kernel acts on Ω as the Galois group of Ω/L. 

### `hasse_norm`

 Hasse's norm theorem. Let `L / K` be a cyclic extension of number fields. A totally positive `x`
in `K` that is a local norm (a limit of norms from `L` in the completion `LocField v` of `K` at `v`)
at every finite place `v` is a norm.

A case of the Hasse norm theorem, with x assumed totally positive, which is stronger than being a
local norm at each real place. 

### `index_ker_abelianLift_comp_artinMap`

 If the kernel of `χ` is the Galois group of `Ω / L`, then the kernel of `χ ∘ artinMap` has index
`[L : K]` in the finite ideles of `K`. 

### `abelianLift_artinMap_eq_one_iff`

 The norm group of the extension `L / K` cut out by `χ`: a finite idele `a` of `K` is killed by
`χ ∘ artinMap` exactly when it is a totally positive element of `Kˣ` times the norm of a finite
idele of `L`. A case of the Artin reciprocity law. 
