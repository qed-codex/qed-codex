---
{
  "module": "proof/rates/PaddedDescent/F/CertTop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/CertTop.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/CertTop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Polynomial-time certificates (`PolyT`) for the top part of the function `A` of
proof/rates/PaddedDescent/F/Prog.lean: the schedule (`schedF_polyT`) and the walk of the
sparsification tree with τ as data (`certWalk`), which proves the interface statement `StCertWalk`
of proof/rates/PaddedDescent/F/Interfaces.lean. The
file also shows that numbers that `A` computes from the number n of variables are given in unary (τ,
the number of levels, the number of layers), and that
the parameters of the evaluations are computed in polynomial time (`markPar_polyT`). The
certificates of the evaluations are in proof/rates/PaddedDescent/F/CertEval.lean, that of `A` itself
in
proof/rates/PaddedDescent/F/CertA.lean. 

 ### The schedule 

### `gU_polyT`

 3K⁸ in unary is polynomial-time in K in unary. 

### `mulU_polyT`

 K·L in unary is polynomial-time in K and L in unary. 

### `sqU_polyT`

 g² in unary is polynomial-time in g in unary. 

### `schedF_polyT`

 The schedule, jointly in the pad and the number t of levels (in unary). Its start does not
depend on the input, and the pad caps every round. 

 ### The walk 

### `certWalk`

 The walk of the sparsification tree is polynomial-time jointly in the pad, τ, the root and
whatever the test depends on. 

 ### The parameters read off the input, in unary 

### `two_pow_sOf_le`

 2^(sOf n) is at most n + 1. 

### `sOf_le`

 sOf n is at most n. 

### `sOf_polyT`

 The precision sOf n is polynomial-time in n. 

### `sOf_unary`

 The precision sOf n is given in unary if n is. 

### `depthOf_unary`

 The number of levels is given in unary if n is. 

### `two_pow_lin_unary`

 2^(a·s + c) is given in unary if n is, for s = sOf n and any numbers a and c, since 2^(sOf n) ≤
n + 1. 

### `tauOf_unary`

 The threshold τ of the sparsification is given in unary if n is, since 2^(sOf n) ≤ n + 1. 

### `capOf_unary`

 The cap of the cut-off sums is given in unary if n is. 

### `betaOf_unary`

 The logarithm of the length of a block of the code is given in unary if n is. 

### `layersOf_unary`

 The number of layers is given in unary if n is. 

### `two_pow_betaOf_le`

 2^(betaOf (sOf n)) is at most n + 2^49. For sOf n = 0 it is 2^49. For s = sOf n ≥ 1 the
logarithm of the logarithm of n is at least 2s + 6, so that
betaOf s = (s + 7)² ≤ 2^(2s + 6) is at most the logarithm of n. 

### `two_pow_betaOf_unary`

 The length of a block of the code is given in unary if n is, since it is at most n + 2^49. 

### `markPar_polyT`

 The parameters of the evaluations are polynomial-time in n in unary. 

### `nOf_unary`

 The number of variables written in the input is given in unary. 
