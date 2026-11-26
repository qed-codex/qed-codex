---
{
  "module": "src/New/Spanning/Frames/QuadricPlancherel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/QuadricPlancherel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/QuadricPlancherel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Plancherel's formula on quadrics

Cauchy–Schwarz in the fibres and Plancherel's formula in the orthonormal coordinates bound a Fourier
kernel between two quadrics. Along a Heisenberg group a partial correlation is a Fourier transform
in the next frame vector. The letters G^(l), R^(l), U_(<l), Y^(l) are those of the head of
`New.Spanning.Frames.Lengths`, and K, M those of `New.Spanning.Frames.Levels`.

## Main definitions and results

* `New.Floors.Gauge.fourierSqNormLe_floorQuadricMeasure`: the kernel from the quadric of a floor to
  the same quadric or to the whole floor, by solving in two disjoint blocks.
* `New.Floors.Gauge.partialCorrelation_heisenbergElem_eq_integral`: the correlation along a
  Heisenberg group.
* `New.Floors.Gauge.parseval_heisenbergMeasure_le`: Parseval's inequality along a Heisenberg group.

Notions from other files:
* `F.partialCorrelation l k g y`: the correlation from floor l on, an integral of k(σ g, σ y).
* `F.IsPairingKernel l k d`: the rules obeyed by an orbital integral twisted by d.
* `orbitPoint b σ`: the vector σ⁻¹ f_b, for the b-th frame vector f_b; its law on floor b is
  `F.floorQuadricMeasure b`.
* `Γ.vecsOfSize i`, `Γ.HasMatrixSize i`: vectors and matrices all of whose entries have size i.
* `FourierSqNormLe`: a bound for the kernel ψ(ξ ⟨v, y⟩) on square norms.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


 ### Masses on the floors and Fourier kernels 

### `floorMassLe_of_chart`

 Let f be measurable and left invariant under R^(b+1) = `partialUnitriangularGroup (b + 1)`. For
each g ∈ K let f(σ g) be at most Ψ(σ⁻¹ f_b) for σ in `floorGroup b`, with f_b the b-th frame vector,
where σ⁻¹ f_b = `orbitPoint b σ` and the measurable function Ψ has integral at most C over the
vectors of size 7 of the quadric of floor b. Then for every g the integral of f(σ g) over the σ on
floor b with σ g near at b + 1 (that is, R^(b+1) σ g meets K) is at most C. 

### `floorMassLe_one_of_le`

 Bounded mass. The measure of the quadric of floor b is the image, under the basis
`F.floorBasis b`, of `quadricMeasure` for the hyperbolic pairs `FloorPairs b m` and the orthonormal
vectors ι, at some value β of the form. If the coordinate vectors of size 11 have mass at most M
for every β, then for every g the σ on floor b with σ g near at b + 1 (`F.IsNear`) have mass at
most M. 

### `floorMassLe_one`

 For every g, the σ on floor b with σ g near at b + 1 (`F.IsNear`) have mass at most
Λ^(99 · 13 n) times the volume of the vectors of size 11 in X'. Here Λ = `Γ.loss` is the constant of
the gauge, n = `𝔰.n`, and X' is spanned by the orthonormal vectors indexed by `F.FreeIndex`. 

### `fourierSqNormLe_floorQuadricMeasure`

 Let ρ be the volume `floorVolume b` of Y^(b) or the measure of the quadric of floor b. The
kernel ψ(ξ ⟨v, y⟩), from the vectors y of size j on the quadric to the vectors v of size i with the
measure ρ, multiplies square norms by at most Λ^(99 n (i+6)) Λ^(99 n (j+6)) (c / |ξ|)^(rank X').
Here Λ = `Γ.loss` is the constant of the gauge, n = `𝔰.n`, c = `P.kernelBound`, |ξ| = `P.modulus ξ`
and rank X' = `card F.FreeIndex`. 

### `correlation_support`

 The support of a correlation. Let k be a pairing kernel for the element d (`IsPairingKernel`),
let t lie in `floorGroup b`, let t⁻¹ q lie in `unipotentBelow b`, and let the matrix q x have
entries of size j. For almost every σ on floor b at which the correlation from floor b + 1 on at (σ
x, σ y) is not zero, the vector t σ⁻¹ f_b has size j + 6. 

### `correlation_plancherel`

 Plancherel's inequality for the amplitude of floor b, that is, the Fourier transform of a
correlation along the quadric of that floor. Let k be a pairing kernel for the element d at floor b,
let t lie in `floorGroup b`, let t⁻¹ q lie in `unipotentBelow b`, and let the matrix q x have
entries of size j (`Γ.HasMatrixSize j`). Let ρ be the Haar measure `floorVolume b` on the vectors of
floor at least b, or the measure `F.floorQuadricMeasure b` of the quadric of floor b. Integrate the
correlation from floor b + 1 on at (σ x, σ y) against ψ(ξ ⟨v + v₀, t σ⁻¹ f_b⟩) over σ on floor b.
Here ψ is the additive character of the place, ⟨·,·⟩ is the form with Gram matrix `T.splitGram`, and
σ⁻¹ f_b = `orbitPoint b σ`, with f = (e_0, …, e_{ϱ-1}, z) the frame. The integral for ρ of the
squared modulus of this transform over the v of size i (`Γ.vecsOfSize i`) is at most Λ^(99 n (i+6))
Λ^(99 n (j+12)) (c / |ξ|)^(card `F.FreeIndex`) times the squared L² norm of the correlation on floor
b. 

 ### Correlations along a Heisenberg group 

### `partialCorrelation_heisenbergElem_eq_integral`

 Let k be a pairing kernel (`IsPairingKernel`) from floor a + 1 on for the element d, and let
n = `P.heisenbergElem a t` with t = (ω, β). Suppose that (σ₀(d s d⁻¹) - σ₀(s^ε)) / M = ξ σ₀(s) for s
in the Heisenberg group `floorUnipotent a`, where σ₀ = `simpleRootSum` and M = `F.levelUnit` is the
level. Then the correlation `F.partialCorrelation` from floor a + 1 on at (n^ε x, n y) is the
integral over σ on floor a + 1 of ψ(-ξ ⟨ω, σ⁻¹ f_(a+1)⟩), with f the frame, times the correlation
from floor a + 2 on at (σ x, σ y). 

### `simpleRootSum_weylRatio_conj`

 Let p, q be sequences of units and j ≤ a + 1. Conjugation by the diagonal element
`weylRatio j p q`, with entry p_b / q_b at e_b for b < j, multiplies the character
`simpleRootSum` (the sum of the entries just above the diagonal of the
frame block) on the Heisenberg group `floorUnipotent a` by p_a / q_a if a < j, and by 1
otherwise. 

### `partialCorrelation_weylRatio_heisenbergElem`

 Let j ≤ a + 1 and ε ≤ 1, let k satisfy `F.IsPairingKernel (a + 1) k (weylRatio j p q)`, and let
n = `P.heisenbergElem a t` with t = (ω, β). Then `F.partialCorrelation (a + 1) k` at (n^ε x, n y) is
the integral over σ, for `F.floorMeasure (a + 1)`, of ψ(-ξ h(ω, σ⁻¹ f_(a+1))) times
`F.partialCorrelation (a + 2) k` at (σ x, σ y). Here ψ is the additive character of the place `P`, h
is the form with Gram matrix `T.splitGram`, and f = (e_0, …, e_{ϱ-1}, z) is the frame. The frequency
ξ is (p_a / q_a - ε) / M if a < j (that is, j = a + 1), and (1 - ε) / M otherwise. 

### `parseval_heisenbergMeasure_le`

 Parseval's inequality along the Heisenberg group N = `floorUnipotent a` of floor a. Let k be a
pairing kernel from floor a + 1 on for the element d, and let the characters of the two points
differ by the invertible frequency ξ on N. For n ∈ N with Φ(n) ≠ 0, let n lie in S and let Φ(n) be
at most C times the squared correlation `F.partialCorrelation` from floor a + 1 on at (n^ε x, n y).
For each n₀ ∈ S let there be t in `partialUnitriangularGroup (a + 1) ⊓ floorGroup a` and q in
`unipotentBelow (a + 1)` such that t q x has entries of size i and, for each n ∈ S, v / u has size
j for some v congruent to (t n₀ (t n)⁻¹ - 1) e*_a modulo the e_b with b < a (`CongrBelow`). Then
the integral of Φ over N is at most C (c / |ξ u|)^(rank X') |u|^(ρ+1/2) Λ^(100 n (i+j+31)) times
the integral over σ on floor a + 1 of the squared correlation from floor a + 2 on at (σ x, σ y).
Here c = `P.kernelBound`, rank X' = `card F.FreeIndex`, |u|^(ρ+1/2) = `F.floorModulus a u` with ρ
the rank of the vector part of N, Λ = `Γ.loss` is the constant of the gauge, and the n in its
exponent is `𝔰.n`. 
