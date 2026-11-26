---
{
  "module": "Paper/Gauges.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Gauges.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Gauges.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Tensors, prices and duality": gauges and duality

The subsection "Gauges": Proposition prop:gauge and Theorem thm:duality, with the steps of their proofs. Both proofs are
carried out in the commutative monoid of the classes of tensors (Ov.Duality.Cls) with its covering relation.


### `def_gauge`

 "A gauge on I is a function p ≥ 0 on tensors with p(1) = 1, p(st) ≤ p(s)p(t) and p(s) ≤ ∑ p(t_j) whenever s is covered by
the t_j." 

 The proof of Proposition prop:gauge, for a commutative monoid M with a covering relation D (for us: the classes of
tensors). A gauge on M is a function with Ov.Duality.IsPre; Ov.Duality.Keeps p x y c says that p keeps (x, y, c). 

### `prop_gauge_chain`

 Proof of Proposition prop:gauge: "The gauges below the given one that keep its triples are closed under infima of
chains." The infimum of a chain (or a directed family) of gauges is a gauge below them that keeps every triple which all
of them keep. 

### `prop_gauge_minimal`

 Proof of Proposition prop:gauge: "By Zorn's lemma there is a minimal one, p": a gauge below p₀ that keeps the triples of
p₀, and that is equal to every such gauge below it. 

### `prop_gauge_radius_cover`

 Proof of Proposition prop:gauge, for r(t) = inf p(tⁿ)^(1/n): "If s is covered by t_1, …, t_l, then sⁿ is covered by their
words of length n; grouping these … and bounding p(t_jᵃ) ≤ c_δ (r(t_j) + δ)ᵃ gives r(s) ≤ ∑ r(t_j)." In Lean r(t) is the infimum
of the a > 0 with p(tⁿ) ≤ C·aⁿ for some C and all n (Ov.Duality.IsPre.rad; it is the printed number by prop_gauge_radius_eq),
and the words are bounded by induction on n. 

### `prop_gauge_radius`

 Proof of Proposition prop:gauge: r is a gauge. "Clearly r(1) = 1 and r(st) ≤ r(s)r(t)"; for covers see
prop_gauge_radius_cover. 

### `prop_gauge_radius_le`

 Proof of Proposition prop:gauge: r ≤ p. 

### `prop_gauge_radius_keeps`

 Proof of Proposition prop:gauge: "If p keeps (x, y, c), then p(tⁿxⁿ) ≤ cⁿ p(tⁿyⁿ), so r keeps it." 

### `prop_gauge_radius_root`

 If p((tⁿ)ᵐ) ≤ C·aᵐ for all m, then p(tᵐ) ≤ C′·bᵐ for all m, with bⁿ = a. 

### `prop_gauge_radius_eq`

 Proof of Proposition prop:gauge: "Let r(t) = inf_{n≥1} p(tⁿ)^(1/n)". The number r(t) of the Lean proof, the infimum of the
a > 0 with p(tⁿ) ≤ C·aⁿ for some C and all n, is the printed one. (That r(t) + δ is such an a, Ov.Duality.IsPre.mem_rad_of_lt,
is the printed bound p(tᵃ) ≤ c_δ (r(t) + δ)ᵃ, which the paper takes from Fekete's lemma.) 

### `prop_gauge_radius_pow`

 Proof of Proposition prop:gauge: "r = p, that is, p(tⁿ) = p(t)ⁿ." 

### `prop_gauge_localize`

 Proof of Proposition prop:gauge: "Let f satisfy p(f) > 0 and let p_f(t) = inf p(tfⁿ)/p(f)ⁿ; the sequence is nonincreasing.
It is again such a gauge: p_f(1) = 1, submultiplicativity follows from p(stf^(a+b)) ≤ p(sfᵃ)p(tfᵇ), and the two other
properties pass to the limit." Here p(fⁿ) = p(f)ⁿ is a hypothesis. The statement says of q = p_f what is used: it is a gauge
below p, it keeps what p keeps, and it keeps (1, f, 1/p(f)), that is, p(f)·p_f(t) ≤ p_f(tf). 

### `prop_gauge_monoid`

 Proposition prop:gauge for a commutative monoid with a covering relation: below every gauge p₀ there is a gauge that is
multiplicative and keeps every triple which p₀ keeps. 

### `prop_gauge`

 **Paper: Proposition prop:gauge.** "Below every gauge there is a spectral point that keeps every triple which the
gauge keeps." A gauge is an Ov.PreSpec; it keeps (x, y, c) if p(tx) ≤ c p(ty) for all t. This is prop_gauge_monoid for the
classes of tensors. 

### `thm_duality_gauge`

 Proof of Theorem thm:duality, first half: "Let p(t) be the infimum of the weights of all certificates for t. Certificates
can be multiplied, and can be raised to a common level and added along covers. As the trivial certificate of level 0 gives
p(1) ≤ 1, and copies of 1 give every t a certificate of level 0, the function p is a gauge if p(1) ≥ 1. … Multiplying a
certificate for tC by A_β gives one for tA_β of one level higher and η times the weight; so p keeps (A_β, C, η)." 

### `thm_duality_exchange`

 Proof of Theorem thm:duality: "So p(1) < 1, and 1 has a certificate of some level k and weight below 1. Then k ≥ 1, and
every term has v_j ≠ 0, as it would weigh 1 otherwise: this is a cover of C^k by terms in which at least one C was
exchanged." (The certificate of level k₀ is raised to the level k = k₀ + 1.) 

### `thm_duality_replace`

 Proof of Theorem thm:duality: "In C^N replace C^k by this cover as long as some term contains it. The total weight never
increases, so it stays at most 1, and each final term has fewer than k factors C." 

### `thm_duality_copies`

 Proof of Theorem thm:duality: "Replacing each remaining factor C by a fixed number c of copies of a nonzero A_β": if C is
covered by c copies of a, then Cⁿ is covered by cⁿ copies of aⁿ. 

### `thm_duality_cover`

 Proof of Theorem thm:duality, second half: from a certificate for 1 of level k₀ and weight below 1, and a cover of C by c
copies of some A_β, a cover of C^N by products of N factors. "Hence there are at most η^(-N) terms. Replacing each remaining
factor C by a fixed number c of copies of a nonzero A_β gives at most c^k η^(-N)" terms; the Lean bound has c + 1 for c, and
k = k₀ + 1. 

### `thm_duality`

 **Paper: Theorem thm:duality.** "Let C ≠ 0 and A_1, …, A_r be tensors on I, not all A_β zero, and suppose that
every spectral point satisfies φ(C) ≤ max φ(A_β). Then for every ε > 0 and all large N, the power C^N is covered by at
most 2^(εN) products of N factors from A_1, …, A_r." The family is indexed by any finite type B. 
