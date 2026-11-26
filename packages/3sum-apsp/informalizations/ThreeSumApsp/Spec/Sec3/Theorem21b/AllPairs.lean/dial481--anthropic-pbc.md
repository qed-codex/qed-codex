---
{
  "module": "ThreeSumApsp/Spec/Sec3/Theorem21b/AllPairs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem21b/AllPairs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem21b/AllPairs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# All pairs with a witness, by marking

The middle step of [VW18, Theorem 4.2], one of the reductions behind Theorem 21(b).
Given three `n × n` matrices `X`, `Y`, `V`, the task is to mark all pairs `(i, j)` for which some
`k` has `X[i,k] + Y[k,j] < V[i,j]` (`Witness`, `PairHit`).  The three ranges are cut into blocks of
`s` indices.

* The last block of a range is moved back so that it ends at `n`; blocks may overlap, and there are
  no padding vertices (`blockOff`, `blockCount`, `exists_block`).
* For a triple of blocks, the `s × s × s` instance `blockTri` has the weights `X[i,k]`, `Y[k,j]` and
  `-V[i,j]`; a pair that is already marked gets the weight `F = 2U + 1` instead of `-V[i,j]`
  (`maskNeg`), which is too large for a negative triangle.
* So every negative triangle that is found is an unmarked pair with a witness (`unmarked_of_neg`),
  marking it keeps the marks right (`Marks.set`) and lowers the number of unmarked pairs
  (`count_set_one`).  If the instance of a triple has no negative triangle, then every pair of the
  triple with a witness in the middle block is marked (`BlockDone`, `blockDone_of_not`), and this
  stays so when more pairs are marked (`BlockDone.set`).
* When all triples are done, the marks are the answer (`Marks.complete`).
* `tripleIdx p I K J` is the position of a triple in the order in which the triples are visited.


 ## Blocks 

### `blockOff`

 The offset of block number `I`: `I s`, or `n - s` if the block would otherwise go beyond `n`. 

### `blockCount`

 The number of blocks: `⌈n/s⌉`. 

### `blockOff_add_le`

 A block ends at `n` or before. 

### `lt_blockCount_iff`

 `i` blocks do not cover the range exactly if `i` is less than the number of blocks. 

### `blockCount_mul_lt`

 The blocks overshoot the range by less than one block. 

### `le_blockCount_mul`

 The blocks cover the range. 

### `blockCount_pos`

 A range that is not empty has a block. 

### `blockCount_le`

 There are at most `n` blocks. 

### `exists_block`

 Every index lies in a block. 

 ## The order of the triples 

### `tripleIdx`

 The position of the triple `(I, K, J)` of numbers below `p` in the lexicographic order. 

### `tripleIdx_inj`

 The position determines the triple. 

### `tripleIdx_lt`

 The positions are below `p³`. 

### `tripleIdx_succ_J`

 The next triple, when only `J` moves. 

### `tripleIdx_succ_K`

 The next triple, when `J` starts again and `K` moves. 

### `tripleIdx_succ_I`

 The next triple, when `J` and `K` start again and `I` moves. 

### `tripleIdx_top`

 The position after the last triple. 

 ## The third matrix of a block instance 

### `maskNeg`

 The weights of the pairs `(a, c)`: `F` for a marked pair, and `-V` otherwise. 

### `length_maskNeg`

 The third matrix is as long as the shorter of the two lists. 

### `getElem_maskNeg`

 An entry of the third matrix. 

### `getD_maskNeg`

 An entry of the third matrix, read with a default. 

### `abs_le_of_mem_maskNeg`

 A bound on `F` and on the entries of `V` is a bound on the entries of the third matrix. 

 ## Marks 

### `Witness`

 The index `k` is a witness for the pair `(i, j)`: `X[i,k] + Y[k,j] < V[i,j]`. 

### `PairHit`

 The pair `(i, j)` has a witness `k < n`. 

### `Marks`

 The list `O` of `n²` marks is right as far as it goes: every entry is 0 or 1, and every pair
marked 1 has a witness. 

### `BlockDone`

 The triple of blocks at the offsets `oI`, `oK`, `oJ` is done: every pair of the first and the
third block that has a witness in the middle block is marked. 

### `blockTri`

 The instance for a triple of blocks. 

### `blockTri_S`

 The weight of a triangle of the instance for a triple of blocks. 

### `blockDone_of_not`

 If the instance of a triple of blocks has no negative triangle, then the triple is done. 

### `unmarked_of_neg`

 A negative triangle of the instance of a triple of blocks is an unmarked pair with a
witness. 

### `Marks.set`

 Marking a pair that has a witness keeps the marks right. 

### `count_set_one`

 Marking an unmarked pair makes the number of unmarked pairs smaller. 

### `BlockDone.set`

 A triple of blocks that is done stays so when another pair is marked. 

### `Marks.complete`

 **When all triples of blocks are done, the marks are the answer.** 

### `marks_replicate`

 At the beginning no pair is marked. 
