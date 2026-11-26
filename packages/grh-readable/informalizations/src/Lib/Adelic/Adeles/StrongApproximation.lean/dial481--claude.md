---
{
  "module": "src/Lib/Adelic/Adeles/StrongApproximation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Adeles/StrongApproximation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Adeles/StrongApproximation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Standard character, self-duality, strong approximation and one-sided Poisson summation

Let `E` be a totally complex field with adele ring `New.𝔸 E`, and let `New.toAdele` be the diagonal
embedding of `E`. `New.stdAddChar` is the standard additive character, and its finite part `New.ψf`
is trivial on the integral adeles `New.Ô`. The file shows that, over a CM field, rational points of
unitary groups are discrete in the adelic group. It treats the conductor and nondegeneracy of the
character, proves that `E` is its own annihilator (also for matrices), and proves strong
approximation for adeles and adelic matrices. It ends with a one-sided Poisson summation inequality
and the compact open group given by the inverse different among self-adjoint finite adeles.

## Main definitions and results

* `New.Space.discreteTopology_Gamma`: `New.Space.Γ` is discrete, because the rational matrices
  `New.ratMatrices` are discrete among the adelic ones. So the image under `New.Space.ratEmbed` of
  any subgroup is discrete.
* `New.stdAddChar_toAdele`, `New.mem_ratAdeles_of_stdAddChar_eq_one`: for `E` totally complex,
  `New.stdAddChar` is trivial on `E`. An adele that pairs trivially with all of `E` lies in `E`. So
  `E` is its own annihilator.
* `New.isDualFamily_ratAdeles`: the characters `x ↦ stdAddChar E (toAdele a * x)`, `a : E`, form a
  dual family for the adeles modulo `E`.
* `New.isDualFamily_ratMatrices`: the same for matrices, with the trace pairing.
* `New.strong_approximation`: strong approximation; `E` plus the adeles supported on a nonempty set
  `S` of finite places is dense in the adeles.
* `New.Exchange.denseRange_rat_matrix_add`: strong approximation for matrices.

Notions from other files:
* `New.𝔸f E`, `New.Ô E`: the finite adeles of `E` and the subring of integral finite adeles.
* `New.PlaceEmbedding.Φ`: a chosen complex embedding `Φ w` of `E` for each infinite place `w`; the
  adele ring `New.𝔸 E` is the product of one copy of `ℂ` for each `w` with `New.𝔸f E`.
* `New.ratAdeles`, `New.ratMatrices`: the images of `E` and of the matrices over `E` under
  `New.toAdele`, as additive subgroups.
* `New.IsDualFamily B₀ χ`: `i ↦ χ i` is an injective homomorphism to the continuous unitary
  characters trivial on `B₀`, and the common kernel of the `χ i` lies in `B₀`.

## Relation to the literature

Known result: Self-duality of a number field in its adeles, strong approximation and a Poisson
inequality. For totally complex fields only, the field is shown to be its own annihilator and the
pairing is shown to be non-degenerate. Strong approximation omits a nonempty set of finite places
and is deduced from duality. Poisson summation is proved only as an inequality, for nonnegative
integrable functions that are lower semicontinuous at the rational points of the sum. Source: J.
Tate, Fourier analysis in number fields and Hecke's zeta-functions, thesis 1950, in Cassels-Fröhlich
ch. XV, Theorem 4.1.4; for strong approximation, Cassels, ch. II §15.

See also `Lib.Adelic.Unitary.WeakApproximation`.



## Rational points of a space embed injectively and discretely

For a hermitian space `V = (J, x)` (`New.Space`: a matrix `J` over the CM field `E` and an adelic
change of basis `x` that brings it to the standard form), `New.Space.ratEmbed` sends a rational
point `γ` of the unitary group of `J` to `x⁻¹ γ x` in the adelic group `New.G` (its underlying
adelic matrix is `adeleMatrix`), and `New.Space.embFin` is its finite part.


### `instance {E : Type*} [Field E] [NumberField E] : Nontrivial (𝔸f E)`

 The ring of finite adeles is nontrivial, since it maps to the completion at a finite place. 

### `xFin`

 For a space `V = (J, x)`, the finite part of the change of basis `x`, in `GL n (𝔸f E)`. 

### `coe_embFin`

 For a space `V = (J, x)` and `γ` in the rational unitary group `U V.J`, the finite part
`V.embFin γ` of `x⁻¹ γ x` is, in `GL n (𝔸f E)`, the conjugate of `γ` by the finite part
`V.xFin` of `x`. 

### `_root_.New.stdSpace_embFin`

 For the standard space (`J = 1`, `x = 1`), the finite part of the embedding of rational points
applies `E → 𝔸f E` to each entry. 

### `fact_embFin_injective`

 The finite part `New.Space.embFin` of the embedding of rational points is injective. 

### `discreteTopology_Gamma`

 The group `V.Γ = x⁻¹ U(J)(E) x` of rational points of a space `V = (J, x)` is discrete, because
the rational matrices are discrete among the adelic ones. 

### `instance {S : Subgroup (U V.J)} : DiscreteTopology (Subgroup.map V.ratEmbed S)`

 The image in the adelic group of any subgroup of the rational points is discrete. 


## The standard adelic additive character: conductor, nondegeneracy, E self-dual

The finite part `New.ψf` sends `a` in `E` to exp(2πi Tr a).

* `New.forall_ψf_mul_eq_one_iff`: the annihilator of `New.Ô` is given by the inverse different.


 ### The finite character 

### `isOfFinOrder_ψf`

 The values of the character `ψf E` of the finite adeles are roots of unity. 

### `stdAddChar_eq_mul_ψf`

 The standard character at an adele `x` is `exp (-2πi ∑ w, 2 Re x_w)`, the sum being over the
infinite places, times `ψf E` of the finite part. 

### `exists_ψf_eq_fourierChar`

 Every value of `ψf E` is `exp (2πi q)` for a rational number `q`. 

### `forall_ψf_mul_eq_one_iff`

 For a finite adele `x` of `E`, the character `ψf E` (the finite part of the standard additive
character) is trivial on `u * x` for all integral finite adeles `u ∈ Ô E` if and only if `d * x`
is integral for every `d` in the different of `E` over `ℚ`. 

### `eq_zero_of_forall_mul_integral`

 A finite adele all of whose multiples are integral is zero. 

### `eq_of_forall_ψf_mul_eq`

 The pairing given by `ψf E`, the finite part of the standard additive character, separates
finite adeles: if `ψf E (t * a) = ψf E (t * b)` for all finite adeles `t`, then `a = b`. 

### `ψf_star`

 For a CM field `E`, the character `ψf E` is invariant under complex conjugation `star` of finite
adeles. 

 ### Norm and trace through the chosen embeddings 

### `abs_norm_eq_prod_norm_sq`

 For `E` totally complex, the absolute norm of `x` is the product of the `‖Φ v x‖ ^ 2` over the
infinite places `v`, where `Φ v` is the chosen embedding at `v`. 

### `one_le_prod_norm_Φ`

 For a nonzero algebraic integer `y` of a totally complex field, the product of the `‖Φ v y‖`
over the infinite places `v` is at least one; `Φ v` is the chosen embedding at `v`. 

### `trace_eq_sum_Φ`

 For `E` totally complex, the trace of `x` is `∑ w, 2 Re (Φ w x)` over the infinite places `w`,
where `Φ w` is the chosen embedding at `w`. 

 ### The annihilator of the rational points 

### `stdAddChar_toAdele`

 For `E` totally complex, the standard additive character `stdAddChar E` of the adeles is trivial
on the diagonal image of `E`. 

### `exists_eq_Φ_of_forall_sum_re_rat`

 Let `E` be totally complex, with chosen embeddings `Φ w` at the infinite places `w`.
If `∑ w, 2 * Re (Φ w b * z w)` is rational for every `b` in `E`, then
`z = fun w ↦ Φ w a` for some `a` in `E`. The factor `2` is the one in `New.trace_eq_sum_Φ`. 

### `mem_ratAdeles_of_stdAddChar_eq_one`

 For `E` totally complex, an adele `x` with `ψ (a x) = 1` for all `a` in `E` lies in the diagonal
image `ratAdeles E` of `E`. Here `ψ = stdAddChar E` is the standard additive character. 

### `eq_zero_of_forall_stdAddChar_eq_one`

 For `E` totally complex, the pairing `ψ (u x)` on the adeles given by the standard character
`ψ = stdAddChar E` is nondegenerate: if `ψ (u x) = 1` for all adeles `u`, then `x = 0`. 

 ## A totally complex field is its own annihilator in its adeles, also for matrices 

### `ψf_inv_two_mul_add_star`

 For a CM field `E`, the character `ψf E` (the finite part of the standard additive character)
takes the same value at a finite adele `x` and at its self-adjoint part `(x + star x) / 2`. 

### `stdAddChar_inv_two_mul_add_star`

 For a field `E` with a CM type, the standard additive character `stdAddChar E` takes the same
value at an adele `x` and at its self-adjoint part `(x + star x) / 2`, where `star` is complex
conjugation and `toAdele` the diagonal embedding of `E`. 

### `isDualFamily_ratAdeles`

 A totally complex field `E` is its own annihilator in its adeles (Tate). Let
`ψ = stdAddChar E`. The characters `x ↦ ψ (a x)`, `a : E`, form a dual family (`IsDualFamily`): they
are continuous, unitary and trivial on the image `ratAdeles E` of `E`; they depend additively and
injectively on `a`; and an adele killed by all of them lies in `ratAdeles E`. 

### `isDualFamily_ratMatrices`

 Self-duality for matrices. Let `ψ = stdAddChar E` be the standard character of the adeles. For
an `n × m` matrix `a` over `E`, consider the character `x ↦ ψ (tr (a x))` of the `m × n` adelic
matrices. These characters form a dual family (continuous unitary characters depending additively
and injectively on `a`) for the image `ratMatrices E m n` of the `m × n` matrices over `E`: they are
trivial on it, and their common kernel lies in it. 


## Strong approximation for adeles and density of E at infinity

* `New.Exchange.idemAdele`: the idempotent adele that is `1` at the finite places in `S` and `0`
  elsewhere.


### `instance : Infinite (FinPlace E)`

 A number field has infinitely many finite places, since they surject onto the primes. 

### `Exchange.idemAdele`

 The idempotent adele with component `1` at the finite places in `S`, and `0` at the other finite
places and at all infinite places. 

### `eq_zero_of_forall_stdAddChar_mul_idemAdele`

 If `S` is a nonempty set of finite places and the character `y ↦ ψ (r y)`, with `r : E` and `ψ`
the standard character, is trivial on all adeles `idemAdele S * u` supported on `S`, then
`r = 0`. 

### `strong_approximation`

 Strong approximation for a totally complex field `E`. Let `S` be a nonempty set of finite
places. The sums `toAdele r + Exchange.idemAdele S * u`, with `r : E` and `u` an adele, are dense
in the adeles. These are the sums of an element of `E` and an adele that vanishes at infinity and
at the finite places outside `S`. 

### `denseRange_Φ`

 The image of a totally complex field `E` under the embeddings `Φ w` chosen by
`PlaceEmbedding E`, one for each infinite place `w`, is dense in the product of copies of `ℂ`. 

 ## Strong approximation for adelic matrices 

### `New.Exchange.denseRange_rat_matrix_add`

 Strong approximation for matrices over a field `E` with a CM type. Let `S` be a nonempty set of
finite places and `x` an invertible `n × n` adelic matrix. The matrices `x⁻¹ A + idemAdele S • B`,
with `A` over `E` and `B` adelic, are dense in the `n × m` adelic matrices. Here `idemAdele S` is
the adele that is `1` at the places in `S` and `0` at all other places. 


## One-sided Poisson summation on the adeles

The main result is `New.IsDualFamily.sum_le_of_fourier`: a finite sum of a non-negative integrable
function over rational points is at most any bound for the finite sums of the absolute values of its
Fourier transform over `E`. Only lower semicontinuity at these points is needed. The proof smooths
the function by a bump on the compact quotient of the adeles by `E` (`New.ratAdeles`) and applies
Fourier inversion there, with the standard character `New.stdAddChar`.


### `IsDualFamily.quotMean_stdAddChar_mul_integral`

 Smooth an integrable function `F` on the adeles by a continuous function `η` on `𝔸 E ⧸ E` with
`|η| ≤ 1`. The Fourier coefficient at `ξ : E` of `z ↦ ∫ η(z + x) F(x) dx` (a mean `quotMean` over
`𝔸 E ⧸ E`: the integral, for the Haar probability measure `addHaarMeasure ⊤`, of the value at a lift
`q.out` of each class `q`) is the coefficient of `η` times the Fourier transform
`∫ ψ(-ξ x) F(x) dx`. Here `ψ = stdAddChar E` is the standard character and `ratAdeles E` the image
of `E` in the adeles. 

### `IsDualFamily.integral_mul_le_of_sum_norm_le`

 Upper bound for `∫ η F` by Fourier inversion on `𝔸 E ⧸ E`. Let `F` be integrable on the adeles
and `η` continuous on `𝔸 E ⧸ E` with values in `[0, 1]`. If `S` bounds the finite sums over `ξ : E`
of the absolute values of the Fourier transform `∫ ψ(-ξ x) F(x) dx`, then `∫ η F ≤ (∫ η) S`. Here
`ψ = stdAddChar E` is the standard character, `ratAdeles E` is the image of `E` under the diagonal
embedding `toAdele`, and `addHaarMeasure ⊤` is the Haar probability measure on the quotient. 

### `IsDualFamily.mul_le_integral_mul_of_le_sum`

 Lower bound for `∫ η F` by folding the integral over `E`. Let `F ≥ 0` be integrable on `𝔸 E`
(for its `volume` measure, which is also used for `∫ x, η x * F x`), let `T` be a finite subset of
the image `ratAdeles E` of `E`, and let `η` be continuous on `𝔸 E ⧸ E` with values in `[0, 1]` and
positive integral; `η x` for `x : 𝔸 E` means `η` evaluated at the class of `x`. If every class at
which `η` is not zero contains a point `u` with `c ≤ ∑ t ∈ T, F (t + u)`, then `(∫ η) * c ≤ ∫ η F`,
where `∫ η` is taken for the Haar probability measure `addHaarMeasure ⊤` on the quotient. 

### `IsDualFamily.sum_le_of_fourier`

 One-sided Poisson summation on the adeles `𝔸 E` of a totally complex number field `E`, with the
diagonal embedding `toAdele` given by the chosen complex embeddings of `PlaceEmbedding`. Let `F ≥ 0`
be integrable and lower semicontinuous at each point of a finite set `T` of rational points
(elements of the image `ratAdeles E` of `E`). Put `F̂(ξ) = ∫ ψ(-toAdele ξ · x) F(x) dx`, where
`ψ = stdAddChar E` and `dx` is the measure `volume` on `𝔸 E`, for which `E` has covolume one (its
`quotMeasure` for `𝔸 E ⧸ E` has mass one); if `S` bounds `∑ ξ ∈ Y, ‖F̂(ξ)‖` for every finite set
`Y ⊂ E`, then `∑ t ∈ T, F t ≤ S`. 


## The inverse different in self-adjoint adeles is compact and open

`New.selfAdjointCodifferent E M` is the group of self-adjoint finite adeles `z` (those with
`z̄ = z`) for which `M z` lies in the inverse different. For `M = 1` it normalises the Haar measure
on the self-adjoint finite adeles.


### `New.selfAdjointCodifferent`

 The additive group of self-adjoint (conjugation-invariant) finite adeles `z` of `E` with
`ψf E (M * z * x) = 1` for all integral finite adeles `x ∈ Ô E`, that is, with `M * z` in the
inverse different. Here `ψf E` is the finite part of the standard additive character. 

### `New.isOpen_selfAdjointCodifferent`

 For a CM field `E` and a finite adele `M`, the group `selfAdjointCodifferent E M` of
self-adjoint finite adeles `z` with `M * z` in the inverse different is open in the self-adjoint
finite adeles. 

### `New.isCompact_selfAdjointCodifferent`

 For a CM field `E` and an invertible finite adele `M`, the group `selfAdjointCodifferent E M` of
self-adjoint finite adeles `z` with `M * z` in the inverse different is compact. 

### `noncomputable instance : MeasureSpace (selfAdjoint (𝔸f E))`

 The Haar measure on the self-adjoint finite adeles that gives `New.selfAdjointCodifferent E 1`
mass one. 

### `instance : IsAddHaarMeasure (volume : Measure (selfAdjoint (𝔸f E)))`

 The volume on the self-adjoint finite adeles is an additive Haar measure. 

### `New.volume_selfAdjointCodifferent_one`

 The group `selfAdjointCodifferent E 1` of self-adjoint finite adeles in the inverse different
has volume one. 
