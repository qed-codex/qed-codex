---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Host/Time.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/Time.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/Time.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The host of Theorem 17: the time of a run is within the worst case

The host procedure `et17` (Exact Triangle by Theorem 17) first computes the parameters, chooses the
prime and computes the sizes.  The time of what follows (the table of doubles, the residues, the
classes, the chunks and the loop over the instances; `hostRunTime`) depends on the data: the prime,
the number of chunks, the scans.  Here it is bounded by the corresponding summands of `hostMain`,
which depend on `n`, `U`, `D` and `g` only (`hostRunTime_le`).

* The prime is at most `√D` (`hostData_p_le`), and there are at most `4ng` instances and no more
  chunks than instances (`hostData_m_le`, `HostTime.chunkCount_le_m`).
* An instance has a piece of at most `q = ⌈s/g⌉` vertices, where `s = ⌊√D⌋`, and at most `⌊n²/√D⌋`
  query pairs, so its time without the scans is at most the worst case (`HostTime.instance_le`).
* All scans but one fail, and a failed scan belongs to a false positive of the chosen prime.  The
  proof of Theorem 17 bounds their number (`F_le_falsePositiveBound`).


### `F_le_falsePositiveBound`

 The number of false positives of the chosen prime is at most `falsePositiveBound`. 

 ## One instance 

### `tWrites_mono`

 Writing the two matrices of an instance takes longer for a longer piece. 

### `le_supTime`

 The time of the solver on an instance with at most `cap` query pairs is at most `supTime`, its
largest time on such instances. 

### `instance_le`

 The time of an instance with a piece of `len ≤ q` vertices, `w ≤ cap` query pairs and `execs`
scans is at most the worst case for `q` and `cap` plus the time of the scans. 

### `sum_le_mul_add`

 A sum of `m ≤ M` terms `f t ≤ A + B e(t)` is at most `M A + B E` if the `e(t)` add up to at most
`E`. 

 ## The data of a run 

### `chunkCount_le_m`

 There are at most as many chunks as instances. 

### `sum_execs_le_falsePositiveBound`

 All scans but one fail, and there are at most `falsePositiveBound` failed scans. 

### `tHostLoop_le`

 The time of the loop over the instances is within its bound.  Both sides are a sum over the
instances plus the same constant; the piece of an instance has `min q (n - c₀)` vertices. 

### `hostRunTime_le`

 **The time of a run after the choice of the prime is within the worst case.** 
