---
{
  "module": "proof/rates/ClauseBound/ParityChecks/CertNum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/CertNum.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/CertNum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Polynomial-time certificates for one decision of the choice of the checks

One decision compares two integers, the numerators of the truncated potential in the two states that
are tried (`Par.num`, proof/rates/ClauseBound/ParityChecks/RunDefs.lean). All their exponents are
numbers given in unary: the parameters m, nb, r, i₀, β, lengths of lists, and the number e of
clauses decided. So the integers have polynomially many bits and are computed in polynomial time.
The parameters
are never data: every certificate is stated for a function q of the context with `QU q`. For each
numerator there is an auxiliary lemma with generic functions in place of the components of q.
The result is `decide1_polyT`. 

 ### The number of checks that contain a clause 

### `colOf_polyT`

 The number of checks among Ls and cur that contain the clause x is polynomial-time. 

### `colOf_unary`

 It is given in unary: it is at most the number of the checks. 

 ### The four numerators 

### `numP_polyT`

 A·nb^{i₀} + Σ_{i ≤ i₀} (−2)^i·nb^{i₀−i}·B_i is polynomial-time. 

### `numI_polyT`

 I·nb + (number of undecided pairs) is polynomial-time. 

### `numR_polyT`

 The numerator of the term that sums over the checks (`Par.numR`), with 2 to the size of each
check, is polynomial-time, for e in unary. 

### `numC_polyT`

 The numerator of the term that sums over the clauses (`Par.numC`), with 2 to the number of
checks that contain each clause, is polynomial-time. 

 ### The numerator of the truncated potential 

### `num_polyT`

 The numerator of the truncated potential is polynomial-time, for e in unary. 

 ### Residues, the numerator with A and the B_i from the given functions `orcA` and `orcB`, one decision 

### `bal_polyT`

 The representative of a modulo 2^β in [−2^{β−1}, 2^{β−1}) is polynomial-time, for β in unary. 

### `numO_polyT`

 The numerator with A and the B_i taken as the representatives modulo 2^β (`bal`) of the values
of the given functions `orcA` and `orcB` is polynomial-time, for e in unary. 

### `decide1_polyT`

 One decision is polynomial-time, for e in unary. 
