---
{
  "module": "proof/consequences/FreeCode/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sentences of KSatFreeCodeStatement.lean that rest on machines

After Definition 6: «Trying all assignments gives s_k ≤ 1, so s_∞ ≤ 1.» Corollary 5: «s_k = 0 for
every k ≥ 3. Hence s_∞ = 0, and both ETH and SETH are false.» After Definition 6, on randomized
algorithms: «and Corollary 5 holds under each of these conventions.»
* `codeReadable`: from the reader `FreeCode.readFree`, which returns n and the formula on the code
  followed by any bits.
* `bruteForce`, `atMostOne`: from `FreeCode.stBrute`. c·(n+2)^c·2^n is at most C·2^{(1+ε)n} for
  every ε > 0, so s_k ≤ 1 + ε.
* `FreeCode.allZeroFrom`, `allZero`: Corollary 5, first with the two tied statements as hypotheses,
  then applied to their proofs: s_3 = 0 from `FreeCode.StTiedThree` (Theorem 2), s_k = 0 for k > 3
  from `FreeCode.StTied` (the reduction).
* `allZeroRandomized`: from `randomnessHelps` and `allZero`.
The other sentences are in proof/consequences/FreeCode/Order.lean and Random.lean. 

### `toN_injective`

 A formula is determined by the same formula with numbers as variables. 

### `codeReadable`

 The code determines the number of variables and the formula, and it tells where it ends:
whatever bits follow it can be read off. 

### `bruteForce`

 «Trying all assignments»: one machine decides k-SAT for every k, within c·(n+2)^c·2^n steps,
with c depending on k. 

### `inTime_one_add`

 By exhaustive search, k-SAT is in time O(2^{(1+ε)n}) for every ε > 0. 

### `atMostOne`

 «Trying all assignments gives s_k ≤ 1, so s_∞ ≤ 1.» 

### `s_eq_zero_of`

 If k-SAT is in time O(2^{δn}) for every δ > 0, then s_k = 0. 

### `allZeroFrom`

 **Corollary 5 from the two tied statements**, which are hypotheses here: «s_k = 0 for every k ≥ 3.
Hence s_∞ = 0, and both ETH and SETH are false», for the numbers s_k defined with the code that does
not depend on k. At k = 3 the Turing machine is that of `StTiedThree` («Theorem 2 gives s_3 = 0»),
at k > 3 that of `StTied` (the reduction); then the general `SatFree.s_eq_zero_of`. Nothing else is
known of the machines. 

### `allZero`

 **Corollary 5**: «s_k = 0 for every k ≥ 3. Hence s_∞ = 0, and both ETH and SETH are false», for
the numbers s_k defined with the code that does not depend on k. It is `FreeCode.allZeroFrom`
applied to `FreeCode.stTiedThree` (Theorem 2) and `FreeCode.stTied` (the reduction). 

### `allZeroRandomized`

 «and Corollary 5 holds under each of these conventions»: with randomized algorithms with error
at most p, for every p ≥ 0, s_k = 0 for every k ≥ 3. 
