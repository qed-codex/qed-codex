---
{
  "module": "src/Lib/LocalGL/Shintani/CosetRootChoice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Shintani/CosetRootChoice.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Shintani/CosetRootChoice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Root choices in a coset, induction, and extension of invariant characters

This file treats descent of class functions along a coset, as in Shintani descent. Given
`π : E →* Γ`, `σ ∈ Γ` and `j : G → E`, it defines root choices over `σ`. It defines the induction
`New.induceClassFn` of class functions and proves Frobenius reciprocity for it. It proves that
descent keeps inner products and commutes with induction. It also proves the following for a
`Γ`-invariant irreducible character `Y` of `G` and a virtual character `Φ` of `G ⋊ Γ` with
|Γ|⟨Φ,Φ⟩ = ⟨Φ|G,Φ|G⟩+|Γ|−1 and ⟨Y,Φ|G⟩ = 1+|Γ|m for some m ∈ ℤ. Under these conditions, the
function equal to `Y` on `G` and to `Φ` off `G` is an irreducible character of `G ⋊ Γ`
(`New.IsIrreducibleChar.extend_semidirect`). Here `New.classInner` is the mean of `conj f * h`,
and `New.virtualChars` is the span of the characters.

## Main definitions and results

* `New.DescendsOnCoset`: the function `h` on `E` descends to `f` on `G` over the coset of `σ`:
  `h s = f γ` for every `s : E` with `π s = σ` and every `γ : G` with `s ^ orderOf σ = j γ`.
* `New.IsRootChoice`, `New.exists_isRootChoice`: a conjugation-equivariant choice, for each `γ`, of
  a root `r γ` over `σ` with `r γ ^ orderOf σ = j γ`, and its existence for the units of an algebra
  over a finite field with a semilinear Galois action.
* `New.IsRootChoice.exists_conj_eq_of_map_eq`, `New.IsRootChoice.index_mul_finMean_eq_classInner`:
  the roots meet every class over `σ`, and descent keeps inner products.
* `New.IsRootChoice.descendsOnCoset_comp`: a function `g` invariant under the kernel of `π` descends
  to `g ∘ r`.
* `New.classInner_induceClassFn_of_surjective`: Frobenius reciprocity for `New.induceClassFn` when
  `π ∘ ρ` is onto.
* `New.DescendsOnCoset.induce`: descent commutes with induction.

Notions from other files:
* `New.IsIrreducibleChar`: `f` is an irreducible character, stated as three conditions: (a) `f` is a
  character, (b) `New.classInner f f = 1`, and (c) for every class function `h` and every `y`, `f 1
  * New.classInner f (h (· * y)) = New.classInner f h * f y`.

## Relation to the literature

Known; see `Lib.LocalGL.Shintani.LiftingGreenCharacters` and `Lib.LocalGL.Green.CuspidalFunctions`
for sources.


### `DescendsOnCoset`

 The function `h` on `E` descends to `f` on `G` over the coset of `σ`: `h s = f γ` for every
`s : E` with `π s = σ` and every `γ : G` with `s ^ orderOf σ = j γ`. 

### `conjCount`

 The number of x in the kernel of π with xtx⁻¹ = s, as a complex number. 

### `induceClassFn`

 Induction of f along ρ over Γ: at s, the index of ker(π∘ρ) times the mean over t ∈ E' of
f(t)·#{x ∈ ker π : xρ(t)x⁻¹ = s}. 

### `IsRootChoice`

 j is injective and r(γ) is a conjugation-equivariant (ord σ)-th root of j(γ) over σ, such
that any x ∈ ker π conjugating one r(δ) to an r(γ) lies in j(G). 

### `IsRootChoice.injective`

 The homomorphism `j` is injective. 

### `IsRootChoice.map_apply`

 `r γ` lies over `σ`. 

### `IsRootChoice.pow_orderOf`

 The power of `r γ` by the order of `σ` is `j γ`. 

### `IsRootChoice.map_conj`

 The choice of roots is equivariant for conjugation by `G`. 

### `IsRootChoice.mem_range_of_conj`

 An element of the kernel of `π` that conjugates a chosen root to a chosen root lies in the
  image of `j`. 

 ### Induction of class functions 

### `conjCount_conj`

 Conjugating `s` by `y` and `t` by `u`, where `u` and `y` have the same image under `π`, does not
change the number of elements of the kernel of `π` that conjugate `t` to `s`. 

### `classInner_induceClassFn_of_surjective`

 Frobenius reciprocity for `induceClassFn`: let `ρ : E' →* E` with `π ∘ ρ` onto `Γ`, `h` a
function on `E'`, and `χ` a class function on `E`. Then the inner product of `χ` with the induction
of `h` equals the inner product of `χ ∘ ρ` with `h`. Here `induceClassFn π ρ h` at `s` is the index
of ker(π∘ρ) times the mean over t ∈ E' of h(t)·#{x ∈ ker π : xρ(t)x⁻¹ = s}. 

### `induceClassFn_mem_virtualChars`

 Let `π ∘ ρ` be onto. If `h` is a `Z`-linear combination of characters of `E'`, then so is its
induction `induceClassFn π ρ h` to `E`. 

 ### Semidirect products: existence of roots, extension of characters 

### `exists_isRootChoice`

 Let `S` be an algebra over the finite field `k'`, let `σ ∈ Gal(k'/k)` act on `Sˣ` through a
`σ`-semilinear ring endomorphism `τ`, and let `j` embed the finite group `G` onto the units fixed by
`σ`. Then there is `r : G → Sˣ ⋊ Gal(k'/k)` such that (a) `r` is a root choice: each `r γ` lies over
`σ`, is an `(ord σ)`-th root of `j γ` and is compatible with conjugation, and any unit conjugating
some `r δ` to some `r γ` lies in `j(G)`; and (b) the unit part of `r γ` lies in every
`k'`-subalgebra that contains `j γ`. 

### `instance : Finite (G ⋊[α] Γ)`

 A semidirect product of finite groups is finite. 

### `finMean_ite`

 On a semidirect product `G ⋊ Γ`, take the function equal to `u` on `G` and to `w` off `G`. Its
mean is the mean of `w` plus the difference of the means of `u` and `w` over `G`, divided by
`|Γ|`. 

### `IsIrreducibleChar.extend_semidirect`

 Let Y be a Γ-invariant irreducible character of G, Φ a virtual character of G⋊Γ with
|Γ|⟨Φ,Φ⟩ = ⟨Φ|G,Φ|G⟩+|Γ|−1 and ⟨Y,Φ|G⟩ = 1+|Γ|m, m ∈ ℤ. Then the function equal to Y on G
and Φ off G is an irreducible character of G⋊Γ. 

### `IsRootChoice.rangeInKer`

 For a choice of roots `r`, the image of `j` in the kernel of `π`. 

### `IsRootChoice.conjRoot`

 For a choice of roots `r`, the map `(x, γ) ↦ x r(γ) x⁻¹` from `(ker π ⧸ j(G)) × G` to the coset
of `σ`, with `x` the chosen representative of its class. 

### `IsRootChoice.card_preimage_eq`

 For a choice of roots, the coset of `σ` has as many elements as the kernel of `π`. 

### `IsRootChoice.bijective_conjRoot`

 For a choice of roots, `IsRootChoice.conjRoot` is a bijection onto the coset of `σ`: it is
injective by `IsRootChoice.mem_range_of_conj`, and both sides have `|ker π|` elements. 

### `IsRootChoice.exists_conj_eq_of_map_eq`

 For a choice of roots `r`, every element `s` of `E` over `σ` is conjugate to some `r γ` by an
element of the kernel of `π`. 

### `IsRootChoice.index_mul_finMean_eq_classInner`

 For a choice of roots `r`, let `h` and `g` descend on the coset of `σ` to `f` and `f'` and be
invariant under conjugation by the kernel of `π`. Then the index of the kernel times the mean of
`conj h * g` over `E`, taken as zero off the coset of `σ`, is the inner product of `f` and `f'`. 

### `IsRootChoice.restrict_subgroup`

 A choice of roots restricts to a subgroup `H` of `E` and its preimage `H₀` in `G`, if the
roots of the elements of `H₀` lie in `H`. 

### `IsRootChoice.descendsOnCoset_comp`

 Given a choice of roots `r`, a function `g` on `E` that is invariant under conjugation by the
kernel of `π` descends on the coset over `σ` to `g ∘ r`. 

### `IsRootChoice.conjCount_root`

 For a choice of roots `r`, the number of elements of the kernel of `π` that conjugate `r δ` to
`r γ` is the number of `v : G` with `δ = v⁻¹ * γ * v`. 

### `DescendsOnCoset.induce`

 Descent commutes with induction. Let `ρ₀ : G' → G` be compatible with `ρ : E' →* E`, with
choices of roots on both sides. If the class function `h` descends to `f`, and the class function
`F` is induced from `f` along `ρ₀` in the sense of Frobenius reciprocity (`hF`), then
`induceClassFn π ρ h` (the index of ker(π∘ρ) times the mean over t of h(t)·#{x ∈ ker π :
xρ(t)x⁻¹ = s}) descends to `F`. 
