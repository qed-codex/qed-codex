---
{
  "module": "src/New/Spanning/Bessel/Orthonormality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Orthonormality.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Orthonormality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Normalisation of a Bessel function and of its cut

Let `W` be an integrable Bessel function on G₁ whose type is an irreducible representation of the
compact group `U(κ)`. The operator `∫ W ⊗ W^*` over 𝖴∖G₁ commutes with this representation, so it
is a scalar, and its trace is the squared L² norm of `W`.

* `New.BesselSystem.orthonormal`: for the full function of a Bessel system the operator is `1`, so
  its coordinates are orthonormal in L²(𝖴∖G₁).
* `New.IsCutPair.exists_integral_cut_mul_conj_eq`: for the cut function it is a scalar between `0`
  and `1`.
* `New.IsCutPair.lintegral_sq_inner_cut_le`: the upper bound, tested on a vector.

Notions from other files:

* `New.Shape.G₁`: the unitary group G₁ of the complex hermitian form given by a shape; `U(κ)` is
  the unitary group of the standard positive form on the index set κ of the shape, embedded in G₁
  by `New.RealPlace.embedH`.
* `New.besselQuotMeasure`: the measure on G₁ that computes integrals over 𝖴∖G₁, where 𝖴 is the
  unipotent group `New.Shape.Form.besselU`.
* `New.IsBesselFunction`: a bounded measurable function on G₁ that transforms on the left by a
  fixed character under 𝖴 and by a unitary representation, its type, under `U(κ)`.
* `New.IsCutPair`: a Bessel function (`.full`) whose squared L² norm is the dimension of its
  value space, and its cut (`.cut`): a Bessel function that vanishes outside a region of bounded
  size, is close to it in L² and agrees with it where the size is small.
* `New.BesselSystem`: a cut pair of irreducible type, with further bounds.

## Relation to the literature

See `New.Spanning.Bessel.CutTailBound` for related work.


### `New.IsBesselFunction.integral_mul_conj_embedH_mul`

 Let `W : G₁ → ℂ^I` be a Bessel function: a bounded measurable function on the unitary group G₁
such that `W (u y) = ψ(u) W y` for `u` in the unipotent subgroup 𝖴, with ψ a fixed character, and
`W (h y) = rep h (W y)` for `h` in the compact unitary group `U(κ)`, which sits in G₁ by
`RealPlace.embedH`. Translating `W` on the left by `s ∈ U(κ)` does not change the integral of
`W y i * conj (W y j)` over 𝖴∖G₁. 

### `New.IsBesselFunction.integral_mul_conj_eq`

 Let `W : 𝔰.G₁ → ℂ^I` be a Bessel function of type `rep`: it is bounded and measurable,
`W (u y) = ψ(u) W y` for `u` in the unipotent subgroup 𝖴 of `𝔰.G₁`, with ψ a fixed character, and
`W (h y) = rep h (W y)` for `h` in the compact unitary group `U(κ)` = `U (1 : Matrix 𝔰.κ 𝔰.κ ℂ)`
inside `𝔰.G₁`, with `rep` a unitary representation. Suppose that `W` is integrable over 𝖴∖G₁ and
that every matrix commuting with all `rep h` is scalar. Then the operator `∫ W ⊗ W^*` over 𝖴∖G₁ is
the scalar `‖W‖₂ ^ 2 / |I|`. 

### `New.BesselSystem.orthonormal`

 The coordinates of the full function of a Bessel system `B` are orthonormal in L²(𝖴∖G₁): the
integral of `B.besselFn .full y i` times the conjugate of `B.besselFn .full y j` for the measure
`besselQuotMeasure` is 1 if `i = j` and 0 otherwise. 

### `New.IsCutPair.integrable_cut`

 Let `W` be a cut pair on G₁: a Bessel function `W .full` and its cut `W .cut`, a Bessel function
that vanishes outside a region whose size is bounded by a power of `b`. By hypothesis a power of the
scaled size, with an exponent proportional to `f` and a base at least 1, times the norm of either
function lies below a majorant `A` of finite integral. Hence the cut function is integrable over
𝖴∖G₁. 

### `New.IsCutPair.exists_integral_cut_mul_conj_eq`

 Let `W` be a cut pair of type `rep` with values in `ℂ^I`: a Bessel function `W .full` and its
cut `W♭ = W .cut`, a Bessel function that vanishes outside a region of size bounded in terms of `b`.
Suppose that `rep` is irreducible: every matrix that commutes with all `rep h` is scalar. Then the
operator `∫ W♭ ⊗ W♭^*` over 𝖴∖G₁ is a scalar `c` between `0` and `1`. 

### `New.IsCutPair.lintegral_sq_inner_cut_le`

 Let `W` be a cut pair of type `rep` with values in `ℂ^I`: a Bessel function `W .full` and its
cut `W♭ = W .cut`, both transforming on the left by a character under the unipotent group 𝖴 and by
`rep` under `U(κ)`, with squared L² norm over 𝖴∖G₁ at most `|I|`; `b` is the parameter of the length
at which `W` is cut, `f` the rate of decay in the length. Suppose that every matrix commuting with
all `rep h` is scalar. Then for every vector `v` the integral of `|⟪v, W♭ y⟫| ^ 2` over 𝖴∖G₁ is at
most `‖v‖ ^ 2`. 
