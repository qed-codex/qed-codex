---
{
  "module": "ThreeSumApsp/Lang/Lib/RadixPass.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/RadixPass.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/RadixPass.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# One pass of a radix sort on a list of indices

The pass sorts the list of indices at perm stably by a key that is read through the index: countSort
writes the sorted list into the w cells after the list, and copy brings it back.  What countSort
leaves is the result of a stable pass on lists (`exists_stablePass`), and `radixPass_ends` puts the
two calls together.  The pass is used with different expressions for the place of the keys, so these
are parameters.


### `exists_stablePass`

 What countSort leaves at dst is a list, and it is the result of a stable pass. 

### `Num`

 The local variables that the pass uses: w, perm, and a local that takes the results of the two
calls, which are not used. 

### `_root_.Light.radixPass`

 The pass: procedure pc is countSort, procedure pp is copy. 

### `Args`

 Where the data of a pass lie. 

### `Args.w`

 the number of indices 

### `Args.perm`

 where the list of indices stands; the w cells after it are scratch space 

### `Args.key`

 the key of the index i is in the cell key + i · stride + off 

### `Args.stride`

 see key 

### `Args.off`

 see key 

### `Args.nb`

 all keys are below nb 

### `Args.cnt`

 nb + 1 cells for the counters 

### `Args.R`

 only the R cells from perm on may change 

### `Args.sort`

 The arguments of the call of countSort. 

### `RadixPass.Pre`

 What a pass assumes: the list π of indices below w stands at perm, the keys lie before the list,
and the counters after the list and its scratch space, within the R cells that may change. 

### `RadixPass.Post`

 What a pass achieves: the list at perm is the result of a stable pass by the key kd, cnt[t] is
the number of indices with a key below t, and only the R cells from perm on have changed. 

### `RadixPass.Pre.sort`

 What countSort assumes holds for the pass: the items are the list at perm, and they go to the w
cells after it. 

### `RadixPass.Post.of_sorted_copied`

 The memory after countSort (μ₁) and after the copy (μ₂). 

### `radixPass_ends`

 **pass**: the list π of indices at perm is replaced by the result of a stable pass by the key
kd.  The five expressions give the place of the keys, the number of buckets and the place of the
counters.  Of the local variables only `Unused` changes. 
