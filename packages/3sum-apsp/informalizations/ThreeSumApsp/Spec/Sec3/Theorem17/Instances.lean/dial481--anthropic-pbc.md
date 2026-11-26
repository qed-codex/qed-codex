---
{
  "module": "ThreeSumApsp/Spec/Sec3/Theorem17/Instances.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/Instances.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/Instances.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The instances and the scans (proofs of Theorems 17 and 19), as functions on lists

The reduction of Theorem 17 makes one instance of Lop-AE-SparseTri for each chunk of a residue class
`W_ϱ` and each piece `C_k` of `C`.  The middle vertices of the instance are the pairs `(c, σ)` with
`c ∈ C_k` and `σ ∈ ℤ_p`.  This file has the two 0/1 matrices of an instance in the form in which a
routine fills them (`xList`, `yList`), the scan of a piece for a witness (`scanHit`), and the search
through all triples for small instances (`hasZero`).

The weights of an instance of Exact Triangle on `n` vertices per part are three lists `AB`, `BC`,
`AC` of `n²` integers: `w(a,b)` at `a n + b`, `w(b,c)` at `b n + c`, `w(a,c)` at `a n + c`.  The
lists `RAC` and `RBC` hold the residues of the weights modulo `p`, and
`S(a,b,c) = w(a,b) + w(b,c) + w(a,c)`.


### `xList`

 The matrix `X` of the instance for the residue `ϱ` and the piece `{c0, …, c0 + len - 1}`: the
middle vertex `(c, σ)` is the column `(c - c0) p + σ`, and `a ∼ (c, σ)` iff `σ ≡ w(a,c) + ϱ`.  `n`
rows of `D` entries. 

### `yList`

 The matrix `Y`: `(c, σ) ∼ b` iff `σ ≡ -w(b,c)`.  `D` rows of `n` entries. 

### `scanHit`

 "scan the piece C_k of its instance for a c with S(a,b,c) = 0". 

### `hasZero`

 Whether there is a zero triangle, by trying all triples (proof of Theorem 19: "smaller instances
are solved by brute force"). 
