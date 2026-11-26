---
{
  "module": "src/Lib/DiscreteSeries/Bessel/FrameFibre.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/FrameFibre.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/FrameFibre.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Haar measure of G₁ and the fibre measure on frames

The group `New.Shape.G₁` is the unitary group of the form `New.Shape.J₁`, of rank `r`, with basis
`e_a`, `x_i`, `z`, `e*_a`: there are `ϱ` hyperbolic pairs `e_a, e*_a`, the span `X₀` of the `x_i` is
positive definite of rank `k`, and `z` is negative. The frame is `e_0, …, e_{ϱ-1}, z`, and 𝖴⁰ is the
unipotent group `New.Shape.Form.besselU0` that fixes it. The file compares Haar measure of G₁ with
the fibre measure of the Gram map on tuples of vectors.

Notions from other files:
* `New.LeGramFibre J E m` says that the image of `m` under `g ↦ g E` is at most the fibre measure of
  the Gram map `E' ↦ E'ᴴ J E'` over the Gram matrix of `E`.
* `New.LeFibreMeasure μ ν π b l` says that `l` is at most the fibre measure `dμ / dν` of `π` over
  `b`.
* `New.volU j` is `vol U(j)`; the measure `volume` on G₁ is Haar measure, normalised through the
  compact dual, and on the unitary group H = U(X₀) it is the Haar measure of mass one.

Main results:
* `New.LeGramFibre.mconv_embedH_le`: tuples with the Gram matrix of the basis vectors outside `X₀`.
  These vectors have fixer `H = U(X₀)`; if their image under `m` is below the fibre measure, then
  `m ∗ dh` is at most `vol U(r) / (2 ^ (r - k) vol U(k))` times Haar measure of G₁.
* `New.RealPlace.lintegral_eq_unipotent_coords`: Lebesgue measure on the `ϱ`-tuples dual to
  `e_0, …, e_{ϱ-1}` and orthogonal to `z`, in coordinates given by 𝖴⁰ and the Gram matrix.
* `New.LeGramFibre.mconv_fixerHaar_le`: frames. The standard frame has fixer 𝖴⁰ H, with the measure
  `ds = New.RealPlace.fixerHaar`; if the image of the frame under `m` is below the fibre measure,
  then `m ∗ ds` is at most `vol U(r) / (2 ^ (ϱ + 1) vol U(k))` times Haar measure of G₁.

## Relation to the literature

Known result: the fibre measure of the Gram map on tuples of vectors, in terms of Haar measure of
the unitary group. The file proves the inequality that is used. Siegel, Über die analytische Theorie
der quadratischen Formen, Ann. of Math. 36 (1935).


### `conjTranspose_definiteCols_mul_self`

 The columns of `definiteCols`, the basis vectors `x_i` of `X₀`, are orthonormal for the standard
hermitian form. 

### `J₁_mul_definiteCols`

 The matrix `J₁` of the form fixes the basis vectors `x_i` of `X₀`. 

### `embedH_mul_definiteCols`

 For `h` in the unitary group `H` of `X₀`, the element `embedH h` of `G₁` acts on the basis
vectors `x_i` of `X₀` by the matrix `h`. 

### `ae_map_mul_eq`

 Let `f` be a measurable map to the unitary group `G₁` whose values all fix the tuple of
vectors given by the columns of `E`. Then almost every element for the image of `μ` under `f`
fixes this tuple. 

 ### Tuples whose complement is definite 

### `leFibreMeasure_definiteCols`

 The definite case, with `k` the dimension of `X₀`. On `k`-tuples of vectors of `X₀`, the image
under `h ↦ h (x_i)` of `vol U(k) / 2 ^ k` times the Haar probability measure of `H = U(X₀)`,
embedded in `G₁` by `embedH`, is at most the fibre measure (`LeFibreMeasure`) of the Gram map
`gramCoords` over the Gram matrix of the `x_i`, the columns of `definiteCols`. Here `volU k` is
`vol U(k)`. 

### `_root_.New.LeGramFibre.mconv_embedH_le`

 The fibre measure on tuples with a definite complement. `G₁` is the unitary group of the
hermitian form with Gram matrix `J₁`: ϱ hyperbolic pairs, the identity on `X₀` (basis `x_i`,
`i ∈ κ`) and `h(z, z) = −1`. Let `e` enumerate the basis, indexed by `BesselIndex`, with the `x_i`
last (`indexX₀ i` is the index of `x_i`), and let `E` be the tuple of the other `r - k = 2 ϱ + 1`
basis vectors. Suppose the image of `m` under `g ↦ g E` is at most the fibre measure `dY / dT` of
the Gram map over the Gram matrix of `E` (`LeGramFibre`). Then the convolution of `m` with the Haar
probability measure of `H = U(X₀)`, embedded in `G₁` by `embedH`, is at most
`vol U(r) / (vol U(k) 2 ^ (2 ϱ + 1))` times Haar measure of `G₁`, normalised through its compact
dual. Here `inclMatrix ℂ f` has the basis vectors with indices `f j` as columns and `volU j` is
`vol U(j)`. 

 ### Coordinates adapted to the frame 

### `_root_.New.Shape.freeCols`

 The matrix with the columns `e_0, …, e_{ϱ-1}` and `x_i`; they span the vectors orthogonal to the
frame `e_0, …, e_{ϱ-1}, z` for the form `J₁`. 

### `conjTranspose_frameCols_mul_self`

 The columns of `frameCols`, the frame vectors `e_0, …, e_{ϱ-1}, z`, are orthonormal for the
standard hermitian form. 

### `conjTranspose_freeCols_mul_self`

 The columns `e_a, x_i` of `freeCols` are orthonormal for the standard hermitian form. 

### `frameCols_gram_freeCols`

 The columns `e_a, x_i` of `freeCols` are orthogonal to the frame `e_0, …, e_{ϱ-1}, z` for
the form `J₁`. 

### `card_frame_add_card_free`

 The `ϱ + 1` vectors of the frame and the `ϱ + k` columns of `freeCols` are together as many as
the basis vectors. 

### `unipotentOf_mul_dualCols_add`

 For `q = (b, s)` in `UnipotentParams`, with `b` a complex `ϱ × k` matrix and `s` a real `ϱ × ϱ`
matrix, and `u = unipotentOf q` the element of 𝖴⁰ with parameters `q`, the tuple `u (e* + e a)` is
`e* + e (skewOfReal s + a - b bᴴ / 2) - x bᴴ`, where `e`, `x`, `e*` are the matrices
`isotropicCols`, `definiteCols`, `dualCols` with columns `e_i`, `x_i`, `e*_i`, and `skewOfReal s` is
the skew-hermitian matrix with real coordinates `s`. 

### `lintegral_eq_unipotent_coords`

 Coordinates on the `ϱ`-tuples `e* + e a + x c`, `p = (a, c)`, which are the tuples dual to
`e_0, …, e_{ϱ-1}` and orthogonal to `z`; `e*` is `dualCols`, `e` is `isotropicCols`, and `(e, x)` is
`freeCols`. Such a tuple is `u (e* + e T / 2)` with `u = unipotentOf q` in the unipotent group 𝖴⁰
and `T = hermOfReal t` its Gram matrix, the hermitian matrix with real coordinates `t`, and
`dp = 2 ^ (-ϱ) dt dq`, where `dq = db ds` is Lebesgue measure on the pairs `q = (b, s)` of
`UnipotentParams`. 

 ### Frames 

### `leFibreMeasure_dualCols`

 The dual vectors `e*_a`, the columns of `dualCols`. On `ϱ`-tuples `y`, the image under
`u ↦ u (e*_0, …, e*_{ϱ-1})` of `2^(-ϱ)` times Haar measure `New.Shape.besselHaar₀` of the unipotent
group 𝖴⁰ is at most the fibre measure (`LeFibreMeasure`) of the map that sends `y` to its products
with the frame `e_0, …, e_{ϱ-1}, z` (columns of `frameCols`), and to the coordinates `gramCoords` of
its Gram matrix, over the image of `(e*_0, …, e*_{ϱ-1})`. 

### `fixerHaar`

 The measure `ds = du dh` on the fixer 𝖴⁰ H of the frame, as a measure on `G₁`: the image under
`(u, h) ↦ u h` of the Haar measure `New.Shape.besselHaar₀` on 𝖴⁰ and the Haar measure of mass one on
`H = U(X₀)`. 

### `_root_.New.LeGramFibre.mconv_fixerHaar_le`

 The fibre measure on frames. If the image of `m` under `g ↦ g F`, with `F = frameCols` the frame
`e_0, …, e_{ϱ-1}, z`, is at most the Gram map's fibre measure (`LeGramFibre`), then the convolution
of `m` with the measure `fixerHaar 𝔰` on the fixer 𝖴⁰ H of the frame is at most
`vol U(r) / (vol U(k) 2 ^ (ϱ + 1))` times Haar measure of `G₁`, normalised through its compact
dual. Here `r` is the rank, `k` the dimension of `X₀`, and `volU j` is `vol U(j)`. 
