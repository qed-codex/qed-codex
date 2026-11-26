---
{
  "module": "src/Lib/Adelic/TraceFormula/TraceComparison.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/TraceComparison.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/TraceComparison.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Comparison of traces of operators on forms for different spaces and signs

A simple trace formula for the unitary group of a hermitian space `V`, with terms sorted by the
characteristic polynomials `R` of rational points. The test function is `e ⊗ φ`, with `e` a cusp
kernel on the real group and `φ` locally constant of compact support on the finite adelic group.

This file proves the Selberg principle: orbital integrals of an irreducible `R` with a root off
the unit circle vanish. For `R` with all roots on the unit circle, it splits orbital integrals into
real and finite factors and matches the classes of different signs. It concludes that the trace on
forms depends neither on the space nor on its signs.

## Main definitions and results

* `New.Space.orbitalIntegral_eq_zero`: the orbital integral is `0` if `R` is irreducible with a root
  off the unit circle.
* `New.Space.exists_geometricSide_singleton_eq`: if `R` is irreducible with all roots on the unit
  circle, `E` contains the 5040th roots of unity and has an even number of infinite places, and the
  parameter has a large gap, its term is a product of characters of the compact unitary group times
  a number that depends only on `R` and `φ`.
* `New.trace_comparison`: let `E` contain the 5040th roots of unity and have an even number of
  infinite places, let `n ≥ 2`, and let the parameter have a large gap. If `φ` is cuspidal at a
  split place and, at a place `w'`, the elements of its support are integral with `0` a simple root
  of the characteristic polynomial modulo `w'`, the reducible `R` contribute nothing, so the trace
  depends neither on the space nor on its signs.

Notions from other files:
* `New.Space E n s`: a hermitian form `J` over `E` with an adelic frame `x` in which it is `diag s`
  at infinity and `1` at the finite places. `V.ratEmbed` embeds `U(J)(E)` in `G = G_∞ × G_f` with
  image `Γ = V.Γ`, and `V.quotMeasure` integrates over `[G] = Γ \ G`.
* `New.IsCuspKernel B e`: `e` is a minimal convolution idempotent on `G_∞` with moment of order
  `B + 1` and decay of order `B`, and `α ⋆ e = e` for some continuous compactly supported `α`.
* `V.polyTerm k φ S γ x`: the value of `k ⊗ φ` at `x⁻¹ γ x` if the characteristic polynomial of `γ`
  lies in `S`, and `0` otherwise.
* `V.formRep e`: the action of `G_f` on the forms of type `e`, which for integrable `e` are the
  bounded automorphic functions on `G` fixed by right convolution with `e`; a level `K` is an open
  subgroup of the standard compact subgroup.
* `New.Space.orbitalIntegral` (in `Lib.Adelic.TraceFormula.OrbitalUnfolding`): the orbital integral
  `I_γ`, the integral of the term of `γ` over `G` modulo the rational centraliser of `γ`.

## Relation to the literature

Comparison of simple trace formulas for unitary groups that differ only at real places. Here
integrable idempotent kernels of very regular discrete series replace pseudo-coefficients, and the
CM field contains the 5040th roots of unity and has an even number of infinite places. There is no
truncation and no endoscopy. Source: Labesse, Changement de base CM et séries discrètes (2011),
Thms 5.4, 5.5 and their proofs; Arthur and Clozel (1989), ch. 1, Lemmas 2.4-2.6; integrable test
functions as in Knightly and Li, Traces of Hecke operators (2006); for the simple trace formula
with a cuspidal component, Flicker and Kazhdan (1988) and Harris and Labesse (2004), Prop. 1.10.5.

Selberg principle that orbital integrals of an idempotent vanish off the elliptic set. Here the
idempotent is a minimal convolution idempotent with polynomial decay on a product of groups
U(p,q), placed inside the adelic orbital integral of a rational point with irreducible
characteristic polynomial. If some eigenvalue has absolute value other than 1, this integral is
zero. Source: Harish-Chandra, Discrete series II, Acta Math. 116 (1966), Thm 11; Blanc and
Brylinski, Cyclic homology and the Selberg principle, J. Funct. Anal. 109 (1992); Hochs and Wang,
Orbital integrals and K-theory classes (2019), Cor 4.8.


 ### The Selberg principle 

### `integral_mul_tripleKernel_tripleRotate`

 The trace property for the triple kernel of `e ⊗ φ` at the rational point `γ`. Let `a` be a
weight on triples that is invariant under left translation by the rational centraliser of `γ`, and
let `b` be `a` composed with the rotation of triples. Then the kernel has the same integral against
`a` and against `b`, if both converge. 

### `mul_orbitalIntegral_eq_zero`

 Let `V` be a hermitian space with a frame, and let `e` be a cusp kernel of order `B ≥ 13 n ^ 3`:
a minimal idempotent with `‖x‖^(B+1) e(x)` integrable, `‖x‖^B e(x)` bounded, and `α ⋆ e = e` for
some continuous compactly supported `α`. Let the rational point `γ` have an irreducible
characteristic polynomial, and let `H` be a measurable function on the real group that moves by at
most `∏_w ‖b_w‖` under right multiplication by `b`. If the real part of `γ` shifts `H` by `ℓ` on the
left and every rational point that commutes with `γ` shifts it by a constant, then `ℓ` times the
orbital integral of `e ⊗ φ` at `γ` (over `G` modulo the rational centraliser of `γ`) vanishes. 

### `orbitalIntegral_eq_zero`

 The Selberg principle: let `e` be a cusp kernel of order `B ≥ 13 n ^ 3`. If the characteristic
polynomial of the rational point `γ` is irreducible and its `i`-th complex root (`numberedRoots`)
under the embedding `Φ w` at the infinite place `w` lies off the unit circle, then the orbital
integral of `e ⊗ φ` at `γ` is zero. 

### `geometricSide_singleton_eq_zero_of_norm_ne_one`

 An irreducible polynomial `R` whose `i`-th complex root at the infinite place `w` lies off the
unit circle does not contribute to the geometric side for `e ⊗ φ` (the integral over `Γ \ G` of the
terms of the rational points with characteristic polynomial `R` is zero). Here `e` is a cusp kernel
of order `B ≥ 13 n ^ 3`. 

 ### All roots on the unit circle 

### `isEllipticSimilitude_of_norm_eq_one`

 A rational point `γ` is an elliptic similitude of `V.J` with multiplier `1` if its
characteristic polynomial is irreducible with all complex roots on the unit circle. 

### `orbitalIntegral_eq_prod_mul`

 Splitting of an orbital integral into real and finite factors, for the product
`typeKernel l s` of the discrete series kernels of parameters `l w`. Let the rational point `γ` be
conjugate by `g` to `(t, y)`, and let `β` be a function on `G_f` such that `x ↦ β (g⁻¹ x)_f` is a
cutoff (a weight of sum one on each orbit) for the rational centraliser of `γ`. Then `I_γ` is the
product of the real orbital integrals at the `t w` and the finite orbital integral at `y`, which is
written with `β`. 

### `exists_ratEmbed_eq_diagTorus`

 Let `y` be an elliptic isometry (multiplier `1`) of a form with Gram matrix `1` in the finite
frame `x` and the sign `s i` on the eigenline of the root `z w (σ w i)`. Then there is a space of
signs `s` with finite frame `x` in which `y` is an isometry, with real component
`diag(z w ∘ σ w)` at each place `w`. 

### `map_embFin_centralizer_le`

 If the finite frames of two spaces conjugate the rational centraliser of `y` in the same way,
then the image in `G_f` of the centraliser of `y` in the first unitary group lies in that for the
second. 

### `map_embFin_centralizer_eq`

 If the finite frames of two spaces conjugate the rational centraliser of `y` in the same way,
then the centralisers of `y` in the two unitary groups have the same image in `G_f`. 

### `map_symm_centralizer_singleton`

 The inverse of a group isomorphism `f` maps the centraliser of `f a` onto that of `a`. 

### `exists_classIntegral_eq`

 Let `E` contain the 5040th roots of unity. Let `y` be an elliptic isometry of a positive form
with orthonormal finite frame `u` (`HasSignType 1 1 y {1} u`), and let `z w` list the roots of its
characteristic polynomial at the place `w`. There is a number `c`, the finite orbital integral of
`φ`, with the following property. Suppose `typeKernel l s`, the product over `w` of the discrete
series kernels `dsKernel` for the parameters `l w`, is a cusp kernel of order `B ≥ 13 n ^ 3`.
Suppose `y` is an elliptic isometry of a form with orthonormal finite frame `x` and signs `s` at the
roots in the order `σ`. Suppose also that `x` conjugates the rational centraliser of `y` as `u`
does. Then on a space `V` of signs `s`, `V.classIntegral` of the class of `(x, y)` is `c` times the
product over `w` of the integrals over `U(diag s)` of `dsKernel` at conjugates of
`diag(z w ∘ σ w)`. 

### `exists_perm_signedClasses`

 Matching the classes. Let `E` contain the 5040th roots of unity, and let `ε`, `ε'` be families
of signs, each with product `1`. There is a permutation `f` of the classes of pairs (finite frame,
rational matrix) that carries those with polynomial `R` and signs `ε` onto those with polynomial
`R` and signs `ε'`. If `(u, y)` has the signs `ε` (`y` is an elliptic isometry, with the signs `ε`
on its eigenlines, of a form with orthonormal frame `u`), then `f` sends its class to the class of
a pair `(x, y)` with signs `ε'` such that `u` and `x` conjugate the rational centraliser of `y` in
the same way. 

### `prod_prod_comp_symm_eq_one`

 If the number of infinite places is even, a family of signs that is a rearrangement of the same
`s` at each place has product `1`. 

### `exists_tsum_signedClasses_eq`

 Let `E` contain the 5040th roots of unity and have an even number of infinite places, and let
`z` be the numbered roots of `R`, on the unit circle. There is a number `c` with the following
property. On every space, suppose the product `typeKernel l s` of the discrete series kernels is a
cusp kernel of order `B ≥ 13 n ^ 3`. Then the contributions of the classes with polynomial `R` and
signs `s` in the order `σ` of the roots add up to the product of the real orbital integrals times
`c`. These classes are `signedClasses`: classes of pairs `(x, y)` with `y` an elliptic isometry of
characteristic polynomial `R`, with those signs on its eigenlines, of a form for which `x` is an
orthonormal frame. 

### `frameClass_mem_signedClasses_iff`

 The class of an elliptic rational point `γ` has the signs `ε` exactly if the form of `V` has
these signs on the eigenlines of `γ`: at each infinite place `w` the matrix `V.J p(γ)` is positive
definite, where `p` takes the value `ε w i` at the `i`-th root. 

### `gram_map_evalInf`

 At the infinite place `w` the frame `V.x` carries the form `V.J` to the diagonal matrix of the
signs `s`. 

### `card_perm_posDef`

 Let `γ` be an elliptic rational point of `V`. For a permutation `σ` take the polynomial with
value `s (σ⁻¹ i)` at the `i`-th eigenvalue of `γ` at `w`. The `σ` for which `V.J` times this
polynomial in `γ` is positive definite are as many as those that fix `s`. 

### `card_mem_signedClasses`

 The class of an elliptic rational point `γ` has the signs `s` in as many orders `σ` of the roots
as there are families, indexed by the infinite places, of permutations that fix `s`. 

### `sum_prod_integral_dsKernel`

 Let the doubled Harish-Chandra parameters `l w` have gap at least `500 n³ + 10 n⁵` and let `z w`
be regular points of the compact torus. The sum over all orders `σ` of the products of the real
orbital integrals of the discrete series kernels is the number of families of permutations that fix
`s` times the product of the conjugate characters of the compact group `U(n)` at the `z w`. The
signs in Harish-Chandra's formula cancel because the number of infinite places is even. 

### `exists_geometricSide_singleton_eq`

 Elliptic terms. Let `E` contain the 5040th roots of unity and have an even number of infinite
places, and let `R` be irreducible with all roots `z w i` on the unit circle. There is a number `c`,
independent of the space, its signs and `l`, such that for all parameters `l` with gap at least
`500 n³ + 10 n⁵` whose kernel is a cusp kernel of order `B ≥ 13 n ^ 3`, the integral over `Γ \ G` of
the terms with characteristic polynomial `R` is `c` times the product of the conjugate characters
of the compact group `U(n)`. 

### `trace_comparison`

 Comparison of traces. Let the CM field `E` contain the 5040th roots of unity and have an even
number of infinite places, let `V`, `V'` be spaces of rank `n ≥ 2` over `E`, and let `l` be a family
of doubled Harish-Chandra parameters with gap at least `500 n³ + 10 n⁵` for the signs of both;
`typeKernel l s` is the product of their discrete series kernels. Let `K` be a level and `a` an
element of the group algebra of the finite adelic group. Suppose that the test function `a ⋆ 1_K`
is cuspidal at a split place `w`, and that the elements of its support are integral at `w'` with
`0` a simple root of the characteristic polynomial modulo `w'`. Then operators that act as `a` on
the forms of parameter `l` and level `K` on `V` and on `V'` have the same trace. 
