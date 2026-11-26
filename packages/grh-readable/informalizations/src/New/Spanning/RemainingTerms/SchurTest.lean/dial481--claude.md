---
{
  "module": "src/New/Spanning/RemainingTerms/SchurTest.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/SchurTest.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/SchurTest.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Schur's test: Cauchy–Schwarz and integration in stages

The amplitude majorant of a term is bounded by Cauchy–Schwarz with a weight that is inverted when
the two frames are exchanged. The resulting integrals are bounded by a mean over the unipotent
elements that fix the frame. The frame is the list of basis vectors e₁, …, e_ϱ, z of the hermitian
space: one isotropic vector from each hyperbolic plane and the vector z of negative norm.

## Main definitions and results

* `New.Filling.boxCutoff`: the cutoff restricted to the set `New.Filling.boxedPoints`.
* `New.Filling.besselCutNormSq`: the squared norm of the cut Bessel function.
* `New.Filling.amplitudeMajorant_sq_le`: Cauchy–Schwarz with the weight `New.Filling.schurWeight`, a
  boxed cutoff times powers of `New.volumeRatio`, bounds the square of
  `New.Filling.amplitudeMajorant` by a product of two integrals `New.Filling.schurIntegral`.
* `New.Filling.lintegral_boxCutoff_le_of_average`: integration in stages.

Notions from other files:
* `New.Filling.classCutoff`: the cutoff of a class at the infinite places.
* `besselU0`: the unipotent elements that fix the frame; `classUnipotent₀ c` is the group of
  rational such elements in the class `c`.


### `boxCutoff`

 The cutoff of the class `c` at the infinite places, restricted to the boxed points: the reduced
points with every component in the cut. 

### `besselCutNormSq`

 The squared norm of the cut Bessel function at a point `y` at the infinite places: the product
over the places `v` of the squared norms of the local cut Bessel functions at `y v`. 

### `schurWeight`

 The weight of Schur's test for the class `c` and the rational element `γ`: the product over the
places `v` of `ν_v ^ (-(k + i))`, where `ν_v` is the ratio of the volumes of the projections of
the frame of `γ` and of the standard frame to the negative space of `y v`, times the boxed cutoff of
`c` at `γ⁻¹ y`. The natural number `i`, the shift, only changes this exponent. 

### `schurIntegral`

 One of the two factors that the Cauchy–Schwarz inequality gives in Schur's test: the integral
of the boxed cutoff of `c`, the squared norm of the cut Bessel function and the weight for `c'`
and `γ` with shift `i`. 

### `inCut_of_besselKernel_ne_zero`

 Let `S` be data of the filling theorem over the CM field `E`, let `γ` be a rational element of
the unitary group and `y` a point at the infinite places. If the cut Bessel kernel of `γ`, the
tensor of the cut Bessel functions at `y` and at `γ⁻¹ y`, is nonzero, then at every infinite place
`v` both components lie in the cut. By definition `InCut g b` says exactly that
`besselLength g ≤ b ^ (6 * 𝔰.n + 2)`. 

### `measurable_schurWeight`

 The weight of Schur's test is measurable. 

### `amplitudeMajorant_sq_le`

 **Cauchy–Schwarz.** Let `S` be data of the filling theorem over the CM field `E`, which contains
a primitive root of unity of order `5040`, and let `S` be admissible: its level is the preimage of
the principal congruence subgroup, reduction is onto, and the size inequalities hold. Let `c`, `c'`
be classes and `γ` a rational element of the unitary group. The square of the amplitude majorant
(the integral of the cutoffs of `c` at `y` and of `c'` at `γ⁻¹ y` against the norm of the cut Bessel
kernel) is at most the product of the Schur integrals for `(c, c', γ)` and `(c', c, γ⁻¹)`. 

### `lintegral_cutoff_mul_eq_mul_right`

 On a unimodular group `G`, let a countable group `Γ` act on the left through `i`, let `p` be a
cutoff, that is, a function whose translates under `Γ` sum to one, and let `F` be invariant under
`Γ`. The integral of `F` against `p` does not change when `F` is translated on the right. 

### `lintegral_cutoff_mul_le_of_average`

 On a unimodular group `G`, let `p` be a cutoff for a countable group `Γ` acting on the left
through `i` and let `F` be invariant under `Γ`. If the mean of `F (u * t x)` over `x ∈ B` is at most
`C` for all `u`, then the integral of `F` against `p` is at most `C` times that of `p`. 

### `enorm_besselSystem_cut_mul`

 The norm of the cut Bessel function is left invariant under the unipotent group `besselU`,
which acts on the function by a unitary character. 

### `lintegral_classCutoff_mul_sq_le`

 Let `S` be data of the filling theorem over the CM field `E`, which contains a primitive root of
unity of order `5040`, and let `S` be admissible. For every class `c`, the integral over the
archimedean points `y` of `S.classCutoff c y` times `S.besselCutNormSq y` is at most
`S.unipotentCovolume`, the common covolume of the unipotent groups of the classes, times the number
`card S.BesselCoord` of Bessel coordinates. 

### `lintegral_eq_lintegral_orbit`

 Let `𝔰.G₁` be the complex unitary group of the shape `𝔰`. Let `f` be measurable on the product
of its copies at the infinite places of the CM field `E`. The integral of `f` is an iterated
integral. The inner one runs over the orbit of `a` under `besselU0`, the unipotent elements that fix
the frame vectors e₁, …, e_ϱ, z, with the measure `𝔰.besselHaar₀` at each place. The outer one runs
over `a`, with `orbitMeasure 𝔰.besselHaar₀ volume` at each place: `volume` weighted by a cutoff, a
function with integral one over each orbit. 

### `lintegral_boxCutoff_le_of_average`

 **Integration in stages.** Let `S` be data of the filling theorem over the CM field `E`, which
contains a primitive root of unity of order `5040`, and let `S` be admissible. Let `F` be measurable
and left invariant under `S.classUnipotent₀ c`, the rational unipotent elements of the class `c`
that fix the frame vectors e₁, …, e_ϱ, z. Let `s` be measurable with components in `besselU0`, the
unipotent elements that fix these vectors, and let `B` have finite positive measure. If for all `u`
with components in `besselU0` and all boxed points `y` the integral of `F (u * s x * y)` over
`x ∈ B` is at most `m B * C`, then the integral of `F` against the boxed cutoff and
`S.besselCutNormSq`, the product of the squared norms of the local cut Bessel functions, is at most
`C` times `S.unipotentCovolume` times the cardinality of `S.BesselCoord`. 
