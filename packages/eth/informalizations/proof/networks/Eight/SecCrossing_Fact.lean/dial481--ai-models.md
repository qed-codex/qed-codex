---
{
  "module": "proof/networks/Eight/SecCrossing_Fact.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_Fact.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_Fact.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 2(b): the programs `fTop` and `fBot` factorize the pieces

The proof of Lemma 2(b) in the section «Two crossing equalities as a sum of ⌈λ/3⌉ + 1 cheaper
functions», from «Now A_i is the sum, over the sets Q ⊆ [t] with |Q| = i» to «use the factorization
through 2λ bits instead».
`stFact_of` proves the statement `StFact` from three statements that other files prove: `StChunk`
(the factorization of the product that belongs to one Q), `StAMul` (the program `aMul` computes A_i)
and
`StSubsets` (A_i is the sum over the sets Q). `lemPieces_b_row` and `lemPieces_b_col` put `StFact`
in the form of the fields `b_row` and `b_col` of `Eight.LemPieces`.

* Factorization with θ = (Q, θ') (`Fact.long_sum`): a word of t + m bits is cut into Q and θ'; the
  words Q with another number of ones than i contribute 0; for the others θ' has the length that
  `StChunk` asks for; the words of t bits
  with i ones are the sets Q ⊆ {0, …, t − 1} with i elements (`Fact.sum_words_count`).
* Factorization through 2λ bits (`Fact.short_sum`): only θ = (the two strings of the first function)
  contributes.
* Bounds: `fTop` has values in {−1, 0, 1}; so has `fBot` with θ = (Q, θ'); otherwise `fBot` is a
  value of `aMul`, and |aMul| ≤ C(t, i) ≤ 2^t on all inputs, also on strings of unequal lengths
  (`abs_aMul_le`, proof/networks/Eight/SecCrossing_MulOut.lean). 

### `StSubsets`

 «Now A_i is the sum, over the sets Q ⊆ [t] with |Q| = i, of the product that takes C at the
blocks s ∈ Q and R at the others.» A statement only; it is proved in `SecCrossing_PiecesAC.lean`. 

### `sum_ofFn`

 A sum over θ ∈ {0,1}^c, written as functions, is the sum over the words of c bits. 

### `card_filter_range`

 The number of s < t with p s, as the size of a set and as a count in the list 0, …, t − 1. 

### `eq_map_getD`

 A word is the list of its bits. 

### `getD_map_range`

 The bit number s < t of the word f 0, …, f (t − 1) is f s. 

### `countP_getD`

 The number of positions s < t with the bit 1 in a word of t bits is its number of ones. 

### `countP_not_getD`

 The number of positions s < t with the bit 0 in a word of t bits is t minus its number of ones. 

### `sum_words_count`

 «A set Q ⊆ [t] is written as a string of t bits»: a sum over the words of t bits with i ones is
the sum over the subsets of {0, …, t − 1} with i elements. The summand is a product over the
positions s of a function of s and of «s ∈ Q». 

### `getD_ofFn`

 The bits of a string as a list, zeros appended, are those of the string as a function. 

### `blkL_ofFn`

 The blocks of a string as a list are those of the string as a function. 

### `abs_prodL_le`

 A product of numbers in {−1, 0, 1} is at most 1 in absolute value. 

### `abs_topAt_le`

 The factor of a block in the first function is in {−1, 0, 1}. 

### `abs_botAt_le`

 The factor of a block in the second function is in {−1, 0, 1}. 

### `tOf_mono`

 ⌈λ/3⌉ does not decrease with λ. 

### `abs_fTop_le`

 All values of the first function are in {−1, 0, 1}, for every input. 

### `abs_fBot_le`

 All values of the second function are at most 2^t in absolute value, t = ⌈λ/3⌉, λ the length of
its first string; θ is any list. 

### `fTop_long`

 The first function at θ = (Q, θ'): f(·,θ) = f_Q(·,θ') if |Q| = i, and 0 otherwise. 

### `fBot_long`

 The second function at θ = (Q, θ'): f'(·,θ) = f'_Q(·,θ') if |Q| = i, and 0 otherwise. 

### `lenW_eq`

 For |Q| = i the index θ' has 3(t − i) + 6i = 3t + 3i bits row-wise and 6(t − i) + 3i = 3t + 3(t
− i) bits column-wise. 

### `long_sum`

 «This is a row-wise factorization of A_i through t + 3(t − i) + 6i = 4t + 3i bits. Column-wise
the roles of R and C are exchanged, which gives t + 6(t − i) + 3i = 7t − 3i bits.» Both directions
at once, for strings a, b (arguments of the first function) and a', b' (of the second): the sum over
all θ is the sum over the sets S with i elements of the product over the blocks, as in `StChunk`;
row-wise the blocks in S are wide, column-wise the others. 

### `short_sum`

 «Every function F : {0,1}^c × X' → ℤ factors through c bits, by F(z,z') = Σ_θ [z = θ]·F(θ,z')». 

### `fact_sum`

 The two factorizations of A_i, over words; tr = false: row-wise, c_i^row = min{2λ, 4t + 3i}
bits; tr = true: column-wise, c_i^col = min{2λ, 7t − 3i} bits. «Whenever one of these numbers
exceeds 2λ, use the factorization through 2λ bits instead.» 

### `stFact_of`

 **Lemma 2(b)** for the programs `fTop` and `fBot`, from the factorization for one Q, the
correctness of `aMul` and the sum over the sets Q. The three hypotheses are filled in by `stFact`
(proof/networks/Eight/SecCrossing_LemPieces.lean). The bounds hold for every list θ, of any length,
which is more than the paper asks. 

### `lemPieces_b_row`

 Lemma 2(b), row-wise half of its first sentence, with the bound of its second sentence: «As a
function of (x,y) and (u,v), A_i factors through c_i^row bits», with values at most 2^t in absolute
value. The field `b_row` of `Eight.LemPieces`. 

### `lemPieces_b_col`

 Lemma 2(b), column-wise half of its first sentence, with the bound of its second sentence: «as a
function of (x,u) and (y,v), through c_i^col bits», with values at most 2^t in absolute value. The
field `b_col` of `Eight.LemPieces`. 
