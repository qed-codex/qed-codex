---
{
  "module": "src/Lib/Adelic/TraceFormula/OrbitalUnfolding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/OrbitalUnfolding.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/OrbitalUnfolding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Kernels of levels as forms, and unfolding of orbital integrals

This file shows that the conjugate of the kernel of a level `K` is a form of type `e`. It expands
the kernel of `e ⊗ (a ⋆ 1_K)` in an orthonormal basis of forms. It writes `vol K` times the trace
on forms as the integral over `[G] = Γ \ G` of the kernel on the diagonal. It introduces classes
of pairs (finite frame, rational matrix) and orbital integrals, and it unfolds the term of an
irreducible characteristic polynomial into orbital integrals. It ends with triple kernels, the
rotation of triples and the trace property of this rotation.

## Main definitions and results

* `New.Space.exists_kernel_form`, `New.Space.partialKernel_convIndicator_eq_sum`: the conjugate of
  the kernel of a level `K` is a form, and the kernel of `e ⊗ (a ⋆ 1_K)`, for `a` in the group
  algebra of `G_f`, expands in an orthonormal basis.
* `New.Space.volume_mul_trace_eq`: the volume of the level times the trace on forms is the integral
  over `Γ \ G` of the kernel on the diagonal.
* `New.frameClass`, `New.Space.orbitalIntegral_unfold`: classes of pairs (finite frame, rational
  matrix) index the conjugacy classes of all spaces at once, and for irreducible `R` the term of `R`
  unfolds into orbital integrals.

Notions from other files:
* `New.Space E n s`: a hermitian form `J` over `E` with an adelic frame `x` in which it is `diag s`
  at infinity and `1` at the finite places. `V.ratEmbed` embeds `U(J)(E)` in `G = G_∞ × G_f` with
  image `Γ = V.Γ`, and `V.quotMeasure` integrates over `[G] = Γ \ G`.
* `New.IsCuspKernel B e`: `e` is a minimal convolution idempotent on `G_∞` with moment of order
  `B + 1` and decay of order `B`.
* `V.polyTerm k φ S γ x`: the value of `k ⊗ φ` at `x⁻¹ γ x` if the characteristic polynomial of `γ`
  lies in `S`, and `0` otherwise.
* `V.formRep e`: the action of `G_f` on the forms of type `e`, which are the bounded automorphic
  functions on `G` fixed by `e`; a level `K` is an open subgroup of the standard compact subgroup.

## Relation to the literature

Known; see `Lib.Adelic.TraceFormula.TraceComparison` for sources.


 ## The kernel of a level is a form 

### `New.Space.exists_kernel_form`

 Let `e` be a cusp kernel of order `B > 8 n ^ 2` on the real group of a space `V` and `K` a
level, that is, an open subgroup of the standard compact subgroup of `G_f`. For fixed `x` there is a
form of type `e` (a bounded automorphic function fixed by `e`) of level `K` whose conjugate is the
kernel `g ↦ ∑_γ (e ⊗ 1_K)(x γ g)`, the sum over the rational points. 

 ## Orbital integrals and the comparison of traces 

### `FrameClass`

 Classes of pairs `(x, y)` of a finite adelic frame `x`, up to the unitary group on the right,
and an invertible rational matrix `y`, under `z • (x, y) = (z x, z y z⁻¹)` for rational `z`. For a
space `V` the class of `(V.xFin, γ)` records the conjugacy class of the rational isometry `γ`, so
that the conjugacy classes of different spaces can be compared. A pair is stored as a marked triple
with the trivial mark. 

### `frameClass`

 The class of a frame and a rational matrix. 

### `frameClass_eq_iff`

 Two pairs of a finite adelic frame and a rational matrix have the same class if and only if a
rational matrix `z` carries the coset `x' G_f` to `x G_f` and conjugates `y'` to `y`; here `G_f` is
the unitary group of the identity over the finite adeles. 

### `signedClasses`

 The classes of the pairs `(x, y)` in which `y` has the characteristic polynomial `R` and is an
elliptic isometry, with the signs `ε` on its eigenlines, of a form for which `x` is an orthonormal
frame. 

### `orbitalIntegrand`

 The term `(k ⊗ φ)(x⁻¹ γ x)` of a rational point `γ`. 

### `orbitalIntegral`

 The orbital integral `I_γ`: the integral of the term of `γ` over `G` modulo the rational
centraliser of `γ`. 

### `classIntegral`

 For a function `k` on the real group and `φ` on the finite adelic one, the contribution of the
class `c` to the integral of the terms with polynomial `R`: the sum of their integrals against
`V.quotMeasure` for the rational points `γ` such that `(V.xFin, γ)` lies in `c`. 

### `mem_U_one_iff_gram_eq`

 Let `y` be a finite adelic orthonormal frame of the form `β` and `V` a space with form `J` and
finite frame `V.xFin`. A rational matrix `z` carries `y` into the coset `V.xFin G_f` if and only if
`zᴴ J z = β`. 

### `frameClass_eq_iff_mem_orbit`

 For a space `V = (J, x)`, let `V.xFin` be the finite part of `x`. Pairs of a finite adelic frame
and a rational matrix are identified under `(x, y) ~ (z x, z y z⁻¹)` for rational `z`, with frames
taken up to the unitary group on the right. Two rational points `γ`, `δ` of `U(J)`, each paired with
the frame `V.xFin`, give the same class exactly if they are conjugate in `U(J)(E)`. 

### `coe_ratEmbed_fst`

 The component of a rational point `γ` at an infinite place `w` is the image of the matrix `γ`
under the embedding at `w`, read in the frame `V.x` of the space. 

### `polyTerm_charpoly`

 The term of a rational point `γ` for its own characteristic polynomial is the integrand of the
orbital integral of `γ`. 

### `conj_ratEmbed_mul`

 Translating `x` on the left by a rational point `t` that commutes with `γ` does not change
`x⁻¹ γ x`. 

### `fixesLeft_orbitalIntegrand`

 The integrand of the orbital integral of `γ` is left invariant under the image in `G` of the
rational centraliser of `γ`. 

### `measurable_orbitalIntegrand`

 The term of `γ` is measurable if the kernel `k` on the real group is. 

### `exists_frameClass_eq_of_classIntegral_ne_zero`

 For a hermitian space `V = (J, x)` over the CM field `E`, let `V.xFin` be the finite part of
`x`. If the contribution `V.classIntegral k φ R c` of the class `c` to the terms with polynomial `R`
is not zero, then `c` is the class of `(V.xFin, γ)` for some rational isometry `γ` of `J`
(`γ : U V.J`) with characteristic polynomial `R`. 

 ### The kernel 

### `inner_kernel_form`

 Let `e` be a cusp kernel, `K` a level, and `F` the form of type `e` and level `K` whose
conjugate is the kernel of `e ⊗ 1_K` at `g`. The inner product of `F` with a form `v` of this type
and level is `vol K` times the value of `v` at `g`. 

### `tsum_kernel_eq_sum`

 The kernel for the characteristic function of the level: if `e` is a cusp kernel of order
`B ≥ 13 n ^ 3`, `K` a level and `b` an orthonormal basis of the forms of type `e` and level `K`,
then `∑_γ (e ⊗ 1_K)(g⁻¹ γ g') = vol K ∑_i b_i(g) conj(b_i(g'))`. 

### `partialKernel_convIndicator_eq_sum`

 The kernel: let `e` be a cusp kernel of order `B ≥ 13 n ^ 3`, `K` a level, `b` an orthonormal
basis of the forms of type `e` and level `K`, and `a` an element of the group algebra of `G_f`. Then
the kernel `∑_γ (e ⊗ (a ⋆ 1_K))(g⁻¹ γ g')`, the sum over all rational points, is
`vol K ∑_i (a b_i)(g) conj(b_i(g'))`. Here `convIndicator` forms `a ⋆ 1_K`. 

### `volume_mul_trace_eq`

 Let `e` be a cusp kernel of order `B ≥ 13 n ^ 3`, `K` a level, and `T` an operator that acts as
the element `a` of the group algebra on the forms of type `e` and level `K`. Then `vol K` times the
trace of `T` is `V.geometricSide` of all polynomials at `a ⋆ 1_K`, that is, the integral over `[G]`
of the kernel of `e ⊗ (a ⋆ 1_K)` on the diagonal. 

 ### Unfolding 

### `lintegral_tsum_polyTerm_lt_top`

 For a test function `φ` and a function `k` on the real group of a space `V` with decay of order
`B ≥ 13 n ^ 3`, the terms with an irreducible polynomial `R` converge absolutely in sum and
integral over `[G]`. 

### `hasSum_classIntegral`

 Let `φ` be a test function on `G_f`, let `k` be measurable on `G_∞` with
`‖k g‖ (∏_w ‖g_w‖) ^ B` bounded, where `B ≥ 13 n ^ 3`, and let `R` be irreducible. The integral over
`[G]` of the sum of the terms `(k ⊗ φ)(x⁻¹ γ x)`, over the rational points `γ` with characteristic
polynomial `R`, is the sum over all classes `c` of their contributions `V.classIntegral k φ R c`. 

### `orbitalIntegral_unfold`

 Unfolding: let `φ` be a test function on `G_f` and `k` a measurable function on the real group
with `‖k g‖ (∏_w ‖g_w‖) ^ B` bounded, where `B ≥ 13 n ^ 3`. If the rational isometry `γ` has an
irreducible characteristic polynomial, then its term `(k ⊗ φ)(x⁻¹ γ x)` is integrable over `G`
modulo the rational centraliser. Moreover, its orbital integral equals the sum of the integrals over
`Γ \ G` of the terms of the rational points `γ'` whose pair `(V.xFin, γ')` lies in the class of
`(V.xFin, γ)`. Here `V.xFin` is the finite part of the frame of `V`. 

 ### Two lemmas on matrices, and triple kernels 

### `row_mul_eq_smul_of_commute`

 If the invertible matrix `k` conjugates `A` to a diagonal matrix with distinct entries `d`, then
a matrix `t` that commutes with `A` multiplies the `i`-th row of `k` by a scalar, the `i`-th
diagonal entry of `k t k⁻¹`. 

### `abs_log_norm_mul_sub_le`

 For a nonzero matrix `Q` and points `a`, `b` of the real group, multiplying `a` by `b` on the
right moves `log ‖Q a_w‖` by at most `‖b_w‖`, in the operator norm. 

### `tripleMeasure`

 The measure on triples `(x, y, u)`, with `x` in `G` modulo the rational centraliser of `γ` and
`y`, `u` in the real group. 

### `tripleKernel`

 The integrand of `I_γ` with `e` written as a triple convolution, at a triple `(x, y, u)` with
`x` in `G` and `y`, `u` in the real group. For the kernel `p(a, b) = e(a⁻¹ b)` on the real group
its factor at infinity is `p(x, x y) p(x y, x y u) p(x y u, γ x)`. 

### `tripleRotate`

 The map of triples `(x, y, u)` that replaces the points `x, x y, x y u` by
`x y, x y u, x ((x⁻¹ γ x)_∞, 1)`. 

### `tripleKernel_tripleRotate`

 The triple kernel is invariant under the rotation of triples. 

### `tripleKernel_ratEmbed_mul`

 The triple kernel of `γ` is left invariant in `x` under the rational points commuting with
`γ`. 

### `measurable_tripleKernel`

 The triple kernel of `γ` is measurable if the kernel `e` on the real group is. 

### `integral_comp_tripleRotate`

 The trace property: for a rational point `γ`, composing with the rotation `V.tripleRotate γ` of
triples does not change the integral for `V.tripleMeasure γ` of a measurable integrable function
`f`, integrable also after the rotation, that is left invariant in `x` under the rational
centraliser of `γ`. Here `V.tripleMeasure γ` lives on triples `(x, y, u)` in `G × G_∞ × G_∞`, with
`x` taken modulo that centraliser, and `V.tripleRotate γ` sends the points `x, x y, x y u` to
`x y, x y u, x ((x⁻¹ γ x)_∞, 1)`. 

### `integrable_mul_tripleKernel`

 Let `e` be a cusp kernel of order `B ≥ 13 (card n)^3`, `φ` a test function on `G_f`, and `γ` a
rational point of `U V.J` with irreducible characteristic polynomial. Let `a` be a measurable weight
on triples `(x, y, u)` (`x` in `G`; `y`, `u` in the real group) with `|a (x, y, u)| ≤ ‖y‖ ‖u‖`, each
norm being the product over the infinite places of the operator norms. Then `a` times
`V.tripleKernel e φ γ` is integrable for `V.tripleMeasure γ` (the measure on such triples with `x`
taken modulo the rational centraliser of `γ`). Here `V.tripleKernel e φ γ` is the integrand of `I_γ`
with `e` written as a triple convolution; its factor at infinity is
`p(x, x y) p(x y, x y u) p(x y u, γ x)` for `p(a, b) = e(a⁻¹ b)`. 

### `integral_tripleMeasure`

 Fubini's theorem for an integrable function of triples `(x, y, u)`, after a substitution `S` in
`(y, u)` that preserves measure. 

### `integral_mul_tripleKernel_mul`

 Let `e` be a cusp kernel, `φ` a test function, and `b` a weight such that both integrands below
are integrable. As `e ⋆ e = e`, the weight may be read at `y u` or at `y` against the triple kernel
of `γ`: both integrals reduce to that of `b(x, y) p(x, x y) p(x y, γ x)` times the factor of `φ`,
where `p(g, h) = e(g⁻¹ h)` on the real group. 
