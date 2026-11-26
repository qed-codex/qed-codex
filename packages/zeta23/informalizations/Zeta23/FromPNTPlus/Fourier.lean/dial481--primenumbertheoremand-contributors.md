---
{
  "module": "Zeta23/FromPNTPlus/Fourier.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "PrimeNumberTheoremAnd contributors",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright the PrimeNumberTheoremAnd contributors; Apache License 2.0",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/FromPNTPlus/Fourier.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/FromPNTPlus/Fourier.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Ported from https://github.com/AlexKontorovich/PrimeNumberTheoremAnd
at commit 6a380f0c4658c04a420a9eb00b1ed62a1e3fde01 (tag v4.32.2), file
PrimeNumberTheoremAnd/Fourier.lean.
Copyright the PrimeNumberTheoremAnd contributors; Apache License 2.0
(http://www.apache.org/licenses/LICENSE-2.0).
Local modifications: redirected the intra-project import to Zeta23.FromPNTPlus.Sobolev.
Re-ported from the
v4.29.0 port (commit 10e1218932db7e2432aa5881d750acb819e91f19) when the project
moved to Lean v4.32.2 / Mathlib 905b95818eb32af7874a58b427f50c1711a5e96c.
Adjusted for Lean v4.33.0-rc2 / Mathlib 51e6992efd06: `Circle.norm_coe` supplied explicitly to two `simp` calls.
Modified 2026 by Anthropic PBC.
-/
```

### `tendsto_intervalIntegral_zero_of_uniform_norm_bound`

 If, eventually in `T`, the integrand `f T` is bounded on `uIoc lo hi` by `B T`
and `B T * |hi - lo| → 0`, then the interval integral `∫ x in lo..hi, f T x → 0`. 

### `tendsto_const_mul_log_add_two_div_add_two_atTop`

 The decay `K * (log (T + 2) / (T + 2)) → 0` as `T → ∞`, for any constant `K`. 

### `norm_fourier_le_integral_deriv_div`

 Fourier-transform decay from an integrable derivative: for integrable,
differentiable `g` with integrable derivative, `‖𝓕 g w‖ ≤ (∫ ‖deriv g x‖) / (2π·|w|)`. 

### `norm_oscillatory_integral_le_integral_deriv_div`

 The oscillatory-integral form of the decay bound: for `0 < T`,
`‖∫ g y · exp(T·i·y)‖ ≤ (∫ ‖deriv g x‖) / T`. 

### `norm_oscillatory_integral_le_integral_deriv_div_abs`

 The `|T|` variant of the oscillatory-integral decay bound: for `T ≠ 0`,
`‖∫ g y · exp(T·i·y)‖ ≤ (∫ ‖deriv g x‖) / |T|`. 
