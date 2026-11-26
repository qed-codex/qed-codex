---
{
  "module": "proof/networks/Eight/Cor/NSETH.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Cor/NSETH.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Cor/NSETH.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, the sentence after Corollary 5: k-DNF tautologies, and taking a witness off an input

The paper's sentence on NSETH rests on two facts: «a k-DNF is a tautology exactly if its negation, a
k-CNF, is unsatisfiable», and a deterministic algorithm is a nondeterministic one. The definitions
are in proof/networks/Eight/Cor/NSETHDefs.lean.
This file proves the first fact, `tautology_iff`, and two facts on `stripW`, which takes a witness
off an input word: it returns the word without the witness (`stripW_withWitness`),
and it is polynomial-time (`stripW_polyT`).

Different from the paper: the negation of a k-DNF ψ is the k-CNF with the same lists and all
literals negated. That formula is satisfiable exactly if the k-CNF with the same lists and the same
literals is (negate the assignment), so the
lemma `tautology_iff` is stated for the k-CNF with the same lists as ψ. 

### `tautology_iff`

 «A k-DNF is a tautology exactly if its negation, a k-CNF, is unsatisfiable», in this form: the
DNF ψ is a tautology exactly if the CNF with the same lists of literals is unsatisfiable. An
assignment a falsifies the DNF exactly if the
assignment with all values negated satisfies the CNF. 

### `stripW_withWitness`

 `stripW` takes the witness off. 

### `stripW_polyT`

 `stripW` is polynomial-time. 
