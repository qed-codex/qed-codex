---
{
  "module": "src/Lib/General/Algebra/LevelModulus.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/LevelModulus.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/LevelModulus.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Level moduli, residue data as Schwartz–Bruhat functions, and descent in positive degree

This file treats the modulus `M ^ c Q`, where `M` and `Q` are the products of two families of places
(the chosen places and the twist places) and `c` is a natural number. For a principal modulus
`(star g)` and a vector `x` with `g x` integral, it writes the translate of the vacuum by `x` as a
combination of the data `New.modDatum` of indicator functions of classes. Finally it proves a lemma
of algebra: if ∏ (T - a i) = 0 with all a i ≠ 0 and ∏ (S T^k - α i a i^k) = 0 for every k > 0, then
∏ (S - α i) = 0.

## Main definitions and results

* `New.Rows.places_levelModulus`: for `c ≠ 0` the places dividing `M ^ c Q` are the places of `M`
  and of `Q`.
* `New.isSchwartzBruhat_residueDatum`: the function `New.residueDatum w f` (`f` of the reductions
  at the places `w i` on matrices integral there, `0` elsewhere) is Schwartz–Bruhat
  (`New.IsSchwartzBruhat`) if no `w i` is conjugate to a `w j`.
* `New.Rows.liftFn_eq_residueDatum`, `New.exists_modulus_places_eq`: it is the lift of a function
  modulo a modulus `New.Modulus`, an ideal prime to its conjugate, with the same set of places;
  such a modulus exists if no `w i` is conjugate to a `w j`.
* `New.exists_rho_finVec_vacElem_eq_sum_modDatum`: if `𝔪 = (star g)` and `g x` is integral, the
  translate of the vacuum by `x` is a combination of the data `New.modDatum` of the indicator
  functions of classes modulo `𝔪`, with values of `New.stdLattice.selfDualAddChar` as coefficients.
* `New.GaloisRep.eval₂_prod_eq_zero_of_mul_pow`: the lemma of algebra just stated, for S and T in a
  ring that commute with the image of a ring homomorphism from a field K.

Notions from other files:
* `New.Modulus.liftFn`: A function Ψ of vectors mod 𝔪, read on finite adelic vectors: Ψ of the
  reduction if the vector is integral at the places of 𝔪 (`New.Modulus.places`), and 0 otherwise.

## Relation to the literature

Known; see `Lib.Weil.MixedModel.ZeroTerm` for sources.



## The level modulus of a set of chosen places and its places

For chosen places `S` (`New.LevelPlaces`: two finite families, with products `M` and `Q`, no place
conjugate to itself or to another), `New.LevelPlaces.levelModulus S c b` is the modulus `M ^ c Q` or
`M ^ c`, according to `b`.


### `Rows.prod_places_le_iff`

 The product of finitely many places `u i` of `E` is contained in the prime of a place `w` if and
only if `w` is one of the `u i`. 

### `LevelPlaces.levelModulus`

 The modulus M^c·Q if b is true and M^c otherwise, with M and Q the products of the places
`New.LevelPlaces.chosenPlace` and `New.LevelPlaces.twistPlace` of S. 

### `LevelPlaces.ideal_levelModulus_one`

 The modulus M·Q is the product of the chosen places and the twist places of S. 

### `LevelPlaces.ideal_levelModulus_one_false`

 The modulus M is the product of the chosen places of S. 

### `Rows.places_levelModulus`

 Let `S` be a choice of chosen places and twist places of `E`, with products `M` and `Q`. For
`c ≠ 0` (the instance `NeZero c`), the places that divide the modulus `S.levelModulus c = M ^ c Q`
are the chosen places and the twist places. 

### `Rows.levelResidueAt`

 For c ≠ 0 and a place dividing M or Q, the reduction from the residue ring modulo M^c·Q to the
residue field at that place. 

### `Modulus.mem_places_of_ideal_eq_prod`

 If the ideal of 𝔪 is the product of the primes u i, then every u i divides 𝔪. 

### `Modulus.matrix_eq_iff_map_modulusResidue_eq`

 The injectivity in the Chinese remainder theorem: if the ideal of 𝔪 is the product of the
distinct primes u i, two matrices over O_E/𝔪 are equal if and only if their reductions at every
u i are equal. 

 ## Residue data and translates of the vacuum 

### `Rows.reductionGL_map_modulusResidue`

 For a place `w` dividing the modulus `𝔪` and an element `k` of the integral finite adelic
unitary group `stdLevel E n`, reducing `k` modulo `𝔪` (`reductionGL`) and then modulo `w`
(`modulusResidue`) is the reduction `stdLevel.reduceAt w k` of `k` at `w`. 

### `Rows.liftFn_eq_residueDatum`

 If the places of `𝔪` are the `w i`, then `New.residueDatum w f` (`f` of the reductions at the
`w i` on matrices integral there, `0` elsewhere) is the lift `New.Modulus.liftFn` to adelic vectors
of the function that sends a matrix `T` modulo `𝔪` to `f` of the reductions `modulusResidue` of `T`
at the `w i`; `vecToMatrix` reads a vector indexed by `n' × n` as a matrix. 

### `exists_modulus_places_eq`

 If no `w i` is conjugate to a `w j`, there is a modulus whose places are the `w i` and which
contains the intersection of these primes. 

### `isSchwartzBruhat_residueDatum`

 If no `w i` is conjugate to a `w j`, then `New.residueDatum w f` (`f` of the reductions at the
`w i` on matrices integral there, `0` elsewhere) is Schwartz–Bruhat at the places `w i`: it depends
only on the components there and, as a function of these, is locally constant of compact support. 

### `modDatum_vacVector`

 The datum `New.modDatum` of a function `Ψ` on matrices modulo `𝔪` with the Gaussian
`Fock.vacVector` as real part is what the operator `schrodingerOp` of the lift of `Ψ` (`vecToMatrix`
reads vectors as matrices) makes of the vacuum `vacElem` of `V.hom V' = Hom(V, V')`. Here
`V : Space E n s` and `V' : Space E n' s'` have signs `s`, `s'` (units ±1), and `E` carries a CM
type (`CMType E`) and Weil data (`WeilData E`). For a function `Φ` on finite adelic vectors,
`New.Space.schrodingerOp W P Φ` is the operator on `𝒮 W` (the space on which `W.ϱ` acts, which
contains the vacuum `vacElem`) that realizes `Φ` at the places `P`: the combination of Heisenberg
translations whose counterpart in the Schrödinger model at `P` carries the indicator of the integral
vectors to `Φ`, if there is one. 

### `exists_rho_finVec_vacElem_eq_sum_modDatum`

 Let the ideal of the modulus `𝔪` be `(star g)`, and let `x` be a finite adelic vector of
`V.hom V' = Hom(V, V')` with `g x` in `Ô E` (integral). Apply the Heisenberg operator `ϱ` of
`New.finVec x` (finite part `α x`, where `α` is the finite idele of the Weil data; real part zero)
to the vacuum `vacElem`. The result is `∑_T New.stdLattice.selfDualAddChar E (z T) • New.modDatum V
V' 𝔪 (Pi.single T 1) Fock.vacVector` for some `z`, where `T` runs over the matrices modulo `𝔪`, and
each datum has real part the Gaussian `Fock.vacVector`, equals the lift of the indicator of `T` at
the places dividing `𝔪`, and equals the vacuum elsewhere. 


## Relations for S T^k in positive degree give the relation for S


### `New.GaloisRep.aeval_prod_eq_zero_of_mul_pow`

 Let `S`, `T` lie in a `K`-algebra `Z` and let `α i`, `a i` be scalars with `a i ≠ 0`. If
`∏ (T - a i) = 0`, and `∏ (S T ^ k - α i * a i ^ k) = 0` for all `k > 0`, then `∏ (S - α i) = 0`. 

### `New.GaloisRep.eval₂_prod_eq_zero_of_mul_pow`

 Let `g : K →+* A` be a ring map from a field `K`, let `S`, `T` in `A` commute with the image of
`g`, and let `α i`, `a i` in `K` with `a i ≠ 0`. If `∏ (T - g (a i)) = 0`, and
`∏ (S T ^ k - g (α i * a i ^ k)) = 0` for all `k > 0`, then `∏ (S - g (α i)) = 0`. 
