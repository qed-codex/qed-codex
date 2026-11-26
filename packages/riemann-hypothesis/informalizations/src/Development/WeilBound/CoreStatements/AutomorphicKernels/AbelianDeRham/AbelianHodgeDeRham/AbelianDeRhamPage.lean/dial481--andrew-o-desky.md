---
{
  "module": "src/Development/WeilBound/CoreStatements/AutomorphicKernels/AbelianDeRham/AbelianHodgeDeRham/AbelianDeRhamPage.lean",
  "declarations": [
    "MainStatements.Hodge.Free.abelianDeRhamPage"
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

## The Hodge subbundle and de Rham exact sequence

[Theorem AG.1668](https://andrewodesky.com/rh/lean/MainStatements.Hodge.Free.abelianDeRhamPage/)

Let $R$ be a commutative ring and $A/R$ an abelian scheme smooth of constant relative dimension $g\ge0$. Put $H=H^1_{\mathrm{dR}}(A/R)$ and $F=\operatorname{im}(H^0(A,\Omega^1_{A/R})\to H)$. Cup product induces an isomorphism $$\bigwedge_R^2H\simeq H^2_{\mathrm{dR}}(A/R).$$ The module $H$ is finite projective of constant rank $2g$. Every global relative one-form is closed, its map to $H$ is injective, and $F$ is finite projective of constant rank $g$ with finite projective quotient $H/F$. The natural maps give an exact sequence $$0\longrightarrow F\longrightarrow H\longrightarrow H^1(A,\mathcal O_A)\longrightarrow0.$$ For every commutative $R$-algebra $R'$ and every base-change square $A'=A\times_RR'$, the natural pullbacks induce isomorphisms $$R'\otimes_RH\simeq H^1_{\mathrm{dR}}(A'/R'),\quad R'\otimes_RF\simeq F',\quad R'\otimes_R H^1(A,\mathcal O_A)\simeq H^1(A',\mathcal O_{A'}),$$ where $F'$ is the image of global one-forms on $A'$ in de Rham cohomology.
