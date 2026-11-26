---
{
  "module": "proof/rates/ClauseBound/Alg/CertEnum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/CertEnum.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/CertEnum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Certificates: evaluation of a network by enumeration, and brute force with the number of nodes as data

Polynomial time (`PolyT`) in the pad and the data for

* `enumF`, the evaluation of a network on g nodes by enumeration of all labels, with g given in
  unary (`stCertEnum`);
* `bruteF`, brute force on K nodes, with K given in unary (`stCertBruteK`).

In `enumF` the label of the nodes a, b is the chunk number min a b · g + max a b of a word. The
position of a chunk is a sum over all earlier chunks, so its number has
to be given in unary; the loops only use numbers below g·g, and the certificate is proved for the
function in which the number of earlier chunks is cut off at g·g. 

 ### Products that agree on the range of the loop 

### `prodL_congr`

 A product over y < n only depends on the factors with y < n. 

 ### The lengths of the chunks 

### `enumLen_unary`

 The length of a chunk is given in unary. 

### `enumBits_unary`

 The number of bits of the word of all labels is given in unary. 

 ### The chunks 

### `chunkCut`

 The chunk number j, with the number of earlier chunks cut off at g·g. 

### `chunkCut_eq`

 Below g·g the cut-off does nothing. 

### `pair_le`

 The number of the chunk of two nodes below g is below g·g. 

### `chunkCut_polyT`

 A chunk, cut off, is polynomial-time. 

 ### Enumeration 

### `enumCut`

 `enumF` with the chunks cut off. 

### `enumCut_eq`

 The cut-off does not change the value. 

### `enumF_polyT`

 Evaluation by enumeration is polynomial-time in the pad, g in unary and the context. 

### `stCertEnum`

 Evaluation of a network by enumeration is polynomial-time. 

 ### Brute force 

### `query0_polyT'`

 The query at the node v, with the number K of nodes in unary. 

### `bruteF_polyT`

 Brute force on K nodes, K in unary. 

### `stCertBruteK`

 Brute force is polynomial-time in the pad, the number of nodes in unary and the instance. 
