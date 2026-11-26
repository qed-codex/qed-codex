---
{
  "module": "ThreeSumApsp/Sec5/Theorem34.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Theorem34.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Theorem34.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 34: directed unweighted APSP

By Theorem 33 it is enough to compute the (min,+)-product of an `n × n^μ` matrix by an `n^μ × n`
matrix, with entries of absolute value `Õ(n^{1-μ})`, in `O(n^{2+μ-ε₁})` time.  Running times are not
defined here; this file checks the steps of the paper's proof, in which `ε' = 0.00175` is the
constant of Theorems 19 and 22:
* the product consists of the products of the blocks of `n^μ` rows with the blocks of `n^μ` columns
  (`theorem_34_blocks`);
* their entries are small enough for Theorem 22, since `μ ≥ 1/2` (`theorem_34_entries`);
* the `n^{2-2μ}` products cost `Õ(n^{2+μ-με'/3})` in all (`theorem_34_total`), which is
  `O(n^{2+μ-ε₁})` for every `ε₁ < με'/3` (`theorem_34_absorb`).


### `theorem_34_blocks`

 Proof of Theorem 34: "Cut the n × n^μ matrix into n^{1-μ} blocks of n^μ
consecutive rows, and the n^μ × n matrix into n^{1-μ} blocks of n^μ consecutive columns.  The
(min,+)-product then consists of n^{2-2μ} products of two n^μ × n^μ matrices, one for each pair of
blocks."  Here m = n^μ and b = n^{1-μ}, so that n = b * m. 

### `theorem_34_entries`

 Proof of Theorem 34: "Their entries have absolute value Õ(n^{1-μ}) ≤ Õ(n^μ), because μ ≥ 1/2".
Stated is the inequality between the two powers, which is what `μ ≥ 1/2` gives; the logarithmic
factors are the same on both sides.  How Theorem 22 is applied to entries of this size is said at
the library's lemma `conditional_theorem_34`. 

### `theorem_34_total`

 Proof of Theorem 34: "Theorem 22 computes each of them in Õ((n^μ)^{3-ε'/3}) time, and
all of them in Õ(n^{2+μ-με'/3}) time", with ε' = 0.00175. 

### `theorem_34_absorb`

 Proof of Theorem 34: "This is O(n^{2+μ-ε₁}) for any constant ε₁ < με'/3". 
