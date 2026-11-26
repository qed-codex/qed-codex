---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsMayerVietorisConnectingExact.lean",
  "declarations": [
    "GlobalTheory.EtC.mayerVietoris"
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

## Mayer–Vietoris for simplicial presheaves on the etale site

[Theorem AG.0430](https://andrewodesky.com/rh/lean/GlobalTheory.EtC.mayerVietoris/)

Let $R$ be a commutative ring and $\mathcal F$ a sheaf of $R$-modules on the big etale site of schemes. For a simplicial presheaf $E$, write $H^n(E,\mathcal F)$ for the cohomology obtained from its sheafified free alternating chain complex and an injective resolution of $\mathcal F$.

Let $f:U\to E$ and $g:V\to E$ be monomorphisms of simplicial presheaves. Suppose that in each simplicial degree, the maps from the sheafified free $R$-modules on $U$ and $V$ to that on $E$ are jointly epimorphic. Put $W=U\times_EV$, with projections $p_U,p_V$. There are connecting homomorphisms $$\partial_n:H^n(W,\mathcal F)\to H^{n+1}(E,\mathcal F)\qquad(n\in\mathbb Z)$$ for which $$H^n(E,\mathcal F)\xrightarrow{(f^*,g^*)}H^n(U,\mathcal F)\oplus H^n(V,\mathcal F)\xrightarrow{p_U^*-p_V^*}H^n(W,\mathcal F)\xrightarrow{\partial_n}H^{n+1}(E,\mathcal F)$$ is exact at all three middle positions when continued by $(f^*,g^*)$. These choices are natural: if $p:E\to E'$, $u:U\to U'$, $v:V\to V'$ give commuting squares between two such covers and $w:W\to W'$ is induced, then $$p^*\partial'_n=\partial_n w^*.$$
