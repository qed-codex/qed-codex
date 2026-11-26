---
{
  "module": "ThreeSumApsp/Lang/PolyBounded.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/PolyBounded.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/PolyBounded.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Polynomially bounded needs

The need of a program is given by explicit expressions in the size n of the input and the bound U on
its numbers.  `PolyBounded F` says that F(n, U) is at most a polynomial in (n + 1)(U + 1).  It is
the calculus `ThreeSumApsp.Scale.SoftO` on the scale `polyScale`, and the tactic `growth_poly`
proves it by following the expression.

Three such functions make a polynomially bounded need (`PolyBounded.polyNeed`), and the need of a
solver that a host calls has three such parts (`PolyNeed.word`, `PolyNeed.cells`, `PolyNeed.depth`).
So the need of a host is polynomially bounded if the need of its solver is; the tactic `poly_need`
proves this from the definition of the need of the host.


 ## Upper bounds that are polynomial in (n + 1)(U + 1) 

### `polyScale`

 The scale of the polynomial bounds in a size `n` and a bound `U`: powers of `(n + 1)(U + 1)` are
not counted, and there is no other quantity. 

### `PolyBounded`

 `F(n, U) ≤ K ((n + 1)(U + 1))^e` for some `K` and `e`. 

### `fst`

 The size `n` is polynomially bounded. 

### `snd`

 The bound `U` is polynomially bounded. 

### `of_le`

 A smaller function has the same bound. 

### `exists_nat_le`

 The bound with natural numbers. 

### `growth_poly`

 Proves `PolyBounded F` as `growth` does.  The given facts bound the quantities that occur, other
than `n` and `U`.  A logarithm or a square root is bounded by its argument. 

### `polyBound`

 A polynomial bound at polynomially bounded parameters. 

### `polyNeed`

 Three polynomially bounded functions make a polynomially bounded need. 

 ## The need of a solver that a host calls

A polynomially bounded need, at a size `A(n, U)` and a bound `B(n, U)` that are polynomially
bounded, has polynomially bounded parts. 

### `word`

 The numbers of the solver. 

### `cells`

 The cells of the solver. 

### `depth`

 The depth of the calls of the solver. 

### `poly_need`

 Proves `PolyNeed need`, where `need` is a record of three explicit expressions: takes the three
parts out of the record and treats each as `growth_poly` does.  The given facts bound the quantities
that occur, other than `n` and `U`; for a solver whose need `r` occurs, with `hr : PolyNeed r`, they
are `hr.word`, `hr.cells` and `hr.depth`. 
