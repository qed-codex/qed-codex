---
{
  "module": "src/New/OneLift/ComparisonOperator/GluedForms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/GluedForms.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/GluedForms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Gluing: the descent of product forms and the denominators

This file treats forms on the definite space `V = V″ ⊕ V°` glued, in
`New.OneLift.ComparisonOperator.GluedLattices`, from a vector for `V″` and a vector for `V°`
across a change of lattice at the chosen places.

The data are a descent pair `O` (`New.DescentPair`), with the space `W = O.W` of rank `r`, and a
splitting `V : New.Rows.DividedSplitting N m a O z`. Here `N` indexes `V″`, `m` indexes `V°`,
`z : r ↪ m` marks `r` basis vectors of `V°`, and `a` indexes the rows of a matrix `s` modulo `ϖ²`,
the linear forms on `V″` on which a finer congruence is imposed. The idele `ϖ = O.genIdele`
generates the product of the chosen places `O.chosenPlace i`, and `Q` is the product of the places
`O.twistPlace i`. We write `(1; 0)` for an inclusion matrix `New.inclMatrix` with `r` columns.

The datum of the theta lift from `W` to `V` asks for `x ≡ (1; 0)` modulo `ϖ`. A product datum asks
for conditions modulo `ϖ²` on the two blocks of `x`. The lattice that connects them is spanned by
the columns of the matrix that is `(1; 0)` on both summands, by `L″_s = {u | s u ≡ 0 modulo ϖ}` in
`V″` and by `ϖ` times the standard lattice of `V°`. The matrix of a basis is called `γ`, and it is
handled through the integral matrix `ϖ γ⁻¹`.

This file computes the descent to `W` of product forms on a glued lattice, from which the slices
of a lift are read off. It also bounds the p-adic gauge of the Cartan product at the point
`(h, h') γ`.

## Main definitions and results

* Slices of lifts. `New.Rows.DividedSplitting.normalizedDescent_productForm`: if `V.IsGlued s L` and
  `b * b' = O.charV`, the descent to `W` of a product form is the complex conjugate of the product
  of `L.weilScalar` with a sum over the congruence group, whose terms are products of a kernel on
  `V″` and one on `V°`. `New.Rows.DividedSplitting.normalizedDescent_stdClassSum_productForm`: the
  same for the sum of product forms over the classes, with `New.Rows.kernelClassSum` on `V″`.
* The denominators. `New.Rows.DividedSplitting.weylGauge_cartanProduct_le`: for a glued lattice, a
  natural number `M ≠ 0` divisible by `ϖ` and points `h`, `h'` on the two summands, the gauge of
  the product of two vectors at the point `(h, h') γ` (with `(h, h')` made block diagonal along
  `V.ε : N ⊕ m ≃ n`) is at most `‖M‖⁻¹ ^ V.denominatorExponent` times their gauges.

Notions from other files:
* `New.DescentPair`: A descent pair: chosen places and twist places, a space W of rank r with
  numbered basis vectors, an embedding of indices into n > r, two diagrams given by their numbers of
  columns of each height, and a character μ whose tame part, a character `O.tamePart w` of the
  residue field at each place w, is trivial off these places.
* `New.LevelPlaces.levelModulus`, `New.Rows.liftMod`: `levelModulus c` is the modulus ϖ^c·Q, and
  `levelModulus c false` is ϖ^c. `liftMod` is a chosen lift of an invertible matrix modulo an
  ideal to an integral point of G_f that is 1 outside the places dividing the ideal and their
  conjugates.
* `New.inclMatrix`: For a map u: m → n of index sets, the n×m matrix whose j-th column is the
  standard basis vector e_{u(j)}.
* `New.modKernel`: The theta kernel at (g, h) of the datum given by a function on matrices modulo an
  ideal and the Fock vector of a polynomial.
* `New.WeylIndex`: `WeylIndex n κ` indexes the standard basis of the vectors of weight κ in n
  letters. Here `κ τ h` is the number of columns of height h at the infinite place τ.

## Relation to the literature

See `New.OneLift.ComparisonOperator.GluingMaps` and
`New.OneLift.ComparisonOperator.FirstFactors` for related work.



## The descent of product forms

The descent `O.normalizedDescent` pairs a form on `V` with the theta kernel; it is adjoint to the
lift from `W`. So the slices of a lift are read off from the descents of product forms.

* `New.Rows.DividedSplitting.normalizedDescent_classForm_mul`: the descent of the form supported on
  the class of `h * L.point` is the complex conjugate of the product of `L.weilScalar` with a kernel
  at `h`. The datum of the kernel at `S` is nonzero only when `(ϖ γ⁻¹) S ≡ ϖ (1; 0)` modulo `ϖ²`.
  There it is a product of values of `O.tamePart` on determinants at the places of `Q`.
* `New.Rows.fockPoly_cartanProduct`: the Fock polynomial of the product of a vector on `V″` and a
  vector on `V°` is the product of their polynomials.


### `kernelClassSum_smul`

 The kernel `kernelClassSum` of `c • y` is `c` times that of `y`. It is the sum, over classes `h`
of the level fixing the rows `w` and the columns off `e`, of the theta kernel of W (signs `O.signs`)
and the standard space on `m`, with character `b` on the latter and the polynomial of `y h`. 

### `letterPoly_schur_inclMatrix_mulVec`

 Let `f : N → n` map the letters `N` to the letters `n`, and let `κ` satisfy
`HasColumnsBelow n N κ`: `#N ≤ #n`, and `κ` has no column of a height `h` with `#N ≤ h < #n`. The
polynomial `letterPoly` of the image of `y` under the Schur matrix of the inclusion matrix of `f` is
the polynomial of `y` with the rows of its variables renamed along `f`. 

### `fockPoly_cartanProduct`

 Let `ε : N ⊕ m ≃ n` split the indices of `V = V″ ⊕ V°`, and let `O.colsPlus` and `O.colsMinus`
satisfy `HasColumnsBelow`: each column of height below the rank of `V` has height below the rank of
`V″`, respectively of `V°`. For `y` of weight `O.colsPlus` on `V″` and `η` of weight `O.colsMinus`
on `V°`, the polynomial `O.fockPoly` of `cartanProduct ε 1 y η` is the polynomial `letterPoly` of
`y` in the variables of the basis vectors of `O.W` of sign `1` on the rows of `V″`, times that of
`η` in the variables of sign `-1` on the rows of `V°`. 

### `idem_mul_mem_of_inv_mul_mem`

 Let `ϖ` generate the product of the chosen places of `O`, let `Q` be the product of its twist
places, and let `idem` be the adele that is `1` at the places dividing `ϖ² Q = O.levelModulus 2` and
`0` elsewhere. Let `γ = L.point` be a unitary point at the chosen places with `ϖ γ⁻¹` integral. If
`idem * (γ⁻¹ x)` has integral entries, then so has `idem * x`. 

### `liftFn_datum_point_inv_mul`

 Let `ϖ` generate the product of the chosen places, with class `V.genResidue` modulo `ϖ²`, let
`Q` be the product of the twist places, and let `ι` be the inclusion matrix of `O.incl : r ↪ n`. The
map `liftFn` extends a function on matrices modulo `ϖ² Q` to adelic vectors `x`, by `0` where `x` is
not integral at the places of `ϖ² Q`. Consider two functions of `T`, supported on `ϖ T ≡ ϖ ι` and on
`(ϖ γ⁻¹) T ≡ ϖ ι` modulo `ϖ²`, where `γ = L.point` and `L.reducedInverse` is `ϖ γ⁻¹` modulo `ϖ²`. On
its support each is the product over the twist places of the residue characters `O.tamePart` at the
determinant of the rows `O.incl` of `T`. Then the extension of the first at `γ⁻¹ x` equals that of
the second at `x`. 

### `normalizedDescent_classForm_mul`

 Let `v` be a vector of the weight whose columns are counted by `O.columnCount`, and let
`γ = L.point`, so that `L.reducedInverse` is `ϖ γ⁻¹` modulo `ϖ²`, with `ϖ` generating the product of
the chosen places. The form `classForm O (h γ) v` on the standard definite space of rank `n` is
supported on the class of `h γ`. Its descent `O.normalizedDescent` to the space `O.W` is, at `g`,
the complex conjugate of a product of two factors. One is `L.weilScalar = χ(δ) / √|δ| ^ #r`, with
`δ` the determinant of `γ` at the chosen places and `χ` the character attached to `O.charW`. The
other is the theta kernel `modKernelStdSpace` of `O.W` and the standard space at `(g, h)`, for the
characters `O.charW`, `O.charV` of the two spaces, the Fock polynomial `O.fockPoly (star v)` of the
conjugate vector, and the following function of `S` modulo `ϖ² Q`. It is `0` unless
`(ϖ γ⁻¹) S ≡ ϖ • inclMatrix _ O.incl` modulo `ϖ²`, and it is then the product over the twist places,
those of `Q`, of the residue characters `O.tamePart` at the determinant of the rows `O.incl` of
`S`. 

### `prod_twist_det_eq_inv_mul_charOfTamePart`

 Let `Y` be invertible modulo `ϖ²` and `1` modulo `ϖ`, let `k = liftMod Y` be its chosen lift to
an integral unitary point, reduced at a place by `stdLevel.reduceAt`, and let `x` be a matrix modulo
`ϖ² Q`. Suppose that the rows `S` of `x Y` in `N` satisfy `w S = w ι` modulo `ϖ²`, where
`w = V.stackOverGenScalar s` is `s` stacked above `ϖ • 1` and `ι` is the inclusion matrix of
`V.fixedEmb`. Then the product over the twist places of the residue characters `O.tamePart` at the
determinant of the rows `O.incl` of `x` is `χ` of the determinant of the same rows of `x k`, divided
by the product of `O.tamePart (det k)` over the twist places. Here `χ = charOfTamePart` is the
product of the `O.tamePart` over all places dividing `ϖ² Q`. 

### `normalizedDescent_productForm`

 Let `V.ε : N ⊕ m ≃ n` split the standard definite space on `n` as `V″ ⊕ V°`, with indices `N`
and `m`. Let `ϖ` generate the product of the chosen places, let the lattice `L` with point `γ` be
glued for `s` (`IsGlued`), and let the characters `b`, `b'` have product `O.charV`. The product form
is the form supported on the class of `diag(h, h') γ` built from the Cartan product of `y` and `η`.
Its descent to `O.W` is, at `g`, the complex conjugate of `L.weilScalar = χ(δ) / √|δ| ^ #r` (`δ` the
determinant of `γ` at the chosen places, `χ` attached to `O.charW`) times a sum over `Y` in
`V.congruenceGroup`, the invertible matrices modulo `ϖ²` that are `1` modulo `ϖ`. The term of `Y` is
a product of two theta kernels `modKernelStdSpace` of `O.W` with a standard space, at `g` times the
integral lift `liftMod Y`.
* On `V″`, at `h`: the finite datum `columnDatum` at `σ` is the character `charOfTamePart` of the
determinant of the rows `e = V.fixedEmb` of `σ` if `w σ ≡ w * inclMatrix _ e` modulo `ϖ²`, where
`w = V.stackOverGenScalar s` is `s` above `ϖ • 1`, and `0` otherwise. The polynomial is that of
`star y` in the basis vectors of `O.W` of sign `1`.
* On `V°`, at `h'`: the datum is the indicator of the inclusion matrix of `z : r ↪ m`, and the
polynomial is that of `star η` in the basis vectors of sign `-1`. 

### `normalizedDescent_stdClassSum_productForm`

 Let the lattice `L` with point `γ` be glued for `s`, and let `b * b' = O.charV`. Fix a point
`h'` of `Gf E m` on `V°`. Sum (`stdClassSum`) the forms supported on the class of `diag(h, h') γ`
and built from `φ h` and `η` (`productForm`) over the classes `h` of level `rowFixingLevel`. The
descent `O.normalizedDescent` of this sum to `O.W` is, at `g`, the complex conjugate of
`L.weilScalar` times a sum over the invertible matrices `Y` modulo `ϖ²` that are `1` modulo `ϖ`. The
term of `Y` is `kernelClassSum`, the theta kernel of `O.W` and `V″` summed over those classes, times
the theta kernel `modKernelStdSpace` of `O.W` and `V°` at `h'`. Both are taken at `g` times
`liftMod Y`, an integral lift of `Y`. 


## A p-adic gauge bound for the Cartan product

In this section `V` is a divided splitting of the descent pair `O` along `z`, `p` is a prime, `ι` is
a p-adic place (an embedding of ℂ in ℂ_p) and `M` is a nonzero natural number. The bounds assume
that `M` is divisible by `ϖ`.

* `New.Rows.DividedSplitting.denominatorExponent`: the exponent of `M` that the change of lattice
  costs. On `V″`, where the columns of the diagram are long, it costs `card a` for each column,
  whatever the height.

The gauge `New.weylGauge κ e g ξ` is the largest `p`-adic absolute value of a coordinate of `g⁻¹`
applied to `ι ∘ ξ` in the weight `(κ, e)`. The place `ι` is not a positional argument. It comes from
the `PadicPlace p` instance, or it is given by name as `(ι := …)`.


### `denominatorExponent`

 The exponent of `M` in the denominator: at each infinite place `τ`, `card a` times the number of
columns of `O.colsPlus` of height below `card N` (a column has distinct entries, so at most `card a`
of them lie in the range of `V.dividedEmb`, the copy of `a` in `N`), plus `card m` times the number
of columns of `O.colsMinus` of height below `card m`, a bound for the number of their boxes. In both
diagrams the entry at `τ h` counts the columns of height `h`. 

### `norm_schur_diagonal_piecewise_inv_le`

 For a prime `p`, a natural number `M ≠ 0` and a set `S` of indices, the Schur matrix of weight
`κ` over `ℂ_[p]` of the diagonal matrix that is `M⁻¹` on `S` and `1` elsewhere has entries of p-adic
norm at most `‖M‖⁻¹ ^ (Σ_τ #S · c_τ)`, with c_τ the number of columns of `κ τ` of height below
`card l` (`κ τ h` counts those of height `h`). 

### `norm_schur_inv_cols_le_weylGauge`

 The bound for one block of columns `f : l → n`. Let `ι` be a p-adic place, with map
`ιₚ : ℂ → ℂ_[p]`, and let `M ≠ 0` lie in the ideal `(ϖ) = O.levelModulus 1 false`, the product of
the chosen places of `O`. Let `κ` have no column of height in `[card l, card n)`. Let `γ = L.point`
be a point of the finite adelic unitary group `Gf E n` at the chosen places with `ϖ γ⁻¹` integral,
and `L.reducedInverse` the matrix `ϖ γ⁻¹` modulo `ϖ²`. After an invertible change of its
`f`-columns, let those with index `j ∉ S` be killed by `V.genResidue`, the class of `ϖ`. Let the
`f`-columns of `g⁻¹` be those of `h⁻¹` placed along `f`. Read the `f`-columns of `(g γ)⁻¹` in
`ℂ_[p]` at each `τ` by the extension (`adeleExtension`) of the embedding `weightEmbedding ιₚ τ` of
`E` to the finite adeles. Then their Schur matrix sends `ιₚ ∘ v` to a vector of norm at most
`‖M‖⁻¹ ^ (Σ_τ #S · c_τ)` times `weylGauge κ 0 h v`, the sup norm of `h⁻¹` applied to `ιₚ ∘ v` in
weight `κ` twisted by the power `0` of the determinant. Here c_τ is the number of columns of `κ τ`
of height below `card l`. 

### `weylGauge_cartanProduct_le`

 Let `V.ε : N ⊕ m ≃ n` split the indices, let `ι` be a p-adic place, and let `M ≠ 0` lie in the
ideal of `O.levelModulus 1 false`, the product of the chosen places of `O`. Let the lattice `L` with
point `γ = L.point` be glued for `s`. The diagrams `O.colsPlus` and `O.colsMinus` count the columns
of each height at each infinite place. The vector `y` has the first weight in the letters `N` and
`η` has the second in the letters `m`. Their product `cartanProduct V.ε 1 y η` includes both in the
letters `n` (it is moved by `1`) and projects their tensor product to the weight with column numbers
`O.columnCount` and determinant exponents `O.detExp`. Then the gauge of the product at
`U.block V.ε (h, h') * γ`, with `U.block` the block diagonal matrix, is at most
`‖M‖⁻¹ ^ V.denominatorExponent` times the gauge of `y` at `h` and the gauge of `star η` at `h'`, the
latter through the conjugate embedding. 
