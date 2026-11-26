---
{
  "module": "proof/maintheorem/WidthThree/Rates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/WidthThree/Rates.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/WidthThree/Rates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # At width 3: from one machine for all δ > 0 to Theorem 2 and to the failure of the exponential time hypothesis

This file goes from the hypothesis «one machine decides 3-SAT within A·2^{δn} steps for every δ > 0»
(`Sat3.SubexpTM`) to four statements:
for every δ > 0 some machine decides 3-SAT within c·2^{δn} steps (Theorem 2 in its decision form),
in two wordings, and the failure of the exponential time hypothesis (Corollary 5), in two wordings.
The proofs derive these four statements from the hypothesis alone. 

 ### From «one machine for all δ > 0» to Theorem 2 and to the failure of the exponential time hypothesis 

### `everyDeltaAMachine_of_subexpTM`

 If one machine decides 3-SAT within A·2^{δn} steps for every δ > 0, then for every real δ > 0
some machine decides 3-SAT within c·2^{δn} steps. 

### `ethFails_of_subexpTM`

 If one machine decides 3-SAT within A·2^{δn} steps for every δ > 0, then the exponential time
hypothesis, in the form «the infimum of the δ for which 3-SAT is in time O(2^{δn}) is positive»,
fails. 

### `everyDeltaAMachineWording_of_subexpTM`

 If one machine decides 3-SAT within A·2^{δn} steps for every δ > 0, then for every real δ > 0
some machine decides 3-SAT in time at most C·2^{δn}, in the wording with a real constant C and a
time function t(n) ≤ C·2^{δn}. 

### `ethFailsWording_of_subexpTM`

 If one machine decides 3-SAT within A·2^{δn} steps for every δ > 0, then the exponential time
hypothesis, in the form «s_k > 0 for all k ≥ 3», fails: it fails at k = 3. 
