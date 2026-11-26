---
{
  "module": "Paper/Means.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Means.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Means.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Prices are nonpositively curved": means

The subsection "Means". For n = 1, 2, … a function W n is a price on two sheets of ℤ² (the type Bool × ℤ × ℤ) with
W n (P, P+g) ≤ Λ|g| on each sheet. The mean E is Cat.mean, the limit along a fixed free ultrafilter of the means over the
windows; it is linear, positive and invariant under translations (Nc/Cat/Mean.lean).


### `meanLength`

 The paper's ν(g) = (E W(P,P+g)²)^(1/2). 

### `meanLength_eq`

 ν(g) is the square root of the limit along a fixed ultrafilter of the means of W(P, P+g)² over both sheets of the
n-th window. 

### `meanNorm`

 The paper's N(g) = inf ν(Sg)/S over integers S ≥ 1. 

### `meanNorm_le`

 "For upper bounds [on N it is enough to prove them] for one S." 

### `le_meanNorm`

 "For lower bounds [on N] it is enough to prove them for ν(Sg)/S for every S." 

### `lem_means_lip`

 What is used of the prices W n: they are pseudometrics, Lipschitz on each sheet, and satisfy (Q), which is Proposition
prop:crossing. 

### `lem_means_even`

 The text before Lemma lem:means: "By translation invariance and Minkowski's inequality ν is even …" 

### `lem_means_subadditive`

 The text before Lemma lem:means: "… and subadditive". 

### `lem_means_Q`

 The first step of the proof of Lemma lem:means: "By the Cauchy–Schwarz inequality ν satisfies (Q) with the norms of
differences for the distances, p and q the norms of x − v and y − u." 

### `meanLength_len`

 ν is an even subadditive function with (Q). 

### `meanNorm_len`

 N is an even subadditive function with (Q), and homogeneous. 

### `lem_means_limit`

 The definition of N: "N(g) = lim ν(Sg)/S = inf ν(Sg)/S." The limit exists and is the infimum, as ν is subadditive. 

### `lem_means_homogeneous`

 The text before Lemma lem:means: "so N is also homogeneous". 

### `lem_means_seminorm`

 The text before Lemma lem:means: N is even and subadditive, as ν is. With lem_means_homogeneous and meanNorm_nonneg this
makes N a seminorm on ℤ². 

### `lem_means_Q_norm`

 The second step of the proof of Lemma lem:means: "Apply this to eight vectors multiplied by S, divide by S² and let
S → ∞: so does N, with the same τ." 

 ### The proof of Lemma lem:means

The steps after "so does N" use of N only that it is even, subadditive and homogeneous and satisfies (Q). This is
Cat.Len N and Cat.Homog N, and it holds for N = meanNorm W by lem_means_seminorm, lem_means_homogeneous and
lem_means_Q_norm. As in the paper c = a + b, e = a − b, f = N(c), f′ = N(e). 

### `meansDiff`

 "∂p = 2N(p) − N(p−a) − N(p−b)". The paper's ∂′q = 2N(q) − N(q−a) − N(q+b) is the same with −b for b. 

### `meansPt`

 "A_i = Mc + ie". With −b for b this is Me + ic. 

### `meansDelta`

 "δ_i = N(A_i − a) − N(A_i − 2a)". 

### `lem_means_display`

 "Take (x,v,y,u) = (p,−p,q,−q) and (o,o′,w,w′) = (a,−a,b,−b) and divide by 4:
N(p)∂p + N(q)∂′q ≤ τ(N(p)² + N(q)²) + (N(a)² + N(b)²)/(2τ)." 

### `lem_means_identity`

 "∂A_i + ∂(A_i − a) = 2(N(A_i) − N(A_i − c)) + δ_i − δ_{i+1}." This holds for every function N. 

### `lem_means_convex`

 "As t ↦ N(tc + ie) is convex, the first difference on the right is at least f − 2N(ie)/M." Here s stands for ie, and
convexity is used at the integers t ≥ 0: the differences N((t+1)c + s) − N(tc + s) do not decrease. 

### `lem_means_telescope`

 "The δ_i are bounded and telescope": the sum of ∂A_i + ∂(A_i − a) over 0 ≤ i < R is at least
2R(f − 2R·f′/M) − 2N(a). 

### `lem_means_near`

 N(p) = Mf + O(R) at the points p = Mc + ie and p = Mc + ie − a with i < R: the error is at most 2Rκ if N(a), N(e) ≤ κ. 

### `lem_means_estimate`

 "∂ is bounded by N(a) + N(b), so N(p)∂p = Mf∂p + O(R)", and the same for ∂′ at q, with f′. "With τ = 1/(2M)" the
display becomes Mf∂p + Mf′∂′q ≤ M(½(f² + f′²) + N(a)² + N(b)²) + O(R). Here f = N(c), f′ = N(e), the points p, q have
N(p) = Mf + O(R), N(q) = Mf′ + O(R) with errors at most 2Rκ, and the last O(R) is 12Rκ². 

### `means_arith`

 The arithmetic of "averaging over i and dividing by 2M", with M = m², f, f′, n = N(a) at most κ, Q = N(a)² + N(b)². 

### `lem_means_average`

 "With τ = 1/(2M), adding the two inequalities, averaging over i and dividing by 2M gives
f² + f′² ≤ ½(f² + f′²) + N(a)² + N(b)² + O(1/R)", where M = R². Here the inequality is doubled and ½(f² + f′²) is
subtracted, and the O(1/R) becomes 36(N(a) + N(b))²/R. 

### `lem_means_parallelogram_le`

 "Thus N(a+b)² + N(a−b)² ≤ 2N(a)² + 2N(b)²." 

### `lem_means`

 **Paper: Lemma lem:means.** For prices W_n on two sheets of ℤ² with W_n(P,P+g) ≤ Λ|g| for points of one sheet, and
N(g) = lim ν(Sg)/S = inf ν(Sg)/S: "N(a+b)² + N(a−b)² = 2N(a)² + 2N(b)² for all a, b ∈ ℤ²." 

### `lem_means_norm`

 Lemma lem:means for the function N = meanNorm W. 
