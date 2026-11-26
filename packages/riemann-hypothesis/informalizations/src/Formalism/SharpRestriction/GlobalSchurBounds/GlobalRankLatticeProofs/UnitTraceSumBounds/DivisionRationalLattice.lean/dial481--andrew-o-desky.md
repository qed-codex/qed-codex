---
{
  "module": "src/Formalism/SharpRestriction/GlobalSchurBounds/GlobalRankLatticeProofs/UnitTraceSumBounds/DivisionRationalLattice.lean",
  "declarations": [
    "Formalism.MainNotions.Ext.finOrdG_holds"
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

## Finite order in a compact finite-adelic stabilizer of a definite form

[Theorem ANT.0550](https://andrewodesky.com/rh/lean/Formalism.MainNotions.Ext.finOrdG_holds/)

Let $F$ be a totally real number field, let $E/F$ be a number-field extension, let $\sigma:E\to E$ be an $F$-algebra endomorphism, and let $J\in M_k(E)$ satisfy $\sigma(J)^t=J$. Put $h(x,y)=\sigma(x)^tJy$. Assume that for every embedding $v:F\hookrightarrow\mathbb R$, either every nonzero $x\in E^k$ has $h(x,x)\in F$ and $v(h(x,x))>0$, or every such $x$ has $h(x,x)\in F$ and $v(h(x,x))<0$. For an $F$-algebra $R$, put $$G(R)=\{g\in\operatorname{GL}_k(E\otimes_FR):(\sigma\otimes1)(g)^tJg=J\}.$$ Let $U\subseteq G(\mathbb A_{F,f})$ be a subgroup compact in the ambient general linear group, and let $y\in G(\mathbb A_{F,f})$. Every $\gamma\in G(F)$ whose finite adelic image belongs to $yUy^{-1}$ has finite order.
