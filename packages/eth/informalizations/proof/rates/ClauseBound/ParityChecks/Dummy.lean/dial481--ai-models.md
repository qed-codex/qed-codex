---
{
  "module": "proof/rates/ClauseBound/ParityChecks/Dummy.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Dummy.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Dummy.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Checks as dummy variables

[q even] = ½·Σ_{y ∈ {0,1}} (−1)^{y·q}. So a parity check j can be replaced by a new variable y_j:
the pair (e, j) of a clause e of check j counts as violated by (ξ, y) if ξ violates e and
y_j = 1. Then 2^r·∏_j [|V_j(ξ)| even] is the sum over y and over all sets S of violated pairs of
(−2)^|S| (`sum_dummy`), and the sets with more than M elements may be left out
modulo 2^{M+1} (`cutoff_dummy`). Different from Lemma 12 of the paper, which gives a set of q marks
in one check the weight σ_q: here every mark has the weight −2. 

### `inc`

 The incidences (e, j) that (ξ, y) violates: e ∈ Λ_j ∩ V(ξ), j ∈ J₁ ∪ J₂, and y_j = 1 if j ∈ J₁. 

### `sum_powerset_neg_two`

 Σ_{S ⊆ T} (−2)^|S| = (−1)^|T|. 

### `card_inc`

 The number of violated incidences, check by check. 

### `fac`

 The factor of check j, as a function of the value b of its dummy variable. 

### `one_add_neg_one_pow`

 1 + (−1)^q = 2·[q even]. 

### `sum_fac`

 The two values of the dummy variable of check j together. 

### `sum_dummy`

 2^r·∏_{j ∈ J₁} [|V_j(ξ)| even]·∏_{j ∈ J₂} (−1)^{|V_j(ξ)|} is the sum over the dummy variables y
and over all sets S of violated incidences of (−2)^|S|. 

### `neg_two_pow_modEq`

 A power of −2 with an exponent above M vanishes modulo 2^{M+1}. 

### `cutoff_dummy`

 The cut-off lemma with dummy variables: modulo 2^{M+1} only the sets of at most M violated
incidences count. 
