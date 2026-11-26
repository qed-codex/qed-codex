---
{
  "module": "proof/networks/Eight/SecCrossing_PolyDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_PolyDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_PolyDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 2 from the eight-square identity: the pieces and their factorizations as programs (definitions only)

Strings are lists of bits here. `aMul` computes A_i as in the proof of Lemma 2(a), «multiplying them
out one at a time»: a polynomial in T is kept as the list of its coefficients, lowest first
(`mulStep`, `mulUpTo`, `mulOut`). `fTop` and `fBot` are the two functions of the factorizations in
the proof of Lemma 2(b), for both directions (tr = false: row-wise, tr = true: column-wise):
«Let θ = (Q, θ'), where a set Q ⊆ [t] is written as a string of t bits, and put f(·,θ) = f_Q(·,θ')
and f'(·,θ) = f'_Q(·,θ') if |Q| = i, and f(·,θ) = f'(·,θ) = 0 otherwise»; θ' lists the indices of
the blocks in their order, 3 bits for a block whose
function (R row-wise, C column-wise) factors through 3 bits, 6 bits for a block of the other kind,
which we call wide; «whenever one of these numbers exceeds 2λ, use the factorization through 2λ bits
instead».
Both directions have the same formulas, because C(x,y,u,v) = R(x,u,y,v). `eightF` is the family of
pieces in the form in which the networks of a grid (proof/rates/ClauseBound/Alg) take it. 

### `blkAt`

 The three bits of a list from position j on; positions beyond the end count as 0. 

### `blkL`

 The block number s (from 0) of a string, zeros appended. 

 ### A_i 

### `FourL`

 Four strings x, y, u, v. 

### `rAt`

 R at the block number s. 

### `cAt`

 C at the block number s. 

### `tL`

 The number of blocks, from the length of the first string. 

### `mulStep`

 One multiplication: the list of coefficients of (r + T·c)·P, where l is the list of coefficients
of P, lowest first. The entry number j is r·l_j + c·l_{j−1}; the list (0 :: l) has l_{j−1} at the
place j. 

### `mulUpTo`

 The list of coefficients after the factors number 0, …, n − 1 have been multiplied in, one at a
time, starting from the polynomial 1. 

### `mulOut`

 The paper's program for A_0, …, A_t: all t factors R(x_s,y_s,u_s,v_s) + T·C(x_s,y_s,u_s,v_s)
multiplied out one at a time. 

### `aMul`

 A_i as a function of (i, x, y, u, v), by the paper's program: the entry number i of the list,
and 0 beyond its end, that is, for i > t. 

 ### The two factorizations 

### `longCap`

 The number of bits of the factorization with θ = (Q, θ'): 4t + 3i row-wise, 7t − 3i column-wise
(for i ≤ t, as everywhere it is used; the subtraction is that of natural numbers). 

### `useLong`

 Is the factorization with θ = (Q, θ') used, that is, does its number of bits not exceed 2λ? 

### `wide`

 Is the block number s wide? Row-wise the blocks in Q (they take C) are wide, column-wise the
others (they take R). 

### `off`

 Where the index of the block number s begins in θ': 3 bits for each earlier block and 3 more for
each earlier wide block. 

### `topAt`

 The factor of the block number s in the first function: ψ_k(a_s, b_s), k the index of the block;
for a wide block, [(a_s, b_s) = index of the block]. 

### `botAt`

 The factor of the block number s in the second function: ψ_k(b_s, a_s); for a wide block with
the index (k, k'), R(k, a_s, k', b_s), which is C(k, k', a_s, b_s). 

### `fTop`

 The first function of a factorization of A_i, as a function of (direction, i, first string a,
second string b, θ); (a, b) is (x, y) row-wise and (x, u) column-wise; λ is the length of a. 

### `fBot`

 The second function of a factorization of A_i; (a, b) is (u, v) row-wise and (y, v) column-wise.
In the factorization through 2λ bits, θ = (θ₁, θ₂) stands for the two strings of the first function. 

### `eightF`

 The functions A_0, …, A_t with their two factorizations, in the form in which the networks of a
grid take a family of pieces: t + 1 pieces, which add up to 2^t·[x = v][y = u]; the piece number i
factors through c_i^row bits
row-wise and c_i^col bits column-wise; no pad is needed; all values are at most 2^t in absolute
value; every number of bits is at most 2λ. The parameter h of a family of pieces is not used. 

 ### Interface statements (nothing is proved or assumed here) 

### `StAMul`

 `aMul` computes A_i. 

### `StFact`

 Lemma 2(b) for the functions `fTop` and `fBot`: they factorize A_i through c_i^row bits row-wise
and c_i^col bits column-wise, with values at most 2^t in absolute value. 

### `StPoly`

 The three programs are polynomial-time. 

### `StKeeps`

 All parts of the family are computed in polynomial time. 
