---
{
  "module": "proof/variables/VariableBound/Cert/Top.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Cert/Top.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Cert/Top.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The exponents of the bound in n and the plan are polynomial-time

This file belongs to Appendix D, the bound in the number n of variables. It is the twin of
proof/sparsification/UniformInK/Cert/Top.lean, whose lemmas on β and on 2^β are used as they are.
The
width k is read from the input, in unary, so every parameter is shown to be given in unary, or to be
polynomial-time, jointly in k, n and s in unary. What differs from the twin: the bounds U, P, B
of Step 3 (`UbD`, `PbD`, `BbD`; in unary by proof/variables/VariableBound/Net/CertEv.lean); the
entries of the networks have up to B = `BbD k n` bits (in
proof/sparsification/UniformInK/Cert/Top.lean B is 0), so the exponent of the networks is
certified for B in unary (`needNetC_polyT`); the exponent for everything else is the formula
`restD`, with the bit lengths of the bounds for the number of objects and for the length of the list
of checks (`restD_polyT`); the plan (`planAtD_polyT`) has three tests. 

 ### The exponent for everything but the networks 

### `restD_aux`

 The formula of the exponent for everything but the networks is polynomial-time when every number
in it is. 

### `restD_polyT`

 The exponent for everything but the networks is polynomial-time if k, K, n and s are given in
unary. 

 ### The exponent of the networks and the plan 

### `bitsS_unary`

 The bound for the bit length of the entries of the rebalanced instance is given in unary if K,
g, P and B are. 

### `needNetC_polyT`

 The exponent of the networks, computed under a bound, is polynomial-time if the solver, the
bound and the index are and U, P and B are given in unary. 

### `planAtD_polyT`

 The plan is polynomial-time if the solver is, k, n and s are given in unary and the index is
polynomial-time. 
