---
{
  "module": "ThreeSumApsp/RunningTimes/Sec5/Corollary39/ZeroWeight.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary39/ZeroWeight.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary39/ZeroWeight.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 39, the zero-weight case, on the word RAM

Corollary 39 reduces weighted k-Clique to triangle problems on N = n^⌊k/3⌋ vertices per
part, one for each of the n^t choices of the fixed vertices.

* The host that builds the graph H and calls a solver of Exact Triangle takes at most n^t (T(N, ·) +
  C N²) steps (`exists_kcTime_le`; the arithmetic is `hostTime_le`).
* A host with such a time proves the transfer claim of the proof of Corollary 39
  for programs of the light language, that is, for the reading `lightModel5` of "is solved in time
  T" (`solvedIn_of_hostTime`, `claim_zeroCliqueFromExactTriangle`).
* With the bound of Theorem 19 for Exact Triangle, the arithmetic of the running times, which holds
  for any reading of "is solved in time T" (`zeroClique_of_theorem_19`), gives O(n^{k -
  ε_T ⌊k/3⌋}), and `realized_zeroKClique` and `FromClaims.solvedAt_of_realized` carry it to the word
  RAM (`corollary_39_zero_of_theorem_19`).


 ## The time of a host 

### `exists_fillT_le`

 Writing the three weight matrices of H takes a constant times N² steps. 

### `hostTime_le`

 The arithmetic of the time of a host: P rounds, each of F ≤ c X steps, a call of t₀ steps and a
further steps, and b ≤ b' X steps outside the rounds. 

### `exists_kcTime_le`

 The time of the host: n^t calls of the solver, and a constant times N² steps for each of them
(proof of Corollary 39: t = numFixed k, N = n ^ width k). 

### `one_le_one_add_logU`

 `1 + log(max(u, 2))` is at least 1. 

### `solvedIn_of_hostTime`

 A host that takes at most n^t (T(N, ℓU) + C N²) steps, where ℓ is the number of pairs of parts,
transfers running times as the proof of Corollary 39 says. 

 ## Corollary 39, the zero-weight case 

### `claim_zeroCliqueFromExactTriangle`

 **The transfer claim of the proof of Corollary 39** holds for programs of the light
language. 

### `corollary_39_zero_of_theorem_19`

 **Corollary 39, the zero-weight case, on the word RAM**, from the bound of Theorem 19 for Exact
Triangle for programs of the light language. 
