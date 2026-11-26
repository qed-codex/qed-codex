---
{
  "module": "src/Lib/GaloisRep/Main/ThetaLift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/ThetaLift.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/ThetaLift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Theta lift of an algebraic form to a larger definite unitary group and its Hecke polynomials

This file constructs the theta lift from the definite unitary group of rank n to that of rank n + s.
The lift is used to separate the Galois representation of a form from those of its lifts. The file
also records how the monic and the reciprocal normalisations of the Hecke polynomial are related.

## Main definitions and results

* `New.exists_theta_lift_heckePoly`: the theta lift of a nonzero form is a nonzero form whose Hecke
  polynomial at split places is the twisted old one times a string of linear factors.

Notions from other files:
* `New.AutChar.HasWeight`: `b.HasWeight c 1` says that `b u = ∏_v u_v ^ c v` whenever `u` has
  integral finite part.
* `New.WeilData`: Weil data on a stably unramified E. They consist of ȷ in E with ȷ = −ȷ̄, Im τȷ > 0
  for every τ in the CM type and (1 − ȷ⁻¹)/2 integral; a finite idele α for which the completed
  integers Ô are self-dual under (z, u) ↦ ψ_f(ȷαᾱzu); and a splitting character υ equal to −1 at
  uniformisers of the places w with w = w̄.

## Relation to the literature

Known result: Theta lift to larger rank, the step that reduces even rank to odd rank. Here a
non-zero theta lift in the convergent range from definite U(n) to U(n+s), with s > n, replaces
endoscopic transfer. It keeps spherical places, and its Hecke polynomials are twisted and gain the
string of a character of U(1). Source: Blasius, Rogawski, Motives for Hilbert modular forms, Invent.
Math. 114 (1993) and Shin, Ann. of Math. 173 (2011) for the idea (endoscopic transfer to odd rank);
Harris, Soudry, Taylor, Invent. Math. 112 (1993) for theta lifts with a varying character.



## The monic Hecke polynomial and the reciprocal one

The two normalisations of the Hecke polynomial at a place `w` agree: `New.heckePoly` (monic of
degree `n` if `t 0 = 1`) at `x ≠ 0` is `x ^ n` times the reciprocal one, `New.heckePolyEval`, at
`x⁻¹`.


### `New.eval_heckePoly`

 At `x ≠ 0` the monic Hecke polynomial at the place `w`, with coefficients built from `t`, is
`x ^ n` times the reciprocal one, `heckePolyEval`, at `x⁻¹`, where `n = card n`:
`∑ (-1)^j q^(j choose 2) t j x^(n - j) = x^n ∑ (-x⁻¹)^j q^(j choose 2) t j`, with `q` the norm of
`w` and `j` running from `0` to `n`. 


## Theta lift to a larger definite group and Hecke polynomials

`New.stdSpace E n` is the sum of `n` norm forms. `New.AlgForm n κ e` and `New.Space.forms` are
smooth algebraic forms of a given weight. `New.maxCompactAt n w` is the maximal compact subgroup at
`w` and `w̄`. `New.HasHeckePolyAt f w hw P` says that `f` is a spherical Hecke eigenform at the
split place `w` with Hecke polynomial `P`. For a character `b` of `U(1)`, `hb.toAlgebraic k j`
(`New.AutChar.HasWeight.toAlgebraic`) is the algebraic Hecke character
`b (x / x̄) υ ^ (-k) |x| ^ (j - k / 2)`. `New.heckeCoeff ψ ∅ w` is `ψ` at a uniformiser.


### `mem_inf_stabilizer_of_integral`

 Let `x` be an integral matrix with `xᴴ * x = 0`, let `B` be a finite set of places with
`stdLevel E n ⊓ trivialOn n B ≤ H`, and let `N ≠ 0` have its principal level inside `H`. Let
`z = N⁻¹ • idem B'`, with `B'` the closure of `B` under conjugation, and let `b` be a character
of `U(1)` of weight `c`. Then an integral `g` such that `z * D i j` is integral for
`D = g⁻¹ - 1` lies in `H` and fixes, under the Weil representation, the vacuum translated by
`z • x`. 

### `mem_Ô_of_mul_add_sum_mem_Ô`

 Let `z` be a finite adele, let `g` be integral at every place where `z` is integral (the places
off `{w | 1 < v (z w)}`), and let `D = g⁻¹ - 1`. If for an integral matrix `u` every entry
`z * D p j + ∑ k, u p k * D k j` is integral, then every entry of `D` is integral: at a place `w`,
a largest entry of a column of `D` that is not integral would force `z` to be integral at `w`. 

### `weilMatrixCoeff_finHeisenbergOp_eq_zero`

 Let the row `ρ p` of `x` be the unit vector at `p`, let `g` be integral at every place where
the finite adele `z` is integral, and let `D = g⁻¹ - 1`. Unless `g` is integral with every
entry `z * D i j` integral, the Weil matrix coefficient at `g` of `F`, the vacuum translated by
`z • x`, is `0`. 

### `exists_isSharp_of_two_mul_card_le`

 Let `H` be an open subgroup of `Gf E n`, let `b` be a character of `U(1)` of weight `c` with
trivial tame part, and let `2 * card n ≤ card m`. Then there exist a set `S` of finite places
avoiding every `w` with `maxCompactAt n w ≤ H`, a Schwartz datum `F` on
`Hom(stdSpace E n, stdSpace E m)`, a level `J ≤ H` and a number `mass` such that `F` is sharp for
`b`, `S` and `J` (`IsSharp`). Sharpness means: `⟨F, F⟩ ≠ 0`; `F` lies in the finite part and is a
vacuum off `S` (fixed by the projection `projOn` on vacua at every set of places disjoint from `S`)
and clean (true here as all signs of the standard spaces are `1`); at finite points `g` integral off
`S`, the coefficient `⟨F, ω(g) F⟩` of the Weil action `ω` (built from `b`) is `⟨F, F⟩` on
`J ⊓ stdLevel E n` and zero elsewhere, where `stdLevel E n` is the stabiliser `K₀` of `Ô ^ n`; and
`mass` is the quotient of `⟨F, F⟩` by the index `[K₀ : J ⊓ K₀]`. 

### `scaleRoots_heckePoly_eq`

 Let `t` and `t'` give the Hecke polynomials at `w` of ranks `card n` and `card n + s`, the
second of degree `card n + s`. Suppose that for all `X` their reciprocal polynomials `heckePolyEval`
satisfy `R' X = R (μ * X) * qPochhammer w.q s (ν * X)` (`qPochhammer w.q s Y` is a product over
`l < s` of factors linear in `q_w ^ l * Y`), where `R` is built from `t` and `R'` from `t'`, and let
`μ * a = 1` and `θ l = q_w ^ l * ν * a` for `l < s`. Then the second Hecke polynomial, with its
roots multiplied by `a`, is the first one times `∏ l < s, (X - θ l)`. 

### `paramsCorrespond_of_isHCParam`

 Let `c ≤ e`, `card n < s`, and let `κ'` agree with `κ` below `card n`, be `e - c` at `card n`
and `0` above. Then in rank `card n` the weight `(κ, e)` is also `(κ', c + κ' (card n))`, so a
parameter `l` of `(κ, e)` in rank `card n` and a parameter `l'` of `(κ', 0)` in rank `card n + s`
correspond. 

### `frobValue_div_mul_heckeCoeff_eq_one`

 The scalars of the theta lift at the place `w` cancel: `q_w ^ s * frobValue 1 n w`, divided by
`b.frobValue (Fin (card n + s)) w` (scalars at `w` built from powers of `√q_w` and values at a
uniformiser) and multiplied by the value at `w` of the algebraic Hecke character
`hb.toAlgebraic s s`, is `1`. Here `b` is a character of `U(1)` of weight `c`. 

### `heckeCoeff_toAlgebraic_eq`

 For `l < s`, the value at `w` of the algebraic Hecke character `hb.toAlgebraic (card n + s)
(s - l)` is `q_w ^ l * frobValue 1 n w` times that of `hb.toAlgebraic s s`. Here `b` is a character
of `U(1)` of weight `c`. 

### `toAlgForm_formLift_ne_zero`

 Rallis' inner product formula makes the theta lift injective on forms of level `J`. Let `b` be
a character of `U(1)` of weight `c`, `v` an edge from type `l` to type `l'` (`IsEdge`), `Ψ` sharp
for `b` and a level `J` (`IsSharp`), and `2 * card n < card n + s`. If the algebraic form of `y`
is not zero and is fixed by `J`, then the algebraic form of the lift of `y` by `v ⊗ Ψ` is not
zero. 

### `exists_hasHeckePolyAt_scaleRoots_eq`

 Let `F ≠ 0` be a form of rank `card n + s` that is spherical at the split place `w`
(`star w ≠ w`), and on which the Hecke polynomial operator at `X` acts by `qPochhammer w.q s
(frobValue 1 n w * X) * heckePolyEval n w t (r * X)`, with `qPochhammer w.q s Y` a product over
`l < s` of factors linear in `q_w ^ l * Y`, where `r = q_w ^ s * frobValue 1 n w / b.frobValue (Fin
(card n + s)) w` and `b` is a character of `U(1)` of weight `c`. Then `F` has a Hecke polynomial `Q`
at `w` (`HasHeckePolyAt`), and `Q` with its roots multiplied by the value at `w` of
`hb.toAlgebraic s s` is `heckePoly w.q (card n) t` times `∏ l < s, (X - θ l)`, where `θ l` is the
value at `w` of `hb.toAlgebraic (card n + s) (s - l)`. 

### `exists_theta_lift_heckePoly`

 Theta lift by `s > n` steps. Let `f ≠ 0` be a form of rank `n ≥ 1` and weight `(κ, e)`, and let
`b` be a character of `U(1)` of weight `c ≤ e` with trivial tame part (`b u = ∏ u_v^{c v}` for `u`
with integral finite part). Let `κ' v h` be `κ v h` for `h < n`, `e v - c v` for `h = n` and `0` for
`h > n`. There is a form `F` of rank `n + s` and weight `(κ', 0)` such that (a) `F ≠ 0`; (b) `F` is
fixed by `K_w` wherever `f` is; (c) at such a split `w`, if `f` has Hecke polynomial `P`, then `F`
has a Hecke polynomial `Q`, and `Q` with its roots multiplied by the value of `hb.toAlgebraic s s`
at `w` equals `P * ∏ l < s, (X - θ l)`, where `θ l` is the value of `hb.toAlgebraic (n + s) (s - l)`
at `w`. Here `hb.toAlgebraic` gives the algebraic Hecke characters `b(x/x̄) υ(x)^{−k} |x|^{j−k/2}`,
evaluated at a uniformiser at `w` (`heckeCoeff`). 
