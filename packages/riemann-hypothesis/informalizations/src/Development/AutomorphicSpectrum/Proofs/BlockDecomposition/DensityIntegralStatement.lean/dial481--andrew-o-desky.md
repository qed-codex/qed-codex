---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/DensityIntegralStatement.lean",
  "declarations": [
    "GlobalTheory.T.density_integral"
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

## Integration over compact sets of nonsingular Gram matrices

[Theorem ANT.1126](https://andrewodesky.com/rh/lean/GlobalTheory.T.density_integral/)

Let $E/F$ be a CM extension of number fields with involution $\sigma$, let $J\in M_M(E)$ be nondegenerate Hermitian, and let $n\ge0$. Put $R=F\otimes_{\mathbb Q}\mathbb R$, $V=(R\otimes_FE)^{M\times n}$, and $B=\operatorname{Herm}_n(R\otimes_FE,\sigma)$. Let $q(X)=X^*JX$ and $B^\times=\{S\in B:\det S\text{ is a unit}\}$. Let $\mu,\nu$ be additive Haar measures on $V,B$ and let $m_S$ be measures on $V$ satisfying the source's Gram-fibre package, specified below. Suppose $\varphi:V\to\mathbb C$ is continuous and $\mu$-integrable, is $m_S$-integrable for every $S\in B^\times$, and the function $S\mapsto\int_V\|\varphi\|\,dm_S$ is continuous on $B^\times$. For every compact $C\subseteq B^\times$, $$\int_{q^{-1}(C)}\varphi(X)\,d\mu(X)=\int_C\left(\int_V\varphi(X)\,dm_S(X)\right)d\nu(S).$$
