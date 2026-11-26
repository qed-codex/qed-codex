---
{
  "module": "ThreeSumApsp/Sec3/Parameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Parameters.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Parameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The parameters and model running times of Sections 3.1 to 3.4

Numbers and functions that the running-time claims of Section 3 and the programs of Section 3 share.
None of them mentions a claim or a machine.

* `TriangleInstance.totalChunks`, the number of chunks in the proof of Theorem 17, and the three
  terms of the additional time of Theorem 17: `termScans`, `termPrime`, `termBuild`.
* The parameters of the proof of Theorem 19: `paramD₅`, `paramG₅` on the route through
  Theorem 5 and `paramD₂₆`, `paramG₂₆` on the route through Corollary 26; `strassen`, the number of
  ring operations of Strassen's algorithm.
* `splitCap`, the size of the pieces into which Corollary 15 splits the query pairs.
* `DivNondecreasing` and `GoodTime`, the condition of Theorem 21(b) on a running time, and
  `uniformTime`, the running time of Theorem 19 as a function of the size and of the bound on the
  weights.  (The number of vertices `n^{1/3}` of Theorem 21(b) is `cbrtCeil n`.)


### `TriangleInstance.totalChunks`

 Proof of Theorem 17: the number of chunks "in all", summed over the residues `ϱ`. 

### `DivNondecreasing`

 Theorem 21(b): "with T(s)/s nondecreasing". 

### `GoodTime`

 Theorem 21(b): a running time "T(s) with T(s)/s nondecreasing", for every fixed bound
`u` on the numbers.

NOTE.  We also ask that `T(s) ≥ s² (1 + log u)`, which is an upper bound for the time to write down
the `3s²` weights of an instance. The paper does not say this, but its bound
`O(n² T(n^{1/3}) log² U)` leaves no room for writing down the instances otherwise.  The condition is
a hypothesis on the running times that are fed into Theorem 21(b), so it makes the claims that use
it weaker, not stronger. 

### `uniformTime`

 The running time `K s^{3−δ} (log s + 1)^e (1 + log u)²` for Exact Triangle on `s` vertices per
part with weights of absolute value at most `u`, as a function of both arguments. 

### `termScans`

 **Theorem 17**, the first term of the additional time, "ν n³ log n/g".  It pays for the scans.
`κ` is the paper's ν. 

### `termPrime`

 **Theorem 17**, the second term of the additional time, "n^{ω+o(1)} D^{3/2}".  It pays for the
choice of the prime.  `MM n` stands for the number of ring operations of the matrix multiplication,
the paper's `n^{ω+o(1)}`. 

### `termBuild`

 **Theorem 17**, the third term of the additional time, "n² D g".  It pays for building the
instances. 

### `strassen`

 Strassen's number of ring operations, up to a constant: `n^{log₂ 7}`. 

### `strassen_nonneg`

 Strassen's number of ring operations is not negative. 

### `paramD₅`

 Proof of Theorem 19, by Theorem 5: "Let D be the largest power of four with D ≤
n^{1/18}". 

### `paramG₅`

 Proof of Theorem 19, by Theorem 5: "and let g := ⌈D^{1/36}⌉". 

### `paramD₂₆`

 Proof of Theorem 19, by Corollary 26: "Let D := ⌊n^{1/18}⌋". 

### `paramG₂₆`

 Proof of Theorem 19, by Corollary 26: "and g := ⌈D^{0.0315}⌉". 

### `splitCap`

 Corollary 15: the size `⌊n²/√D⌋` of the sets into which `W` is split (at least 1, so
that the split makes sense for all values of the parameters). 
