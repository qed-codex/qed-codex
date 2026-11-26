---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Host/NeedPolynomial.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/NeedPolynomial.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/NeedPolynomial.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The host of Theorem 17: the need stays polynomial

The need of a procedure says what it asks of the limits of a run: the largest number that it forms,
the cells that it uses, and the depth of its calls.  If the need of the solver is polynomially
bounded (`PolyNeedN`), then so is the need of the host (`hostNeed_poly`: `PolyNeed` of `hostNeed`).
The need of the host is an explicit expression in `n`, `U`, `D`, `g` and a few quantities derived
from them.  Each of these is at most a polynomial in `(n + 1)(U + 1)` (`PolyBounded`), and such
bounds are closed under sums, products and powers.

* The quantities: `⌊√D⌋ ≤ D`, the number of binary digits of `U` is at most `U`,
  `2^{len + 1} ≤ 4(U + 1)`, `2^⌈log₂ n⌉ ≤ 2(n + 1)`, `⌊n²/√D⌋ ≤ n²`, `⌈s/g⌉ ≤ s + g` with
  `s = ⌊√D⌋`.
* The numbers (`polyBounded_hostWord`), the cells (`polyBounded_chooseCells`,
  `polyBounded_hostLayout`), and each of the three parts of the need of the solver on the instances
  of the host (`polyBounded_sup`).  The depth adds `O(⌈log₂ n⌉)` calls (`polyBounded_clog`).


 ## The quantities 

### `queryCapNat_le_sq`

 `⌊n²/√D⌋ ≤ n²`. 

### `two_pow_bitLen_le`

 `2^{len + 1} ≤ 4(U + 1)` for the number `len` of binary digits of `U`. 

### `two_pow_clog_le`

 `2^⌈log₂ n⌉ ≤ 2(n + 1)`. 

### `polyBounded_bitLen`

 The number of binary digits of `U` is at most `U`. 

### `polyBounded_two_pow_bitLen`

 `2^{len + 1} ≤ 4(U + 1)` is polynomially bounded. 

### `polyBounded_two_pow_clog`

 The size of the matrices of Strassen's recursion. 

### `polyBounded_clog`

 The depth of Strassen's recursion. 

### `polyBounded_pow_clog`

 `(2^c)^⌈log₂ n⌉ = (2^⌈log₂ n⌉)^c`. 

### `polyBounded_queryCapNat`

 The number of query pairs of an instance. 

 ## The numbers, the cells, and the solver 

### `polyBounded_hostWord`

 The numbers that the host forms. 

### `polyBounded_hostLayout`

 The cells of the arrays of the host. 

### `polyBounded_chooseCells`

 The cells for the choice of the prime.  The scratch space of Strassen's recursion is at most
the size `4^K s` of a matrix, with `K = ⌈log₂ n⌉` and `s = ⌊√D⌋`. 

### `polyBounded_sup`

 A polynomially bounded function of the parameters `n`, `D`, `w` of an instance, at its largest
over the instances of the host, which have at most `⌊n²/√D⌋` query pairs. 

### `hostNeed_poly`

 **The need of the host stays polynomial**, if the parameters, the numbers that the parameter
procedures form, and the need of the solver are polynomially bounded. 
