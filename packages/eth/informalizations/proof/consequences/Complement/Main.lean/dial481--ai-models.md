---
{
  "module": "proof/consequences/Complement/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Complement/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Complement/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, Corollary 7 for cliques and vertex covers, on Turing machines, through the formula for independent sets

`tm_of_reader`: let Ms be a machine cut into polynomial-time steps that, on `codeWith G s` with s ≤
n, returns a number f(G, s) within c·2^{(δ/2)n} steps on states of size at most c·(n + n² + 2)^c,
and let `post` be a polynomial-time map from numbers to words. Then a Turing machine of Mathlib with
finite alphabets, started on `codeWith G s`, halts with `post` (f(G, s)) within ⌊C·2^{δn}⌋ steps. It
is `GraphProblems.tm_of_stepped` on the instances (G, s).
`stOnTuringMachines`: the machine Z of `stFromSized` after `readClique` and `readCover`, with the
number written by `Nat.bits` (counting) or with «the number is not 0» as the output (deciding;
«subsets of … cliques, and supersets of vertex covers …, are again such sets»,
`GraphProblems.stDecide`). 

### `tm_of_reader`

 From a machine cut into steps on the words `codeWith G s` to a Turing machine: if Ms has
polynomial-time steps and returns f(G, s), for s ≤ n, within c·2^{(δ/2)n} steps on states of size at
most c·(n + n² + 2)^c, and `post` is polynomial time, then a Turing machine with finite alphabets
halts on `codeWith G s` with `post (f(G, s))` within ⌊C·2^{δn}⌋ steps. 

### `stOnTuringMachines`

 The two clauses of `GraphProblems.CorGraphsCount` and the two of `GraphProblems.CorGraphsDecide`
on cliques and vertex covers, on Mathlib's Turing machines, from the interface
`GraphProblems.StSized`: for every δ > 0 Turing machines compute the numbers of cliques and of
vertex covers of size s, and decide whether there is a clique with at least s vertices and whether
there is a vertex cover with at most s vertices, in time O(2^{δn}). 
