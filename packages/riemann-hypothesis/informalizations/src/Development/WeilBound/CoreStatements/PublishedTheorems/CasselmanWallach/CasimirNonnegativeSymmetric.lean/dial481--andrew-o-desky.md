---
{
  "module": "src/Development/WeilBound/CoreStatements/PublishedTheorems/CasselmanWallach/CasimirNonnegativeSymmetric.lean",
  "declarations": [
    "PositivityTheory.CW.SeminormApproximation.approx"
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

## Simultaneous approximation by compact-finite vectors

[Theorem REP.1531](https://andrewodesky.com/rh/lean/PositivityTheory.CW.SeminormApproximation.approx/)

Fix $n\ge0$, a signature $\varepsilon$, a complex inner-product space $H$, and a family $\sigma:M_n(\mathbb C)\to\operatorname{End}_{\mathrm{cont},\mathbb C}(H)$. Let $H^\infty$ and $H_{K\text{-fin}}$ be its smooth and compact-finite vectors for the unitary group of the diagonal Hermitian form with signature $\varepsilon$. For an ordered word $W$ of real Lie algebra elements, let $D_W$ be the corresponding iterated infinitesimal operator, and put $S_{\mathcal W}(x)=\sum_{W\in\mathcal W}\|D_Wx\|$ for a finite list of words. Assume the following density conditions: compact-finite vectors are smooth, their derivatives remain compact-finite, and for every smooth $y$, finite $\mathcal W$, and $\eta>0$, some compact-finite $v$ has $S_{\mathcal W}(y-v)<\eta$.

Let $E$ be a complex topological vector space whose topology is defined by seminorms $p_i$, $i\ge0$, and let $T:H\to E$ be complex-linear. Suppose each $p_i(Tx)$ on smooth vectors is bounded by $C_iS_{\mathcal W_i}(x)$ for some finite list $\mathcal W_i$ of Lie words and real $C_i$. For every continuous seminorm $Q$ on $E$, Lie word $W$, $y\in H^\infty$ and $\delta>0$, there is $v\in H_{K\text{-fin}}$ with $$Q(T(y-v))\le\delta,\qquad \|y-v\|\le\delta,\qquad \|D_W(y-v)\|\le\delta.$$
