---
{
  "module": "proof/consequences/CircuitLowerBound/Alg/Time.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Alg/Time.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Alg/Time.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): the time bound of the algorithm

The arithmetic for the proof, elsewhere in this development, of the interface statement `StAlg` from
a procedure for #3-SAT and the statements on the formula (`StForm`), on circuits as data (`StNorm`),
on the schedule (`StCertSched`) and on the last place of a chain (`StFlip`). For a given c₀ the
engine for #3-SAT is
taken with δ = 1/(32·(3c₀ + a₀ + 1)), where a₀ is the constant of `StForm`, which does not depend on
the table; so the machine is fixed before the table. For a table e the formula has at most (3c₀ +
a₀)(m+1) + g(e) variables; so the engine takes
at most c·2^{(m+1+g(e))/32} steps, the host multiplies this by a polynomial in m whose coefficients
depend on e, and the product is at most 2^{⌊m/8⌋} from some m₀(e) on (`Time.exists_threshold`). 

### `final_le`

 K·2^{m/32}·2^{m/32} ≤ 2^{⌊m/8⌋} for m ≥ 16(K + 1). 

### `base_le`

 The length of the input and the size of the states are polynomial in m. Here n is the number of
gates and Nv the number of variables. 

### `exists_threshold`

 The threshold. 
