---
{
  "module": "src/Lib/GaloisRep/Main/DivisibleSelmerModules.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/DivisibleSelmerModules.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/DivisibleSelmerModules.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selmer modules with divisible coefficients

`O` is a discrete valuation ring and `New.Selmer.DivisibleQuot O` is the module `Frac(O) / O`. For a
matrix-valued function `ρ` on the Galois group `Gal(Ω/E)` of `Ω` over the number field `E`
(`EmbeddedNumberField E`) with entries in `O` and `a ≠ 0`, the Selmer module with coefficients in
`O / a` is identified with the `a`-torsion of the Selmer module with coefficients in `Frac(O) / O`,
so it is no longer than the latter.

## Main definitions and results

* `New.Selmer.comp_mem_selmerModule_iff`, `New.Selmer.selmerModuleMapOfInjective`: an injective map
  of coefficient modules preserves and reflects the Selmer conditions, and so maps Selmer modules
  injectively.
* `New.Selmer.length_torsionBy_selmerModule`: if the map identifies `O / a` with the `a`-torsion of
  the coefficients, the Selmer module with coefficients in `O / a` has the length of the `a`-torsion
  of the other.
* `New.Selmer.divisibleSelmerLength`, `New.Selmer.length_le_divisibleSelmerLength`: the length of
  the Selmer module with coefficients in `Frac(O) / O` (for `E` with `CMFieldWithRoot5040 E`), which
  bounds the lengths of those with coefficients in `O / a`.

Notions from other files:
* `New.selmerModule ρ S L B`: the locally constant cocycles for `ρ` with values in `B ^ n` that are
  unramified outside `S` and obey the linear relations `L`.

## Relation to the literature

Known. The comparison of Selmer groups with coefficients in `O / a` and in `Frac(O) / O` is
standard; here it is immediate, because cocycles are counted and not classes.


### `comp_mem_selmerModule_iff`

 An injective map `f` of coefficient modules preserves and reflects the Selmer conditions:
`f ∘ z` is in the Selmer module (the locally constant cocycles for `ρ` that are unramified outside
the set `S` of finite places and obey the relations `L`) if and only if `z` is. 

### `selmerModuleMapOfInjective`

 The map of Selmer modules `z ↦ f ∘ z` induced by an injective map `f` of coefficient
modules. 

### `selmerModuleMapOfInjective_apply`

 The value at `g` and `i` of the image of a Selmer cocycle `z` under the map induced by `f` is
`f (z g i)`. 

### `selmerModuleMapOfInjective_injective`

 An injective map of coefficient modules induces an injective map of Selmer modules. 

### `range_selmerModuleMapOfInjective`

 If `f` identifies `O / a` (that is, `QuotSpan a`) with the `a`-torsion of `B`, then composition
with `f` maps the Selmer module (cocycles for `ρ` unramified outside `S` that obey the relations
`L`) with coefficients in `O / a` onto the `a`-torsion of the one with coefficients in `B`. 

### `length_torsionBy_selmerModule`

 If `f` identifies `O / a` (that is, `QuotSpan a`) with the `a`-torsion of `B`, then the Selmer
module (cocycles for `ρ` unramified outside `S` that obey the relations `L`, not classes) with
coefficients in `O / a` has the length of the `a`-torsion of the one with coefficients in `B`. 

### `length_torsionBy_selmerModule_divisibleQuot`

 For `a ≠ 0`, the Selmer module (cocycles for `ρ` unramified outside `S` that obey the relations
`L`) with coefficients in `O / a` has the length of the `a`-torsion of the Selmer module with
coefficients in `DivisibleQuot O = Frac(O) / O`. 

### `length_selmerModule_le_divisibleQuot`

 For `a ≠ 0`, the Selmer module (cocycles for `ρ` unramified outside `S` that obey the relations
`L`) with coefficients in `O / a` is no longer than the one with coefficients in
`DivisibleQuot O = Frac(O) / O`. 

### `divisibleSelmerLength`

 For `E` a CM field containing the 5040th roots of unity (`CMFieldWithRoot5040`), the length over
`O` of the Selmer module with coefficients in `Frac(O) / O`: the locally constant cocycles for `ρ`
that are unramified outside `S` and obey the relations `L`. 

### `length_le_divisibleSelmerLength`

 Let `E` be a CM field containing the 5040th roots of unity (`CMFieldWithRoot5040`) and `a ≠ 0`.
The Selmer module (cocycles for `ρ` unramified outside `S` that obey the relations `L`) with
coefficients in `O / a` has length at most `divisibleSelmerLength ρ S L`, the length of the one with
coefficients in `Frac(O) / O`. 
