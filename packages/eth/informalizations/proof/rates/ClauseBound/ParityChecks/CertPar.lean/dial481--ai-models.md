---
{
  "module": "proof/rates/ClauseBound/ParityChecks/CertPar.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/CertPar.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/CertPar.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Certificates for the parameters of the count through parity checks

All numbers that the program of proof/rates/ClauseBound/ParityChecks/ProgDefs.lean computes from the
number n of variables, the bound Δ on the occurrences of a variable and the number m of clauses are
given in unary when n, Δ
and m are: the five parameters of the choice of the checks (`parQ_QU`), the cap for the marks, the
code parameters, the bounds for the rows and columns of the incidences, and the bounds for the
shared bits and the size of the networks of marks (`UbOL_unary`, `PbOL_unary`). The lemmas on
numbers made from the five parameters are stated for any function q of the context whose five
components are given in unary. 

 ### The five parameters 

### `LD_unary`

 ⌈log₂(2Δ)⌉ is given in unary. 

### `nbOf_unary`

 nb is given in unary if n is. 

### `beta0_unary`

 β₀ is given in unary if nb is. 

### `rOf_unary`

 r is given in unary if n and β₀ are. 

### `i0Of_unary`

 i₀ is given in unary if n is. 

### `beta1_unary`

 β₁ is given in unary if i₀ is. 

### `parQ_m`

 The first parameter is m. 

### `parQ_nb`

 The second parameter is nb. 

### `parQ_r`

 The number of checks is 0 if m ≤ nb. 

### `parQ_i₀`

 The fourth parameter is i₀. 

### `parQ_β`

 The fifth parameter is n + β₀ + β₁ + 2. 

### `parQ_QU`

 The five parameters are given in unary if n, Δ and m are. 

 ### Numbers made from the parameters 

### `capM_unary`

 The cap for the marks is given in unary. 

### `colMax_unary`

 The bound for the number of checks that contain a clause is given in unary. 

### `rowMax_unary`

 The bound for the number of clauses of a check is given in unary. 

### `occOL_unary`

 The bound for the number of clauses in which a variable occurs is given in unary. 

### `blkOL_unary`

 The length of the blocks of the code is given in unary. 

### `bitOL_unary`

 The number of bits of a position in a block is given in unary. 

### `parM_polyT`

 The parameters of the network of marks are polynomial-time. 

### `Ub_unary`

 The bound for the shared bits of a network of marks is given in unary if its arguments are. 

### `Pb_unary`

 The bound for the size of a network of marks is given in unary if its arguments are. 

### `g_unary`

 3K⁸ is given in unary if K is. 

### `UbOL_unary`

 The bound for the shared bits of the networks is given in unary. 

### `PbOL_unary`

 The bound for the size of the networks is given in unary. 
