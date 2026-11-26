---
{
  "module": "proof/consequences/FreeCode/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Definition 6 and Corollary 5 with the code that does not depend on k: which machines stand behind the sentences (definitions and statements only)

`KSatFreeCodeStatement.lean` has the paper's sentences; a sentence «there is a machine …» reads the
same whichever way it was proved. Here each is tied to a named machine cut into steps:
* a reader `dec` of the code (`Reads dec`: the code of φ on n variables is read as (n in unary, φ
  with numbers as variables)); `StReader`: there is a polynomial-time one. `Reads` fixes the reader
  on every code, so nothing depends on which one is taken;
* «Trying all assignments»: `bruteCore` behind the reader (`StBrute`);
* «Theorem 2 gives s_3 = 0»: `SplitSat.core3 ℓ τ`, the machine of Theorem 2 in its decision form
  without its own reader, behind the reader (`StTiedThree`);
* «s_3 = 0 implies s_k = 0 …; the reduction (sparsify, then split every long clause …)»:
  `SplitSat.reduceCore` on `core3`, behind the reader (`StTied`).
This file has no theorem. 

### `Reads`

 `dec` reads the code: the code of φ on n variables as (n in unary, φ with numbers as variables).
Nothing is asked on other words. 

### `StReader`

 There is a polynomial-time reader. 

### `StLength`

 The length of the code of a k-CNF on n variables is polynomial in n, for fixed k. 

### `DecidesFree`

 The machine Ms, cut into steps, decides w-SAT on the code that does not depend on k, with the
exponent δ and the constant c: on the code of a w-CNF φ on n variables it ends within c·2^{δn}
steps, on states of size at most c·(n+2)^c, with the bit «φ is satisfiable». 

### `StBehindReader`

 **For EVERY reader and EVERY procedure D** that decides w-SAT on (N in unary, formula) with the
exponent δ (`SplitSat.DecidesW`): D behind the reader decides w-SAT on the code, within the same
number of steps. 

### `bruteCore`

 Exhaustive search on (n in unary, formula): for each number y < 2^n test in one step whether the
assignment that gives xᵢ the i-th binary digit of y satisfies the formula; add up; answer
«satisfiable» if the sum is positive. 

### `StBrute`

 **«Trying all assignments».** There are a polynomial-time reader and ONE Turing machine with
finite alphabets such that (1) `bruteCore` behind the reader ITSELF has polynomial-time steps and
decides k-SAT, for every k, within c·2^n steps, on states of size at most c·(n+2)^c, with c
depending on k; (2) the Turing machine simulates it with polynomial overhead; (3) the Turing machine
decides k-SAT, for every k, within c·(n+2)^c·2^n steps, with c depending on k. 

### `StTiedThree`

 **«Theorem 2 gives s_3 = 0».** For every δ > 0 there are a polynomial-time reader, ℓ, τ such
that (1) the machine of Theorem 2 in its decision form (`core3 ℓ τ`) behind the reader ITSELF has
polynomial-time steps and decides 3-SAT with the exponent δ; (2) a Turing machine with finite
alphabets simulates it with polynomial overhead; (3) that Turing machine decides 3-SAT within
⌊c·2^{δn}⌋ steps. 

### `StTied`

 **Corollary 5, tied to the reduction.** For every k ≥ 3 and δ > 0 there are a polynomial-time
reader, τ, ℓ₃, τ₃ such that (1) the reduction (sparsify at width k with the parameter τ, split every
long clause, ask the machine of Theorem 2 in its decision form) behind the reader ITSELF has
polynomial-time steps and decides k-SAT with the exponent δ; (2) a Turing machine with finite
alphabets simulates it with polynomial overhead;
(3) that Turing machine decides k-SAT within ⌊c·2^{δn}⌋ steps. (Without (1), a machine that runs the
    reduction and another machine for k-SAT side by side would meet (2) and (3), and only the
    correctness of the reduction would be needed, not its running time.) 
