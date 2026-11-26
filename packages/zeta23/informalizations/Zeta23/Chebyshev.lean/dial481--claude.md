---
{
  "module": "Zeta23/Chebyshev.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Chebyshev.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Chebyshev.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Chebyshev.lean — discharge of the Chebyshev-type hypothesis H-cheb.

Paper: "More than two thirds of the zeros of the Riemann zeta function lie on
the critical line", Lemma [lem:cheb], displays [eq:cheb1]–[eq:cheb2]:

  "For x ≥ 2,
     Σ_{n≤x} Λ(n) ≪ x,   Σ_{n≤x} Λ(n)/√n ≤ 3√x  (x ≥ x₀),
     Σ_{n≤x} Λ(n)/(√n log n) ≪ √x/log x,   Σ_{n≤x} Λ(n)² ≪ x log x,    [eq:cheb1]
     Σ_{n≤x} Λ(n)²/n = (log x)²/2 + O(log x),
     Σ_{n≤x} Λ(n)²/n (log x − log n) = (log x)³/6 + O((log x)²).       [eq:cheb2]"

H-cheb is classical [MV07 §2.2].  All sums here run over n ∈ Finset.Ioc 0 ⌊x⌋₊,
matching Mathlib's `Chebyshev.psi`.  The ≪-bounds are stated with explicit
existential constants; the paper's "≤ 3√x eventually" is provided in the robust
∃-constant form (the constant is not load-bearing downstream — [eq:Bdef] only
needs *some* B = l + C√X).

The two [eq:cheb2] asymptotics need Mertens' first theorem
Σ_{n≤x} Λ(n)/n = log x + O(1), which is not in Mathlib; it is supplied by
`mertensFirst` below, via Zeta23/FromPNTPlus/Mertens.lean.

Everything else comes from Mathlib (NumberTheory.Chebyshev ψ-bounds +
elementary induction/splitting arguments).
-/
```

 ## [eq:cheb1], first bound: Σ_{n≤x} Λ(n) ≪ x 

### `sum_vonMangoldt_le`

 [eq:cheb1].1: Σ_{n≤x} Λ(n) ≪ x, with Mathlib's explicit Chebyshev constant. 

 ## [eq:cheb1], second bound: Σ_{n≤x} Λ(n)/√n ≪ √x 

### `abel_sqrt`

 Abel summation specialised to Σ_{n≤x} Λ(n)/√n, in terms of ψ. 

### `integral_tail_bound`

 The tail integral bound: ∫₁ˣ t^{-3/2} ψ(t) dt ≤ log 4·(2√x − 2) + (log x)². 

### `sum_vonMangoldt_div_sqrt_le_precise`

 Precise partial-summation bound: Σ_{n≤x} Λ(n)/√n ≤ 2 log 4·√x + 2 log x + (log x)²/2. 

### `sum_vonMangoldt_div_sqrt_le`

 [eq:cheb1].2, all-x form: Σ_{n≤x} Λ(n)/√n ≤ (2 log 4 + 16)·√x for x ≥ 1. 

### `sum_vonMangoldt_div_sqrt_le_three_explicit`

 [eq:cheb1].2 with the threshold explicit (effective version): the witness of
`sum_vonMangoldt_div_sqrt_le_three` is `x₀ = max 1 ((48/(3 − 2 log 4))⁴)` (≤ 2.0·10⁹). 

### `sum_vonMangoldt_div_sqrt_le_three`

 [eq:cheb1].2, the paper's literal form (∃-version; witness = the explicit threshold above). 

 ## [eq:cheb1], third bound: Σ_{n≤x} Λ(n)/(√n log n) ≪ √x/log x 

### `sum_one_div_sqrt_le`

 Σ_{n≤N} 1/√n ≤ 2√N (elementary induction). 

### `sum_vonMangoldt_div_sqrt_mul_log_le`

 [eq:cheb1].3: Σ_{n≤x} Λ(n)/(√n log n) ≤ C·√x/log x for x ≥ 2.
(The n = 1 summand is 0 in Lean: Λ 1 = 0.) 

 ## [eq:cheb1], fourth bound: Σ_{n≤x} Λ(n)² ≪ x log x 

### `sum_vonMangoldt_sq_le`

 [eq:cheb1].4: Σ_{n≤x} Λ(n)² ≤ (log 4 + 4)·x·log x, from Λ(n) ≤ log n ≤ log x. 

 ## [eq:cheb2]: the two Mertens-type asymptotics

Mertens' first theorem Σ_{n≤x} Λ(n)/n = log x + O(1) is supplied by
`Mertens.sum_mangoldt_div_eq_log` (see
Zeta23/FromPNTPlus/Mertens.lean), so both [eq:cheb2] bounds are unconditional. 

### `mertensFirst`

 Mertens' first theorem (von Mangoldt form): |Σ_{n≤x} Λ(n)/n − log x| ≤ log 4 + 4
for x ≥ 1.  Paper [lem:cheb] cites it as "Mertens' formula"; classical [MV07 §2.2]. 

### `Msum`

 Partial sums of Λ(n)/n, in the Icc form produced by Abel summation. 

### `M2sum`

 Partial sums of Λ(n)²/n, in the Icc form produced by Abel summation. 

### `abel_log_Msum`

 Abel summation with f = log, c n = Λ n / n. 

### `abel_log_M2sum`

 Abel summation with f = log, c n = Λ n ^ 2 / n. 

### `integrableOn_inv_mul_mono`

 Integrability of t⁻¹·M on (1, x] for a monotone nonnegative M. 

### `sum_log_mul_vonMangoldt_div_bound`

 Partial summation step: Σ_{n≤x} log n · Λ(n)/n = (log x)²/2 + O(log x). 

 ### The proper-prime-power defect

[lem:cheb] proof: "Σ_{n≤x} Λ(n)²/n = Σ_{n≤x} Λ(n) log n/n + O(1) (the two differ
only at proper prime powers)".  The defect Σ_{n≤x} Λ(n)(log n − Λ(n))/n is
supported on prime powers pᵏ with k ≥ 2, where its value is (k−1)log²p/pᵏ;
summing over all p, k bounds it by an absolute constant. 

### `log_sq_div_sq_le`

 log²m/m² ≤ 64·(m^{7/4})⁻¹ for m ≥ 2 (via log m ≤ 8·m^{1/8}). 

### `defect_term_le`

 Per-term bound for the defect: (k−1)·log²p/pᵏ ≤ 256·k·2⁻ᵏ·(p^{7/4})⁻¹. 

### `rpow_inv_le_telescope`

 the telescoping step: for 2 ≤ m, (m^{7/4})⁻¹ ≤ 2(1/√(m−1) − 1/√m). 

### `sum_range_rpow_inv_le`

 partial sums with remainder: Σ_{m ≤ N} (m^{7/4})⁻¹ ≤ 3 − 2/√N for N ≥ 1. 

### `tsum_rpow_neg_seven_quarters_le`

 Σ' m⁻⁷ᐟ⁴ ≤ 3. 

### `defect_bounded_explicit`

 The defect sum bounded by the explicit numeral 1537 = 512·3 + 1 (effective version;
uses the √-telescoping bound ζ-style Σ' m^{−7/4} ≤ 3 above). 

### `defect_bounded`

 The defect sum is bounded by an absolute constant (from the explicit bound). 

### `sum_vonMangoldt_sq_div_eq_explicit`

 [eq:cheb2].1 with the constant explicit: C2a = 2(log 4 + 4) + 1537/log 2 (≤ 2230). 

### `sum_vonMangoldt_sq_div_eq`

 [eq:cheb2].1: Σ_{n≤x} Λ(n)²/n = (log x)²/2 + O(log x).
Paper [lem:cheb]: "Σ_{n≤x} Λ(n)²/n = Σ_{n≤x} Λ(n) log n/n + O(1) ..., and partial
summation from Mertens' formula gives Σ_{n≤x} Λ(n) log n/n = ½log²x + O(log x)."
(From the explicit-constant version.) 

### `sum_vonMangoldt_sq_div_mul_log_sub_eq_explicit`

 [eq:cheb2].2 with the constant explicit: C2b = C2a/2 + 1/log 2. 

### `sum_vonMangoldt_sq_div_mul_log_sub_eq`

 [eq:cheb2].2: Σ_{n≤x} (Λ(n)²/n)(log x − log n) = (log x)³/6 + O((log x)²).
Paper [lem:cheb]: "The second formula is ∫₁ˣ (Σ_{n≤t} Λ(n)²/n) dt/t."  (From the explicit-constant version.) 

### `chebyshevMertens`

 The full H-cheb package [lem:cheb], instantiating the
`Zeta23.ChebyshevMertens` hypothesis structure of Hypotheses.lean.  Everything is
unconditional: Mathlib's Chebyshev ψ-bound + Abel summation + the Mertens
theorem (Zeta23/FromPNTPlus/Mertens.lean). 
