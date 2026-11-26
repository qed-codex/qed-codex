---
{
  "module": "Paper/Approximate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Approximate.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Approximate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, appendix "Approximate computation"


### `VPBar`

 VP closure: like VP, with approximating circuits. 

### `def_approx`

 **Paper: Definition def:approx.** "A circuit over k((ε)) approximates a polynomial f over the field k if its output
is f + εg with all coefficients of g in k[[ε]]. The closure of VP is defined like VP with approximating circuits."
Coefficientwise: no negative powers of ε, and the part of ε⁰ is f. 

### `lem_few_approx`

 **Paper: Lemma lem:few-approx.** "The lemma on sums with few terms remains true if f_j has coefficients in
k[ε,ε⁻¹] and t is the part of ε⁰ of the sum, no negative powers occurring." 

### `exists_cut_off`

 "Cut the constants off": finitely many series can be replaced by Laurent polynomials so that the products of
n of them keep the coefficients of ε^i, i ≤ 0. 

### `wire_series`

 A wire over the Laurent series is the one over k. 

### `hubTen_series`

 The hub tensors over the Laurent series are those over k. 

### `hubs_series`

 The hub decomposition over the Laurent series: the coefficient of an entry is a sum over the balanced sets of the
hub tensors over k, with functionals in k((ε)). 

### `flat_rate_approximating`

 "So Proposition prop:flat-rate holds for approximating circuits: cut the constants off, and note that Lemma
lem:balanced holds over every commutative ring." 

### `flat_rate_approx_complete`

 "… and with it Theorem thm:flat-rate", for every family that is complete for grid sums. 

### `contracting_approx_rate`

 The contracting case with the calculation of Theorem thm:contracting. 

### `approx_rate_closed`

 Both cases over KK, for circuits with constants in KK[ε,ε⁻¹]. 

### `thm_approx`

 **Paper: Theorem thm:approx.** "The theorem on all fields holds for circuits that approximate HC_m, respectively
PERM_m. In particular VNP is not contained in the closure of VP over every field." 
