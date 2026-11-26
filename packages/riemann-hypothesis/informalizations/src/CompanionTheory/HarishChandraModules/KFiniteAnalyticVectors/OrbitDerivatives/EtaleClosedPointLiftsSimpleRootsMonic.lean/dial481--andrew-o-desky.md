---
{
  "module": "src/CompanionTheory/HarishChandraModules/KFiniteAnalyticVectors/OrbitDerivatives/EtaleClosedPointLiftsSimpleRootsMonic.lean",
  "declarations": [
    "CompanionTheory.D.gk.FinalFormK.dense_sm'"
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

## Density of smooth vectors for a matrix-group representation

[Theorem REP.1407](https://andrewodesky.com/rh/lean/CompanionTheory.D.gk.FinalFormK.dense_sm'/)

Let $G\subset\mathrm{GL}_n(\mathbb C)$ be closed in $M_n(\mathbb C)$. Assume there is a continuous real-linear map $\theta:M_n(\mathbb C)\to M_n(\mathbb C)$ with $\theta(g)=g^{-1}$ for every $g\in G$. Let $H$ be a complex Hilbert space, and let $\sigma:M_n(\mathbb C)\to\operatorname{End}_{\mathbb C}^{\mathrm{cont}}(H)$ restrict to a representation of $G$. Assume $g\mapsto\sigma(g)v$ is continuous on $G$ for every $v\in H$.

The vectors $v$ whose orbit maps are smooth form a dense subset of $H$. Here smoothness means that near each $g\in G$, the orbit map agrees on $G$ with a smooth map defined on an open subset of the real vector space $M_n(\mathbb C)$.
