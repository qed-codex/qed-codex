---
{
  "module": "src/Lib/Shimura/TraceFormula/TestFunction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/TraceFormula/TestFunction.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/TraceFormula/TestFunction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Test vectors, and the regular Hecke element that does not kill them

A test vector has a cuspidal type at one split place and is spherical at another.

* `New.Variety.exists_local_hecke_element`: a Hecke element that averages against a character at one
  place.
* `New.Variety.exists_test_function`: the test function `b₁ b₀`, with `b₀` averaging against the
  type at `w₀` and `b₁` acting as a central translate of an injective operator `U_t` at `w₁`.

Conventions: `New.Variety.levelGU` is the principal level `K(𝔑)`, `New.Variety.conjAtSplit` embeds
`GL(E_w)` at a split place `w` into the adelic group, `New.Variety.GU` is the group of similitudes
of the standard form, `New.proIwahori` is the pro-p Iwahori subgroup, and `New.Variety.heckeAlgebra`
is the Hecke algebra inside the group ring, acting through `asAlgebraHom`.

Notions from other files:
* `New.Variety.SplitFinPlace`: The finite places w of E with w̄ ≠ w, that is, those split over the
  maximal real subfield.
* `New.Variety.IsRegularHecke`: f is regular if f(x⁻¹y⁻¹x) ≠ 0, with y in GL_n(E) and x adelic,
  forces the characteristic polynomial of y to be separable.
* `New.Variety.dualComponent`: The inverse transpose of the component at a split place; a left
  inverse of `New.Variety.conjAtSplit`.
* `New.iwahoriHeckeHom`: t ↦ U_t, the mean over `New.proIwahori` composed with the action of a
  dominant diagonal t, on the vectors fixed by `New.proIwahori`.
* `New.Variety.GUPlus`: The monoid of similitudes `g` whose inverse has integral entries, that is,
  which enlarge the standard lattice.

## Relation to the literature

Known; see `Lib.Shimura.TraceFormula.MarkedDefiniteSums` for sources.


### `IsTestVector`

 `v` is a test vector for `π` at the split places `w₀` and `w₁`: it is nonzero, has the
cuspidal type `(J, χ)` at `w₀` and is spherical at `w₁`. The local groups act through
`conjAtSplit`, and the level at `w` is the preimage of `levelGU (Fin a) 𝔑` under
`conjAtSplit w`. 

### `IsTestVector.place_ne`

 The two places are distinct. 

### `IsTestVector.notMem_star_fst`

 `𝔑` does not lie in the conjugate of `w₀`. 

### `IsTestVector.mem_snd`

 `𝔑` lies in `w₁`. 

### `IsTestVector.notMem_star_snd`

 `𝔑` does not lie in the conjugate of `w₁`. 

### `IsTestVector.level_le`

 The level at `w₀` lies in `J`. 

### `IsTestVector.le_localIntGL`

 `J` lies in the maximal compact subgroup at `w₀`. 

### `IsTestVector.isCuspidalType`

 `χ` is non-trivial on the part of `J` in every unipotent radical. 

### `IsTestVector.level_le_proIwahori`

 The level at `w₁` lies in the pro-`p` Iwahori subgroup. 

### `IsTestVector.ne_zero`

 The vector is nonzero. 

### `IsTestVector.isEigenvector`

 `J` acts on `v` by `χ`. 

### `IsTestVector.fixed`

 The maximal compact subgroup at `w₁` fixes `v`. 

### `exists_local_hecke_element`

 Averaging at one split place `w` of the CM field `E` whose conjugate does not contain `𝔑`, for a
representation `π` of `GL_a(𝔸f E)` on `W`, with the local group `GL_a(E_w)` acting through
`conjAtSplit w`. Let `J ≤ GL_a(O_w)` contain the local level, let `χ` be a character of `J` trivial
on it, let `t ∈ GL_a(E_w)`, and let `z` be central with `z · conjAtSplit w t` in `GUPlus`. Then some
Hecke element `b` is supported on the elements `conjAtSplit w j * z * conjAtSplit w t` for `j ∈ J`,
sends vectors of level `𝔑` to vectors on which `J` acts by `χ`, and satisfies `(T * π z⁻¹)(b x) = y`
for every endomorphism `T` of `W` and all `x`, `y` with `T(π(conjAtSplit w (j t)) x) = χ j • y` for
all `j ∈ J`. 

### `dominant_doubleCoset_mul`

 `I t I · I s I ⊆ I (t s) I` for the pro-`p` Iwahori subgroup `I = proIwahori` and dominant
diagonal `t`, `s`. 

### `strictlyDominantAt`

 The adelic elements `g` such that `dualComponent w g`, the inverse transpose of the component
of `g` at `w`, lies in a double coset `I s I`, where `I = proIwahori` and `s` is diagonal and
strictly dominant. 

### `mul_mem_strictlyDominantAt`

 The set `New.Variety.strictlyDominantAt w` is closed under products. 

### `isRegularHecke_of_strictlyDominantAt`

 Let `f` be a Hecke element of level `𝔑` that is a combination of basis elements [g] with
`dualComponent w g` in some `I s I`, for `I = proIwahori` and `s` diagonal strictly dominant.
Suppose `𝔑 ∉ w̄` and the pullback of `levelGU` under `conjAtSplit w` lies in `I`. Then `f` is
regular: for `y ∈ GL_a(E)` and adelic `x`, if f(x⁻¹y⁻¹x) ≠ 0 then the characteristic polynomial of
`y` is separable. 

### `isRegularHecke_pow_succ_of_strictlyDominantAt`

 The positive powers of a Hecke element whose terms are strictly dominant at `w` are regular, if
the level at `w` lies in `proIwahori` and `𝔑` does not lie in the conjugate of `w`. 

### `exists_iwahori_hecke_element`

 Let the level at `w` lie in `proIwahori` and let `𝔑` not lie in the conjugate of `w`. Then some
Hecke element `b` sends vectors of level `𝔑` to vectors fixed by `proIwahori`, kills no nonzero
vector fixed by `proIwahori`, and commutes with every `c` whose terms are similitudes trivial at
`w`; the terms of `b * c` are strictly dominant at `w`. 

### `asAlgebraHom_mem_levelSpace_of_mem_levelSpace`

 An element of the Hecke algebra of level `𝔑` sends vectors of level `𝔑` to vectors of level
`𝔑`. 

### `exists_test_function`

 The test function. Let `π` be a representation of `GL_a(𝔸f E)` on `W`, and let `φ` be a test
vector of level `𝔑` (nonzero, of cuspidal type `(J, χ)` at `w₀` and spherical at `w₁`). Suppose `φ`
is fixed by a Hecke element `c` supported on unitary similitudes whose component at `w₁` is `1`.
Then there is a Hecke element `b` such that no power of `b * c` kills `φ`, and every positive power
is regular (nonzero at `x⁻¹y⁻¹x`, `y ∈ GL_a(E)`, only if `y` has separable characteristic
polynomial). Every positive power also sends vectors of level `𝔑` to vectors on which `J`, through
`conjAtSplit w₀`, acts by `χ`. 
