---
{
  "module": "src/Lib/DiscreteSeries/Bruhat/FourierKernels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/FourierKernels.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/FourierKernels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fourier kernels between solved measures

The measure theory, valid at any place, that bounds the kernel ψ(ξ ⟨v, y⟩), tested on measurable
integrable functions that vanish off a given set. The square norm of a function is the square of its
L² norm. A measure that is solved in a block has three kinds of coordinates: those of the block,
whose measures give bounded mass to a box; inner coordinates, in which Plancherel's inequality is
applied; and the remaining outer coordinates, which are estimated by the volume of a box.

* `New.Floors.Place.FourierSqNormLe`: the kernel ψ(ξ ⟨v, y⟩) multiplies square norms by at most a
  given constant. The bound passes to images of the measures.
* `New.Floors.Place.IsSolvedIn.setLIntegral_le`: a bound for the integral, over a box, of a function
  of the inner coordinates by its integral in those coordinates alone.
* `New.Floors.Place.IsSolvedIn.fourierSqNormLe`: the bound for the kernel between two measures that
  are solved in two disjoint blocks.

Notions from other files:
* `New.Floors.Place`: a place A, with its character ψ, its modulus |·| = `modulus` and the constant
  c = `kernelBound` of Plancherel's inequality.
* `New.Floors.Place.IsSolvedIn`: a measure on A^κ is the volume in the coordinates off a block times
  a family of measures in the coordinates of the block, each of mass at most M on a box.
* `New.Floors.coordinateBox`: the box of a set R, that is, the vectors with all coordinates in R.

## Relation to the literature
Standard consequences of Fubini's theorem and the inequalities of Cauchy–Schwarz and Plancherel.


### `enorm_integral_sq_le`

 Cauchy–Schwarz on the support: if g vanishes off S, then the square of its integral is at most
μ(S) times the integral of its square over S. 

### `setLIntegral_comp_fst_le`

 Let each measure ζ(w) give mass at most M to V. The integral over B × V of a function of the
first variable is at most M times its integral over B. 

### `lintegral_enorm_integral_kernel_sq_le`

 Cauchy–Schwarz in the fibres. Let each measure ζ(w) give mass at most M to V, and let f vanish
unless its second variable lies in V. Integration over the fibres multiplies the square norm of f by
at most M. 

### `integrable_integral_kernel`

 The integral over the fibres of an integrable function is integrable. 

### `enorm_integral_prod_compProd_sq_le`

 Cauchy–Schwarz in the first of three variables (y, w, z). If f vanishes unless y lies in S, then
the square of its integral is at most μ(S) times the integral over y of the square of its integral
over w and z. 

### `FourierSqNormLe`

 The kernel ψ(ξ ⟨v, y⟩), with ψ the character of the place and ⟨v, y⟩ = v* J y, multiplies
square norms by at most C from the functions on (S, ρ) to the functions on (S', ρ'). It is tested on
the measurable integrable functions φ that vanish off S. 

### `FourierSqNormLe.mono`

 The constant may be enlarged. 

### `FourierSqNormLe.map`

 A bound for the kernel (`FourierSqNormLe`) passes to the images of the two measures under maps
f', f with ξ₁ ⟨f' v, f y⟩ = ξ ⟨v, y⟩ for all v, y; the two products are formed with J₁ and J. It
holds on all sets U', U, with U' measurable, whose preimages lie in S', S. 

### `enorm_psi_mul`

 Multiplication by a value of ψ preserves the absolute value. 

### `lintegral_lintegral_fourier_le`

 Plancherel's inequality in the second of two variables: the partial Fourier transform multiplies
square norms by at most (c / |ξ|)^(card ι), where c = `kernelBound` and |·| = `modulus`. 

### `lintegral_lintegral_fourier_integral_kernel_le`

 Plancherel's inequality in w, after Cauchy–Schwarz in z. Let each measure ζ(y, w) give mass at
most M to V, and let f(y, w, z) vanish unless z lies in V. The partial Fourier transform in w of the
integral of f over z has square norm at most (c / |ξ|)^(card ι) M times that of f. Here ψ is the
character of the place, c = `kernelBound` and |·| = `modulus`. 

### `blockChart`

 The vector with outer coordinates p.1.1, inner coordinates p.1.2 and coordinates p.2 in the
block, along a bijection e of indices. 

### `preimage_blockChart_coordinateBox`

 A vector lies in the box of R exactly when its three parts do. 

### `measurableSet_coordinateBox`

 The box of a measurable set is measurable. 

### `setLIntegral_le_of_le_comp_fst`

 If T(y, w, z) ≤ K H(y, w), the integral of H(y, w) over all w is at most D, and each measure
ζ(y, w) gives mass at most M to V, then the integral of T over (S × U) × V is at most K M D μ(S). 

### `measurable_enorm_integral_fourier_sq`

 The square of the transform of φ is a measurable function of its variable v. 

### `measurable_lintegral_fourier_integral_kernel`

 The square norm in y of the partial Fourier transform in w of the integral over z of a
measurable f(y', y, w, z) is a measurable function of y' and w'. 

### `enorm_integral_fourier_sq_le`

 Cauchy–Schwarz in the outer coordinates. Let a chart x(y, w, z) carry (μ × volume) ⊗ ζ to ρ, let
φ(x(y, w, z)) vanish unless y lies in S, and let the product v* J x(y, w, z) be b(y) + w'*w +
a(y, w, z). The square of the transform of φ at v is at most μ(S) times the square norm in y of the
partial Fourier transform at w' of the integral of ψ(ξ a) φ(x) over z. 

### `exists_inl_inl_eq_of_injective`

 Indices given by an injective map that avoids the inner coordinates and the block of the chart
are outer coordinates. 

### `star_blockChart_dotProduct_mulVec`

 The product v* J y for v = `blockChart e' p'` and y = `blockChart e p`, two charts with the same
inner indices, where the rows of J at these indices and at the block of v are those of the identity
matrix and `out` locates that block among the outer indices of y. In a triple, p.1.1 is outer, p.1.2
inner and p.2 in the block. The product is that of the block of v with outer coordinates of y, plus
that of the inner coordinates, plus the term of the outer coordinates of v. 

### `IsSolvedIn.exists_blockChart`

 Let ρ be solved in a block, that is, let it be the volume in the free coordinates times measures
of mass at most M on the box of R in the block, and let inner coordinates off the block be given.
The free coordinates split into the inner ones and the rest, the outer ones. In `blockChart`, ρ is
the volume in the outer and the inner coordinates times such measures. 

### `IsSolvedIn.setLIntegral_le`

 Let ρ be solved in a block with fibres of mass at most M on the box of R, that is, let it be the
volume in the coordinates off the block times such measures in the block. For a function G of inner
coordinates off the block, the integral over the box of R is at most the volume of the box in the
outer coordinates, times M, times the integral of G over the box in A^ι. 

### `IsSolvedIn.fourierSqNormLe`

 Let ρ be solved in the block `blk`, meaning it is the volume in the other coordinates times an
s-finite kernel of block measures, each of mass at most M on the box of R (vectors with all
coordinates in R). Let ρ' be solved likewise in `blk'` with M' and a measurable R', and let the
inner coordinates and both blocks be pairwise disjoint. If the rows of J at the inner indices and at
`blk'` are those of the identity, then for a unit ξ the kernel ψ(ξ v* J y), with ψ the character of
the place, multiplies square norms from the box of R with ρ to the box of R' with ρ' by at most
(c / |ξ|) per inner coordinate (c = `kernelBound`, |·| = `modulus`), times M, M' and the volume of R
(resp. R') raised to the number of coordinates outside the inner ones and `blk` (resp. `blk'`). 
