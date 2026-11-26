---
{
  "module": "proof/statements/ClauseBoundStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/ClauseBoundStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/ClauseBoundStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The statements: ONE machine counts the satisfying assignments of a k-CNF with m clauses, for all k and m, within a bound in k·m

Definitions only (no theorem, no proof). Imports `CountKSatStatement.lean` (and through it
`KSatStatement.lean`, `ThreeSatStatement.lean`) and Mathlib.

## How to read it

Read first, in those files: formulas `Sat3.CNF n` (lists of clauses, a clause is a list of literals
on x₀ … xₙ₋₁), `SatK.IsKCNF k φ` (at most k literals per clause, no clause written twice), the code
`SatK.enc k φ` (1ⁿ 0, then k slots per clause), the count `SatK.numSat φ` (over all 2ⁿ assignments)
and its word `SatK.binary n N` (n + 1 bits, lowest first).
* In `CountInRate r` the machine M and the constant C are chosen before k, n, m and φ: ONE machine
  for all widths and all sizes, and the constant in the exponent does not depend on k.
* The width k is part of the input, in unary. It is a declared width: at least the length of the
  longest clause; every clause takes k slots even if it is shorter.
* The number m of clauses is `φ.length`. The time bound depends on k and m only.
* `AllOccur φ`: every one of the n variables occurs. So n ≤ k·m, and the satisfying assignments
  counted are those of the variables that occur.
* The shift m + 2 in `rPow` makes the bounds meaningful for every m ≥ 1; for m ≥ 2 it changes r(m)
  by a bounded factor, which C absorbs.
* A larger exponent α in `rPow α` is the stronger statement.

## What the statements do not say

* Nothing for k = 0 (the code does not determine the formula) and nothing for m = 0 (the bound would
  be C, but the machine has to read 1ᵏ 0).
* Nothing about inputs that are not codes of such formulas: the hypotheses are a promise on the
  input.
* C is not explicit, and the bounds are asymptotic: they are below exhaustive counting (2ⁿ with n ≤
  k·m) only where C·k·m·r(m) < n.
* Nothing in terms of n: a formula with many clauses per variable gains nothing here. Bounds in n
  need sparsification or another network at the top.
* The machine model is Mathlib's multi-stack machine `Turing.FinTM2`; one step runs a statement as
  far as its next `goto` or `halt`, as explained in `ThreeSatStatement.lean`.
* No «decides» form is stated; a machine that counts also decides. 

### `AllOccur`

 Every one of the variables x₀ … xₙ₋₁ occurs in some clause. Then the assignments of x₀ … xₙ₋₁
are the assignments of the variables that occur. 

### `enc`

 The input: 1ᵏ 0, then the code of φ as an instance of k-SAT (1ⁿ 0, then k slots per clause). The
number m of clauses is not written; it is the number of clause records. 

### `CountsTM`

 `M`, started on the code of (k, φ), where k ≥ 1, φ is a k-CNF with m ≥ 1 clauses and all its
variables occur, halts within `t k m` steps with the number of satisfying
assignments, in n + 1 bits, as output. One machine for all k, n and m. 

### `bound`

 The time bound C·2^{C·k·m·r(m)}, rounded down. The same C is the factor in front and the factor
in the exponent; it does not depend on k. 

### `CountInRate`

 «#k-SAT with m clauses is in time 2^{O(k·m·r(m))}, the O not depending on k»: one machine,
finite alphabets, one constant C. 

### `rPow`

 r(m) = 1/(log₂(m+2))^α. 

### `TargetSqrt`

 2^{O(km/√(log m))}. 
