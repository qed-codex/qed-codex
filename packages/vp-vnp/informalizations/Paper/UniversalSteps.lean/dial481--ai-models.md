---
{
  "module": "Paper/UniversalSteps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/UniversalSteps.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/UniversalSteps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Cutting computations": the universal automaton is exact


### `prop_universal_automaton`

 **Paper: proof of Proposition prop:universal, the automaton is exact.** "So accepting runs correspond to matched
sequences of length t, provided that these are long enough": the value of the automaton's program is the sum of the
weights of the accepting runs of the machine. 

### `prop_universal_machine`

 **Paper: proof of Proposition prop:universal, the pointer machine is exact.** "So an accepting run of cost c gives
exactly one accepting run of the machine with the same weight, of at most O(|z|+c) steps, and there are no others", as
used: the accepting runs of the machine form a finite set, their weights sum to pv(z), and they have O(|z|+τ) steps. 

### `prop_universal_series`

 **Paper: proof of Proposition prop:universal, exactness and time.** The series of the automaton has the value pv(z) in
O((|z|+τ) lg(|z|+τ)²) letters. 
