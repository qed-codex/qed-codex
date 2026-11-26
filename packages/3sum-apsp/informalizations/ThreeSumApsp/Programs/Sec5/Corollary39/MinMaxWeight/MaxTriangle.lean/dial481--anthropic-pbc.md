---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary39/MinMaxWeight/MaxTriangle.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/MinMaxWeight/MaxTriangle.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/MinMaxWeight/MaxTriangle.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Max-Weight Triangle from Exact Triangle, as a host

Proof of Corollary 39: "By [VW13, Theorem 3.3], finding a maximum weight triangle costs O(log² n)
times as much" as deciding whether there is a triangle of weight zero.

maxTri(n, U, ab, bc, ac, res, fr) first finds the weight W of a maximum weight triangle, by a search
from -3U upwards with the powers of two up to 6U (`mtWeight_spec`); the question whether there is a
triangle of weight at least w is an instance of Negative Triangle (`mtProbeW_spec`), which is solved
with the help of the solver of Exact Triangle.  Then it finds the largest a such that some triangle
of weight W has its first vertex ≥ a, then the largest b for this a, then the largest c for these a
and b, by three searches with the powers of two up to n (`mtStage_spec`, `mtVertices_spec`); here a
decision is an instance of Exact Triangle in which the other vertices are switched off by the weight
6U + 1 (`mtProbeZ_spec`).  All instances have the n vertices per part of the given one.  The four
searches are one loop (`search_spec`).  `isHost_maxTri` puts the procedures together.


 ## The text 

### `Size`

 The locals of maxTri(n, U, ab, bc, ac, res, fr).  The arguments; the free pointer is also the
address of the table of the powers of two up to 6U.  Then n²; the number of powers of two up to 6U;
three arrays of n² cells; the free pointer for the solvers; the weight 6U + 1 that switches off; the
bounds 10U and 7U + 1 of the instances; the vertices a and b; the weight W; the address of the table
of the powers of two up to n, and their number; a local that is never written and holds 0.  The
locals of the search lie between them. 

### `Table`

 The locals of the search: the address of the table of the powers of two, the number reached so
far, the number of powers that are still to be tried, the candidate, and the answer of the decision
for the candidate. 

### `searchLoop`

 The search: while powers are left, the candidate is the number reached plus the largest power
that is left; probe puts the answer of the decision for the candidate into its local; if it is yes,
the candidate is reached. 

### `mtInit`

 Sizes, bounds, the two tables of powers of two, and the addresses. 

### `mtProbeW`

 The decision "some triangle has weight at least the candidate". 

### `mtWeight`

 The weight of a maximum weight triangle. 

### `mtProbeZ`

 The decision "some triangle of weight W has a ≥ local ia, b ≥ local ib, c ≥ local ic". 

### `mtStage`

 One of the three searches for a vertex. 

### `mtVertices`

 The three vertices. 

### `maxTriBody`

 maxTri(n, U, ab, bc, ac, res, fr). 

### `maxTriTime`

 The time of maxTri, if the solver of Exact Triangle takes T n U steps. 

### `mtNeedAt`

 The need of maxTri, if the two solvers need re and rn. 

### `maxTriNeed`

 The need of maxTri, if the solver of Exact Triangle needs r n U. 

 ## The local variables and the memory 

### `mtBase`

 The address of the first of the three arrays. 

### `mtFrame`

 The local variables of maxTri after the beginning.  The eight parameters are those that change:
the address of the table of the search, the number reached, the number of powers that are left, the
candidate, the answer, the vertices a and b, and the weight W. 

### `MtMem`

 The two tables of powers of two are in the memory, and nothing below the free pointer has
changed. 

### `MtMem.keep`

 A change from the first of the three arrays on keeps the tables. 

### `MtLim`

 What the proofs about maxTri use of the limits. 

### `MtLim.of_ok`

 `MtLim` follows from the need of maxTri. 

 ## The beginning 

### `mtInit_spec`

 **The beginning**: the locals are set, and the two tables are written. 

 ## The search 

### `search_spec`

 **The search** starts at a number lo₀ for which the decision is yes, while it is no for
lo₀ + 2^L, and ends at a number for which it is yes, while it is no for the next number.  Inv is
what the decisions need of the memory and keep. 

 ## The surroundings 

### `MtCtx`

 The program holds a solver of Exact Triangle, a solver of Negative Triangle, and the three
procedures affine, mask, pw. 

 ## The weight of a maximum weight triangle 

### `MtMemW`

 What the decisions of the first search need of the memory and keep: the tables and the two
negated matrices. 

### `two_pow_lv_cast`

 y < 2^(lv y) ≤ 2y, in ℤ. 

### `mtProbeW_spec`

 **The decision of the first search**: is there a triangle of weight at least the candidate? 

### `mtWeight_spec`

 **The first search** finds the weight of a maximum weight triangle. 

 ## The three vertices 

### `MtMemZ`

 What the decisions of the other three searches need of the memory and keep: the tables, and the
third matrix with W subtracted. 

### `mask_fits`

 The entries fit in a word, also with 6U + 1 added. 

### `_root_.Light.Sec3.FindInst.Exact`

 Some triangle of the instance with a ≥ a₀, b ≥ b₀, c ≥ c₀ has weight exactly W. 

### `HoldsThree`

 The locals ia, ib, ic of the list l hold a, b, c. 

### `mtProbeZ_spec`

 **The decision of the other searches**: is there a triangle of weight W with vertices from a, b
and c on?  These three numbers are held by the locals ia, ib, ic, whatever the answer local holds.


### `mtStage_spec`

 **One of the three searches for a vertex**: the three numbers of the decision are functions a,
b, c of the candidate. 

### `mtVertices_spec`

 **The three vertices** of a triangle of maximum weight are written to the place for the answer.


 ## The procedure 

### `maxTri_spec`

 **maxTri** finds a triangle of maximum weight. 

### `polyNeed_maxTriNeed`

 The need of maxTri is polynomially bounded if the need of the solver is. 

### `isHost_maxTri`

 **Max-Weight Triangle from Exact Triangle**: from every solver of Exact Triangle, the procedures
of the host for Negative Triangle and affine, mask, pw, maxTri make a solver of Max-Weight Triangle.
Every call of the given solver is on an instance with the same number of vertices. 
