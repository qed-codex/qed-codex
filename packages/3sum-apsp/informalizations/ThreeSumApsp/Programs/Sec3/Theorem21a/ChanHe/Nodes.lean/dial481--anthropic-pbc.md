---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Nodes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Nodes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Nodes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The recursion tree of the reduction from 3SUM to Convolution-3SUM

Theorem 21(a), after [CH20, Theorem 5.1].
nodes(f, s₁, l₁, s₂, l₂, s₃, l₃, cx, fr) runs through the first f levels of the recursion tree whose
root is the triple of sets at s₁, s₂, s₃ (`ChanHe.nodes`), depth first, and asks a solver of
Convolution-3SUM for the one-array instance of each node.  It returns 1 if one of the answers is
yes, and 0 if not (`nodes_spec`, by induction on f).

The text of the procedure is cut into parts, with a lemma for each.
* The parameters are read from a block in the memory (`nodesParams_ends`).
* At a node the procedure computes the modulus, writes the array at the free pointer and calls the
  solver (`nodesOwn_ends`, `c3_meets`).
* For each of the three sets in turn it writes the heavy elements of the set at the free pointer,
  where the array is no longer needed, and calls itself with the heavy elements in place of the set
  (`nodesChild₁_ends`, `nodesChild₂_ends`, `nodesChild₃_ends`; the child meets what the procedure
  assumes by `NodesPre.child₁`, `child₂`, `child₃`).
* The answer is yes if one of the four answers is (`nodesAnswer_ends`, `NodeArgs.yes_succ`).
The parts are put together in `nodesMain_ends`; the time is `tNodes_succ_le`.


 ## Pure facts 

### `conv_range_iff`

 Convolution-3SUM holds of the list of the first `N` cells of an array if and only if `ConvOne N`
holds of the array. 

### `flag_sum_pos`

 One of four answers is yes if and only if their sum is positive. 

### `lam_le`

 The number of binary digits of the labels is at most V + 2. 

 ## The procedure 

### `LEVELS`

 The local variables of nodes: the arguments f, s₁, l₁, s₂, l₂, s₃, l₃, cx, fr; the parameters V,
m, Λ, np, pr, cnt, read from the block at cx; the modulus M; the length 8m² of the array; the free
pointer behind the array; the result of nodeArray, which is not used; the answer of the solver; and
for each of the three children the number of heavy elements and the answer.  At the end local 0
receives the result, as in every procedure. 

### `nodesParams`

 The parameters are read from the block at cx. 

### `nodesOwn`

 The node itself: its modulus, its array at the free pointer, and the answer of the solver. 

### `nodesChild₁`

 The first child: the heavy elements of the first set are written at the free pointer, and the
procedure calls itself with them in place of the first set. 

### `nodesChild₂`

 The second child. 

### `nodesChild₃`

 The third child. 

### `nodesAnswer`

 The answer is yes if one of the four answers is. 

### `nodesMain`

 A triple of nonempty sets with at least one level to go. 

### `nodesBody`

 nodes(f, s₁, l₁, s₂, l₂, s₃, l₃, cx, fr), over the procedures pSelf (itself), pMod (modulus),
pArr (nodeArray), pC3 (a solver of Convolution-3SUM), pHeavy (heavy): the answer is 0 if no level is
left or one of the sets is empty. 

### `NodesCtx`

 What the procedure assumes about the program: it begins with the program of a solver of
Convolution-3SUM, holds the procedure itself, and meets the specifications of the three routines
that the procedure calls. 

### `treeCalls_le`

 The number of calls of the procedure is at most three times the number of nodes, plus one. 

### `one_le_treeCalls`

 The procedure is called at least once. 

 ## Needs and times 

### `modulusNeed_ok`

 What is allowed at a node covers what modulus needs. 

### `nodeArrayNeed_ok`

 What is allowed at a node covers what nodeArray needs behind the array. 

### `solverNeed_ok`

 What is allowed at a node covers what the solver needs behind the array. 

### `collNeed_ok`

 What is allowed at a node covers what heavy needs behind its output. 

### `childNeed_ok`

 What is allowed at a node covers what a child needs behind its set of heavy elements. 

### `tResid_mono`

 The time of resid grows with the lengths of the sets. 

### `tTally_mono`

 The time of tally grows with the lengths of the sets. 

### `tColl_mono`

 The time of coll grows with the lengths of the sets. 

### `tHeavy_mono`

 The time of heavy grows with the lengths of the sets. 

### `tModulus_mono`

 The time of modulus grows with the lengths of the sets. 

### `tNodeArray_mono`

 The time of nodeArray grows with the lengths of the sets. 

 ## The parts of the procedure 

### `NodesFits`

 What the limits allow at a node: an address fits in a word; behind the free pointer there is
room for a set and the array; the number of levels is at most the number of cells, so that it fits
in a word; the numbers up to 64 (V + 1) and 64 (m² + 1) fit in a word; and one more level of calls
is allowed. 

### `NodesPre.fits`

 What the procedure assumes provides what the limits have to allow at a node. 

### `NodesPre.child₁`

 The first child of a node meets what the procedure assumes, with one level less.  μ₀, μ and μ'
are the memories when the procedure is called, before heavy, and after heavy. 

### `NodesPre.child₂`

 The second child of a node meets what the procedure assumes, with one level less. 

### `NodesPre.child₃`

 The third child of a node meets what the procedure assumes, with one level less. 

### `NodeArgs.node`

 The node with the modulus `Mo`. 

### `nodesLocals`

 The list of the local variables of nodes: the arguments, with x for the number of levels; the
parameters that are read from the block at cx; and the list t of what has been computed since. 

### `nodesParams_ends`

 **The parameters** are read from the block at cx. 

### `c3_meets`

 The solver of Convolution-3SUM, called for the array of a node at the free pointer. 

### `nodesOwn_ends`

 **The node itself**: the modulus is computed, the array is written at the free pointer, and the
solver answers for it. 

### `nodesChild₁_ends`

 **The first child.**  Started in a memory μ that agrees below fr with the memory μ₀ in which the
procedure was called, the part leaves the number of heavy elements of the first set and the answer
for the child in HEAVY1 and ANS1, and changes no cell below fr.  x, y, z are the values of LEN, FR2,
RES, which are no longer used. 

### `nodesChild₂_ends`

 **The second child**: as for the first, with HEAVY2 and ANS2. 

### `nodesChild₃_ends`

 **The third child**: as for the first, with HEAVY3 and ANS3. 

### `nodesAnswer_ends`

 **The answer** is yes if one of the four answers is.  The lemma is stated for arbitrary locals,
so that the 26 values need not be listed; for a state that is written as a list, hloc holds by
definition and determines the four statements. 

### `tNodes_succ_le`

 The time of a node: its own work and the three subtrees.  The 178 steps are
28 + 47 + 3 · 25 + 12 for the parts of nodesMain and 16 for the four tests of nodesBody. 

### `NodeArgs.yes_succ`

 The nodes of a tree with a nonempty root: the root and the nodes of the three subtrees. 

### `nodesMain_ends`

 **A triple of nonempty sets with at least one level to go**: the parts, one after the other.
The four tests of nodesBody have taken 16 steps. 

### `nodes_spec`

 **The recursion tree**: the procedure meets its specification. 
