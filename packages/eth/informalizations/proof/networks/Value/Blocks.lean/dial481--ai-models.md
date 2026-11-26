---
{
  "module": "proof/networks/Value/Blocks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Value/Blocks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Value/Blocks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The strings on the edges of the clique of the groups, block by block

Proof of Lemma 1, paragraph «The algorithm». This file proves four of the statements of
proof/networks/Value/Defs.lean:
* `stLayout`: «In this order, the pair {a, b} is assigned a block of c_{a,b} consecutive positions
  of {1, …, L}; the L − Y_{γ,γ'} positions after the last block hold the appended bits»;
* `stSameBlock`: «both W̃_γ and W̃_γ' read θ_{a,b} from the same block of this string, so θ_{a,b} =
  θ_{b,a}»;
* `stAppendedZero`: «the appended bits must be 0»;
* `stBlocks`: the strings of L bits on the edges whose appended bits are 0 are the choices of «one
  string θ_{a,b} ∈ {0,1}^{c_{a,b}} per pair {a,b} of nodes in different groups».
The last is proved edge by edge (`edge_unique`): the strings of L bits on one edge {γ, γ'} with
appended bits 0 are the choices of one block per pair (a, b), a ∈ G_γ, b ∈ G_γ' (`NetE.sum_mdec`:
cut the string into its blocks; back: write the blocks one after the other and append zeros).
`NetE.sum_mdec` is not public in proof/machines/StepMachines/Prog/NetVal.lean; the line
`import all StepMachines.Prog.NetVal` is there only to reach it. 

### `stLayout`

 «For each pair of groups {γ, γ'} choose an order of the pairs {a, b} … In this order, the pair
{a, b} is assigned a block of c_{a,b} consecutive positions of {1, …, L}; the L − Y_{γ,γ'} positions
after the last block hold the appended bits.» 

### `stSameBlock`

 «both W̃_γ and W̃_γ' read θ_{a,b} from the same block of this string, so θ_{a,b} = θ_{b,a}». 

### `stAppendedZero`

 «the appended bits must be 0»: otherwise the factor [all appended bits are 0] of one of the
tables is 0. 

### `thetaAt_eq_readBlocks`

 «so θ_{a,b} = θ_{b,a}»: whichever of the two tables reads it, the string that is read for the
nodes a, b in different groups is the one that `readBlocks` has at the pair {a, b}. 

### `readBlocks_mem`

 «θ_{a,b} ∈ {0,1}^{c_{a,b}}»: what the tables read from one string of L bits per edge is a choice
of one string of c_{a,b} bits per pair {a, b} of nodes in different groups. 

### `length_blockString`

 A string θ_{a,b} of a choice of blocks has as many bits as the procedures say, whichever of a, b
is the smaller. 

### `mem_mD_iff`

 The strings of L bits whose bits after the last block are 0. 

### `edge_unique`

 One edge of the clique of the groups, given by the group indices G, G' (in either order): for
every choice of one string t(a, b) of c_{a,b} bits per pair (a, b), a in group G, b in group G',
exactly one string of L bits has these strings in its blocks and zeros after the last block. 

### `EdgeReads`

 What the choice θ of blocks asks of the string w at the place p = (γ, γ') of a choice of one
string per edge: for γ < γ', w has L bits, zeros after the last block, and θ_{a,b} in the block of
(a, b) for all a ∈ G_γ, b ∈ G_γ'; at all other places w is empty. 

### `blocks_iff`

 The three conditions on Λ (one string of L bits per edge; all appended bits are 0; the tables
read θ from Λ), said edge by edge. The hypothesis `hSB` says that the two tables at an edge read the
same block. 

### `stBlocks`

 The choices of one string of L bits per edge {γ, γ'} with all appended bits 0 are the choices of
«one string θ_{a,b} ∈ {0,1}^{c_{a,b}} per pair {a,b} of nodes in different groups». 
