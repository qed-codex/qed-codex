---
{
  "module": "proof/consequences/Sat3Graph/Host.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Host.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Host.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From steps of a step machine to steps of a Turing machine, for the deciders on graphs used for the decision problems of Corollary 7 («In particular, they decide …»)

No sentence of the paper stands behind this file; the paper counts operations.
* `decidesGraph_mono`, `decidesColor_mono`: a bound in steps stays true when δ and c are made
  larger.
* `outputs_of_simulates`: let the Turing machine M simulate the machine Ms, cut into steps, with
  polynomial overhead (`SplitSat.Simulates`). If Ms, started on a word x of length at most 2·(n+2)²,
  ends with a bit b within c·2^{(δ/2)n} steps on states of size at most c·(n+2)^c, then M, started
  on x, halts with b within ⌊C·2^{δn}⌋ steps: the overhead is a polynomial in n, which is at most a
  constant times 2^{(δ/2)n}. The computation is that of `SplitSat.decidesTM_of_simulates`.
* `hostedFor_of`, `hostedColor_of`: so a decider with polynomial-time steps and the exponent δ/2 is
  hosted by a Turing machine with the exponent δ. 

### `DecidesColor`

 The machine Ms, cut into steps, says on the code of a graph G on n vertices whether G can be
colored with k colors, within c·2^{δn} steps, on states of size at most c·(n+2)^c. (The body of
`StColoring`.) 

### `size_mono`

 c·(n+2)^c grows with c. 

### `time_mono`

 c·2^{δn} grows with c and δ. 

### `decidesGraph_mono`

 `DecidesGraph Ms p δ c` stays true when δ and c are made larger. 

### `decidesColor_mono`

 `DecidesColor Ms k δ c` stays true when δ and c are made larger. 

### `outputs_of_simulates`

 Let M simulate Ms with polynomial overhead. There is C such that: whenever Ms, started on a word
x of length at most 2·(n+2)², ends with the bit b within T ≤ c·2^{(δ/2)n} steps on states of size at
most c·(n+2)^c, then M, started on x, halts with b within ⌊C·2^{δn}⌋ steps. 

### `hostedFor_of`

 A decider for a property of (G, s) with polynomial-time steps and the exponent δ/2 is simulated
with polynomial overhead by a Turing machine with finite alphabets that decides the property within
⌊C·2^{δn}⌋ steps. 

### `hostedColor_of`

 The same for k-Coloring. 
