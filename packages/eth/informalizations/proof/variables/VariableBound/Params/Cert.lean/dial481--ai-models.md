---
{
  "module": "proof/variables/VariableBound/Params/Cert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Params/Cert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Params/Cert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Setting and parameters of Appendix D: certificates

The numbers n̄, β, r̄, t̄ of proof/variables/VariableBound/Params/Defs.lean are given in unary when
their arguments are. Each of n̄, r̄, t̄ is made from the length of a list: the numbers below a bound
given in unary that pass a test.
The test compares products of powers whose exponents are given in unary, because the index is below
that bound (for n̄ the exponent is 2^a ≤ 2(n + 1)); so it is polynomial-time
(`filter_range_polyT`). For n̄ = 2^(length − 1) the bound n̄ ≤ n + 1 is used as well. The class
PolyT of polynomial-time functions and its closure lemmas come from proof/machines/ToTuring and
proof/rates/ClauseBound/ParityChecks/CertLib.lean. 

### `filter_range_polyT`

 The list of the i < n that pass a test is polynomial-time, for n in unary; the test is only
needed for indices given in unary. 

### `two_pow_log_le`

 2^⌊log₂ n⌋ ≤ n + 1. 

### `nbD_le`

 n̄ ≤ n + 1. 

### `nbD_unary`

 n̄ is given in unary if n is and Δ is polynomial-time. 

### `beta_unary`

 β is given in unary if n and n̄ are and m is polynomial-time. 

### `rbD_unary`

 r̄ is given in unary if β is. 

### `size_unary`

 The number of binary digits of m is given in unary if m is polynomial-time. 

### `tbD_unary`

 t̄ is given in unary if r̄ is and m and n̄ are polynomial-time. 

### `stCertParam`

 «Setting and parameters»: the computed n̄, β, r̄, t̄ are given in unary if n, Δ, m, β, n̄, r̄
are. 
