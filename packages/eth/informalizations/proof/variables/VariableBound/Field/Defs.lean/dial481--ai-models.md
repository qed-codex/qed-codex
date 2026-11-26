---
{
  "module": "proof/variables/VariableBound/Field/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 13 (Family of checks) for the family that a program lists: «In time polynomial in m one can list sets Γ_u, u ∈ Ω»

The field GF(2^s) as a program. An element is a word of s bits, lowest bit first: the word (b_0, …,
b_(s−1)) stands for the residue of b_0 + b_1·X + … + b_(s−1)·X^(s−1) modulo a polynomial
X^s + g of degree s over the field with two elements; the word g of s bits holds the coefficients of
the lower part. Addition is `xorW`; multiplication by X is `mulX` (shift, and add g if the top
bit was set); multiplication is `mulW` (Horner's rule over the bits of the second factor); powers
are `powW` (repeated multiplication).

«An irreducible polynomial of degree s is found by search»: `modW s` is the first word g of s bits,
in the order of the numbers 0, 1, …, 2^s − 1, that passes the test `irrW`: every word other than 0
has an inverse under `mulW g`. The text does not say which test it means; for s ≥ 1 this one holds
exactly if X^s + g is irreducible (`irrW_iff`, proof/variables/VariableBound/Field/Search.lean).

`famD m a` is the list of the sets Γ_u, u ∈ Ω, for m clauses and v = 2^a, with s = ⌈log₂(16m)⌉; the
clauses are the numbers E < m, ι(E) = E, and ϑ_E is the word of s bits of the number E.
The two statements at the end are what the rest of Appendix D uses. 

 ## The arithmetic 

### `xorW`

 The sum of two elements: bit by bit. 

### `zeroW`

 The word 0, as long as g. 

### `oneW`

 The word 1, as long as g (if g is not empty). 

### `mulX`

 X·w modulo X^s + g: shift by one place, and add g if the top bit of w was set. 

### `mulW`

 x·y modulo X^s + g, by Horner's rule over the bits of y: x·(b + X·y') = b·x + X·(x·y'). 

### `powW`

 u^e modulo X^s + g, by repeated multiplication; u^0 = 1 also for u = 0. 

### `ipW`

 The inner product modulo 2 of two words. 

 ## The search for the polynomial 

### `wordsL`

 All words of s bits, in the order of the numbers 0, 1, …, 2^s − 1 that they write, lowest bit
first. 

### `irrW`

 The test: every word of s bits other than 0 has an inverse modulo X^s + g, where s is the length
of g. 

### `modW`

 The lower part of the first polynomial of degree s that passes the test. 

 ## The family 

### `gamW`

 Γ_u for u = (u₁, u₂, u₃, u₄), as the increasing list of the numbers E < m of its clauses: the
first a − 1 bits of u₁·ϑ_E + u₂ are 0, and ⟨u₃^E, u₄⟩ = 1. 

### `sD`

 The number s of bits: 16m ≤ 2^s < 32m for m ≥ 1. 

### `famD`

 The list of the sets Γ_u, u ∈ Ω, for m clauses and v = 2^a: all u ∈ 𝔽⁴ in lexicographic order,
those with |Γ_u| > 16m/v left out. 

### `setD`

 A list of numbers of clauses as a set of clauses. 

 ## The statements 

### `StFamD`

 Lemma 13 (Family of checks) for the listed family: for v = 2^a with 2 ≤ v ≤ m, the list is not
empty and has fewer than (32m)⁴ members, every member is an increasing list of numbers below m, and
the members, indexed by their places in the list, have (a), (b), (c). 

### `StCertFamD`

 Lemma 13 (Family of checks), second sentence: the list is computed in polynomial time, jointly
in m and a, both given in unary. 
