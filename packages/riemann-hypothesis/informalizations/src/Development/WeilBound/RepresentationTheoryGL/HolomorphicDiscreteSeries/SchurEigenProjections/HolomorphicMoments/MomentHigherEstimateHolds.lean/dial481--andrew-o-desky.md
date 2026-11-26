---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/HolomorphicDiscreteSeries/SchurEigenProjections/HolomorphicMoments/MomentHigherEstimateHolds.lean",
  "declarations": [
    "PositivityTheory.UnitaryDecomposition.moment_higher_estimate_holds"
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

## A weighted coefficient moment for a discrete-series restriction

[Theorem REP.0064](https://andrewodesky.com/rh/lean/PositivityTheory.UnitaryDecomposition.moment_higher_estimate_holds/)

Let $n\ge2$ and let $G=U(\varepsilon)$, $G'=U(\varepsilon')$ have ranks $n+1,n$, with $G'$ embedded in $G$ by fixing a designated positive coordinate $z$. Suppose $\varepsilon$ has a negative sign and at least as many positive as negative signs. Let $\pi,\sigma$ satisfy the discrete-series conditions in ([A nonzero discrete-series coefficient integral gives an intertwiner](https://andrewodesky.com/rh/lean/PositivityTheory.RgHe.LowestKTypeModel.ofInt/)) on complex Hilbert spaces $H,H'$, with parameters $\lambda,\mu$ strictly decreasing and integral after shifts by $n/2,(n-1)/2$ respectively. Suppose $|\lambda_i|,|\mu_j|\le B$, and parameter differences across unequal signs in each group are at least $200(n+1)^3$. Let $\nu$ be any Haar measure on $G'$.

Let $P:H\to H'$ be a bounded complex-linear intertwiner with $\|P\|\le1$, let $w\in H'$ satisfy $\|w\|=\|P^*w\|=1$, and put $\xi=P^*w$, $c(h)=\langle w,\sigma(h)w\rangle$. Assume $\kappa>0$, $c\in L^1(G',\nu)$, and $$\int_{G'}\overline{c(h)}\,\overline{c(h^{-1}x)}\,d\nu(h)=\kappa\overline{c(x)}\qquad(x\in G').$$ Assume some smooth $\eta\in H$ has $\langle\eta,\xi\rangle\ne0$ and $$\int_{G'}\overline{c(h)}\langle\eta,\pi(h)a\rangle\,d\nu(h) =\kappa\langle\eta,\xi\rangle\langle\xi,a\rangle\qquad(a\in H).$$ For every unit vector $v$ in the lowest compact-type subspace of $\pi$, $$\int_G\left(\sum_i|(g^{-1})_{iz}|^2\right)|\langle\xi,\pi(g)v\rangle|^2\,dg \le\bigl(8(n+1)B\bigr)^{8(n+1)}\int_G|\langle\xi,\pi(g)v\rangle|^2\,dg.$$ Both displayed nonnegative integrals over $G$ are understood as extended integrals for a fixed Haar measure on $G$.
