---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/FrameReading/PJEigB.lean",
  "declarations": [
    "PositivityTheory.Rg.BcB.F.Tail.JB.jEigFin"
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

## Finitely many simultaneous Iwahori eigenparameters

[Theorem REP.1174](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.BcB.F.Tail.JB.jEigFin/)

Let $E$ be a CM number field, $a,b\ge0$, and let $P_a,P_b$ be finite lists of discrete automorphic representations of general linear groups over $E$, of positive constituent ranks summing to $a,b$, together with chosen irreducible finite local components and infinitesimal characters. Let $w$ be a finite place and $\varpi\in E_w^\times$ have valuation one. A second list is equivalent to a given list if a permutation of constituents identifies all finite local isomorphism classes and all infinitesimal-character multisets.

For any lists $P'_a,P'_b$ equivalent to $P_a,P_b$, form their normalized local parabolic products $\pi_a,\pi_b$ at $w$, and let $\rho=\pi_a\boxtimes\pi_b$. Let $I_a,I_b$ be the standard Iwahori subgroups, set $I=I_a\times I_b$, and write $q=\#\kappa(w)$. For strictly decreasing integer tuples $x\in\mathbb Z^a,y\in\mathbb Z^b$, let $T_{x,y}$ act by the double-coset indicator of $(\operatorname{diag}(\varpi^{x_i}),\operatorname{diag}(\varpi^{y_j}))$, with each Iwahori subgroup given volume one. Define $$d_N(x)=q^{\frac12\sum_{i=0}^{N-1}(N-1-2i)x_i}.$$ There exist a finite set $Z\subset(\mathbb C^\times)^a\times(\mathbb C^\times)^b$ and $m\ge0$, depending on the original lists, $w$, and $\varpi$, such that every equivalent pair satisfies $\dim_{\mathbb C}\rho^I\le m$ and the following implication for all $\xi\in(\mathbb C^\times)^a$, $\eta\in(\mathbb C^\times)^b$: if $0\ne v\in\rho^I$ and $$T_{x,y}v=d_a(x)d_b(y)\prod_i\xi_i^{x_i}\prod_j\eta_j^{y_j}v$$ for every such $x,y$, then $(\xi,\eta)\in Z$.
