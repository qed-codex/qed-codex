---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary39/GraphH/Build.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/GraphH/Build.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/GraphH/Build.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 39 in the light language: what the hosts for k-Clique share

Proof of Corollary 39: "We enumerate the n^t ways of fixing one vertex in each of the first t parts,
and for each of them we build H".  The hosts for weight zero and for minimum and maximum weight do
this in the same way.  `hostSetup_spec` computes N = n^⌊k/3⌋, n^t and the places (`matH`);
`buildH_spec` writes the three matrices of H for one choice of the fixed vertices, by three calls of
`fillH_spec`, and they are an instance of a triangle problem with the graph H (`HoldsH.pre`,
`HoldsH.graphAt_eq`, collected in `Built`); `nextChoice_spec` goes to the next choice.

The paper's bound n^ν on the weights is a free parameter U, and its bound (k choose 2) n^ν on the
weights of H is lenH k * U, where lenH k is the number of pairs of parts.

The local variables that both hosts use are in the namespace `KC`; `hostPairs` lists them with their
values before a round, and `HostLocals` says what the pieces of text of this file read.


 ## Small pieces 

### `powE`

 The power n^j, as an expression. 

### `powE_cost`

 The cost of the expression. 

### `powE_safe_val`

 The expression is safe if the powers up to n^j fit in a word, and its value is n^j. 

### `zeroStmt`

 Write 0 to the cells base + j, …, base + j + len - 1 (base is local vb). 

### `zeroStmt_assigns`

 `zeroStmt` assigns no local variable. 

### `zeroStmt_spec`

 **zeroStmt** writes 0 to len cells and changes nothing else; 5 steps for each cell. 

 ## The text 

### `lenH`

 The number of pairs of parts; the weights of H are at most lenH k times as large as those of the
graph. 

### `buildH`

 Build H for the current choice of the fixed vertices: its three weight matrices. 

### `hostSetup`

 What a host does first.  `Choice` holds the free pointer.  The host computes N and n^t, then the
places of the three matrices of H behind the k cells of the chosen vertices and the first cell
behind them, and makes the first choice. 

### `nextChoice`

 Go to the next choice of the fixed vertices. 

### `buildH_assigns`

 `buildH` assigns only `Row`, `Col`, `Place` and `Entry`. 

### `nextChoice_assigns`

 `nextChoice` assigns only `Round`. 

### `fillT`

 The time of fillMat for the matrix number i. 

 ## The layout of the memory, and the locals that hold it 

### `matH`

 The places behind the k cells of the chosen vertices at fr: `matH k n fr i` is the address of
matrix number i of H, for i = 0, 1, 2, and `matH k n fr 3` is the first cell behind the matrices. 

### `matH_places`

 The four places, written out. 

### `matH_bounds`

 Each of the three matrices lies behind the chosen vertices and before `matH k n fr 3`. 

### `HostLocals`

 What both hosts hold in the locals `Size` to `Behind` during their loops. 

### `HostLocals.of_keep`

 `HostLocals` survives a piece of text that assigns only `Row`, `Col`, `Place` and `Entry`. 

 ## The three matrices of H in the memory 

### `tri_ext`

 Two instances with the same three matrices are equal. 

### `KcInst.Pre.abs_le`

 The weights in the memory are bounded by U. 

### `fillCtx_of_pre`

 The context of sumPairs from the precondition of the task. 

### `length_pairsN_le`

 Each of the three lists of pairs is a part of all pairs. 

### `lenH_pos`

 There is at least one pair of parts. 

### `BuildOk`

 What building H needs of the limits. 

### `triInstOf`

 The instance of a triangle problem that buildH leaves in the memory: H, with its three matrices
behind the k cells at fr. 

### `graphAt`

 The graph whose three weight matrices stand in the memory μ behind the k cells at fr. 

### `KcInst.H`

 The graph H of the choice number F of the fixed vertices. 

### `HoldsH`

 The three matrices of H for the choice number F of the fixed vertices stand in the memory μ,
behind the k cells at fr.  μ₀ is a memory that holds the weights. 

### `HoldsH.graphAt_eq`

 The three matrices in the memory are the graph H. 

### `absLe_matrixH`

 The entries of a matrix of H are at most lenH k times as large as the weights of the graph. 

### `HoldsH.pre`

 The three matrices are an instance for a solver of a triangle problem. 

### `fillH_spec`

 **One matrix of H.**  With the row odometer at ro and the column odometer at co, fillMat writes
the sums over the list number i of pairs to the place dst of matrix number i, which local dl holds.


### `Built`

 **What buildH achieves** for the choice number F of the fixed vertices.  The cells below fr and
the chosen vertices are as before, and the three matrices behind them are an instance of a triangle
problem with the graph H. 

### `buildH_spec`

 **buildH** writes the graph H of the choice number F of the fixed vertices. 

 ## The set-up and the next choice 

### `hostSetup_spec`

 **hostSetup** computes the sizes and the places, and chooses vertex 0 in every part. 

### `nextChoice_spec`

 **nextChoice** turns the choice number F of the fixed vertices into the choice number F + 1. 

### `hostPairs`

 The locals that both hosts use in the same way, with their values before the round for the
choice number F of the fixed vertices. 
