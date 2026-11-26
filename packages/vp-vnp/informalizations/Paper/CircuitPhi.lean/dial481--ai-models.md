---
{
  "module": "Paper/CircuitPhi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/CircuitPhi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/CircuitPhi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, proof of Lemma lem:circuit: the clause sum Φ


### `lem_circuit_assignment`

 **Paper: proof of Lemma lem:circuit, one assignment.** "So there is exactly one assignment for each matched sequence
and each sequence of states": an assignment g that violates no clause gives a matched sequence with the first and last
state, and each of these comes from exactly one. 

### `lem_circuit_value`

 **Paper: proof of Lemma lem:circuit, the value at a code.** The sum over the assignments at the code of an input is
the value of the automaton on it. 

### `withInputs`

 One more clause for every variable of the code: if its bit is 1 its weight is the variable. 

### `inputWeights`

 The weights: constants, and the variables of the code. 

### `lem_circuit_phi`

 **Paper: proof of Lemma lem:circuit, Φ.** A clause sum with at most 1600 B⁹ literals, weights that are constants or
variables, degree at most N, and the automaton's value at the code of every word of fewer than N symbols: what the proof
uses of Φ. ("It has degree at most n, and at the code of a word it takes that word's value ... This has v^O(1) literals.")
B is the sum of the numbers of steps, places, states, symbols and tapes. That Φ is the printed sum over words is not
stated. 
