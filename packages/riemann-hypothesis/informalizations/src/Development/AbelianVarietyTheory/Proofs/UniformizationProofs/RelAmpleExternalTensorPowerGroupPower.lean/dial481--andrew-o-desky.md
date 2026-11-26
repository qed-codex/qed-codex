---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UniformizationProofs/RelAmpleExternalTensorPowerGroupPower.lean",
  "declarations": [
    "GlobalTheory.Segre.Embeds.box"
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

## Sections giving an embedding on a product

[Theorem AG.1246](https://andrewodesky.com/rh/lean/GlobalTheory.Segre.Embeds.box/)

Let $B$ be an affine scheme, $\pi:Y\to B$ a morphism, and $Y'\to B$ the $j$-fold fibre product of $Y\to B$, with projections $\rho_i$ for $0\le i<j$, where $j\ge0$. Let $L$ be line-bundle gluing data on $Y$, and let $L'$ be line-bundle gluing data on $Y'$ with open charts $U'_k$ covering $Y'$. Suppose each $U'_k$ maps into a specified chart $U_{\alpha(k,i)}$ of $L$ under $\rho_i$, and on overlaps the transition germs of $L'$ are the products of the corresponding pulled-back transition germs of $L$.

Let $(s_i)_{i\in I}$ be sections of $L$ whose nonvanishing loci cover $Y$, such that each such locus is affine and its ring of functions is generated over $\Gamma(B,\mathcal O_B)$ by the ratios $s_h/s_i$. There is a family $(t_\eta)_{\eta\in I^j}$ of sections of $L'$ with the same property over $B$: its nonvanishing loci cover $Y'$, each is affine, and the ratios $t_\xi/t_\eta$ generate its ring of functions over the base ring.
