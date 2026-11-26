---
{
  "module": "Nc/Hc/Grid.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Hc/Grid.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Hc/Grid.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Grid completeness of the permanent and of the Hamiltonian cycle polynomial

A sum over two families of bits of products of weights, one for every incidence, is a Hamiltonian cycle polynomial
with affine entries, in every characteristic. For every incidence there are seven segments and ten gadgets.


### `Seg`

 The segments of a grid: one for every bit of the two families; for every incidence the one that chooses the
weight, one for each of the two sides and one for each of the four pairs of bits; and some for padding. 

### `Seg.equivSum`

 The segments as a disjoint union. 

### `Opt`

 The options of a segment. 

### `Gad`

 The ten gadgets of an incidence. 

### `gridPort`

 The two options of every gadget. 

### `gridRow`

 The row of segments of a grid. 

### `choice`

 The selection that belongs to two families of bits. 

### `gridWeight`

 The weights of the options: only the choices at the incidences carry one. 

### `choice_cases`

 The three kinds of gadgets at one incidence. 

### `valid_choice`

 The selection of two families of bits uses every gadget exactly once. 

### `incidence_cases`

 The pair chosen at an incidence is the pair of the bits of its two ends. 

### `eq_choice_of_valid`

 The selections that use every gadget exactly once are those of the
pairs of families of bits. 

### `gridRow_noParallel`

 Every option of a grid, except at most one in its segment, runs through a gadget. 

### `hcSum_grid`

 Over every commutative semiring, a sum over two families of bits of
products of weights, one for every incidence, is the sum over the cycles through all vertices of the grid graph. 

### `card_gridVtx`

 The number of vertices of a grid. 

### `hcSum_equiv`

 Renaming the points does not change the sum over the cycles. 

### `aeval_genHC`

 Substitution in the Hamiltonian cycle polynomial gives the sum over the cycles. 
