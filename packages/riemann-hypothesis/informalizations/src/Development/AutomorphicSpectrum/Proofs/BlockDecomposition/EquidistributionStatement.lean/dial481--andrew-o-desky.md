---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/EquidistributionStatement.lean",
  "declarations": [
    "GlobalTheory.T.equidistribution"
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

## A limit formula for scaled S-integral lattice sums

[Theorem ANT.0267](https://andrewodesky.com/rh/lean/GlobalTheory.T.equidistribution/)

Let $F$ be totally real of degree $d$, let $F_\infty=\prod_{v\mid\infty}F_v$, and let $\theta:\mathbb R\to F_\infty$ be a continuous ring homomorphism. Choose additive Haar measure $\mu_\infty$ for which the embedded $\mathcal O_F$ has a fundamental domain of volume one, and additive Haar measures $\mu_v$ on every $F_v$ with $\mu_v(\mathcal O_v)=1$. Let $I$ be a finite set, $S$ a finite set of finite places, $\varphi:F_\infty^I\to\mathbb R$ continuous of compact support, and $\psi_v:F_v^I\to\mathbb R$ continuous of compact support for $v\in S$. Then, as $\varepsilon\downarrow0$, $$\varepsilon^{d|I|}\sum_{x\in\mathcal O_{F,S}^I}\varphi(\theta(\varepsilon)x_\infty)\prod_{v\in S}\psi_v(x_v) \longrightarrow\left(\int\varphi\,d\mu_\infty^I\right)\prod_{v\in S}\int\psi_v\,d\mu_v^I.$$
