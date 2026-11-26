---
{
  "module": "src/New/Spanning/Unfolding/BesselFormula.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselFormula.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselFormula.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Bessel function as an integral over `R(F_∞)`

The group `R(F_∞)` is the product of the groups `R` at the infinite places. So the tensor product of
the local Bessel functions, each an integral over `R`, is one integral over `R(F_∞)`.

Notions from other files:
* `GInf E ε` is `G(F_∞)`, one copy of `U(diag ε)` for each infinite place of `E`, and `New.G E ε` is
  the adelic group `G(F_∞) × G(𝔸_f)` of the hermitian space `V`. The group `𝔰.G₁` is the complex
  unitary group of `ϱ` hyperbolic planes, the positive form with basis `𝔰.κ` and a negative vector.
* `S.Fits V l kw Y η`: the grading `Y` of `V` is standardly indexed, the Bessel system of the
  filling data `S` at each infinite place `v` has type `(l v, kw v)`, the kernel `typeKernel l ε` is
  idempotent, and the finite part of `V.x` is described by `S` and the central element `η`.
* `Y.besselGroup` is `R = U ⋊ H`, with `U = Y.unipotent` and `H` the unitary group of `κ`, embedded
  by `Y.inclX`; `Y.leviPart (n * Y.inclX a) = a`, and `Y.besselReal` is the group `R(F_∞)` of the
  real points of `R`.
* `𝔰.besselGraph` is the local group `R`, as pairs `(g, a)` in `G₁ × U(κ)` with `g (embedH a)⁻¹` in
  the local unipotent group `besselU`.
* `S.adelicToInf` takes the components at the infinite places in rescaled bases, and
  `h.realHomeomorph` identifies `G(F_∞)` with the product of copies of `G₁`: at each place it
  changes the basis and multiplies on the left by a fixed element, made from the distinguished
  matrix `V.x` of `V`.
* `𝔰.besselGraphMeasure` is the Haar measure `du dh` on the local group `R`, and
  `(l v).dsCoeffInFrame` is the coefficient of the discrete series of parameter `l v` on `G₁`.
* `S.besselSystem v` is the Bessel system at `v`. Its functions take values in `ℂ^I`, with
  `I = (S.besselSystem v).Index` finite, and `U(κ)` acts on `ℂ^I` by the unitary matrices
  `(S.besselSystem v).rep`. An element of `S.BesselCoord` is a choice of one index in `I` at each
  `v`, so `S.BesselCoord → ℂ` is the tensor product of the spaces `ℂ^I`.
* `WeylIndex 𝔰.κ kw` indexes a basis of the Weyl module of weight `kw`, in which forms take values.
* `h.weylBesselEquiv` is a fixed linear identification of the values of forms with the dual of the
  values of the Bessel function, and `ψ_U` is the generic character of `Y.unipotent`.

## Relation to the literature

Related work on Bessel periods and on second moments is listed in `New.Spanning.Unfolding.Moments`.


### `dotProduct_prod_integral`

 The dot product of a vector `a` with the tensor product of finitely many vector-valued integrals
`∫ f v` is one integral over the product space, if each `f v` is integrable. 

### `unitSignEquiv`

 The unitary group of the standard form, written with signs all equal to one, is isomorphic to
the one written with the unit matrix, by the identity on matrices. 

### `coe_unitSignEquiv`

 The isomorphism `unitSignEquiv` does not change the matrix. 

 ### The group `R(F_∞)` place by place 

### `realCoords`

 The homomorphism that takes a real point of the group of `V` to the components at the infinite
places (`S.adelicToInf`) of its image in the adelic group of `S` (`h.adelicEquiv`). At each place it
is a conjugation that carries `U(diag ε)` onto `G₁`. 

### `realCoords_mul_realHomeomorph`

 The homeomorphism `realHomeomorph` turns left translation by `s` into left translation by
`realCoords s`. 

### `realCoordsHomeomorph`

 The map `realCoords` as a homeomorphism: it is `realHomeomorph` followed by right multiplication
by the inverse of its value at one. 

### `adelicToInf_mem_besselU`

 Let `g` lie in `Y.unipotent`, the adelic unipotent group of the grading `Y` of `V`. Carry `g` to
the adelic unitary group of `S` by `h.adelicEquiv`. Then its component in `G₁` at each infinite
place `v` lies in `besselU`, the block upper unitriangular subgroup of `G₁`. 

### `mem_unipotent_of_snd_eq_one`

 Suppose the hermitian space `V` of signs `ε` with grading `Y` fits the filling data `S` (the
hypothesis `h`), so that `h.adelicEquiv` identifies the adelic unitary group `New.G E ε` of `V` with
that of `S`. A point `g` with trivial finite part lies in the unipotent group `Y.unipotent` if, at
each infinite place, the component in `G₁` (`adelicToInf`) of its image under `h.adelicEquiv` lies
in `besselU`, the block upper unitriangular subgroup of `G₁`. 

### `adelicToInf_mul_inv_inclX`

 Let `s` be a real point of the group of `V`, and `a` an adelic point of the unitary group `H` of
the definite form on `𝔰.κ`, embedded by `Y.inclX`. The component in `G₁` at `v` of the adelic point
`(s, 1) * (Y.inclX a)⁻¹` is `realCoords s v`, the component of `(s, 1)`, times the inverse of the
component `a.1 v` of `a`, embedded in `G₁` by `embedH`. 

### `besselRealToPi`

 The components at the infinite places of an element `s` of `R(F_∞)`: the pair of the component
of `s` in `G₁` and of its Levi part in `U(κ)`. 

### `besselRealToPi_apply_fst`

 The component in `G₁` at `v` of `besselRealToPi s` is that of `s`. 

### `besselRealToPi_apply_snd`

 The component in `U(κ)` at `v` of `besselRealToPi s` is that of the Levi part of `s`. 

### `continuous_besselRealToPi`

 The map `besselRealToPi` is continuous, as both components at each place are. 

### `besselRealToPi_surjective`

 Suppose the hermitian space `V` with grading `Y` fits the filling data `S`. Then
`besselRealToPi` is surjective: it maps `Y.besselReal`, the real points of the Bessel group
`R = U ⋊ H` of `Y`, onto the product over the infinite places of the local Bessel group
`𝔰.besselGraph`. 

### `besselRealEquiv`

 The group `R(F_∞)` is the product of the groups `R` at the infinite places: `besselRealToPi` as
an isomorphism of topological groups. 

### `exists_integral_pi_eq`

 Suppose the hermitian space `V` with grading `Y` fits the filling data `S` (the hypothesis `h`),
so that `besselRealToPi` identifies `Y.besselReal`, the real points of the Bessel group `R = U ⋊ H`,
with a product of copies of the local Bessel group `𝔰.besselGraph`. The latter has the Haar measure
`𝔰.besselGraphMeasure`, a product of Haar measures on its unipotent and Levi factors. For a real
constant `c`, the integral of any `F` against the product of these measures is `c` times the
integral of `F ∘ besselRealToPi` against the Haar measure `haar` of `Y.besselReal`. 

 ### The three factors of the integrand 

### `besselChar`

 The standard additive character of `E` at `-(M ϖ)⁻¹` times the sum `simpleRootSum` of the
entries at the simple roots of the image of `r` in the adelic group of `S`. Here `M = S.M` is the
product of the two level primes and `ϖ = S.deltaE` is the chosen generator of the different of `E`.
On `R(𝔸)` this is a character that is trivial on `H(𝔸)`; it extends `ψ_U` when the constant
`c = Y.genericConst` of `ψ_U` satisfies `ȷ * c = -(M ϖ)⁻¹`, where `ȷ = WeilData.j` is the purely
imaginary element of `E` fixed by the Weil data. 

### `besselChar_inl_inv`

 Suppose `V` fits `S`. Let `s` be a point of `GInf E ε = ∏_v U(diag ε)`, so that `(s, 1)` is the
adelic point with infinite part `s` and trivial finite part, and let `g_v = realCoords s v` be its
conjugate in the complex unitary group `G₁` at `v`. The inverse of `besselChar (s, 1)` is the
product over `v` of `wave (-simpleRootSum g_v)`. 

### `conj_typeKernel`

 Suppose `V` fits `S` (the hypothesis `h`), so that `h.realHomeomorph` gives each point of
`GInf E ε = ∏_v U(diag ε)` a component in the complex unitary group `G₁` at each infinite place `v`.
The kernel `typeKernel l ε` is the product over `v` of the formal degree times the conjugate
coefficient of the discrete series of doubled Harish-Chandra parameter `l v`. Its conjugate at
`g⁻¹ y` is the product of the formal degrees times the product of `(l v).dsCoeffInFrame` at
`g_v⁻¹ y_v`, where `g_v` and `y_v` are the components of `g` and `y`, and `dsCoeffInFrame` is the
coefficient carried from `U(diag ε)` to `G₁` by the fixed unitary matrix `UnitarySignFrame 𝔰 ε`. 

### `weylBesselEquiv_conjWeylRep`

 Suppose `V` fits `S` (the hypothesis `h`); in particular the Bessel system `S.besselSystem v` at
`v` has weight `kw v`. Let `ζ` be a vector of the Weyl module of weight `kw`, in the basis indexed
by `WeylIndex 𝔰.κ kw`. A point `a` of `GInf E 1`, the product over `v` of the compact unitary group
`U(κ)` on the index set `𝔰.κ`, acts on `ζ` by `conjWeylRep kw 0 a`, the Schur matrix of the complex
conjugate of `a`; the argument `0` is the exponent of the determinant twist. In the coordinates
`weylBesselEquiv` this action is the transpose of the Kronecker product `kroneckerPi` of the unitary
matrices `(S.besselSystem v).rep` by which `a⁻¹` acts on the values of the local Bessel
functions. 

### `prod_formalDegree_ne_zero`

 If `V` fits `S`, the product over the infinite places `v` of the formal degrees of the discrete
series of parameters `l v` is not zero. 

### `prod_besselIntegrand`

 Suppose `V` with grading `Y` fits `S` (the hypothesis `h`). Let `g`, `y` be points of
`GInf E ε = ∏_v U(diag ε)`, carried to `∏_v G₁` by `realHomeomorph`, and let `u v` be a vector of
the value space `ℂ^I` of the Bessel system at `v`, on which `U(κ)` acts by `rep`. The local
integrand `besselIntegrand l rep x u y` at `(r, a)` in the local Bessel group is
`l.dsCoeffInFrame (x⁻¹ r y) • wave (-simpleRootSum r) • rep a⁻¹ u`. Let `s` be a real point of the
Bessel group of `Y`; its components `besselRealToPi s v` are made with `realCoords`, and
`realCoords s * realHomeomorph y = realHomeomorph (s * y)`. At these components the tensor product
of the integrands, in coordinates `S.BesselCoord`, is the product of the coefficients at
`(realHomeomorph g)⁻¹ * realHomeomorph (s * y)`, times the inverse of `besselChar` at `s`, times the
tensor product of the `u v` moved by the Kronecker product `kroneckerPi` of the matrices `rep` of
the inverse of the Levi part of `s`. 

### `exists_besselFn_eq_integral`

 **The Bessel function as one integral.** Let `E` be a CM field, fix a unitary matrix that
carries the form of `G₁` to the diagonal form of signs `ε`, and suppose the hermitian space `V` with
grading `Y` and central element `η` fits the filling data `S`; in particular the Bessel system of
`S` at `v` has type `(l v, kw v)`. There are a point `g` of `GInf E ε = ∏_v U(diag ε)` and a linear
form `t` on the Weyl module of weight `kw`, whose basis is indexed by `WeylIndex 𝔰.κ kw`, with the
following property. Evaluate the tensor product `S.besselFn .full` of the local Bessel functions
(not their cuts) at a point `y`, carried to `∏_v G₁` by `realHomeomorph`, and pair it with a vector
`ζ` of the Weyl module, carried to the dual of the values of the Bessel function by
`weylBesselEquiv`. The result is the integral of `conj (typeKernel l ε (g⁻¹ s y)) (besselChar s)⁻¹
t(a ζ)` over `s = n a` in `Y.besselReal`, the real points of the Bessel group `R = U ⋊ H` of `Y`,
against the Haar measure `haar`, whose normalisation is absorbed in `t`. 
