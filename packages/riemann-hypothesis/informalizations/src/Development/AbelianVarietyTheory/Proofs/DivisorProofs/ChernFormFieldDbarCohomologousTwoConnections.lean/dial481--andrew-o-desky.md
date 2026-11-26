---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChernFormFieldDbarCohomologousTwoConnections.lean",
  "declarations": [
    "GlobalTheory.ChernCalc.dbarCoh_chernFld"
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

## Chern forms from compatible local matrix families are cohomologous

[Theorem AG.0368](https://andrewodesky.com/rh/lean/GlobalTheory.ChernCalc.dbarCoh_chernFld/)

Let $M$ be a topological space with a holomorphic atlas of complex dimension $n$, and let $G_y(z),G'_y(z)$ be two families of complex $r\times r$ matrices. Assume that for each $y$, both $G_y$ and $G'_y$ are smooth and invertible on a neighborhood of $y$. Assume also that, for every $y$ and every sufficiently nearby $z$, there are matrix functions $T,K,K'$ holomorphic and invertible near $z$ with $$G_z(w)=T(w)G_y(w)K(w)^*,\qquad G'_z(w)=T(w)G'_y(w)K'(w)^*$$ for all $w$ sufficiently close to $z$. For every $j\ge0$, the $j$th Chern-form fields $c_j(G),c_j(G')$ defined below define global $\bar\partial$-closed forms and there is a global form $u$ such that $$c_j(G)-c_j(G')=\bar\partial u.$$
