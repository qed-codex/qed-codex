---
{
  "module": "src/New/Spanning/Bessel/OpenCellPairing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/OpenCellPairing.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/OpenCellPairing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One pairing on the open cell, at all places together

Let `X` be a finite family of Bessel systems (`New.BesselSystem`), `W` the tensor product of their
Bessel functions and `W♭` that of their cuts. Let `φ` be a function of `z` of modulus at most `1`,
left invariant under the fixers of the frames and not necessarily a product over the places, such
that `φ (z) W♭ (γ z) ⊗ W♭ (z)^*` vanishes outside boxes. The integral of this product is bounded by
the root of the product of the local bounds `New.pairingBoundSq`, plus the integral of `‖φ‖` times
the norm of the difference between the uncut and cut kernels.

The operator bounds of `New.BesselSystem.exists_isOpenCellBound` multiply over the places, and one
shift that is no worse than the mean gives the bound for `W`.

Notions from other files:
* `BesselSystem`: two continuous functions on the group `G₁`, `besselFn .full` and its cut
  `besselFn .cut`, with values in `ℂ^I`, parameters `b` and `f`, and a degree `deg`.
* `frameBox ρ`: the `y` with `‖y⁻¹ f_a‖ ≤ ρ` for every vector `f_a` of the frame; `besselFixer` is
  the subgroup that fixes these vectors.
* `besselLength y`: the infimum of `‖s y‖ + 1` over `s` in the Bessel subgroup.
* `realFrameGram γ`: the matrix of products `h(f_a, γ f_b)` for the hermitian form `h`;
  `gramDiscReal Z` is `|det Z| ^ 2 - |D| ^ 2`, with `D` the leading minor one size smaller.
* `pairingBoundSq γ deg ρ d`: the square of the bound of the open cell at one place, a power of
  `ρ ^ (9 n) / 𝗀` times `d ^ 2 / (deg * openCellConst * (𝗀 / 2) ^ (k - 1))`, where
  `𝗀 = gramDiscReal (realFrameGram γ)`, `n = 𝔰.n` and `k = 𝔰.k`.

## Main definitions and results

* `New.BesselSystem.pairKernel`: the matrix of `W (y) ⊗ W (γ⁻¹ y)^*`. Its adjoint is the matrix of
  `W (γ⁻¹ y) ⊗ W (y)^*`, which is `New.BesselSystem.piKernel` at `γ⁻¹`.
* `New.BesselSystem.enorm_integral_pairKernel_cut_le`: compact support and the bound for the pairing
  of the cut functions.

## Relation to the literature

See `New.Spanning.Bessel.FillingData` for related work.


### `piKernel`

 The matrix of the operator `W (γ z) ⊗ W (z)^*`, as a vector with the Hilbert–Schmidt norm. Here
`W` is the tensor product, over a finite family `X` of Bessel systems, of the Bessel functions
(`σ = .full`) or of their cuts (`σ = .cut`). The adjoint of `piKernel X σ γ⁻¹ y` is
`pairKernel X σ γ y`. 

### `one_le_b`

 The parameter `b` of a Bessel system is at least `1`, being at least eight times the rank. 

### `inCut_of_piKernel_ne_zero`

 Where `piKernel X .cut γ z`, the matrix of the cut kernel `W♭ (γ z) ⊗ W♭ (z)^*`, is not zero,
every component of `γ z` satisfies `InCut`: its `besselLength` is at most `b ^ (6 n + 2)`, where
`n = 𝔰.n` is the number of vectors in the frame. 

### `integrableOn_smul_piKernel`

 For either side `σ` (uncut or cut), the product of `piKernel X σ γ` and a measurable function of
modulus at most `1`, both translated by `t`, is integrable on every compact set. 

### `exists_isCompact_enorm_integral_piKernel_le`

 Let `X v` be Bessel systems with size parameter `b`, one for each place `v`, and `W` the tensor
product of their Bessel functions. Let the frame Gram matrix of each `γ v` have `0 < gramDiscReal`,
and let some `y` have both `y v` and `(γ v)⁻¹ * y v` in `frameBox (ρ v)`, where `b ≤ ρ v`. Let `φ`
be measurable, of modulus at most `1`, and left invariant under the fixer `besselFixer` of the frame
at each place. There are a compact set `A` and a point `t` of the fixer such that the integral over
`A` of `φ` times the kernel `piKernel X .full γ`, the matrix of `W (γ z) ⊗ W (z)^*`, both translated
by `t`, has Hilbert–Schmidt norm at most the root of the product of the local bounds
`pairingBoundSq` at the places; and `A` contains every `z` in the boxes for which the components `x`
of `γ t z` have `besselLength` at most the corresponding `ρ v`. 

### `hasCompactSupport_and_enorm_integral_piKernel_le`

 Let `X v` be Bessel systems with size parameter `b`, one for each place `v`, and `W`, `W♭` the
tensor products of their Bessel functions and of their cuts. Let the frame Gram matrix of each `γ v`
have `0 < gramDiscReal`, and let some `y` have both `y v` and `(γ v)⁻¹ * y v` in `frameBox (ρ v)`,
where `b ^ (6 n + 2) ≤ ρ v` and `n = 𝔰.n` is the number of vectors in the frame. Let `φ` be
measurable, of modulus at most `1`, left invariant under the fixer `besselFixer` of the frame at
each place, and such that `φ` times the cut kernel `piKernel X .cut γ`, the matrix of
`W♭ (γ z) ⊗ W♭ (z)^*`, vanishes unless `z` lies in the boxes. Then this product has compact support,
and the Hilbert–Schmidt norm of its integral is at most the root of the product of the local bounds
`pairingBoundSq` at the places, plus the integral of `‖φ‖` times the norm of the difference of the
uncut kernel `W (γ z) ⊗ W (z)^*` and the cut kernel. 

### `pairKernel`

 The matrix of the operator `W (y) ⊗ W (γ⁻¹ y)^*`, as a vector with the Hilbert–Schmidt norm.
Here `W` is the tensor product, over a finite family `X` of Bessel systems, of the Bessel functions
(`σ = .full`) or of their cuts (`σ = .cut`). It is the adjoint of `piKernel X σ γ⁻¹ y`, the matrix
of `W (γ⁻¹ y) ⊗ W (y)^*`. 

### `adjointIsometry`

 The passage to the adjoint (conjugate transpose) of a complex matrix indexed by `I × I`, a real
linear isometry for the Hilbert–Schmidt norm. 

### `enorm_integral_pairKernel_cut_le`

 **One pairing.** Let `X v` be Bessel systems with size parameter `b`, one for each place `v`,
and `W`, `W♭` the tensor products of their Bessel functions and of their cuts. Let the frame Gram
matrix of each `γ v` have `0 < gramDiscReal`, and let some `y'` have both `y' v` and
`(γ v)⁻¹ * y' v` in `frameBox (ρ v)`, where `b ^ (6 n + 2) ≤ ρ v` and `n = 𝔰.n` is the number of
vectors in the frame. Let `φ` be measurable, of modulus at most `1`, left invariant under the fixer
`besselFixer` of the frame at each place, and such that `φ` times the cut kernel
`pairKernel X .cut γ`, the matrix of `W♭ (y) ⊗ W♭ (γ⁻¹ y)^*`, vanishes unless `y` lies in the boxes.
Then this product has compact support, and the Hilbert–Schmidt norm of its integral is at most the
root of the product of the local bounds `pairingBoundSq`, plus the integral of `‖φ‖` times the norm
of the difference of the uncut kernel `W (y) ⊗ W (γ⁻¹ y)^*` and the cut kernel. 
