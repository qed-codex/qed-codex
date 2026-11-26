---
{
  "module": "ThreeSumApsp/Util/Asymptotics/Dominated.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/Dominated.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/Dominated.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Bounds up to a constant factor, in several parameters

The paper writes `f = O(g)` for functions of several parameters that are tied by side conditions,
such as `D ^ 18 ≤ n` for the parameters `n`, `D`, `w`. `Dominated dom f g` says this: there is a
constant `C ≥ 0` with `f x ≤ C * g x` for every tuple `x` of parameters that satisfies `dom x`. If
there is no side condition, `dom` is `fun _ => True`. The type `α` of the parameters is best a
structure with one named field for each of them, so that a bound reads
`Dominated (fun p => p.D ^ 18 ≤ p.n) (fun p => cost p) fun p => p.n ^ 2 / p.D`.

The lemmas of this file are the steps that the paper takes without comment: such bounds can be
chained (`Dominated.trans`), added (`Dominated.add`, `Dominated.add_add`), multiplied and divided
(`Dominated.mul`, `Dominated.mul_left`, `Dominated.const_mul`, `Dominated.pow`,
`Dominated.div_right`), joined by a case distinction (`Dominated.ite`), restricted to a smaller
domain (`Dominated.mono_dom`) and specialized (`Dominated.comp`). With them no proof has to name a
constant. A bound enters the calculus by `Dominated.of_le`, `Dominated.of_le_const_mul` or
`Dominated.of_exists_const`, and leaves it by `obtain ⟨C, hC, hle⟩` or `Dominated.exists_const_and`.
For functions of one natural number, `Dominated.of_eventually` takes a bound for all large `n`,
`Dominated.isBigO` gives Mathlib's `f =O[atTop] g`, and `isBigO_comp_add_one` substitutes a size
that need not tend to infinity.

In every closure lemma the bound comes first and the side conditions follow.

For nonnegative `f` and `g` the notion is Mathlib's `f =O[𝓟 {x | dom x}] g`, big-O along the
principal filter of the domain (`dominated_iff_isBigO_principal`). The one-sided form is taken
because a running time is bounded from above only.

## The notions of "bounded up to a constant" in this library

* `f =O[atTop] g` of Mathlib bounds `|f|` for large `n`. In this sense `IsBigOPow f a` is `O(n^a)`,
  `IsPowPolylog f a` is `O(n^a (log n)^e)` for some `e`, and `IsPowLittleO f a` is `n^{a+o(1)}`.
  The exponents of the theorems are stated with them.
* `UpperBigOPow`, `UpperPowPolylog` and `UpperPowLittleO` are the same three classes as bounds on
  `f` and not on `|f|`, for running times. A two-sided bound gives the one-sided one
  (`IsBigOPow.upperBigOPow`, `IsPowPolylog.upperPowPolylog`, `IsPowLittleO.upperPowLittleO`).
* `Dominated dom f g` bounds `f` on the whole domain, for several parameters. It comes from a bound
  for large `n` by `Dominated.of_eventually` and gives one by `Dominated.isBigO`.
* `Scale.SoftO t e` says that a count `t` with values in `ℕ` is `Dominated` by a monomial with the
  exponents `e`, up to powers of one more quantity; the tactic `growth` reads the exponents off an
  explicit expression. It gives a `Dominated` bound by `Scale.SoftO.dominated`. Its instance
  `SoftOSqrtPow` gives `IsPowPolylog` by `SoftOSqrtPow.isPowPolylog`.


### `Dominated`

 `f = O(g)` on the domain `dom`: there is a constant `C ≥ 0` with `f x ≤ C * g x` whenever
`dom x`. It is an upper bound on `f` and not on `|f|`. 

 ### Entering the calculus 

### `of_le_const_mul`

 A bound with an explicit nonnegative constant. 

### `of_le`

 A bound with constant one. 

### `refl`

 Every function is bounded by itself. 

### `of_exists_const`

 A bound with a constant of unknown sign, when `g` is nonnegative on the domain. 

### `_root_.ThreeSumApsp.dominated_iff_isBigO_principal`

 For nonnegative functions, `Dominated` is Mathlib's big-O along the principal filter of the
domain. 

### `const`

 A constant is `O(g)` when `g ≥ 1` on the domain. 

 ### Leaving the calculus 

### `exists_const_and`

 Two bounds, by nonnegative functions, hold with one constant. 

 ### Chaining, restricting, substituting 

### `trans`

 `f = O(g)` and `g = O(h)` give `f = O(h)`. 

### `mono_dom`

 A bound holds on every smaller domain. 

### `mono_left`

 The left side may be replaced by a smaller function. 

### `mono_right`

 The right side may be replaced by a larger function. 

### `congr`

 Both sides may be replaced by functions that agree with them on the domain. 

### `comp`

 Substituting the parameters: a bound in `x` gives a bound in `y` at `x = φ y`, on every domain
that `φ` maps into `dom`. 

 ### Sums and case distinctions 

### `add`

 `O(h) + O(h) = O(h)`. 

### `add_add`

 `O(g₁) + O(g₂) = O(g₁ + g₂)` for nonnegative `g₁`, `g₂`. 

### `ite`

 A case distinction: a bound on `f₁` where `p` holds and a bound on `f₂` where it does not, both
by the same nonnegative `g`. 

 ### Products and quotients 

### `const_mul`

 A nonnegative constant factor on the left side is absorbed. 

### `mul_const`

 A nonnegative constant factor on the left side is absorbed. 

### `const_mul_of_nonneg`

 A constant factor of any sign in front of a function that is nonnegative on the domain is
absorbed. 

### `mul_left`

 Both sides may be multiplied from the left by a function that is nonnegative on the domain. 

### `mul_right`

 Both sides may be multiplied from the right by a function that is nonnegative on the domain. 

### `div_right`

 Both sides may be divided by a function that is nonnegative on the domain. 

### `mul`

 `O(g₁) · O(g₂) = O(g₁ g₂)` for nonnegative `f₁`, `f₂`. 

### `pow`

 `O(g) ^ e = O(g ^ e)` for nonnegative `f`. 

 ### Functions of one natural number 

### `of_eventually`

 A bound that holds from some unknown point on. If `g` is positive from `n₀` on, the finitely
many values in between cost only a larger constant. 

### `of_eventually_add_one`

 A bound by a nonnegative `g` that holds from some unknown point on gives a bound by `g + 1`
everywhere. 

### `isBigO`

 A bound on `|f|` from some point on is Mathlib's `f =O[atTop] g`. 

### `isBigO_comp_add_one`

 If `G = O(g)` with `g ≥ 0`, then `G(size n) = O(g(size n) + 1)` for every `size : ℕ → ℕ`. The
sizes need not tend to infinity; the `+ 1` covers the finitely many sizes at which the bound does
not hold yet. 
