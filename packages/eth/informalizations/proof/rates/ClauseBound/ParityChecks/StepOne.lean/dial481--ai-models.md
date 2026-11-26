---
{
  "module": "proof/rates/ClauseBound/ParityChecks/StepOne.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/StepOne.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/StepOne.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Parity checks: the first step

Lemmas for Step 1 of Appendix D of the paper (parity checks, and a cut-off modulo a power of 2):

* the two expansions [q even] = Σ_i σ_i·C(q,i) and (−1)^q = Σ_i (−2)^i·C(q,i);
* if the checks are good, the inclusion–exclusion sum cut off at nb marks, times the indicators that
  every check is violated an even number of times, is the indicator that no clause is
  violated;
* the cut-off lemma (Lemma 12) for one ξ: modulo 2^ν only the tuples of marks with at most M marks
  count, if M ≥ ν − 1 + |J₁|.

For the cut-off lemma: without the bound on the number of marks the two sides are equal, because a
product of sums over subsets is a sum over tuples of subsets; and the term of a tuple with
more than M marks is divisible by 2^ν, because σ_i is divisible by 2^(i−1) and (−2)^i by 2^i. 

 ### The expansions 

### `two_mul_sig`

 2σ_i = (−2)^i + [i = 0]. 

### `two_mul_ev`

 2·[q even] = 1 + (−1)^q. 

### `neg_one_pow_eq`

 (−1)^q = Σ_i (−2)^i·C(q,i). 

### `ev_eq`

 [q even] = Σ_i σ_i·C(q,i). 

### `sum_powerset_sig`

 The sum of σ over the subsets of a set, by their numbers of elements. 

### `sum_powerset_neg_two`

 The sum of (−2)^|s| over the subsets s of a set. 

### `sum_powerset_neg_one'`

 The sum of (−1)^|s| over the subsets s of a set that is not empty. 

 ### The product identity 

 ### The cut-off lemma 

### `fac`

 The factor of check j in the term of a tuple. 

### `prod_mul_prod`

 Two products over disjoint sets of checks as one product over all checks. 

### `dom`

 The sets from which the members of a tuple are taken. 

### `sum_all`

 Without a bound on the number of marks: the sum over all tuples is the product. 

### `two_pow_dvd_sig`

 σ_i is divisible by 2^(i−1). 

### `two_pow_dvd_neg_two_pow`

 (−2)^i is divisible by 2^i. 

### `dvd_term`

 The term of a tuple with more than ν − 1 + |J₁| marks is divisible by 2^ν. 

### `cutoff_one`

 The cut-off lemma for one ξ. 
