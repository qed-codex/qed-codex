---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UniformizationProofs/SubmoduleEqTopOfSupSmulOfIsNilpotent.lean",
  "declarations": [
    "GlobalTheory.AbLaw.veryAmpleBy_of_isNilpotent"
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

## Lifting very ampleness across a nilpotent thickening

[Theorem AG.1439](https://andrewodesky.com/rh/lean/GlobalTheory.AbLaw.veryAmpleBy_of_isNilpotent/)

Let $R,R_0$ be commutative rings and $g:R\twoheadrightarrow R_0$ a surjective homomorphism with nilpotent kernel. Let $f:X\to\operatorname{Spec}R$ and identify $X_0=X\times_R R_0$, with projection $j_0:X_0\to X$ and structure map $f_0$. Let $H$ and $H_0$ be line bundles on $X$ and $X_0$, with a specified isomorphism $w:H_0\simeq j_0^*H$. For $n\ge0$, let $s_0,\ldots,s_n$ be global sections of $H$ and $\bar s_0,\ldots,\bar s_n$ global sections of $H_0$ such that $w(\bar s_i)=j_0^*s_i$ for each $i$. If the $\bar s_i$ define a closed immersion $X_0\hookrightarrow\mathbb P_{R_0}^n$ over $R_0$, then the $s_i$ define a closed immersion $X\hookrightarrow\mathbb P_R^n$ over $R$.
