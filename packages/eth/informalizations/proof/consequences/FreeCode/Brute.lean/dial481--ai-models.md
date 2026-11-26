---
{
  "module": "proof/consequences/FreeCode/Brute.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Brute.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Brute.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # After Definition 6: «Trying all assignments gives s_k ≤ 1»

`bruteCore` (proof/consequences/FreeCode/Defs.lean) tests, for each number y < 2^n, in one step,
whether the assignment that gives xᵢ the i-th binary digit of y satisfies the formula, and adds up.
* `bruteCore_runs`: on (n in unary, φ with numbers as variables) it ends after 2·2^n steps with the
  bit that says whether φ is satisfiable, on states of size at most twice the size of the input plus
  3n + 12.
* `bruteCore_polyTimeSteps`: its steps are polynomial time.
* `stBrute` (= `FreeCode.StBrute`): exhaustive search behind the reader `readFree` decides k-SAT for
  every k, and one Turing machine with finite alphabets simulates it with polynomial overhead. 

### `satAt_toN`

 The assignment that gives xᵢ the i-th binary digit of y passes the test of exhaustive search
exactly if it makes a literal of every clause true. 

### `sum_satAt_pos`

 The number of y < 2^n that pass the test is positive exactly if φ is satisfiable. 

### `bruteCore_runs`

 **Exhaustive search**: on (n in unary, φ with numbers as variables) `bruteCore` ends after 2·2^n
steps with the bit that says whether φ is satisfiable, on states of size at most 2·(size of the
input) + 3n + 12. 

### `bruteCore_polyTimeSteps`

 The steps of exhaustive search are polynomial time. 

### `brute_behind`

 Exhaustive search behind any reader of the code: on the code of a k-CNF on n variables it ends
after 2·2^n steps with the bit that says whether φ is satisfiable, on states of size at most
c·(n+2)^c, where c = 2·(2^k·(2k+1) + 3) + k + 16. 

### `stBrute`

 **«Trying all assignments».** The reader `readFree` and one Turing machine with finite
alphabets: exhaustive search behind the reader has polynomial-time steps and decides k-SAT, for
every k, within c·2^n steps on states of size at most c·(n+2)^c; the Turing machine simulates it
with polynomial overhead, and decides k-SAT, for every k, within c·(n+2)^c·2^n steps. This is the
statement `FreeCode.StBrute`. 
