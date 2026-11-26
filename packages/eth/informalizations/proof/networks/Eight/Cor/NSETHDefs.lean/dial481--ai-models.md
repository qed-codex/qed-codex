---
{
  "module": "proof/networks/Eight/Cor/NSETHDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Cor/NSETHDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Cor/NSETHDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, the sentence after Corollary 5: what «NSETH» means here (definitions only)

The paper: «The nondeterministic variant NSETH, which says that for every ε > 0 there is a k such
that the tautologies among the k-DNF formulas on n variables are not recognized in nondeterministic
time 2^{(1−ε)n}, is false as well».
This file has no theorem and imports only `KSatStatement.lean` (and through it
`ThreeSatStatement.lean` and Mathlib). Read those two first: literals, the code `SatK.enc k` of a
list of lists of literals, and time on Mathlib's machines are taken from them.

## How to read it
* A k-DNF on x₀ … xₙ₋₁ (`DNF n`, `IsKDNF k ψ`) is a list of terms, a term a list of at most k
  literals; the formula is the OR of its terms, a term the AND of its literals. No term is written
  twice, so that the length of the code is bounded in
  terms of n, as for instances of k-SAT. The type and the code are those of a k-CNF; only the
  reading differs.
* `Tautology ψ`: every assignment makes all literals of some term true. The empty term is always
  true; the formula without terms is never true.
* Mathlib has no nondeterministic Turing machine. Nondeterministic time is therefore put in VERIFIER
  form, with Mathlib's deterministic multi-stack machine `Turing.FinTM2`: the machine gets a word w,
  the witness (the guesses), together with the
  code x of the formula, as the one word `withWitness w x` = 1^{|w|} 0 w x.
  `RecognizesTautTM k M t`: for every n and every k-DNF ψ on n variables, ψ is a tautology IF AND
  ONLY IF for some w the machine M, started on `withWitness w (enc k ψ)`, halts within
  t(n) steps with the one bit 1 as its output. Nothing bounds the length of w, but within t(n) steps
  the machine sees at most a bounded multiple of t(n) bits of its input. Nothing is asked of runs
  that do not end with the output 1 in time: they
  may end with another output, run longer, or never halt.
* `TautInNTimeTM k δ`: some such machine with finite alphabets and some constant c, with t(n) =
  ⌊c·2^{δn}⌋: the tautologies among the k-DNF formulas are recognized in nondeterministic time
  O(2^{δn}). n is the number of variables.
* `NSETH_TM`: for every ε > 0 there is a k ≥ 1 such that NOT `TautInNTimeTM k (1 − ε)`.

## Where it differs from the paper and its source (Carmosino, Gao, Impagliazzo, Mihajlin, Paturi, Schneider, ITCS 2016)
* Verifier form in place of nondeterministic machines. The two agree up to a constant factor in the
  time: a nondeterministic machine that accepts within T steps becomes a verifier whose witness is
  the list of its at most T choices, and a verifier
  becomes a nondeterministic machine that guesses the bits of w when they are read. This is standard
  and is NOT proved here.
* «Time 2^{(1−ε)n}» is read as O(2^{(1−ε)n}), with a constant c that may depend on k and ε, as
  classes NTIME(·) are usually defined and as in `SatK.InTimeTM`.
* k ≥ 1 in place of «a k»: at k = 0 two different formulas have the same code (see
  `KSatStatement.lean`). NSETH with «some k ≥ 3» in place of «some k ≥ 1» is a stronger statement,
  so refuting this form refutes that one too.
* Time is counted on accepting runs only. For the time bounds here, which a machine can count down,
  this is the same as asking that all runs halt in time (standard; not proved here). 

### `DNF`

 A formula in disjunctive normal form on the variables x₀ … xₙ₋₁: the OR of a list of terms, a
term being the AND of a list of literals. The type is that of `Sat3.CNF n`; only the reading
differs. 

### `Tautology`

 Every assignment makes all literals of some term true. 

### `IsKDNF`

 A k-DNF: at most k literals per term, and no term written twice, so that the length of its code
is bounded in terms of n. 

### `withWitness`

 The input of a verifier: the length of the witness w in unary, a 0, the witness, then the word
x. 

### `RecognizesTautTM`

 `M` recognizes the tautologies among the k-DNF formulas in nondeterministic time `t n`, in
verifier form: ψ is a tautology exactly if for some witness w the machine, started on w and the code
of ψ, halts within `t n` steps with the output 1. 

### `TautInNTimeTM`

 The tautologies among the k-DNF formulas on n variables are recognized in nondeterministic time
O(2^{δn}): one machine, finite alphabets, one constant. 

### `NSETH_TM`

 NSETH on Turing machines: «for every ε > 0 there is a k such that the tautologies among the
k-DNF formulas on n variables are not recognized in nondeterministic time 2^{(1−ε)n}». 
