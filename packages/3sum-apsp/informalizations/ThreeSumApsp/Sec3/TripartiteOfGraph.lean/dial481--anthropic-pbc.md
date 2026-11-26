---
{
  "module": "ThreeSumApsp/Sec3/TripartiteOfGraph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/TripartiteOfGraph.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/TripartiteOfGraph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section 3.2: from an arbitrary graph to a tripartite one

"an instance on an arbitrary n-vertex graph reduces to this form by taking three copies of the
vertex set and giving every missing edge the weight 3n^ν + 1, which lies in no zero triangle (this
replaces ν by ν + 1)".  The instance is `tripartiteOfGraph`.  A triangle with a missing edge does
not have weight zero (`not_isZeroTriangle_tripartiteOfGraph`), so the instance has a zero triangle
exactly if the graph has one (`hasZeroTriangle_tripartiteOfGraph_iff`).  Its weights are at most
`n^{ν+1}` in absolute value (`weightsBoundedBy_tripartiteOfGraph`; nothing else rests on this last
lemma).


### `tripartiteOfGraph`

 Section 3.2: "taking three copies of the vertex set and giving every
missing edge the weight 3n^ν + 1".  `U` stands for the bound `n^ν` on the weights of the given
graph. 

### `not_isZeroTriangle_tripartiteOfGraph`

 Section 3.2: "the weight 3n^ν + 1, which lies in no zero triangle". 

### `hasZeroTriangle_tripartiteOfGraph_iff`

 Section 3.2: "an instance on an arbitrary n-vertex graph reduces to this
form by taking three copies of the vertex set and giving every missing edge the weight 3n^ν + 1,
which lies in no zero triangle".

NOTE.  An integer `U`, a bound on the absolute values of the weights of the edges of `G`, stands for
the paper's `n^ν`, which need not be an integer. 

### `weightsBoundedBy_tripartiteOfGraph`

 Section 3.2: "(this replaces ν by ν + 1)".

NOTE.  Stated for a natural number `κ`, so that `3n^κ + 1` is an integer, and for `n ≥ 4`: for
`n ≤ 3` the weight `3n^κ + 1` exceeds `n^{κ+1}`. 
