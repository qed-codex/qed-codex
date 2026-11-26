---
{
  "module": "src/Lib/Weil/CompactLift/DefiniteThetaLift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/CompactLift/DefiniteThetaLift.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/CompactLift/DefiniteThetaLift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Theta lifts between definite unitary groups and algebraic lifts by jets

This file studies the theta correspondence from the definite space `I_n` to `I_n'` (`New.stdSpace`),
for a weight that goes up from rank `n` to the larger rank `n'` (`New.IsLiftWeight`). There are two
lifts between these groups. The theta lift is an integral of a theta kernel over `[U(n)]`, and the
algebraic lift is a class sum with the matrix of jets `New.thetaKernel`.

## Main definitions and results

* `New.IsHCParam.paramsCorrespond_iff`: the parameter `l` of the weight in rank `n` corresponds to
  `l'` (`New.ParamsCorrespond`) exactly when `l'` is the parameter of the weight `(κ, ea)` in rank
  `n'`, with the same columns `κ`.
* `New.exists_lift_ofAlgForm_eq_smul`: the analytic theta lift `New.Space.lift` with the joint
  harmonic `New.jointHarmonic` as real datum is a constant (possibly zero), divided by the index of
  the level, times the lift `New.Kernel.lift` of algebraic forms by `New.thetaKernel`.
* `New.isThetaLift_thetaKernel`: the lifts of the kernels of jets are theta lifts in the sense of
  `New.Space.IsThetaLift`.

Notions from other files:
* `New.IsLiftWeight`: `n < n'`, no column of `κ` has height strictly between the two ranks, and the
  exponent in rank `n` is `eb` plus the number `κ w (card n)` of columns of height `n`.
* `New.thetaKernel`: the kernel whose matrix at a finite datum is made of the Taylor coefficients
  (jets) of its theta series, paired with Schur polynomials.
* `New.IsHCParam`: `l` lists twice the Harish-Chandra parameter of the weight `(κ, e)`, in some
  order: at each place `w` the numbers `l w i` are distinct, and each of them is
  `hcParameter κ e (card n) w p` for some position `p < card n`.
* `New.stdSpace`: the definite space `I_n`, the sum of `n` norms with its standard lattice.

## Relation to the literature

Known result: Theta lift for a definite unitary pair as a class sum on algebraic modular forms. The
pair is U(n)×U(n′) over a CM field with `New.WeilData`, n < n′, and the kernel is the matrix of
Taylor coefficients of the theta function against Schur polynomials. The constant is left
unspecified. Source: B. Gross, Algebraic modular forms, Israel J. Math. 113 (1999); Kashiwara–Vergne
1978; R. Howe, Transcending classical invariant theory, JAMS 2 (1989).


 ## The harmonic theta lift of definite spaces as a multiple of the algebraic lift 

### `New.IsHCParam.image_comp_eq`

 The image of `l w` under a map `f`, for `l` twice the Harish-Chandra parameter of `(κ, ec)`
(`New.IsHCParam`), is the image of the first `card n` values of `hcParameter`. 

### `New.IsHCParam.paramsCorrespond_iff`

 Theta correspondence of definite spaces of ranks `n < n'`. Let `E` be a number field, let
`κ τ h` be the number of columns of height `h` at the infinite place `τ`, and let the weight
`(κ, ec)` go up from rank `n` to rank `n'` along `eb` (`New.IsLiftWeight`): `card n < card n'`, no
column has height strictly between `card n` and `card n'`, and `ec τ = eb τ + κ τ (card n)`. Let `l`
be the parameter of `(κ, ec)`, that is, twice its Harish-Chandra parameter in some order; then `l`
and `l'` correspond (`New.ParamsCorrespond`: the block rule `New.IsBlockRule` (for `n ≤ n'`, among
its conditions: the entries `l' w - 2 ea w + card n` are those of `l w - 2 eb w + card n'` plus
`doubledBlock (card n' - card n)`) holds at every infinite place, for the signs `1` and characters
of U(1) of weights `ea`, `eb`) exactly when `l'` is the parameter of `(κ, ea)`. 

### `New.exists_smul_schurCoeffPoly_eq_jointHarmonic`

 The joint harmonic is a multiple of the Fock polynomial of two highest vectors. Let `E` be a CM
field with Weil data, let the weight `(κ, ec)` of rank `n` go up to rank `n'` along `eb`, and let
`l`, `l'` be parameters of `(κ, ec)` and `(κ, ea)`. Then `jointHarmonic ea eb l l' 1 1` is a
multiple of `schurCoeffPoly` at the highest vectors of `l` and of `l'`, the latter paired by the
Gram matrix `weylGramOver` of the weight. `jointHarmonic ea eb l l' 1 1` is the product over the
infinite places `w` of the chosen polynomials `jointHarmonicAt`, each in the variables of `w` and,
by `isJointHarmonic_jointHarmonicAt`, a joint highest vector for the match of `l' w` with `-l w`.
Here a parameter is twice the Harish-Chandra parameter, and `schurCoeffPoly A ξ` is the polynomial
`z ↦ Aᵀ S_κ(z) ξ` for the Schur matrix `S_κ`. 

### `New.exists_lift_ofAlgForm_eq_smul`

 The harmonic theta lift is a multiple of the algebraic lift. Let the weight `(κ, ec)` of rank
`n` go up to rank `n'` along `eb`, let `l`, `l'` be the parameters (twice the Harish-Chandra
parameters) of `(κ, ec)` and `(κ, ea)`, and let `c ≠ 0` be the scale of the jets, the Taylor
coefficients of theta series. There is a number `β` (possibly zero) with the following property for
all characters `a`, `b` of weights `ea`, `eb` (with characters `ψ`, `ψ'` of the residue fields at
the finite places, as in `HasWeight`), every level `K`, every finite datum `f` and every algebraic
form `φ`. The theta lift of the function `F_φ = ofAlgForm l 1 φ` with datum (joint harmonic) ⊗ `f`
is `β / [K₀ : K ∩ K₀]` times `F_φ'`. Here `K₀ = stdLevel E n`, and `φ'` is the lift of `φ` at `f` by
the kernel `New.thetaKernel hκ c ha hb K`, for the measure that gives `K` volume `1`. 

 ## The algebraic lift by jets as a theta lift 

### `integral_theta_mul_algFormCoeff_add`

 The theta integral over `[U(n)]` (for `quotMeasure`) against the coefficient of an algebraic
form `φ` at a linear form is additive in the linear form. Here `θ` is the theta functional,
`pairWeil` the Weil action of the pair twisted by `a`, `b`, and `v` any test function. 

### `isThetaLift_thetaKernel`

 Let `(κ, e)` go up from rank `n > 0` to rank `n' > 0` along `eb`, let `a o n` and `a o n'` be
characters at the ranks `n` and `n'` of weights `ea` and `eb` (with residue-field characters `ψ o`,
`ψ' o` at the finite places), let `c ≠ 0` and let `K` be a level. Then the lifts of the kernels of
jets `New.thetaKernel` at the scale `c` compute theta lifts (`New.Space.IsThetaLift`): for every
polynomial `P` and linear form `t` there is one linear form `t'` such that, for every index `o`,
finite datum `Φ` and form `φ`, the coefficient at `t'` of the lift of `φ` is the theta integral,
with datum `P ⊗ Φ`, of the coefficient of `φ` at `t`.

The existence of `t'` for every `P` and `t` is the consequence for theta lifts of Howe's (GL n', GL
n)-duality on polynomials on matrices; the multiplicity formula of the duality is not stated
here. 
