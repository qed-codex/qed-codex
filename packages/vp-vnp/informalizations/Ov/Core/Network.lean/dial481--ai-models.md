---
{
  "module": "Ov/Core/Network.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Core/Network.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Core/Network.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Networks

A tensor that is the value of a network is a restriction of the product of the wires on the edges of the
network, wherever its vertices are placed. The paper uses special cases: in Lemma lem:exponents, that ⟨q⟩_uw
is a restriction of ⟨q⟩_uv ⟨q⟩_vw, and the same for trees; and Lemma lem:hubs. The statements are about
functions, not graphs: a vertex v has a table T v, a function of all labels, which is *local*: it depends
only on the labels of the edges at v and on the indices held by the party of v.


### `Restr.of_contract`

 Contraction with one tensor. The legs of t are at vertices (the leg l at ρ l), every vertex v is
placed at the party ξ v and has a local table T v: it depends only on the legs of s that are held by
the party ξ v and on the legs of t at v. If s is the sum over all labels of the legs of t of the
product of the tables and of t, then s is a restriction of t, with the legs at their places. 

### `outer`

 The product of tensors with separate legs. 

### `Equi.push_outer`

 Giving the legs of a product with separate legs to parties. 

### `outer₂`

 The product of two tensors with separate legs. 

### `Equi.push_outer₂`

 Giving the legs of a product of two tensors with separate legs to parties. 

### `sum_unit_two`

 A sum over pairs of labels that must be equal. 

### `Restr.of_network`

 **Networks.** The vertices v are placed at the parties ξ v, the legs j of s are held
by the parties π j. There are edges e with labels in Λ e and ends a e, b e, and tensors t k with
their legs m at the vertices ρ k m. Each vertex has a local table T v: it depends only on the legs of
s held by the party ξ v, on the labels of the edges at v, and on the legs of the t k at v. If s is
the sum over all labels of the product of the tables and of the t k, then s is a restriction of the
product of the edges and of the t k, all at their places. 

### `Restr.of_edges`

 Networks without other tensors: if s is the sum over all labels of the edges of the product of
local tables, then s is a restriction of the product of the wires on the edges, at their places. 
