---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/CurveCohomologyKilledByFiniteCover.lean",
  "declarations": [
    "UpperTheory.curve_cohomology_killed_by_finite_cover.killAff"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## A finite curve cover kills a class on a nonempty affine open

[Theorem AG.0686](https://andrewodesky.com/rh/lean/UpperTheory.curve_cohomology_killed_by_finite_cover.killAff/)

Assume the étale foundation package below. Let $q>0$, let $\Omega$ be algebraically closed with $q$ invertible in $\Omega$, and let $C/\Omega$ be an integral smooth proper curve. Let $U\subset C$ be a nonempty affine open, $m>0$ and $i$ integers, and $$x\in H^m_{\mathrm{et}}(U,\mathbb Z/q(i)).$$ There exist a curve $C'$ integral, smooth and proper over $\Omega$ and a finite surjective morphism $\gamma:C'\to C$ such that the pullback of $x$ to $\gamma^{-1}U$ vanishes.
