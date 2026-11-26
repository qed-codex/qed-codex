---
{
  "module": "Zeta23/MV/Eigen.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/MV/Eigen.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/MV/Eigen.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# MV steps 2–3 — the Preissmann–Lévêque eigen-identity and the eigenvalue bound

* `eigen_identity` (arXiv:2203.14950 Lemma 2.1): pure Finset algebra
  over ℂ + partial fractions + the conjugate eigen-relation; the `−iμ` cross piece dies under
  `Re` — the cancellation at the heart of Montgomery–Vaughan.
* `eigen_bound`: with `c = √δ`, summing the identity over `m` for a unit
  eigenvector and inserting `spacing_sq` (≤ 9) and `Uform_le` (≤ 73):
  `μ² ≤ 9 + 2·73 = 155 ≤ 13²`.


### `eigen_identity`

 **Step 2, Preissmann–Lévêque identity.**  Only injectivity of `freq` and
positivity of `c` are needed.  `heig` is the eigen-relation `(H u)_m = iμ u_m` for the
skew-Hermitian `H_{mn} = c_m c_n/(freq m − freq n)`. 

### `eigen_bound`

 **Step 3, eigenvalue bound**: every eigenvalue of the normalized matrix
(`c = √δ`) with a unit eigenvector has `|μ| ≤ 13`. 
