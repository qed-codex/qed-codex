---
{
  "module": "proof/consequences/FromPrinted/SplitSat.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/SplitSat.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/SplitSat.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, Corollary 5 along the reduction that its printed proof cites, on the machine `Printed.SAT`, which decides with Algorithm 1

The proof in the paper: «… Theorem 2 gives s_3 = 0, which is the negation of ETH; … By a theorem of
Impagliazzo, Paturi and Zane, which rests on their Sparsification Lemma, s_3 = 0 implies s_k = 0 for
every k ≥ 3; the reduction (sparsify, then split every long clause into clauses of 3 literals with
new variables) uses no randomness … Hence s_∞ = lim_k s_k = 0 ≠ 1.»
The reduction and what is proved of it for every procedure D for 3-SAT are those of
proof/consequences/SplitSat/ (`SplitSat.exists_parameters`, which rests on `SplitSat.stSparsifyK`,
`stReduce`, `stReduceCert`); they are used as they stand.
* `stSATsplit`, `stTiedTM`: the reduction run on the machine of Theorem 2 in its decision form, and
  a Turing machine of Mathlib that simulates it.
* `stTiedThreeTM`: «Theorem 2 gives s_3 = 0», tied to the machine of Theorem 2 in its decision form,
  from `Printed.stDecides`.
* `endFrom`, `eth_and_seth_false`: Corollary 5, first with the two tied statements as hypotheses,
  then applied to their proofs. s_3 = 0 is taken from `StTiedThreeTM`, and s_k = 0 for k > 3 from
  `StTiedTM`; then the general `SatK.sTM_eq_zero_of`.
What is different from the paper is listed at the head of proof/consequences/SplitSat/Defs.lean. 

### `stSATsplit`

 **k-SAT with the machine named**: for every k ≥ 3 and δ > 0 there are τ, ℓ₃, τ₃ such that
`SATsplit k τ ℓ₃ τ₃`, the reduction run on the machine of Theorem 2 in its decision form without its
reader, has polynomial-time steps and decides k-SAT with the exponent δ. This is the statement
`FromPrinted.SplitSat.StSATsplit`. 

### `stTiedTM`

 **Tied to the machine, on Mathlib's Turing machines**: for every k ≥ 3 and δ > 0 there are τ,
ℓ₃, τ₃ such that `SATsplit k τ ℓ₃ τ₃` itself has polynomial-time steps and decides k-SAT with the
exponent δ, a Turing machine M with finite alphabets simulates it with polynomial overhead, and M
decides k-SAT within ⌊c·2^{δn}⌋ steps. This is the statement `FromPrinted.SplitSat.StTiedTM`. In the
proof the named machine has the exponent δ/2. 

### `stTiedThreeTM`

 **«Theorem 2 gives s_3 = 0», tied to the machine of Theorem 2 in its decision form**: for every
δ > 0 there are ℓ, τ such that `Printed.SAT ℓ τ` itself has polynomial-time steps and decides 3-SAT
with the exponent δ, a Turing machine M with finite alphabets simulates it with polynomial overhead,
and M decides 3-SAT within ⌊c·2^{δn}⌋ steps. This is the statement
`FromPrinted.SplitSat.StTiedThreeTM`; ℓ and τ are those that `Printed.stDecides` gives for δ/2. 

### `endFrom`

 **Corollary 5 from the two tied statements**, which are hypotheses here: «s_k = 0 for every k ≥ 3.
Hence s_∞ = 0, and both ETH and SETH are false.» At k = 3 the Turing machine is that of
`StTiedThreeTM` («Theorem 2 gives s_3 = 0»), at k > 3 that of `StTiedTM` (the reduction); then the
general `SatK.sTM_eq_zero_of`. Nothing else is known of the machines. 

### `eth_and_seth_false`

 **Corollary 5**: «s_k = 0 for every k ≥ 3. Hence s_∞ = 0, and both ETH and SETH are false.» The
statement is `PaperSentences.CorEth` of PaperSentencesStatement.lean. It is `endFrom` applied to
`stTiedTM` (the cited reduction of k-SAT to 3-SAT) and `stTiedThreeTM` (Theorem 2). 
