---
{
  "module": "Paper/Fan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Fan.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Fan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Prices are nonpositively curved": the proof of Theorem thm:cn

The fan, its four estimates, the claims (i) to (iv) on the seminorm N of the fan, and the end of the proof. The two sheets
are indexed by Bool; x true and x false are the paper's x and v, and θ = 1/T.


### `dist_congr_of_zero`

 Points at distance 0 have the same distances from all points. 

### `dist_chain_le`

 Steps of length at most c add up. 

### `thm_cn_segments`

 New points on segments, by Proposition prop:random: for every q the point (q, j), 0 ≤ j ≤ M, is placed at b q with
probability j/M and otherwise at a q, "with one random number for all". 

 ### The fan 

### `FanPts`

 The points of the fan: the old points, the points γ_i on both sheets, and the points G(i,j) on both sheets. 

### `old`

 An old point. 

### `γ`

 The point γ_i on the sheet b. 

### `G`

 The point G(i,j) on the sheet b. 

### `IsFan`

 The fan for a given n, with θ = 1/T, L_i = |zγ_i| and ρ = 1 − jθ/n²: a price d on the old points, the γ_i and the
G(i,j) that extends w, with the four estimates of the paper,
"|γ_iγ_{i+1}| ≤ D/n², |zG(i,j)| = ρL_i, |G(i,j)G(i,j+1)| ≤ θL_i/n², |G(i,j)G(i+1,j)| ≤ ρD/n²",
and with what the text says on the places: γ_0 is at x (at v on the second sheet), γ_{n²} at m, |G(i,j)γ_i| ≤ (1−ρ)L_i, and
G(n²,j) "has distance 0 from its copy on the other sheet". 

### `thm_cn_fan`

 **The fan** of the proof of Theorem thm:cn. "For a given n add, by Proposition prop:random, points γ_i, 0 ≤ i ≤ n²,
placed at m with probability i/n² and otherwise at x on the first sheet, at v on the second, with one random number for all.
Then, by the same proposition, add points G(i,j), 0 ≤ j ≤ Tn², placed at z with probability j/(Tn²) and otherwise at γ_i,
again with one random number." Then the four estimates hold. 

 ### The fan in the coordinates of the windows 

### `fanPt`

 "For (i,k) ∈ ℤ² on either sheet let P(i,k) = G(i′,j′), where i′ is i clamped to [0,n²] and j′ is i+k+n clamped to
[0,Tn²]". 

### `fanDist`

 "… and let W_n be the pull-back of n² times the distance". 

### `fanLen`

 L_i = |zγ_i|, as a function on the sheets (i is clamped to [0,n²]). 

### `fanPot`

 The distance of P(i,k) from x, respectively v. 

### `z_γ_le`

 "As L_i ≤ D + |zm| …" 

### `fanDist_price`

 W_n is a price on the two sheets. 

### `lipschitz`

 "… we may take Λ = 2D + |zm|." 

### `step_ii`

 A step in the direction (1,−1) "changes i only": it has length at most ρD. 

### `from_z`

 "The distance from z gives" a lower bound for W_n: n²(ρL_i − ρ′L_i′) ≤ W_n(P(i,k), P(i′,k′)). 

### `step_iii`

 A step in the direction (0,1) has length at most θL_i. 

### `fanPot_last`

 "Steps in the direction (1,0) lead to a common end": the two ends have distance 0, so their distances from x and v add
up to at least |xv|. 

### `fanPot_zero`

 The steps in the direction (1,0) start "from a point within O(1/n) of x, respectively v". 

### `thm_cn_iv_step`

 The display of claim (iv): "Let L′ = L_{i+S}, L = L_i; for n ≥ AS the new j is not negative. The distance from z gives
W(P, P + S(1,−1−A)) ≥ |n²ρ(L′ − L) + ASθL′|." Here P = P(i,k), j = i + k + n ≥ AS, ρ = 1 − jθ/n² and θ = 1/T. 

 ### The sequence of fans and its seminorm

Above, fanDist, fanLen and fanPot belong to one fan, for one n. From here on d n is a fan for every n, and fanW (fanWs on one
sheet), fanL and fanP are the corresponding sequences: the paper's W = (W_n), L = (L_i), and the distances from x and v. 

### `fanW`

 The sequence W = (W_n) of the fans d n. (The window for n = 0 is empty; there the fan for n = 1 is used.) 

### `fanWs`

 W on each sheet. 

### `fanL`

 The sequence L = (L_i). 

### `fanP`

 The distances from x, respectively v. 

### `fanΛ₂`

 "Let Λ₂ = E L², over both sheets". 

### `thm_cn_lipschitz`

 "As L_i ≤ D + |zm|, we may take Λ = 2D + |zm|." 

### `thm_cn_Λ₂_le`

 "… so Λ₂ ≤ (D + |zm|)²". 

### `thm_cn_i`

 **Claim (i)** of the proof of Theorem thm:cn: "N(1,0) ≥ D". 

### `thm_cn_ii`

 **Claim (ii)** of the proof of Theorem thm:cn: "N(1,−1)² ≤ D²(1 − θ + θ²)". 

### `thm_cn_iii`

 **Claim (iii)** of the proof of Theorem thm:cn: "N(0,1)² ≤ θ²Λ₂". 

### `thm_cn_iv_bound`

 "n²|L′² − L²| ≤ 2SD(D + |zm|)", for L′ = L_{i+S} and L = L_i. 

### `thm_cn_iv_telescope`

 "n²(L′² − L²) telescopes along i to the mean SΓ", with Γ = |mz|² − ½|xz|² − ½|vz|²: here for S = 1, and only that the mean
is at least Γ, which is what claim (iv) uses. (Cat.mean_steps passes from S = 1 to any S.) 

### `thm_cn_iv_square`

 The next sentence of claim (iv): "Square this, use 2L′(L′ − L) ≥ L′² − L², and note that … 1 − ρ ≤ 2θ … and
n²|L′² − L²| ≤ 2SD(D + |zm|)." So for large n, at the points P = P(i,k) of the window,
W(P, P + S(1,−1−A))² ≥ (ASθ)²L′² + ASθ·n²(L′² − L²) − 4Aθ²S²D(D + |zm|). 

### `thm_cn_iv_mean`

 The end of claim (iv), for ν: "n²(L′² − L²) telescopes along i to the mean SΓ, while … the mean of L′² is Λ₂": so
ν(S(1,−1−A))² ≥ S²(A²θ²Λ₂ + AθΓ − 4Aθ²D(D + |zm|)) for every S. 

### `thm_cn_iv`

 **Claim (iv)** of the proof of Theorem thm:cn: "N(1,−1−A)² ≥ A²θ²Λ₂ + AθΓ − O(Aθ²)", with
Γ = |mz|² − ½|xz|² − ½|vz|² and with 4D(D + |zm|) for the constant in O, which depends on neither A nor θ. ("Divide by S²";
"for lower bounds it is enough to prove them for ν(Sg)/S for every S".) 

### `thm_cn_end`

 **The end** of the proof of Theorem thm:cn. "By Lemma lem:means the second differences of l ↦ N(1,−1−l)² are 2N(0,1)², so
by (iii) ψ(l) = N(1,−1−l)² − l²θ²Λ₂ is concave on l = −1, 0, 1, …, so ψ(A) ≤ ψ(0) + A(ψ(0) − ψ(−1)). Insert (i), (ii), (iv),
divide by A and let A → ∞: θΓ − O(θ²) ≤ D²(−θ + θ²) + θ²Λ₂." 

### `thm_cn`

 **Paper: Theorem thm:cn.** "Let x, v, m, z be points of a price with |xm|, |vm| ≤ D and |xv| = 2D. Then
|zm|² ≤ ½|zx|² + ½|zv|² − D²." 
