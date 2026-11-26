---
{
  "module": "proof/sparsification/SparsificationLemma/Mach/LemSparsification.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Mach/LemSparsification.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Mach/LemSparsification.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 4 in its form for deciding

`lemSparsification_of` derives `LemSparsification` from `SparsABCD`, the theorem on sparsification
with parts (a) to (d), at width k = 3. Given a real ε > 0 take a rational q with 0 < q < min(ε, 1)
and s = `precE C 3 q`.
* The time: the input has s + 5 bits and the code of φ, which has at most 25(n+2)^4 bits because no
  clause is written twice. So C·(length of the input + 8)^C is at most c·(n+1)^c with
  c = C·(s+412)^C + 4C, and 2^(qn) ≤ 2^(εn).
* The number of clauses: a variable occurs in at most (3C/q)^48 clauses of an output, and every
  clause has a variable, so M(ε) = ⌈(3C/q)^48⌉ + 1 will do (`stLenOfOcc`).
* Satisfiability: an assignment that satisfies φ satisfies one of the outputs, and an assignment
  that does not satisfies none.
`lemSparsification` takes only the statement `Prints` on the machine as a hypothesis. 

### `length_encIn_le`

 The length of the input plus 8 is at most (s+412)·(n+1)^4, for a 3-CNF on n variables in which
no clause is written twice. 

### `poly_le`

 C·(length of the input + 8)^C ≤ c·(n+1)^c with c = C·(s+412)^C + 4C. 

### `lemSparsification_of`

 Lemma 4 from the theorem on sparsification, parts (a) to (d). 

### `lemSparsification`

 Lemma 4 from a machine that prints the outputs. 
