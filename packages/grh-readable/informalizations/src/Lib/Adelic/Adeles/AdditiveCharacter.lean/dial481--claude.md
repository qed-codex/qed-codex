---
{
  "module": "src/Lib/Adelic/Adeles/AdditiveCharacter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Adeles/AdditiveCharacter.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Adeles/AdditiveCharacter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The additive character, Haar measures and the rational lattice in the adeles

The adeles `New.𝔸` of a number field `E` are one copy of `ℂ` for each infinite place, times the
finite adeles `New.𝔸f`; this is the adele ring when `E` is totally complex. `New.Ô` is the ring of
integral finite adeles. The file defines the standard additive character and the Haar measures
used in Fourier analysis on `New.𝔸`. For a totally complex field `E`, it proves that `E`, embedded
diagonally by `New.toAdele`, is a cocompact lattice of covolume one, and so are vectors and matrices
over `E`. The proof uses a fundamental domain built from a fractional ideal.

## Main definitions and results

* `New.ψf`: the character of the finite adeles that is trivial on `New.Ô` (`New.ψf_eq_one_of_mem`)
  and is `𝐞 (tr a)` on `a ∈ E` (`New.ψf_coe`), where `𝐞 t = exp (2πi t)`. These two properties
  define it, since every finite adele is an element of `E` plus an integral one.
* `New.stdAddChar`: its product with `𝐞 (-∑_w 2 re x_w)`. Here `x_w` is the component of the adele
  at the infinite place `w`.
* `New.volume_Ô`: `volume` on the finite adeles gives `New.Ô` the mass `New.volÔ`. On a completion
  `New.LocField w`, `volume` gives the local integers mass one (`New.volume_LocInt`). On the adeles
  it is the product with Lebesgue measure on each `ℂ`.
* `New.ratAdeles`, `New.ratVectors`, `New.ratMatrices`: the rational points, vectors and matrices.
* `New.HasFundDomain`: a compact set contains a fundamental domain of volume one.
* `New.IsCovolOneLattice`: a discrete cocompact subgroup whose quotient measure has mass one.

Notions from other files:
* `New.LocField`, `New.LocInt`: The completion E_w of E at the finite place w and its ring of
  integers.
* `New.PlaceEmbedding E`: a choice, for each infinite place `w`, of a complex embedding `Φ w` of
  `E` that induces `w`. The map `New.toAdele` uses these embeddings at the infinite places.

## Relation to the literature

For totally complex `E` the file proves a known result: a number field is a discrete subgroup of its
adeles with compact quotient, here with a measure for which the covolume is one.



## A fundamental domain for a fractional ideal and its volume

`New.exists_fundDomain_prod` builds a fundamental domain `F ×ˢ O` for a number field `I` acting by
translations on `V × W` (in the applications: infinite part times finite part of adeles), with `F` a
fundamental parallelotope of a fractional ideal, and gives the volume of `F`.


### `New.exists_fundDomain_prod`

 Let `j : I →+ V × W` be additive on the number field `I`. Assume that the second component of
`j` lies in the subgroup `O` exactly on the fractional ideal `J`, and that `W` is the sum of the
second components and `O`. Assume also that the first component is the Minkowski embedding followed
by a measure-preserving linear isomorphism `e`. Then there is a bounded measurable set `F` in `V`
such that (a) `F` has volume `N(J) 2^(-r₂) √|disc I|`, with `r₂` the number of complex places, and
(b) for each `x` exactly one `a : I` has `j a + x ∈ F ×ˢ O`. 


## The standard additive character and the Haar measures on adeles

Instances give the topological and measurable structure of the adeles, the finite adeles, the
completions `New.LocField w` and the unitary groups `New.U J` of complex matrices.


 ### The standard additive character and the mass of the integral adeles 

### `fourierChar_eq_one_iff`

 The character `𝐞 t = exp (2πi t)` is trivial exactly at the integers. 

### `volÔ`

 The number 2^{r₂}/√|disc E|, where r₂ is the number of complex places of E. When E is totally
complex and the infinite places carry Lebesgue measure, it is the volume of the integral finite
adeles for which the quotient of the adeles by E has total mass one. 

### `mk_algebraMap_surjective`

 Every class of finite adeles modulo `Ô` contains an element of `E`. 

### `fourierChar_trace_eq_one`

 For an algebraic integer `a` of `E`, the value `𝐞 (tr a) = exp (2πi Tr_{E/ℚ} a)` is one. 

### `ψf`

 The standard additive character of the finite adeles: ψ_f(x) = exp(2πi Tr_{E/ℚ}(a)) for any
a in E with x − a integral. 

### `stdAddChar`

 The standard additive character of `New.𝔸 E` (the adele ring when E is totally complex): the
product of exp(−2πi ∑_w 2 Re x_w) over the infinite places and ψ_f of the finite part. 

### `volume_LocInt`

 The chosen Haar measure on the completion `E_w` gives its ring of integers mass one. 

### `volume_Ô`

 For the chosen Haar measure on the finite adeles of E, the ring Ô of integral finite adeles
has volume 2^{r₂}/√|disc E|. 

 ### The finite character, and further instances 

### `ψf_coe`

 On an element `a` of `E` the finite character `ψf` takes the value `exp (2πi Tr_{E/ℚ} a)`. 

### `ψf_eq_one_of_mem`

 The finite character `ψf` is trivial on the ring `Ô E` of integral finite adeles. 

### `isAddHaarMeasure_𝔸`

 The measure `volume` on `New.𝔸 E` (the adeles, when E is totally complex) is an additive Haar
measure. 

 ## Rational points as a cocompact lattice of covolume one 

### `Φ_mk_eq_or_star_eq`

 A complex embedding `φ` is the chosen embedding `Φ` of its place or the conjugate of it. 

 ### Rational points, fundamental domains and lattices 

### `ratAdeles`

 The image of E in its adeles under the diagonal embedding, as an additive subgroup. 

### `ratVectors`

 The additive subgroup of adelic vectors indexed by n that is the image of E^n under the
coordinatewise diagonal embedding. 

### `ratMatrices`

 The additive subgroup of m×n adelic matrices that is the image of the m×n matrices over E
under the entrywise diagonal embedding. 

### `HasFundDomain`

 For an additive map `f : I →+ B` and a set `C` in `B`: `C` is compact and contains a measurable
set `D` of volume one such that every `x` in `B` has exactly one `a` in `I` with `f a + x ∈ D`. 

### `IsCovolOneLattice`

 A lattice of covolume one: a discrete subgroup `Λ` of `B` with `B ⧸ Λ` compact and of quotient
measure one, such that the translates of one compact set by `Λ` cover `B`. 

### `IsCovolOneLattice.exists_compact_cover`

 Some compact set meets every coset of `Λ`. 

 ### From a fundamental domain to a lattice 

### `HasFundDomain.pi`

 If a compact set `C` contains a fundamental domain of volume one for `f : I →+ B`
(`HasFundDomain f C`), then for a finite index type `n` the power `C^n` contains one for the
coordinatewise map `(n → I) →+ (n → B)`. 

### `HasFundDomain.isCovolOneLattice`

 Let `f : I →+ B` be additive, `B` a second countable locally compact Hausdorff abelian group
with Haar measure. If the compact set `C` contains a measurable `D` of volume one whose translates
by the `f a` partition `B` (`HasFundDomain f C`), then the image of `f` is a lattice of covolume
one: it is discrete and cocompact, with quotient measure of mass one. 

 ### The rational points of the adeles and finiteness in compact sets 

### `exists_mixedEquiv`

 Let `E` be a totally complex number field, with a chosen complex embedding `Φ v` for each
infinite place `v`. Some volume-preserving ℝ-linear isomorphism from the Minkowski space of `E` to
`InfinitePlace E → ℂ` sends the Minkowski embedding of each `x : E` to the family `(Φ v x)_v`. 

### `exists_hasFundDomain`

 Let `K` be a number field and `φ : K → V` a ring homomorphism. Let `e` be a volume-preserving
ℝ-linear isomorphism from the Minkowski space of `K` to `V` that turns the Minkowski embedding into
`φ`. Then for some `R > 0` the closed ball of radius `R` in `V` times the integral finite adeles
`Ô K` is compact and contains a fundamental domain of volume one (`New.HasFundDomain`) for the map
`K → V × 𝔸f K` given by `φ` and the diagonal embedding into the finite adeles. 

### `exists_hasFundDomain_toAdele`

 Let `E` be a totally complex number field with chosen embeddings at the infinite places. For
some `R > 0`, the closed ball of radius `R` in the infinite part `InfinitePlace E → ℂ` times the
integral finite adeles `Ô E` is compact and contains a fundamental domain of volume one
(`HasFundDomain`) for `E` acting on its adeles through the diagonal embedding `toAdele`. 

### `isCovolOneLattice_ratAdeles`

 For totally complex `E` the rational points `New.ratAdeles E` form a lattice of covolume one in
the adeles of `E`: a discrete subgroup whose compact quotient has measure one. 

### `isCovolOneLattice_ratVectors`

 For totally complex `E` and finite `n` the rational vectors `New.ratVectors E n` form a lattice
of covolume one in the adelic vectors indexed by `n`. 

### `isCovolOneLattice_ratMatrices`

 For totally complex `E` and finite `m`, `n` the rational matrices `New.ratMatrices E m n` form
a lattice of covolume one in the adelic `m × n` matrices. 

### `finite_preimage_of_discreteTopology_range`

 An injective additive map `f` into a Hausdorff topological group, with discrete image, sends
only finitely many points into a given compact set. 

### `IsCovolOneLattice.finite_preimage`

 Let `f : I →+ B` be an injective additive map whose image is a lattice of covolume one in `B`
(discrete, with compact quotient of measure one). Then for every compact set `C`, only finitely many
`a` in `I` have `f a ∈ C`. 

### `finite_setOf_toAdele_mem`

 For totally complex `E`, a compact set of adeles contains the diagonal images of only finitely
many elements of `E`. 

### `isCovolOneLattice_ratVectors.finite_preimage`

 For totally complex `E` and finite `n`, a compact set of adelic vectors indexed by `n` contains
the coordinatewise diagonal images of only finitely many vectors over `E`. 

### `finite_setOf_map_toAdele_mem`

 For totally complex `E` and finite `m`, `n`, a compact set of adelic `m × n` matrices contains
the entrywise diagonal images of only finitely many matrices over `E`. 
