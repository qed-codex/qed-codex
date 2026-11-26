---
{
  "module": "proof/rates/ClauseBound/ParityChecks/CertLib.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/CertLib.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/CertLib.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # More closure lemmas for polynomial-time functions

Polynomial time (PolyT) for operations on numbers that the closure lemmas of
proof/machines/ToTuring/Lib and proof/rates/PaddedDescent/F/FuelCert.lean do not cover: the
remainder of an integer modulo a natural number, powers of an
integer with the exponent in unary, products over a range, binomial coefficients with the lower
number in unary, factorials, and the two logarithms to base 2. The parameters of the choice of the
checks are a structure, `Par`, which is never passed as data: a certificate is stated for a function
q of the context whose five components are given in unary (`QU q`). 

### `unary_congr`

 «Given in unary» passes to a function with the same values. 

### `unary_min_right`

 The smaller of any number and a number given in unary is given in unary. 

 ### Integers 

### `emod_natCast`

 The remainder of an integer modulo a natural number, by cases on the sign. 

### `modZ_polyT`

 The remainder of an integer modulo a natural number is polynomial-time. 

### `ediv_natCast`

 The quotient of an integer by a natural number, rounded down, by cases on the sign. 

### `divZ_polyT`

 The quotient of an integer by a natural number is polynomial-time. 

### `div_two_pow_polyT`

 The quotient of an integer by a power of 2 is polynomial-time, for the exponent in unary. 

### `mod_two_pow_polyT`

 The remainder of an integer modulo a power of 2 is polynomial-time, for the exponent in unary. 

### `powZ_polyT`

 A power of an integer is polynomial-time, for the exponent in unary. 

### `prod_range_polyT`

 A product of integers over i < n is polynomial-time, for n in unary; the factors are only needed
for indices given in unary. 

### `map_range_polyT`

 A list of values at i < n is polynomial-time, for n in unary; the values are only needed for
indices given in unary. 

 ### Natural numbers 

### `factorial_polyT`

 k! is polynomial-time, for k in unary. 

### `descFactorial_polyT`

 n(n − 1)⋯(n − k + 1) is polynomial-time, for k in unary. 

### `choose_polyT`

 The binomial coefficient C(n, k) is polynomial-time, for k in unary. 

### `clog_two_eq`

 ⌈log₂ n⌉ is the number of binary digits of n − 1. 

### `clog_polyT`

 ⌈log₂ n⌉ is polynomial-time. 

### `clog_unary`

 ⌈log₂ n⌉ is given in unary, for any polynomial-time n. 

### `log_polyT`

 ⌊log₂ n⌋ is polynomial-time. 

### `log_unary`

 ⌊log₂ n⌋ is given in unary if n is. 

### `sup_range_unary_min`

 The largest of f 0, …, f (n − 1) is given in unary if n and the numbers are; the numbers are
only needed for indices given in unary. 

### `foldl_range_min`

 A fold over 0, …, n − 1 only needs its step for indices at most n. 

 ### The parameters of the choice of the checks 

### `QU`

 The five parameters are given in unary. 

### `QU.comp`

 The property passes to a polynomial-time change of the context. 
