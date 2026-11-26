---
{
  "module": "src/Lib/Adelic/TraceFormula/ReduciblePolynomials.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/ReduciblePolynomials.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/ReduciblePolynomials.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The geometric side, polynomial by polynomial

The geometric side of the trace formula is the integral over `x ∈ [G]` of the sum of the values
of `k ⊗ φ` at `x⁻¹ γ x`, over the rational points `γ`. For a cusp kernel `k` of large enough order
it is the sum of the parts given by the characteristic polynomials `R` of the `γ`. If moreover `φ`
is cuspidal at one split place and, on its support, `0` is a simple root of the characteristic
polynomial modulo a place `w'`, then the part of an `R` that is not irreducible is `0`.

Notions from other files:
* `Space E n s`: a hermitian space `V` over `E`, with a matrix `V.J` and an adelic point;
  `U V.J` is its group of rational points and `V.ratEmbed` maps that group into `G E s`.
* `G E s`: the adelic unitary group, with factors `GInf E s` at the infinite places and `Gf E n`
  at the finite ones; `V.Γ` is the image of `U V.J` in it and `V.quotMeasure` computes integrals
  over the quotient `[G] = V.Γ \ G E s`.
* `V.polyTerm k φ S γ x`: the value of `k ⊗ φ` at `x⁻¹ γ x` if the characteristic polynomial of
  `γ` lies in `S`, and `0` otherwise.
* `IsCuspKernel B k`: the kernel `k` on `GInf E s` is a minimal idempotent for convolution that is
  reproduced by a compactly supported function and decays to order `B`.
* `IsCuspidalAt hw φ`: at the split place `w` the sums of the translates of `φ` over the unipotent
  radicals of the proper parabolic subgroups over the residue field vanish.

Part of a known result: Comparison of simple trace formulas for unitary groups that differ only at
real places. See `Lib.Adelic.TraceFormula.TraceComparison`.


### `exists_isCoprime_mul_of_not_irreducible`

 A monic polynomial that is neither irreducible nor a proper power is a product of two coprime
polynomials of positive degree. 

### `charpoly_atPlace_conj_ratEmbed`

 Let `γ` be a rational point of the space `V`, embedded by `V.ratEmbed` in the adelic group, and
`x` an adelic point. At a finite place `w`, the characteristic polynomial of the component of
`x⁻¹ γ x` is the image over the completion `LocField w` of the characteristic polynomial of `γ`. 

### `tsum_polyTerm_ratEmbed_mul`

 For a set `S` of polynomials, the sum of `V.polyTerm k φ S γ x` over the rational points `γ`,
that is, of the values of `k ⊗ φ` at `x⁻¹ γ x` for the `γ` with characteristic polynomial in `S`,
does not change when `x` is multiplied on the left by a rational point `δ`. 

### `measurable_tsum_polyTerm`

 For a measurable `k` and a test function `φ`, the sum of the values of `k ⊗ φ` at `x⁻¹ γ x`,
over the rational points `γ` with characteristic polynomial in `S`, is measurable in `x`. 

### `integrable_tsum_polyTerm`

 Let `k` be a cusp kernel of order `B ≥ 13 * card n ^ 3` (`IsCuspKernel`), and `φ` a test
function. The sum of the values of `k ⊗ φ` at `x⁻¹ γ x`, over the rational points `γ` with
characteristic polynomial in `S`, is integrable in `x` over the quotient `[G]` of the adelic
group by the rational points, for the measure `V.quotMeasure`. 

### `geometricSide`

 The part of the geometric side given by the polynomials in `S`: the integral over `[G]` of the
sum of the values of `k ⊗ φ` at `x⁻¹ γ x`, over the rational points `γ` whose characteristic
polynomial lies in `S`. Here `k` is a cusp kernel of order `B ≥ 13 * card n ^ 3`, so the sum is
integrable. It is a linear form in the test function `φ : TestFunction (Gf E n)`, which has an
underlying function `φ.1 : Gf E n → ℂ`. 

### `geometricSide_apply`

 The value of the linear form `geometricSide` at `φ`, as an integral over `[G]`. 

### `geometricSide_coe_finset`

 Let `k` be a cusp kernel of order `B ≥ 13 * card n ^ 3` and `φ` a test function. For a finite
set `F` of polynomials, the part `geometricSide F` of the geometric side, which is the integral
over `[G]` of the sum of the values of `k ⊗ φ` at `x⁻¹ γ x` over the rational points `γ` with
characteristic polynomial in `F`, is the sum of the parts given by the elements of `F`. 

### `hasSum_geometricSide`

 Let `V` be a hermitian space with a point over the CM field `E`, and let `φ` be a test function
on `G_f`. Let `k` be a cusp kernel of order `B ≥ 13 * card n ^ 3` on `G_∞`: a minimal idempotent for
which `‖x‖^(B+1) k(x)` is integrable, `‖x‖^B k(x)` is bounded, and `α ∗ k = k` for some continuous
compactly supported `α`. The geometric side, which is the integral over `[G]` of the sum of the
values of `k ⊗ φ` at `x⁻¹ γ x` over all rational points `γ`, is the convergent sum over the
polynomials `R` of its parts given by the `γ` with characteristic polynomial `R`. 

### `geometricSide_translate`

 Let `k` be a cusp kernel of order `B ≥ 13 * card n ^ 3`. Each part `geometricSide S` of the
geometric side, an integral over the quotient of the adelic group by the image `V.Γ` of the rational
points, is invariant under the conjugation `TestFunction.translate (g, g)` of the test function,
`y ↦ φ(g⁻¹ y g)`, by a finite adelic point `g`. The proof is the substitution `x ↦ x * (1, g)`. 

### `geometricSide_singleton_eq_zero_of_forall`

 For a cusp kernel `k` of order `B ≥ 13 * card n ^ 3`, the part of the geometric side given by
the polynomial `R` (the integral of the sum over the rational points with characteristic polynomial
`R`) is `0` if the test function `φ`, with underlying function `φ.1`, vanishes at all finite adelic
points whose component at the finite place `w` has as characteristic polynomial the image of `R`
over the completion `LocField w`. 

### `geometricSide_singleton_eq_zero`

 Let `k` be a cusp kernel of order `B ≥ 13 * card n ^ 3`. Let the test function `φ` be cuspidal
at the split place `w` (the sums of its translates over the unipotent radicals of the proper
parabolic subgroups over the residue field vanish), and let each point of the support of `φ` be
integral at `w'` with `0` a simple root of its characteristic polynomial modulo `w'`
(`HasSimpleZero`). If the polynomial `R` is not irreducible, then the part of the geometric side
given by `R`, the integral of the sum over the rational points with characteristic polynomial `R`,
is `0`. 
