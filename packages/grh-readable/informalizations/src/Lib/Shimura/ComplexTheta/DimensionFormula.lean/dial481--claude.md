---
{
  "module": "src/Lib/Shimura/ComplexTheta/DimensionFormula.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ComplexTheta/DimensionFormula.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ComplexTheta/DimensionFormula.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Theta functions on complex tori: dimension formula, base points, multipliers

This file treats Appell–Humbert data `(B, χ)` with positive Riemann form `E` for a full lattice
`L` in a finite-dimensional complex space `V`. It proves the convergence of theta series and the
existence of a nonzero theta function. It proves that the square of the dimension of the space of
theta functions equals the index of `L` in its dual lattice, and that the twisted translations by
the dual lattice act irreducibly. It shows that multiples of a positive type have no base point.
It also defines the canonical multiplier and the normalised translations.

## Main definitions and results

* `New.IsAppellHumbert.finrank_sq_eq_relIndex`: for Appell–Humbert data with positive `E`,
  `(dim thetaSpace)² = [dual : L]`, the dimension is positive, and the twisted translations by the
  dual lattice span all endomorphisms of the space of theta functions; so the space is irreducible
  (`New.IsAppellHumbert.thetaSpace_le_of_thetaShift_mem`, `New.IsAppellHumbert.schur_lemma`).
* `New.IsAppellHumbert.exists_mem_thetaSpace_nsmul_apply_ne_zero`: for Appell–Humbert data with
  positive `E` and `n ≥ 2` the theta functions of type `(n B, χ ^ n)` have no common zero.
* `New.ThetaTori.canonicalMultiplier`, `New.ThetaTori.normalizedShift`: a canonical multiplier
  `exp (πi E(b x, x))` for a linear map `b`, and the twisted translations divided by it, which, for
  Appell–Humbert data and `b` with `E (b u) w = E u w - E u (b w)`, obey a Heisenberg law
  (`New.IsAppellHumbert.normalizedShift_normalizedShift`).

Notions from other files:
* `New.RealComplexForm.thetaSpace`: the entire `f` with
  `f (z + l) = χ l * exp (B l z + B l l / 2) * f z` for `l ∈ L`.
* `New.RealComplexForm.thetaShift`: translation by `a` twisted by `exp (-(B a z + B a a / 2))`.
* `New.RealComplexForm.dualLattice`: the `v` in `V` with `E(v, l)` an integer for all `l` in `L`.

## Relation to the literature

Frobenius' dimension formula and irreducibility of the theta group. Here the statement is
basis-free, with the square of the dimension equal to the index of the lattice in its dual. It is
proved together with irreducibility from a theta kernel on the torus without a symplectic basis, and
the orthogonality relation and the absence of base points follow. Source: G. Frobenius, Über die
Grundlagen der Theorie der Jacobischen Functionen, Crelle 97 (1884); Birkenhake–Lange, Complex
Abelian Varieties, 3.2.7, 4.1.5, 6.4; survey of proofs in D. Bump, A. Pekker, Proc. AMS 130 (2002)
3473–3481.

See also `Lib.Shimura.Uniformisation.AppellHumbert`.


 ### Convergence of theta series 

### `IsAppellHumbert.summable_and_analyticAt_tsum`

 Normal convergence of theta series, for Appell–Humbert data (B, χ) (instance `hB`). Let `T c`,
for `c` in a finite-dimensional complex space `P`, be real-linear maps of `V`, analytic in `c`
near `b`, with `Re (B x (T b x)) > 0` for `x ≠ 0`. The series over `l ∈ L` with terms
`term q l = exp (exponent q l) / χ l`, where
`exponent q l = ξ (u + T c l) - B l z - B l (T c l) / 2` at `q = (c, ξ, u, z)`, converges at
`c = b` for every `p = (ξ, u, z)`, and its sum is analytic in `q` at `(b, p)`. 

### `IsAppellHumbert.poincareSeries_mem_thetaSpace_and_quotMean`

 Let `L` be a full-rank lattice in a finite-dimensional complex space `V`, and let (B, χ) be
Appell–Humbert data (instance `hB`) with `Re B(x, x) > 0` for `x ≠ 0`. The Poincaré series
`K(x, y) = ∑_{l ∈ L} exp(B(x, y − x + l) − B(l, y) − B(l, l)/2)/χ(l)` has these properties: (a) it
converges for all `x, y`; (b) it is jointly continuous in `(x, y)`; (c) for each `x` it is a theta
function of type (B, χ) in `y`; (d) the diagonal `x ↦ K(x, x)` has mean `(χ 0)⁻¹` over `V ⧸ L`; and
(e) it does not vanish at some point `(w, w)`. 

### `IsAppellHumbert.linearPart_symm`

 The form `B (I • u) v + I * B u v`, which is `2 I` times the part of `B` that is complex-linear
in the first variable, is symmetric. 

### `IsAppellHumbert.exists_mem_thetaSpace_ne_zero`

 For Appell–Humbert data (B, χ) (instance `hB`) whose Riemann form is positive (instance `hp`)
there is a nonzero theta function of type (B, χ). 

### `IsAppellHumbert.finite_dualLattice_quotient`

 For Appell–Humbert data (B, χ) with positive Riemann form (instances `hB`, `hp`), `L` has finite
index in its dual lattice, as both are full lattices. 

### `linearPartForm`

 The form `T u v = (i / 2) (C (i u) v + i C u v)`, which is minus the part of `C` that is
complex-linear in the first variable. 

### `continuous_uncurry_thetaShift`

 The twisted translates of a theta function `f`, `(u, z) ↦ thetaShift B u f z`, form a continuous
function of two variables. 

### `pairingIntegrand`

 For tuples `s`, `t` of theta functions, the function
`x ↦ exp (T b b / 2) * ∑ i, conj ((thetaShift x (s i)) 0) * (thetaShift x (t i)) b` on `V`, with `T`
the form `linearPartForm B`. Its mean over `V ⧸ L` pairs `s` with `t`. 

### `isContPeriodic_pairingIntegrand`

 The integrand `pairingIntegrand s t b` is continuous and periodic under `L`. 

### `pairingMean`

 The mean over `V ⧸ L` of `pairingIntegrand s t b`; at `b = 0` it is the inner product of the
tuples `s` and `t` of theta functions. 

### `differentiable_pairingMean`

 The mean `pairingMean s t` is holomorphic in `b`. 

### `pairingMean_neg`

 Swapping the tuples and the sign of `b` conjugates `pairingMean`, the mean over `V ⧸ L` of
`pairingIntegrand s t b`. 

### `pairingMean_eq_zero_of_eq_zero`

 Liouville's theorem applied to the mean `m = pairingMean`: if `m s t 0 = 0`, then `m t s`
vanishes everywhere. 

### `IsAppellHumbert.exists_injective_to_dual_quotient`

 Upper bound for the dimension. Let `(B, χ)` be Appell–Humbert data with positive Riemann form
for a full-rank lattice `L` in `V`. If there are `n` linearly independent theta functions `s i` of
type `(B, χ)`, then there is an injective `ℂ`-linear map from `n`-tuples of such theta functions to
the functions on the dual lattice `B.dualLattice` modulo `L`. 

### `IsAppellHumbert.finite_thetaSpace`

 For Appell–Humbert data with positive Riemann form, the space of theta functions has finite
dimension. 

### `IsAppellHumbert.finrank_thetaSpace_pos`

 For Appell–Humbert data with positive Riemann form, the space of theta functions has positive
dimension. 

### `IsAppellHumbert.linearIndependent_thetaShiftEnd_out`

 For Appell–Humbert data with positive Riemann form, the twisted translations
`New.IsAppellHumbert.thetaShiftEnd` by representatives of the dual lattice modulo `L` are linearly
independent endomorphisms of the space of theta functions. 

### `IsAppellHumbert.relIndex_dualLattice_eq_finrank_end`

 For Appell–Humbert data with positive Riemann form, the index of `L` in its dual lattice is the
dimension of the endomorphism algebra of the space of theta functions. 

### `IsAppellHumbert.span_range_thetaShiftEnd_eq_top`

 For Appell–Humbert data with positive Riemann form, the twisted translations by the dual lattice
span the endomorphisms of the space of theta functions.

Known result: irreducibility of the action of the theta group. 

### `IsAppellHumbert.finrank_thetaSpace_sq`

 For Appell–Humbert data with positive Riemann form, the square of the dimension of the space of
theta functions is the index of `L` in its dual lattice.

Known result: Frobenius' dimension formula. 

### `IsAppellHumbert.finrank_sq_eq_relIndex`

 Let `(B, χ)` be Appell–Humbert data for `L` with positive Riemann form. (a) The translations by
the dual lattice span the endomorphisms of the space of theta functions. (b) The square of its
dimension is the index of `L` in the dual lattice. (c) The dimension is positive.

Known result: Frobenius' dimension formula and irreducibility of the action of the theta group. 

### `IsAppellHumbert.thetaSpace_le_of_thetaShift_mem`

 Irreducibility: for Appell–Humbert data with positive Riemann form, a complex space of
functions that contains all twisted translates, by the dual lattice, of one non-zero theta
function contains every theta function. 

### `IsAppellHumbert.schur_lemma`

 Schur's lemma: for Appell–Humbert data (L, B, χ) with positive Riemann form, a linear
endomorphism of the theta functions of type (B, χ) that commutes with the twisted
translations `New.RealComplexForm.thetaShift` by the dual lattice is a scalar. 

### `IsAppellHumbert.exists_nsmul_mem_of_mem_dualLattice`

 For Appell–Humbert data with positive Riemann form, some positive integer `N` multiplies every
vector of the dual lattice into `L`. 


## Multiples of a positive type have no base point

Throughout, `L` is a full lattice in a finite-dimensional complex space `V`, and `(B, χ)` are
Appell–Humbert data for `L` (`New.IsAppellHumbert`) whose Riemann form is positive
(`New.IsPosRiemann`).


### `New.ThetaTori.eq_zero_of_differentiable_of_mul_eq_zero`

 Let f and g be entire functions on a finite-dimensional complex space with f·g = 0. If f is not
identically zero, then g is identically zero. 

### `New.IsAppellHumbert.exists_mem_thetaSpace_nsmul_apply_ne_zero`

 For Appell–Humbert data (B, χ) with positive Riemann form and n ≥ 2, the theta functions of
type (nB, χⁿ) have no common zero. 


## The canonical multiplier and normalised translations

* `New.ThetaTori.canonicalMultiplier`: for a linear map `b`, the multiplier `exp (π i E(b x, x))`,
  defined on all of `V`. By `New.ThetaTori.isAppellHumbert_canonicalMultiplier` it satisfies the
  Appell–Humbert conditions `New.IsAppellHumbert` if b + b* = 1 (adjoint for `E`), the real part of
  `B` is symmetric and `E(b L, L)` is integral.
* `New.ThetaTori.normalizedShift`: the twisted translation `New.RealComplexForm.thetaShift B x`
  divided by this multiplier. The theta functions are the entire functions fixed by it along `L`
  (`New.ThetaTori.mem_thetaSpace_iff_normalizedShift`). If b + b* = 1 and `B` admits some
  Appell–Humbert multiplier, it obeys the Heisenberg law
  `New.IsAppellHumbert.normalizedShift_normalizedShift`.


### `ThetaTori.canonicalMultiplier`

 The canonical multiplier x ↦ exp(πi E(bx, x)) attached to a complex-linear endomorphism b of
V, where E is the Riemann form of B. 

### `ThetaTori.normalizedShift`

 Normalised translation: the twisted translation by x, divided by the canonical multiplier
exp(πi E(bx, x)). 

### `thetaShift_prod`

 For the sum of the pull-backs of forms B_i along linear maps A_i, the twisted translate by u of
the product of the f_i∘A_i is the product of the pulled-back translates of f_i by A_i u. 

### `ThetaTori.mem_thetaSpace_iff_normalizedShift`

 The theta functions for L, B and the canonical multiplier of b are the entire functions
fixed by the normalised translations by the elements of L. 

### `ThetaTori.isAppellHumbert_canonicalMultiplier`

 Let E be the Riemann form of `B`. If b + b* = 1 for E, that is E(bu, w) + E(u, bw) = E(u, w)
(hypothesis `adj`), the real part of `B` is symmetric and E(b L, L) is integral, then `B` and the
canonical multiplier are Appell–Humbert data for L. 

### `IsAppellHumbert.normalizedShift_normalizedShift`

 Heisenberg law: if (L, B, χ) are Appell–Humbert data and E(bu, w) + E(u, bw) = E(u, w), the
normalised translation by y followed by that by x is exp(2πi E(bx, y)) times that by x + y. 
