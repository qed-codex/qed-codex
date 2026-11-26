---
{
  "module": "proof/networks/Eight/SecCrossing_Cert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_Cert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_Cert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 2 from the eight-square identity: «computable in time poly(λ)»

Lemma 2 of the paper says of the functions A_i, and of the functions of both factorizations, that
they are «computable in time poly(λ)». This file gives certificates (`Groundwork.PolyT`,
proof/machines/ToTuring/PolyT.lean: some fragment of a
multi-stack machine of Mathlib turns the word of the input into the word of the output within a
number of steps polynomial in the length of the input) for the three programs `aMul`, `fTop`, `fBot`
of proof/networks/Eight/SecCrossing_PolyDefs.lean, and for all parts of the family `eightF`
(`stKeeps`).
That the programs compute A_i and factorize it is proved in other files.

How: ψ, R and C are functions of finitely many blocks of three bits, hence tables. The strings are
lists of bits, so λ and t = ⌈λ/3⌉ are given in unary. The program for A_i («multiplying them out one
at a time») is a loop of t rounds whose state is a list of at most t + 1 integers of at most t + 1
bits
(`len_mulUpTo_le`, proof/networks/Eight/SecCrossing_MulOut.lean). The index i comes in binary and
may be huge; it is only used to look an entry of a list up. The number s of a block is the length of
a loop in `off`; it is replaced by min(s, t) inside the product over s < t.
The auxiliary statements are in the namespace `Eight.SecCrossing_Cert`. 

 ### Closure lemmas 

### `prodL_polyT'`

 A product over s < n is polynomial-time, for n in unary; the factors need to be polynomial-time
only at indices cut off at n (min(s, n)). 

### `tOf_unary`

 t = ⌈λ/3⌉ is given in unary, for λ in unary. 

 ### Blocks 

### `blkAt_polyT`

 Three bits of a list from a position on. 

### `blkL_polyT`

 The block number s of a string. 

### `psi_polyT`

 ψ_k(p, q) is a table. 

### `Rb_polyT`

 R is a table. 

### `Cb_polyT`

 C is a table. 

 ### A_i 

### `rAt_polyT`

 R at the block number s. 

### `cAt_polyT`

 C at the block number s. 

### `tL_unary`

 The number of blocks is given in unary. 

### `mulStep_polyT`

 One multiplication is polynomial-time. 

### `mulOut_polyT`

 «multiplying them out one at a time takes time poly(λ)»: the paper's program is polynomial-time.
It is a loop of t rounds; a loop is polynomial-time if each round is and the words of all the states
that occur have polynomial length
(Groundwork.PolyT.foldl), which is len_mulUpTo_le. 

### `aMul_polyT`

 The entry number i of the list, i in binary, is polynomial-time. 

 ### The two factorizations 

### `longCap_polyT`

 The number of bits of the factorization with θ = (Q, θ') is polynomial-time. 

### `useLong_polyT`

 The choice between the two factorizations is polynomial-time, for λ in unary. 

### `wide_polyT`

 The test `wide` (whether the block number s takes the factor through 6 bits rather than ψ,
through 3 bits) is polynomial-time. 

### `off_polyT`

 The place where the index of the block number s begins is polynomial-time, for s in unary. 

### `topAt_polyT`

 The factor of the block number s in the first function is polynomial-time, for s in unary. 

### `botAt_polyT`

 The factor of the block number s in the second function is polynomial-time, for s in unary. 

### `Arg`

 The arguments of `fTop` and `fBot`: direction, i, two strings, θ. 

### `lam_unary`

 λ, the length of the first string, is given in unary. 

### `t_unary`

 t is given in unary. 

### `card_polyT`

 The test «|Q| = i» is polynomial-time. 

### `topLong_polyT`

 The first function of the factorization with θ = (Q, θ') is polynomial-time. 

### `botLong_polyT`

 The second function of the factorization with θ = (Q, θ') is polynomial-time. 

### `fTop_polyT`

 The first function of a factorization is polynomial-time. 

### `fBot_polyT`

 The second function of a factorization is polynomial-time. 

 ### The numbers of bits 

### `crow_unary`

 c_i^row = min{2λ, 4t + 3i} is given in unary, for λ in unary; i may be in binary. 

### `ccol_unary`

 c_i^col = min{2λ, 7t − 3i} is given in unary, for λ in unary; i may be in binary. 

### `stPoly`

 **Lemma 2 of the paper**, «computable in time poly(λ)», said there of A_i in (a) and of the
functions of both factorizations in (b): the program `aMul` is one polynomial-time function of (i in
binary, the four strings as
lists of bits), and `fTop` and `fBot` are polynomial-time functions of (direction, i in binary, two
strings and θ as lists of bits). Same as in the paper, with «time poly(λ)» read as: polynomial in
the length of the input, on a
multi-stack machine of Mathlib; for i ≤ t and θ of at most 2λ bits that is polynomial in λ. 

### `stKeeps`

 All parts of the family `eightF` are computed in polynomial time: the number t + 1 of pieces,
the numbers of bits c_i^row and c_i^col and the bound t on the sizes in unary, the factor 2^t in
binary, and the two functions of
the factorizations. The paper has no sentence on the numbers; for the functions see Lemma 2 (b) of
the paper and `fTop_polyT`, `fBot_polyT` above. 
