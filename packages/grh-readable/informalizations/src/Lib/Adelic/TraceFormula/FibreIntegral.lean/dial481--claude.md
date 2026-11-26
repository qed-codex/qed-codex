---
{
  "module": "src/Lib/Adelic/TraceFormula/FibreIntegral.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/FibreIntegral.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/FibreIntegral.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integration over the fibres of a conjugation map

A group `Γ` acts on a group `G` by conjugation through `j : Γ → G`. Let `X` be a slice of a closed
set `C ⊆ G` (`IsSlice`): the map `(g, y) ↦ g y g⁻¹` from `Γ × X` onto `C` is open in the sense of
`IsSlice.eventually_exists_conj_mem`, and its fibres are the orbits of a closed subgroup `H` of `Γ`.
The file proves two steps of the descent of invariant distributions from `C` to `X`.

* Step 1, images. Integration over the fibres takes a test function `Ψ` on `Γ × G` to a test
  function on `C`. A test function on `G` that extends it is an image of `Ψ` (`IsImage`), and one
  exists (`IsSlice.exists_isImage`).
* Step 2, Haar measure. An invariant distribution on `C` kills the image of `Ψ` as soon as the
  integrals of `Ψ (·, y)` over `Γ` vanish for all `y ∈ X`
  (`IsInvariantDistribution.eq_zero_of_isImage`).

Functions on `Γ × X` and on `C` are handled as restrictions of test functions on `Γ × G` and on `G`.

Notions from other files:
* `TestFunction G`: the locally constant functions of compact support from `G` to `ℂ`.
* `TestFunction.translate (a, b) f`: the test function `x ↦ f (a⁻¹ * x * b)`.
* `compactMean ρ L x`: the mean of the orbit of the vector `x` under a compact subgroup `L`.

## Relation to the literature

Known result: descent of invariant distributions to a slice, after Harish-Chandra.


 ### Conjugation of test functions 

### `TestFunction.conjugate`

 The action of `Γ` on the test functions on `G` by conjugation through `j : Γ → G`. 

### `TestFunction.conjugate_apply`

 The conjugate of the test function `f` by `g ∈ Γ` through `j : Γ → G` takes the value
`f ((j g)⁻¹ * x * j g)` at `x`. 

### `TestFunction.isSmoothRep_conjugate`

 The action of `Γ` on the test functions on `G` by conjugation through `j` is smooth: every test
function is fixed by the elements of a neighbourhood of `1`. 

 ### Test functions on products and on closed subsets 

### `TestFunction.eval`

 The value of a test function at a point, as a linear form. 

### `TestFunction.integrable`

 A test function is integrable for every measure that is finite on compact sets. 

### `TestFunction.tensor`

 The product `(y, z) ↦ a y * b z` of two test functions. 

### `TestFunction.tensor_apply`

 The product of the test functions `a` and `b` takes the value `a y * b z` at `(y, z)`. 

### `TestFunction.partialApply`

 The test function `z ↦ Ψ (y, z)`. 

### `TestFunction.integrable_prodMk_left`

 For a test function `Ψ` on `Y × Z`, the function `y ↦ Ψ (y, z)` is integrable for every measure
that is finite on compact sets. 

### `TestFunction.setIndicator`

 The characteristic function of a compact open set. 

### `TestFunction.setIndicator_apply`

 The characteristic function of `V`, as a test function, is `V.indicator 1`. 

### `exists_isCompact_isOpen_superset_subset`

 In a locally compact non-archimedean group, a compact open set lies between any compact set and
any open set containing it. 

### `exists_isCompact_isOpen_preimage_eq`

 A compact open subset of a closed subset `C` of a locally compact Hausdorff non-archimedean
group is cut out by a compact open subset of the group. 

### `TestFunction.exists_extension`

 A test function on a closed subset `C` of a locally compact Hausdorff non-archimedean group is
the restriction of a test function on the group. 

 ### Invariant distributions 

### `IsInvariantDistribution`

 `I` is an invariant distribution on `C`: a linear form on the test functions on `G` that is
invariant under conjugation by `Γ` and depends only on the restriction to `C`. 

### `IsInvariantDistribution.map_conjugate`

 `I` is invariant under conjugation by `Γ`. 

### `IsInvariantDistribution.eq_zero`

 `I` kills the test functions that vanish on `C`. 

### `IsInvariantDistribution.map_compactMean`

 An invariant distribution `I` on `C`, for conjugation by `Γ` through `j`, takes the same value
at a test function and at the mean of its conjugates over a compact subgroup `L` of `Γ`. 

### `TestFunction.sum_compactMean_conjugate_eq_zero`

 Let `κ` be a finite family in `Γ` and `φ` a test function on `G`. Suppose that, for each `k` in
the compact subgroup `K`, the right translates of `φ` by the elements `j (κ i * k)` sum to zero.
Then the mean `ψ` of the conjugates of `φ` over `K` satisfies `∑ i, ψ (x * j (κ i)) = 0`. 

 ### Uniqueness of Haar measure, with a parameter (for Step 2) 

### `TestFunction.exists_isOpen_subgroup_forall_mul_right_eq`

 There is an open subgroup of `Γ` whose elements fix a given test function `Ψ` on `Γ × Y` under
right translation in the first variable. 

### `TestFunction.exists_eq_sum_tensor`

 If `Γ` has a compact open subgroup `K`, every test function on `Γ × Y` is a finite sum of
products `(g, y) ↦ 1_{a O} g * ψ y`, for one compact open subgroup `O`, cosets `a O` and test
functions `ψ` on `Y`; here `tensor` is the product, `indicator _ _` is the characteristic function
of the compact open subgroup `O`, and `translate (a, 1) (indicator _ _)` is the characteristic
function of `a O`. 

### `TestFunction.map_eq_zero_of_integral_eq_zero`

 **Uniqueness of Haar measure, with a parameter.** Let the group `Γ` have a compact open subgroup
`K`, and let `Λ` be a linear form on the test functions (locally constant, of compact support) on
`Γ × Y` that is invariant under left translations in the first variable and kills the functions
that vanish on `Γ × X`. Then `Λ Ψ = 0` if the integral of `Ψ (·, y)` for a left Haar measure `μ`
vanishes for each `y ∈ X`. 

 ### Step 1: slices and images 

### `IsSlice`

 `X` is a slice of the closed set `C ⊆ G` for conjugation by `Γ` through `j`: the map
`(g, y) ↦ g y g⁻¹` takes `Γ × X` onto `C`, its fibres are the orbits `{(g h, h⁻¹ y h) | h ∈ H}` of
the closed subgroup `H`, and it is open in the sense of `eventually_exists_conj_mem`. 

### `IsSlice.isClosed_subgroup`

 `H` is closed. 

### `IsSlice.isClosed`

 `C` is closed. 

### `IsSlice.mem_iff`

 `C` is the set of the conjugates of the elements of `X`. 

### `IsSlice.conj_mem_iff`

 A conjugate of an element of `X` lies in `X` exactly if the conjugating element is in `H`. 

### `IsSlice.eventually_exists_conj_mem`

 For every neighbourhood `O` of `1` in `Γ`, the points of `C` near a point of `X` are conjugate
  into `X` by elements of `O`. 

### `IsSlice.conj_mem`

 The set `C` of the conjugates of the elements of a slice `X` is stable under conjugation by
`Γ`. 

### `fibreIntegral`

 The integral of `Ψ` over the orbit `{(g h, h⁻¹ y h) | h ∈ H}` of `(g, y)`, for a measure `ν` on
`H`; here `h` acts on `y` through `j`. 

### `IsImage`

 `f` is an image of `Ψ`: its value at `g y g⁻¹`, for `g ∈ Γ` and `y ∈ X`, is the integral of `Ψ`
over the `H`-orbit of `(g, y)`. 

### `isLocallyConstant_fibreIntegral`

 The integral `fibreIntegral j ν Ψ g y` of a test function `Ψ` over the orbit
`{(g h, h⁻¹ y h) | h ∈ H}` is locally constant in `(g, y)`. 

### `mem_image_tsupport_of_fibreIntegral_ne_zero`

 If the integral of `Ψ` over the orbit `{(g h, h⁻¹ y h) | h ∈ H}` is not zero, then `g y g⁻¹` is
`g' y' g'⁻¹` for a point `(g', y')` in the support of `Ψ`. 

### `IsImage.conjugate`

 Let `f` be an image of `Ψ` (its value at `g y g⁻¹`, for `y ∈ X`, is the integral of `Ψ` over the
`H`-orbit of `(g, y)`), and let `Ψ'` be the left translate of `Ψ` by `a` in the first variable. Then
the conjugate `x ↦ f (a⁻¹ x a)` is an image of `Ψ'`. 

### `IsSlice.isImage_zero`

 Let `X` be a slice, so that `H` conjugates `X` into itself. If `Ψ` vanishes on `Γ × X`, then its
integrals over the `H`-orbits in `Γ × X` vanish, that is, `0` is an image of `Ψ`. 

### `IsInvariantDistribution.eq_of_isImage`

 Let `X` be a slice of `C`, so that `C` consists of the conjugates of the elements of `X`. Two
images `f` and `f'` of `Ψ` agree on `C`, since both are given there by the integrals of `Ψ` over
`H`-orbits. Hence an invariant distribution `I` on `C`, a linear form that is invariant under
conjugation and depends only on the restriction to `C`, has the same value on them. 

### `fibreIntegral_mul_conj`

 For a left Haar measure `ν` on `H`, the integral of `Ψ` over the orbit
`{(g h, h⁻¹ y h) | h ∈ H}` does not change when `(g, y)` is replaced by another point
`(g a, a⁻¹ y a)` of the orbit. 

### `TestFunction.integrable_mul_conj`

 For a closed subgroup `H` and a Haar measure `ν` on it, a test function on `Γ × G` is integrable
along the orbit `h ↦ (g h, h⁻¹ y h)`. 

### `IsImage.add`

 Let `H` be closed, and let `f` and `f'` be images of `Ψ` and `Ψ'` (their values at `g y g⁻¹`,
for `y ∈ X`, are the integrals over the `H`-orbit of `(g, y)`). Then `f + f'` is an image of
`Ψ + Ψ'`. 

### `IsSlice.fibreIntegral_conj_eq`

 Let `X` be a slice. The integral of `Ψ` over the `H`-orbit of `(g, g⁻¹ x g)` is the same for all
`g` that conjugate `x` into `X`, since two such `g` differ by an element of `H`. 

### `IsSlice.isLocallyConstant_fibreIntegral_conj`

 Let `X` be a slice of `C` (the conjugates of `X` make up `C`, and nearby points of `C` are
conjugated into `X` by elements near `1`), and for each `x ∈ C` let `g x` conjugate `x` into `X` (no
continuity of `g` is assumed). The integral of `Ψ` over the `H`-orbit of `(g x, (g x)⁻¹ x (g x))` is
a locally constant function of `x`. 

### `IsSlice.exists_isImage`

 **Images.** Let `X` be a slice of `C` for conjugation by `Γ`: the map `(g, y) ↦ g y g⁻¹` from
`Γ × X` onto `C` is open, and its fibres are the orbits of the closed subgroup `H` of `Γ`. For a
Haar measure `ν` on `H`, every test function `Ψ` on `Γ × G` has an image: a test function `f` on `G`
whose value at `g y g⁻¹`, for `y ∈ X`, is the integral of `Ψ` over the orbit of `(g, y)`. 

 ### Step 2: invariant distributions on images 

### `IsInvariantDistribution.exists_linearMap_eq_of_isImage`

 Let `X` be a slice of `C` and `I` an invariant distribution on `C` (a linear form on the test
functions on `G`, invariant under conjugation by `Γ` and depending only on the restriction to `C`).
There is a linear form `Λ` on the test functions on `Γ × G` such that `Λ Ψ = I f` for every image
`f` of `Ψ` under integration over the fibres of `Γ × X → C`. 

### `IsInvariantDistribution.eq_zero_of_isImage`

 **Descent to a slice.** Let `Γ` have a compact open subgroup `K` and let `μ` and `ν` be Haar
measures on `Γ` and on `H`. Let `X` be a slice of `C` with the fibres of `Γ × X → C` the orbits of
`H`, and let `I` be an invariant distribution on `C`: a linear form on the test functions on `G`
that is invariant under conjugation by `Γ` and depends only on the restriction to `C`. If the
integral of `Ψ (·, y)` over `Γ` vanishes for each `y ∈ X`, then `I f = 0` for every image `f` of
`Ψ`: a test function whose value at `g y g⁻¹`, for `g ∈ Γ` and `y ∈ X`, is the integral of `Ψ` over
the orbit of `(g, y)`. 
