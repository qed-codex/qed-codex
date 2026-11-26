---
{
  "module": "proof/statements/CircuitLowerBoundInfinitelyOftenStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/CircuitLowerBoundInfinitelyOftenStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/CircuitLowerBoundInfinitelyOftenStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7) with «infinitely many lengths» written out

`CircuitLowerBoundStatement.lean` says: there is a language L in E^NP that is not decided by
circuits of size O(n), that is, for every c there is SOME length n at which no circuit with at most
c·(n+1) gates decides L. This file states the same with
«for every c there are INFINITELY MANY such lengths». The two are equivalent, because every set of
words of one length is decided by some circuit, so that finitely many lengths can be paid for by a
larger c; this file only states the
stronger-looking form, so that the equivalence need not be taken on trust.

Definitions only (no theorem, no proof). It imports `CircuitLowerBoundStatement.lean` (languages,
circuits `Circuit` with `eval`, the class `InENP`: read that file first) and, through it, Mathlib. 

### `DecidedAt`

 Some circuit with at most s gates decides L on the words of length n. 

### `CorCircuitsInf`

 The circuit lower bound for E^NP (Section 7), infinitely often: there is a language in E^NP such
that for every c and every N there is a length n ≥ N at which no circuit with at most c·(n+1) gates
decides it. 

### `AllDecided`

 Every set of words of length n is decided by some circuit. 
