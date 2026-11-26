---
{
  "module": "Zeta23/FromPNTPlus/Mertens.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "PrimeNumberTheoremAnd contributors",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright the PrimeNumberTheoremAnd contributors; Apache License 2.0",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/FromPNTPlus/Mertens.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/FromPNTPlus/Mertens.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Ported from https://github.com/AlexKontorovich/PrimeNumberTheoremAnd
at commit 10e1218932db7e2432aa5881d750acb819e91f19, file
PrimeNumberTheoremAnd/Mertens.lean.
Copyright the PrimeNumberTheoremAnd contributors; Apache License 2.0
(http://www.apache.org/licenses/LICENSE-2.0).
Original authors per that project's blueprint (Euler–Maclaurin and Mertens
sections drawn from Leo Goldmakher, "A quick proof of Mertens' theorem",
https://web.williams.edu/Mathematics/lg5/mertens.pdf).

Declarations ported (source lines 1–371):
  Mertens.sum_Ioc_one_eq_sum_Ioc_zero, Mertens.sum_log_eq, Mertens.sum_log_le,
  Mertens.integral_log_le, Mertens.sum_log_ge, Mertens.sum_log_eq_log_factorial,
  Mertens.sum_log_eq_sum_mangoldt, Mertens.E₁Λ, Mertens.sum_mangoldt_div_eq,
  Mertens.E₁Λ.ge, Mertens.E₁Λ.le, Mertens.sum_mangoldt_div_eq_log,
  Mertens.E₁Λ.bounded'.

Local modifications:
  * the source's `section EulerMaclaurin` (B1 ... sum_eq_integral_add_integral_deriv)
    now lives in Zeta23/FromPNTPlus/EulerMaclaurin.lean (re-ported from upstream
    v4.32.2, where that section was split out of Mertens.lean into its own file),
    imported here;
  * dropped `import Architect` and all `@[blueprint ...]` attributes and
    `blueprint_comment` blocks (blueprint tooling we do not vendor); statement
    text retained as plain docstrings on the main theorems;
  * dropped three root-level helpers unused by the ported region (each is
    referenced only past our truncation point): Filter.EventuallyEq.iff_eventually,
    Real.inv_log_eq_o_one, Real.one_eq_o_log_log — nothing is injected into the
    Real or Filter namespaces by this file;
  * dropped a stray `#check ArithmeticFunction.vonMangoldt_sum`;
  * truncated after E₁Λ.bounded' (everything later — the sorry'd E₁Λ.bounded,
    the prime-form/second/third theorems — is not ported; no sorry enters);
  * added the closing `end Mertens`.
Modified 2026 by Anthropic PBC.
-/
```

### `sum_log_eq`

 For any `x ≥ 1`, `∑ n ≤ x, log n = x log x - ({x} - 1/2) log x - x + 1 + ∫ t in 1..x, ({t} - 1/2)/t`. 

### `sum_log_le`

 For any `x ≥ 1`, `∑ n ≤ x, log n ≤ x log x`. 

### `sum_log_ge`

 For any `x ≥ 1`, `∑ n ≤ x, log n ≥ x log x - 2x`. 

### `sum_log_eq_log_factorial`

 For any `x`, `∑ n ≤ x, log n = log ⌊x⌋!`. 

### `sum_log_eq_sum_mangoldt`

 For any `x`, `∑ n ≤ x, log n = ∑ d ≤ x, Λ(d) ⌊x/d⌋`. 

### `E₁Λ`

 The remainder term in Mertens' first theorem (von Mangoldt form): `E₁Λ x = ∑ d ≤ x, Λ(d)/d - log x`. 

### `E₁Λ.ge`

 For any `x ≥ 1`, `E₁Λ x ≥ -2`. 

### `E₁Λ.le`

 For any `x ≥ 1`, `E₁Λ x ≤ log 4 + 4`. 

### `sum_mangoldt_div_eq_log`

 Mertens' first theorem (von Mangoldt form): for `x ≥ 1`, `|∑ d ≤ x, Λ(d)/d - log x| ≤ log 4 + 4`. 
