---
{
  "module": "Paper/Rate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Rate.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Rate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "The main theorem", and the results of the introduction


 ### The geometry of the proof of Proposition prop:flat-rate 

### `prop_flat_rate_direction`

 "So |t_S| ≥ (2/9)k^(3/2) by the Cauchy–Schwarz inequality." Here hubDir A is the direction t_S. 

### `prop_flat_rate_lengths`

 "Leading every end to the hub of its side gives total length at most N − (4/81)k", with hubs ±o of length 2/(9√k). 

### `ratePos`

 The place of an end: (a, b), a < b, at ½e_a and (b, a) at −½e_a. 

### `hubPt`

 The hubs of the sets as parties. 

### `prop_flat_rate_pushforward`

 "The push-forward of a unit tensor on all ends is that on the set of their positions." 

### `rate_numbers14`

 The last step of Proposition prop:flat-rate: "this gives even ℓk^(3/2)/14". 

### `SomeSetPays`

 What Lemma lem:few gives: for some balanced set the choice costs k times the price of the unit tensor on all
ends, and the set what its hubs cost. 

### `rate_of_someSetPays`

 The steps "Ends", "Hubs" and "Comparison" of the proof of Proposition prop:flat-rate, given what the lemma on sums
with few terms says. 

### `balEnum`

 A finite numbering of the balanced sets, for Lemma lem:few. 

### `someSetPays_of_few`

 From the bound of the lemma on sums with few terms, with J ≤ 2^k, to the inequality for one set. 

### `fklTen_onEnds`

 The tensor of f_{k,ℓ}, pushed to the parties, is a tensor on the ends. 

### `prop_flat_rate`

 **Paper: Proposition prop:flat-rate.** "In the flat case, for k ≥ 2 and ℓ ≥ 100√k every circuit over k for f_{k,ℓ}
has at least 2^(ℓk^(3/2)/16) gates." 

### `prop_flat_rate_printed`

 **Paper: Proposition prop:flat-rate**, for f_{k,ℓ} with exactly the printed variables. 

### `exists_cube_root`

 The largest cube with 200 r³ ≤ B. 

### `rate_of_projection`

 The proof of Theorem thm:flat-rate for anything that gives circuits for f_{k,ℓ} with five times as many gates
once m ≥ κk³ℓ2^(kℓ): r is largest with 200r³ ≤ ⌊log m⌋, k = r², ℓ = 100r. 

### `thm_flat_rate`

 **Paper: Theorem thm:flat-rate.** "In the flat case there is m₀ such that for m ≥ m₀ every circuit over k for PERM_m
has more than 2^((log m)^(4/3)/1600²) gates." 

### `flat_rate_complete`

 Theorem thm:flat-rate for every family that is complete for grid sums ("the factor 3 becomes 40"). 

### `thm_main_calculation`

 "(log m)²/log log m ≥ (log m)^(4/3) for large m", and indeed more than any multiple: the bound of the contracting
case exceeds that of the flat case. 

### `thm_simple`

 **Paper: Theorem thm:simple.** "For every C there is m₀ such that for all m ≥ m₀ no circuit over ℝ with at most m^C
gates computes PERM_m." 

### `vp_subset_vnp.`

 "VP is contained in VNP." 

### `cor_classes`

 **Paper: Corollary cor:classes.** "Over ℝ, VP is a proper subset of VNP." The witness is the permanent: it is in VNP
by Ryser's formula and not in VP by Theorem thm:simple. 

### `thm_main_form`

 m^(c(log m)^(1/3)) = 2^(c(log m)^(4/3)). 

### `thm_main`

 **Paper: Theorem thm:main.** "There are c > 0 and m₀ such that for all m ≥ m₀ every circuit over ℝ that computes
PERM_m has more than m^(c(log m)^(1/3)) gates." 
