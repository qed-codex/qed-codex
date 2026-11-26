---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/ExponentialNegativity/TopGap.lean",
  "declarations": [
    "PositivityTheory.Rg.Rs.gap_holds"
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

## A multiplicity inequality for small Satake parameters

[Theorem AGR.0301](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.Rs.gap_holds/)

Let $E$ be a totally complex number field, $N\ge0$, and $V$ a nonzero irreducible translation-stable space of smooth automorphic forms on $\operatorname{GL}_N(\mathbb A_E)$ whose elements are square integrable. Let $w$ be a finite place, $q_w=\#(\mathcal O_E/w)$, and let $B$ be a multiset of nonzero complex numbers. Suppose $V$ has a nonzero spherical vector at $w$, and every nonzero spherical vector in $V$ has Satake multiset $B$. For every $z\in\mathbb C$ with $|z|<q_w^{-1/2}$, $$\operatorname{mult}_{B}(z)\le\operatorname{mult}_{B}(q_wz).$$
