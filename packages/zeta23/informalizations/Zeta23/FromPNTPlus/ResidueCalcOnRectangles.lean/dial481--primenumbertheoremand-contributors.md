---
{
  "module": "Zeta23/FromPNTPlus/ResidueCalcOnRectangles.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "PrimeNumberTheoremAnd contributors",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright the PrimeNumberTheoremAnd contributors; Apache License 2.0",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/FromPNTPlus/ResidueCalcOnRectangles.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/FromPNTPlus/ResidueCalcOnRectangles.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Ported from https://github.com/AlexKontorovich/PrimeNumberTheoremAnd
at commit 6a380f0c4658c04a420a9eb00b1ed62a1e3fde01 (tag v4.32.2), file
PrimeNumberTheoremAnd/ResidueCalcOnRectangles.lean.
Copyright the PrimeNumberTheoremAnd contributors; Apache License 2.0
(http://www.apache.org/licenses/LICENSE-2.0).
Local modifications: removed the Architect blueprint tooling (import Architect,
blueprint_comment blocks, @[blueprint ...] attributes) and redirected intra-project
imports to Zeta23.FromPNTPlus.*.
Re-ported from the
v4.29.0 port (commit 10e1218932db7e2432aa5881d750acb819e91f19) when the project
moved to Lean v4.32.2 / Mathlib 905b95818eb32af7874a58b427f50c1711a5e96c.
Modified 2026 by Anthropic PBC.
-/
```

### `RectangleIntegral`

 A `RectangleIntegral` of a function `f` is one over a rectangle
  determined by `z` and `w` in `ℂ`. 

### `RectangleIntegral'`

 A `RectangleIntegral'` of a function `f` is one over a rectangle
  determined by `z` and `w` in `ℂ`, divided by `2 * π * I`. 

### `HolomorphicOn`

 A function is `HolomorphicOn` a set if it is complex
  differentiable on that set. 

### `RectangleIntegralHSplit`

 Given `x₀ a x₁ : ℝ`, and `y₀ y₁ : ℝ` and a function
`f : ℂ → ℂ` so that both `(t : ℝ) ↦ f(t + y₀ * I)` and
`(t : ℝ) ↦ f(t + y₁ * I)` are integrable over both
`t ∈ Icc x₀ a` and `t ∈ Icc a x₁`, we have that
`RectangleIntegral f (x₀ + y₀ * I) (x₁ + y₁ * I)` is the sum of
`RectangleIntegral f (x₀ + y₀ * I) (a + y₁ * I)` and
`RectangleIntegral f (a + y₀ * I) (x₁ + y₁ * I)`. 

### `RectanglePullToNhdOfPole`

 Given `f` holomorphic on a rectangle `z` and `w` except at
a point `p`, the integral of `f` over the rectangle with
corners `z` and `w` is the same as the integral of `f` over a
small square centered at `p`. 

 ## Residue calculus: residues, simple poles, and the rectangle residue theorem

The simple-pole `residue`, `sumResiduesIn`, the `HasSimplePolesOn` scaffold, and the rectangle
residue theorem `RectangleIntegral'_eq_sumResiduesIn`. Extracted from `CH2.lean` as general,
reusable contour-integration lemmas (see issue #1537). 

### `HasSimplePolesOn`

 Every pole of `f` in `s` is at most simple: the meromorphic order is `≥ -1` everywhere on `s`
(no poles of order `≤ -2`).

**Temporary scaffold.** The placeholder `residue` below (and Mathlib's current residue-theorem API)
is only correct for simple poles, so this hypothesis is added to Lemma 5.1 / Proposition 5.2 and
their sub-lemmas to make them provable with the present API. It holds in the intended applications
(e.g. `ζ'/ζ`, whose poles are all simple) and is to be removed once Mathlib gains general
higher-order residue support. 

### `residue`

 **Placeholder definition — valid only for simple poles.** The residue of `f` at `z₀`, defined
as the simple-pole limit `lim_{z → z₀} (z - z₀) · f z` (matching the convention of
`Phi_circ.residue` / `Phi_star.residue`). At a point of analyticity this is `0` and at a simple
pole it is the usual residue, but at a higher-order or essential singularity the limit diverges
and this returns a junk value.

A general complex residue (and the residue theorem) is planned for Mathlib but not yet available,
so results stated in terms of this `residue` are likely **not provable in full generality** with
the current API. This is a deliberate stopgap, to be replaced with the robust notion once the
Mathlib residue-theorem API lands. 

### `sumResiduesIn`

 The sum of residues of `f` over a region `S`, as a `tsum` over `S`. Points of analyticity
contribute `0`, so this is effectively the sum over the poles of `f` in `S`; when finitely many
poles lie in `S` the `tsum` equals the finite sum of their residues, regardless of `|S|`. (With
infinitely many poles, summability must be assumed for the value to be meaningful.) 

### `RectangleIntegral'_eq_sumResiduesIn`

 The Residue Theorem on a rectangle for functions with simple poles. 
