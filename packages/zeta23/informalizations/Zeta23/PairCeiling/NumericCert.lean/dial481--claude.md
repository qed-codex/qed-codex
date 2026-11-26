---
{
  "module": "Zeta23/PairCeiling/NumericCert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/NumericCert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/NumericCert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/PairCeiling/NumericCert.lean — the NUMERIC CERTIFICATE half of the bandwidth-1 pair-correlation ceiling theorem:
a kernel-checkable fixed-point interval checker for the grid discrepancies of a periodic
configuration, given per-frequency ENCLOSURES of its form factor.

Conventions: N = period = total multiplicity; S(j) (j = 1..N) the form factor at integer
frequency j; the spectral measure puts mass s_j := S(j)/N at x_j := j/N; C(x) := Σ_{x_j ≤ x} s_j (right-continuous step), D := C − x²/2,
E(x) := ∫₀ˣ D.  On the grid:  T_j := Σ_{i≤j} S(i),  U_j := Σ_{i≤j} T_{i−1},
   D(x_j) = T_j/N − j²/(2N²) =: Dright j,   D(x_j⁻) = T_{j−1}/N − j²/(2N²) =: Dleft j,   E(x_j) = U_j/N² − j³/(6N³) =: Egrid j
(E is cellwise ∫_{x_{i−1}}^{x_i}(C(x_{i−1}) − t²/2)dt = T_{i−1}/N² − (i³ − (i−1)³)/(6N³)).  Between atoms D is decreasing, so sup_{(0,1]}|D| is the
grid maximum of |Dleft|, |Dright|, and |E′| = |D| gives sup_{[0,1]}|E| ≤ max_j|Egrid j| + sup|D|/N — those two bridges belong to the analytic
half (Stability.lean); this file delivers the GRID bounds.

THE CERTIFICATE.  Data: N, a scale K, integer enclosures (lo_j, hi_j) meaning lo_j ≤ K·S(j) ≤ hi_j, and rational targets.  `check` runs ONE pass
of exact integer interval arithmetic (only +, ·, max, |·| on ℤ — every quantity is an integer combination of the K·S(j): 2N²K·Dright j =
2N·(K T_j) − j²K, 6N³K·Egrid j = 6N·(K U_j) − j³K) and compares with the targets by cross-multiplication.  `cert_of_check`: if `check d = true`
then FOR EVERY real sequence S inside the enclosures the four families of bounds hold.  The instance files prove `check d = true` with
`decide +kernel` (kernel evaluation; no native_decide, no extra axioms).  What is NOT proved here: that the true form factor of a given
configuration lies in the enclosures — for a concrete law those come from an interval-arithmetic computation outside Lean and are a displayed
hypothesis of the final statement.
-/
```

 ## 1. Real-side grid quantities (shared with the stability lemma) 

### `T`

 T_j := Σ_{i=1}^{j} S(i). 

### `U`

 U_j := Σ_{i=1}^{j} T_{i−1}. 

### `Dright`

 D(x_j) (right limit): C(x_j) − x_j²/2 with C(x_j) = T_j/N. 

### `Dleft`

 D(x_j⁻) (left limit): C(x_{j−1}) − x_j²/2. 

### `Egrid`

 E(x_j) = U_j/N² − j³/(6N³). 

### `D1`

 D(1) and E(1). 

 ## 2. Enclosure hypothesis 

### `EnclOK`

 `EnclOK K S j l`: the list l = [(lo,hi), …] encloses K·S(j+1), K·S(j+2), … in order. 

 ## 3. The integer checker 

### `CertData`

 certificate data: period N, scale K, enclosures for j = 1..N, and rational targets n/d for |D(1)|, |E(1)|, the grid sup of |D| (both
one-sided limits) and the combined 'max_j |E(x_j)| + sup|D|/N'. 

### `St`

 loop state after the first j enclosures: integer bounds for K·T_j, K·U_j, and running maxima
M1 ≥ |2N²K·D(x_i^±)|, M2 ≥ |6N³K·E(x_i)| over i ≤ j; ok = all enclosures were nonempty. 

### `St.init`

 the initial state. 

### `step`

 one step of the interval propagation (written without lets so that `simp only [step]` exposes the fields). 

### `run`

 run the loop over the enclosure list. 

### `check`

 **the checker** (pure integer arithmetic). 

 ## 4. Soundness 

### `abs_le_max_abs`

 a ≤ x ≤ b ⇒ |x| ≤ max |a| |b|. 

### `LoopInv`

 the loop invariant. 

### `scaled_Dright`

 the scaled grid quantities are integer combinations of K·T, K·U (N ≠ 0). 

### `loopInv_step`

 one step preserves the invariant. 

### `step_ok_imp`

 the ok flag only decreases. 

### `loopInv_run`

 the loop preserves the invariant along an enclosed list. 

### `cert_of_check`

 **soundness of the checker.** 
