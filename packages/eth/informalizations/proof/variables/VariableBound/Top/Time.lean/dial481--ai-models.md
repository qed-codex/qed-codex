---
{
  "module": "proof/variables/VariableBound/Top/Time.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/Time.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/Time.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 6: the running time of the padding machine against the bound in n, with a constant that does not depend on the width k

`stTimeD : StTimeD`, from `StArithD`, `StPlanLeD` and `StDecM`: for the exponent function `eD` of
the algorithm for the bound in n, the number q·(|x| + 2^(eD x) + 1)^q of steps of a padding machine
is at
most D·2^(D·k²·n·r(n)), for a constant D that depends on q and not on k. It follows
proof/sparsification/UniformInK/Top/Time.lean; the proof is the same, without the parameter a. Write
X = k²·n·r(n).
* For the code x of (k, φ), with φ a k-CNF on n ≥ 1 variables, |x| + 1 ≤ (n+2)^(5k)
  (`UniformInK.Time.length_enc_succ_le`). Because r(n) ≥ 1/(c₁·(log₂(n+2))^c₁), log₂(n+2) =
  O(n·r(n)), so log₂(|x| + 1) = O(k·n·r(n)) = O(X).
* The exponent is at most n. If n is below a constant, then n = O(n·r(n)) = O(X). Otherwise
  `StArithD` gives one of two cases: the exponent is at most A·k²·n·e(l)·(s+1) = O(X),
  where l is the level picked for n and s its precision; or ⌊log₂ n⌋ < B·k², and then n = O(X). The
  small n and this second case take the place of the other cases of Step 6 of the paper (n < K₀^17,
  or k larger than (log n)^(1/4)), in which the algorithm tries all assignments. 

### `stTimeD`

 Step 6: the number of steps of a padding machine with the exponent function of the algorithm for
n is within the bound in n with k² in the exponent; the constant does not depend on k. Hypotheses:
the bound for the
exponent of a plan (`StArithD`), the exponent is at most n (`StPlanLeD`), and the decoding of the
input (`StDecM`). 
