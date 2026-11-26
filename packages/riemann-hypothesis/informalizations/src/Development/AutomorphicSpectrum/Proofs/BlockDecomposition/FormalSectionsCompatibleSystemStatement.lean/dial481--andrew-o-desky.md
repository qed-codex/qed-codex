---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/FormalSectionsCompatibleSystemStatement.lean",
  "declarations": [
    "GlobalTheory.T.formal_sections_compatible_system"
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

## Algebraization preserving sections and their quadratic identities

[Theorem AG.1617](https://andrewodesky.com/rh/lean/GlobalTheory.T.formal_sections_compatible_system/)

Assume the projective formal-effectivity principle: compatible closed subschemes of the reductions of a fixed projective space over any complete Noetherian adic ring arise from a closed subscheme of that projective space. Let $R$ be a Noetherian commutative ring complete for an ideal $I$, and set $R_e=R/I^{e+1}$. Let $Y_e$ be $R_e$-schemes with maps $\beta_e:Y_e\to Y_{e+1}$ identifying $Y_e$ with the reduction of $Y_{e+1}$. Let $L_e$ be line bundles with specified invertible identifications $L_e\simeq\beta_e^*L_{e+1}$. Fix $m\ge0$ and compatible sections $s_{e,0},\ldots,s_{e,m}$ of $L_e$. Suppose the sections for $e=0$ give a relatively very ample closed immersion into $\mathbb P^m_{R_0}$.

There are a proper $R$-scheme $X$, a line bundle $L$, sections $s_0,\ldots,s_m$ giving a relatively very ample closed immersion, and maps $b_e:Y_e\to X$ with invertible identifications $b_e^*L\simeq L_e$, such that $$Y_e\simeq X\times_R R_e,\qquad b_{e+1}\beta_e=b_e,\qquad b_e^*s_i=s_{e,i}.$$ Moreover, for any $i_1,i_2,i_3,i_4$, if $s_{e,i_1}s_{e,i_2}=s_{e,i_3}s_{e,i_4}$ for every $e$, then $s_{i_1}s_{i_2}=s_{i_3}s_{i_4}$. For any subset $A\subseteq\{0,\ldots,m\}$, if the nonvanishing loci of $(s_{0,i})_{i\in A}$ cover $Y_0$, the nonvanishing loci of $(s_i)_{i\in A}$ cover $X$.
