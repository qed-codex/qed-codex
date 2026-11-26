---
{
  "module": "src/Formalism/HermitianLattices/HermitianLatticesProofs/LocDual.lean",
  "declarations": [
    "Formalism.HermitianLatticesTheory.locDual"
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

## Localization and duality for a Hermitian module

[Theorem ALG.1057](https://andrewodesky.com/rh/lean/Formalism.HermitianLatticesTheory.locDual/)

Let $R$ be an integral domain with fraction field $K$, equipped with an involution preserving $R$. Let $V$ be a $K$-vector space and let $h:V\times V\to K$ be Hermitian, conjugate-linear in the first variable. For a finitely generated $R$-submodule $L\subseteq V$, define $$L^\#=\{x\in V:h(y,x)\in R\text{ for every }y\in L\}.$$ For a prime ideal $P\subset R$, put $$S_P=\{s\in R:s\notin P,\ \bar s\notin P\},\qquad R_P^{\mathrm h}=S_P^{-1}R,\qquad L_P^{\mathrm h}=S_P^{-1}L,$$ and $D_P(L)=\{x\in V:h(L,x)\subseteq R_P^{\mathrm h}\}$. Then $$(L^\#)_P^{\mathrm h}=D_P(L),\qquad D_P(L_P^{\mathrm h})=D_P(L).$$ Moreover, $$L^\#=L\quad\Longleftrightarrow\quad D_P(L_P^{\mathrm h})=L_P^{\mathrm h}\text{ for every maximal ideal }P.$$
