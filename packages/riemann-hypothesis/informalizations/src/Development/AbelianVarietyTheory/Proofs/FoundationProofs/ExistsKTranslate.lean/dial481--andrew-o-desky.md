---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/ExistsKTranslate.lean",
  "declarations": [
    "GlobalTheory.HarmModule.globalize"
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

## Globalizing an irreducible graded Lie module inside a unitary representation

[Theorem REP.0762](https://andrewodesky.com/rh/lean/GlobalTheory.HarmModule.globalize/)

Let $p,q\ge0$ with $p+q\ge1$, let $G$ be the determinant double cover of $U(p,q)$, and let $K$ be the inverse image of $U(p)\times U(q)$. Let $\pi$ be a strongly continuous unitary representation of $G$ on a complex Hilbert space $H$. Let $M$ be a nonzero irreducible complex $\mathfrak{gl}_{p+q}$-module satisfying the compact local-finiteness and rational-weight conditions below, and let $E:M\to H$ be injective and complex-linear.

Assume, for every $Y\in\mathfrak u(p,q)$ and $x\in M$, $$\left.\frac{d}{dt}\pi(\exp_G(tY))Ex\right|_{t=0}=E(Yx).$$ Assume also that for every $Y\in\mathfrak u(p,q)$ and $y\in M$ there are $C\ge0$ and $\rho>0$ such that $$\|E(Y^ky)\|\le C\rho^k k!\qquad(k\ge0).$$ Suppose $c\in\mathbb Q$ and finite-dimensional subspaces $N_m\subseteq M$, $m\ge0$, have linear span $M$ and satisfy $$\sum_{i=1}^pE_{ii}x=(c+m)x\qquad(x\in N_m).$$ Then there are an irreducible strongly continuous unitary representation $\sigma$ on $H_\sigma$, an injective linear map $j:M\to H_\sigma$, and a linear isometry $J:H_\sigma\to H$ such that $j(M)$ is dense and is exactly the $K$-finite subspace, the derived action on $j(M)$ is the given action on $M$, and $$Jj=E,\qquad J\sigma(g)=\pi(g)J\quad(g\in G).$$
