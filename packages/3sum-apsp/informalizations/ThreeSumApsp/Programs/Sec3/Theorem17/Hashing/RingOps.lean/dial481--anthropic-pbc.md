---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/RingOps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/RingOps.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/RingOps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Vectors: sums, differences, and the product in ℤ[x]/(x^p - 1)

The proof of Theorem 17 computes with matrices over the ring ℤ[x]/(x^p - 1); an element of the ring
is a vector of p integers, and a ring operation takes "O(p²) word operations".

* vlin(dst, a, b, n, s): dst[i] := a[i] + s b[i] for i < n, with s = 1 or s = -1; dst may be the
  segment a itself (accumulation).  It is one pass (`vlin_spec`), and what it writes is `vadd` or
  `vsub` (`vlinList_one`, `vlinList_neg_one`).
* cconv(dst, a, b, p): dst := the cyclic convolution of a and b.  The inner loop adds up the p terms
  of one entry (`cconvEntry_spec`), the outer loop stores the p entries (`cconv_spec`).  The partial
  sums stay below p α β if the entries of a and b are bounded by α and β (`abs_convPartialSum_le`).


 ## Sums and differences 

### `Dst`

 The local variables of vlin: the arguments dst, a, b, n, s, and the counter. 

### `vlinBody`

 vlin(dst, a, b, n, s): for i < n: dst[i] := a[i] + s b[i]. 

### `vlinList`

 The list that vlin writes. 

### `vlinList_one`

 With s = 1 it is the sum. 

### `vlinList_neg_one`

 With s = -1 it is the difference. 

### `vlinAt`

 Entry j of that list. 

### `VlinPre`

 What vlin assumes: the lists A and B of n numbers of absolute value at most V stand at a and b;
the n cells at dst lie in the memory, do not meet b, and are the cells at a or do not meet them. 

### `vlin_spec`

 **vlin** writes a + s b to dst and changes nothing else, in at most 23 n + 6 steps. 

### `vlin_meets`

 **vlin** as a procedure. 

 ## The product 

### `convTerm`

 A term of the convolution. 

### `convPartialSum`

 The sum of the first j terms of entry r of the convolution. 

### `convPartialSum_succ`

 One more term. 

### `cconv_eq_map_convPartialSum`

 The convolution is the list of these sums. 

### `abs_convTerm_le`

 A term is at most α β in absolute value. 

### `abs_convPartialSum_le`

 A sum of j terms is at most j α β in absolute value. 

### `Dst`

 The local variables of cconv: the arguments dst, a, b, p; the number r of the entry; the number
i of the term; the sum (Acc); the index into b. 

### `cconvTerm`

 One term: j := r - i or r + p - i; sum := sum + a[i] b[j]. 

### `cconvEntry`

 One entry: sum := the entry number r of the convolution. 

### `cconvBody`

 cconv(dst, a, b, p): for r < p: dst[r] := the entry number r. 

### `CconvPre`

 What the inner loop of cconv assumes: the lists A and B of p numbers, bounded by α and β, stand
at a and b, and p α β fits in a word. 

### `cconvTerm_spec`

 **One term of cconv.** 

### `cconvEntry_spec`

 **One entry of cconv**, in at most 32 p + 8 steps. 

### `CconvInv`

 The state of cconv before round r: the first r entries are written, and no cell outside dst has
changed. 

### `cconv_spec`

 **cconv** writes the cyclic convolution to dst and changes nothing else, in at most
32 p² + 21 p + 6 steps. 

### `cconv_meets`

 **cconv** as a procedure. 
