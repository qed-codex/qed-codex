---
{
  "module": "ThreeSumApsp/Util/Asymptotics/Scale.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/Scale.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/Scale.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Orders of growth of counts

The time and the need of a program are natural numbers, given by explicit expressions in the
parameters of the input.  Only their order of growth is needed.  This file has one calculus
that reads the order of growth off such an expression, so that no constant is ever written out.

A *scale* (`Scale α ι`) fixes the parameters `x : α` for which bounds are claimed (`dom`) and some
quantities that are at least 1 there: the *bases* `base i`, whose powers are counted, and one more,
`hidden`, whose powers are not.  `s.SoftO t e` says that the count `t` is at most a constant times a
power of `hidden` times the monomial `∏ i, base i ^ e i`.  Three examples:

* bases `n`, `√D`, `κ log n` and `hidden = 1`: `s.SoftO t ![2, 1, 1]` is `t = O(n² √D κ log n)`;
* one base `√n` and `hidden = log n`: `s.SoftO t ![3]` is `t = Õ(n^{3/2})`;
* no base and `hidden = n U`: `s.SoftO t ![]` says that `t` is polynomially bounded.

So `SoftO` is `O` up to powers of `hidden`: it is `O` itself if `hidden = 1`, and `Õ` if `hidden` is
a logarithm.  The bounds hold on the whole domain and not only from some point on.

The exponents follow the expression.  A constant has the exponents 0 (`SoftO.const`), a sum the
larger ones (`SoftO.add`), a product their sum (`SoftO.mul`), a power their multiple (`SoftO.pow`).
Exponents may be raised (`SoftO.mono`), and the count may be replaced by a smaller one
(`SoftO.of_le`, `SoftO.of_forall_le`).  If every base is at most `2 ^ hidden`, the binary logarithm
of a bounded count has the exponents 0 (`SoftO.log2`).

The tactic `growth [h₁, h₂, …]` applies these rules from the outside to the inside of the
expression.  The facts `hᵢ` bound the quantities at which the rules stop: parameters, and functions
whose bound is a lemma of its own.  A function that is to be followed into its definition is
unfolded first.

A bound leaves the calculus by `SoftO.exists_le`, or as a `Dominated` statement by
`SoftO.dominated`.


### `Scale`

 What upper bounds are measured in: quantities that are at least 1 on a domain. 

### `Scale.dom`

 The parameters for which bounds are claimed. 

### `Scale.hidden`

 The quantity whose powers are not counted. 

### `Scale.base`

 The quantities whose powers are counted. 

### `Scale.one_le_hidden`

 `hidden ≥ 1` on the domain. 

### `Scale.one_le_base`

 Every base is at least 1 on the domain. 

### `ofBases`

 The scale with the given bases in which nothing is hidden. 

### `mon`

 The monomial `∏ i, base i ^ e i`. 

### `SoftO`

 The count `t` is at most a constant times a power of `hidden` times the monomial with the
exponents `e`, on the domain of the scale. 

### `mon_le_mon`

 All bases are at least 1, so a monomial grows with its exponents. 

### `one_le_mon`

 A monomial is at least 1. 

### `pow_mul_mon_le`

 The bound grows with all exponents. 

 ### Entering and leaving 

### `of_le_hidden`

 A count that is at most `hidden`. 

### `of_dominated_base`

 A count that is at most a constant times a base. 

### `of_le_base`

 A count that is at most a base. 

### `of_dominated`

 A count that is at most a constant times a monomial. 

### `exists_le`

 The bound, written out. 

### `dominated`

 If `hidden = 1`, the bound is the monomial. 

 ### The rules 

### `mono`

 The exponents may be raised. 

### `of_le`

 A smaller count has the same bound. 

### `of_forall_le`

 A quantity `f` that is at most `g` everywhere has the bound of `g`, at any argument. 

### `of_forall_le₂`

 A quantity `f` with two arguments that is at most `g` everywhere has the bound of `g`. 

### `const`

 A constant has the exponents 0. 

### `add`

 A sum has the larger exponents. 

### `add_le`

 A sum of two counts with the same bound. 

### `mul`

 In a product the exponents add up. 

### `pow`

 The `k`-th power multiplies the exponents by `k`. 

### `max`

 A maximum has the larger exponents. 

### `sub`

 A difference has the exponents of its first term. 

### `div`

 A quotient has the exponents of its numerator. 

### `ceilDiv`

 A quotient that is rounded up has the larger exponents of numerator and denominator. 

### `log`

 A logarithm is at most the number. 

### `sqrt`

 A square root is at most the number. 

### `log2`

 The binary logarithm of a bounded count is at most a constant times `hidden`, if every base is
at most `2 ^ hidden`. 

### `growth_rules`

 Takes a goal `s.SoftO t ?e` apart, from the outside to the inside of the expression `t`, and
finds the exponents.  Constants, sums, products, powers with a constant exponent, maxima,
differences and quotients are treated by the rules of the calculus.  Every other quantity needs one
of the given facts.  A fact may be a rule with hypotheses, such as `SoftO.of_forall_le h` for an
inequality `h`, or `SoftO.log`.  The quantities for which no fact is given remain as goals. 

### `growth`

 Proves `s.SoftO t e`: finds the exponents of the expression `t` with `growth_rules` and the
given facts, and compares them with `e`.  If they are larger than `e`, the summands of `t` whose
exponents are larger remain as goals. 
