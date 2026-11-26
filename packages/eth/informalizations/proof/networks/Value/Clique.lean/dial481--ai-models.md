---
{
  "module": "proof/networks/Value/Clique.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Value/Clique.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Value/Clique.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The value of the (K, λ)-clique: from two copies on every edge to one string per edge

After Definition 3 the paper says that only the terms in which the two copies on every edge agree
contribute, and that the value is a sum over one string in {0,1}^λ per edge.
This file proves the statements of the first part of proof/networks/Value/Defs.lean, directly on the
sum that defines the value of the clique as a network:
* `stSumOverSettings`: the value is by definition a sum over the settings z = (z_w) of the nodes;
* `stCopiesMustAgree`: a term in which two copies differ is 0, and in the other terms the factors of
  the edges are 1;
* `stOneStringPerEdge`: the choices of settings in which all copies agree are the choices of one
  string per edge. A setting z_w is the concatenation of its K − 1 copies, so for given copies there
  is exactly one setting (`SecNetworks.sum_settings`, read with an indicator as summand);
* `stCliqueValueOf`, `stCliqueValue`: the sentence itself, from these three. 

### `stSumOverSettings`

 The value of a (K, λ)-clique is by definition a sum over the settings of its nodes. 

### `stCopiesMustAgree`

 Only the terms in which the two copies on every edge agree contribute. 

### `stOneStringPerEdge`

 The choices of settings in which all copies agree are the choices of one string per edge. 

### `stCliqueValueOf`

 The value as a sum over one string per edge, from the three statements before it: restrict the
sum over the settings to the terms in which all copies agree, and change the variable. 

### `stCliqueValue`

 The remark after Definition 3: the value of the clique is the sum, over one string in {0,1}^λ
per edge, of ∏_{w∈[K]} W_w at the strings on the edges at w. 
