---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/PadicValuationThetaKernelJetBoundStatement.lean",
  "declarations": [
    "GlobalTheory.T.padicValuation_thetaKernelJet_bound"
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

## A p-adic bound for translated theta jets

[Theorem PHT.1230](https://andrewodesky.com/rh/lean/GlobalTheory.T.padicValuation_thetaKernelJet_bound/)

Fix the source's arithmetic CM datum and its complete theta-kernel input package. Let $E$ be its CM field, let $d_0$ be its distinguished quadratic integer and $\operatorname{rd}_E$ its root discriminant. Let $S$ be a finite set of rational primes and let $b_p\ge0$ vanish outside $S$, with $$\sum_{p\in S}b_p\log p\le\log\operatorname{rd}_E.$$ Assume the coordinate-expansion package: every designated coordinate vector has, at every $p$-adic embedding, a finite expansion in integral lattice matrices with coefficients of norm at most $p^{b_p}$.

Choose a discriminant twelfth root $\delta$ for the designated elliptic curve with unit ideal, and a point $t_0\in\mathbb C$ on its period lattice $\Lambda$ with $$2t_0\in\Lambda,\qquad \frac{1\pm i\sqrt{d_0}}2t_0\notin\Lambda.$$ Let $Q>0$ have only split prime divisors. Fix a theta-pair datum with ranks $a\le d$, $d$ even, weight multiplicities $n_\tau$, vacuum, Weil action, and level-$Q$ finite theta expansion. Let $g,g'$ lie in its rank-$a$ and rank-$d$ adelic groups, and let $u$ be an integral rank-$d$ element. For a prime $p$, suppose $g$ and $g'u$ have trivial components above $p$. For every embedding $\lambda:\overline{\mathbb Q}\hookrightarrow\mathbb C_p$ and every differential-minor index $T$, the translated theta jet $c_T=(P_T(\partial)\,\omega(g,g')F)(0)$ is algebraic and $$|\lambda(c_T)|_p\le p^{a(\sum_\tau n_\tau)(b_p+\tfrac14\mathbf1_{p=d_0}+v_p(Q))+ad\,v_p(Q)}.$$
