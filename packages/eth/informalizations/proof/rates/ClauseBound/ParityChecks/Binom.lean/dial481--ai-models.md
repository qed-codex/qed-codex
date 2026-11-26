---
{
  "module": "proof/rates/ClauseBound/ParityChecks/Binom.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Binom.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Binom.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Bounds on binomial coefficients, as used for the numbers of shared bits in Step 3 of Appendix D

A product of binomial coefficients is at most the binomial coefficient of the sums, because
C(a,i)·C(b,j) is one term of Vandermonde's formula for C(a+b, i+j). The logarithm of C(t, μ) is
at most μ'·max{1, log₂(3t/μ')} for μ ≤ μ': if μ' ≤ t, then C(t, μ) is one term of Σ_{ν ≤ μ'} C(t, ν)
≤ (3t/μ')^μ', and otherwise C(t, μ) ≤ 2^t ≤ 2^μ'. Rounding a logarithm up costs at most
one bit. 

### `choose_mul_choose_le`

 C(a,i)·C(b,j) ≤ C(a+b, i+j). 

### `clog_le_logb_add_one`

 Rounding a binary logarithm up costs at most one bit. 

### `prod_choose_le`

 A product of binomial coefficients is at most the binomial coefficient of the sums. 

### `logb_choose_le`

 log₂ C(t, μ) ≤ μ'·max{1, log₂(3t/μ')} for μ ≤ μ', μ' ≥ 1. 
