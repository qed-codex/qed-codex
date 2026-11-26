---
{
  "module": "proof/variables/VariableBound/Search/Cert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Search/Cert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Search/Cert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 2 of Appendix D as a program: the certificate

Proves `VariableBound.StCertSearchD`: the search for the checks is polynomial-time (`PolyT`) in the
pad, jointly in everything it reads, if the function that returns X(𝓛) is; the numbers m, n̄, β, r̄,
t̄ are given in unary.

* `loadSum` and `upsNum`: all exponents are numbers given in unary or lengths of lists, so the
  integers have polynomially many bits, as Step 2 of Appendix D says of Υ.
* `argminD`: a fold whose state is empty or a pair (candidate, its key), so its length is bounded.
* `searchD`: a fold whose state the pad cuts off after every round (`PaddedDescent.F.foldl_cap`). 

### `loadSum_polyT`

 Σ_E 2^load(E) is polynomial-time, for m in unary. 

### `upsNum_eq`

 `upsNum` with the powers taken in the natural numbers. 

### `upsNum_polyT`

 The numerator of Υ is polynomial-time, for m, n̄, β, r̄, t̄ in unary. 

### `stepD_cases`

 A step of `argminD` returns the new pair or the old state. 

### `fold_stepD_mem`

 The state of `argminD` is empty or a pair (l, key l) for a member l of the list. 

### `argminD_polyT`

 The first member with the smallest key is polynomial-time, if the key and the list are. 

### `roundD_polyT`

 One round is polynomial-time, if the function that returns X(𝓛) and the list of the candidates
are; m, n̄, β, r̄, t̄ in unary. 

### `stCertSearchD`

 Step 2, the algorithm as a program: the search is polynomial-time in the pad, jointly in
everything it reads, if the function that returns X(𝓛) is; m, n̄, β, r̄, t̄ are given in unary. 
