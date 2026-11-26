---
{
  "module": "proof/variables/VariableBound/Net/CertEv.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/CertEv.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/CertEv.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 3: one evaluation is polynomial-time

One evaluation (`evD`) is the sum, over the admissible profiles, of the values of their networks,
each computed by the clique solver. For a polynomial-time solver it is polynomial-time (PolyT)
jointly in the width k, n and Δ (given in unary), n̄, M, the
pad, the index of the solver, the flag that chooses between the sums for X and for F of Step 3, and
the data (ψ, 𝓛): `stCertEvD`, the interface statement `StCertEvD`.
The certificates of the value of a network through the solver, of the network of one profile and of
the test «admissible» are hypotheses.

The bounds of «The total» and «The parameters» that do not depend on the formula are given in unary
when k, K, n and Δ are: `UbD_unary`, `PbD_unary`, `BbD_unary`, with `tbMax_unary`, `sbMax_unary`,
`objMax_unary`. P = ⌈2P₀⌉ is the
ceiling of a rational number; with a natural number in the place of s̄ the ceiling disappears
(`PD_natCast`, `PbD_eq`). 

 ### The bounds in natural numbers 

### `PD_natCast`

 P = ⌈2P₀⌉ for a natural number s̄: 2·(⌈n/g⌉(1 + Δ(t̄ + 3)) + ⌈r̄/g⌉·s̄). 

### `PbD_eq`

 The bound P that does not depend on the formula, in natural numbers, with g = 3K⁸. 

 ### The bounds are given in unary 

### `tbMax_unary`

 The bound for t̄ is given in unary if n and Δ are polynomial-time. 

### `sbMax_unary`

 The bound for s̄ is given in unary if Δ is. 

### `objMax_unary`

 The bound for the number I + m of objects is given in unary if n and Δ are. 

### `UbD_unary`

 The bound on the total U in «The total» of Step 3, with the logarithms rounded up, is given in
unary if k, K, n and Δ are. 

### `PbD_unary`

 The bound P that does not depend on the formula is given in unary if K, n and Δ are. 

### `BbD_unary`

 B = (k + 1)·14n + 1 is given in unary if k and n are. 

 ### One evaluation 

### `objs_polyT`

 The list of the objects is polynomial-time. 

### `nPr_polyT`

 The number of the numbers that are tried as profiles is polynomial-time if g is given in unary
and the data are polynomial-time. 

### `ctx_polyT`

 The context of the network of a profile is polynomial-time if g and n are given in unary and the
data, the profile and the flag are polynomial-time. 

### `CertEv.stCertEvD`

 `StCertEvD`: one evaluation is polynomial-time jointly in all its arguments, the width k, n and
Δ given in unary, if the solver is polynomial-time; given the certificates of the value of a network
through the solver, of
the network of one profile (condition (iii) of the definition of a network) and of the test
«admissible». 
