---
{
  "module": "proof/variables/VariableBound/Field/Cert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Cert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Cert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 13 (Family of checks), the claim that the sets Γ_u, u ∈ Ω, are listed in time polynomial in m: the list is computed in polynomial time

One certificate (`PolyT`) for each program of proof/variables/VariableBound/Field/Defs.lean, jointly
in all its arguments as functions of a context x. No mathematics of fields is used, only lengths of
words:
the sum of two words is as long as the shorter one, X·w is at most as long as w, and a product is at
most as long as the word g of the polynomial.
In every certificate the arguments are polynomial-time functions of the context. A number that a
program counts up to must moreover be given in unary (`Unary`), and the docstring says so:
the exponent of a power, the number s of bits together with 2^s, the number m of clauses, and, in
the last theorem, a. 

 ### Lengths 

### `length_xorW`

 The sum of two words is as long as the shorter of them. 

### `length_mulX_le`

 X·w is at most as long as w. 

### `length_mulW_le`

 A product is at most as long as the word g. 

 ### The arithmetic 

### `xorW_polyT`

 The sum of two words is polynomial-time. 

### `zeroW_polyT`

 The word 0 of the length of g is polynomial-time. 

### `oneW_polyT`

 The word 1 of the length of g is polynomial-time. 

### `mulX_polyT`

 Multiplication by X is polynomial-time. 

### `ipW_polyT`

 The inner product of two words is polynomial-time. 

### `mulW_polyT`

 Multiplication is polynomial-time. 

### `powW_polyT`

 Powers are polynomial-time, if the exponent is given in unary. 

 ### The search for the polynomial 

### `wordsL_polyT`

 The list of all words of s bits is polynomial-time, if s and 2^s are given in unary. 

### `irrS`

 The test `irrW` with the number s of bits as an argument of its own. 

### `irrS_polyT`

 The test with the number s of bits as an argument is polynomial-time, if s and 2^s are given in
unary. 

### `length_of_mem_wordsL`

 Every word in the list of the words of s bits has s bits. 

### `modW_polyT`

 The search for the polynomial is polynomial-time, if s and 2^s are given in unary. 

 ### The family 

### `gamW_polyT`

 The set Γ_u is polynomial-time jointly in m, a, g and u, if m is given in unary. 

### `sD_unary`

 The number s of bits is given in unary, for any polynomial-time m. 

### `two_pow_sD_le`

 2^s ≤ 32m + 1 for the number s of bits. 

### `two_pow_sD_unary`

 2^s is given in unary for the number s of bits, if m is. 

### `stCertFamD`

 Lemma 13 (Family of checks), the claim that the sets Γ_u, u ∈ Ω, are listed in time polynomial
in m: the list is computed in polynomial time, jointly in m and a, both given in unary. 
