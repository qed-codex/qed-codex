---
{
  "module": "src/Formalism/PadicSubsetSums/StableGradedCounts/ZBrauerNesbittAlg.lean",
  "declarations": [
    "Formalism.IrreducibleCountingLemmas.Z.brauer_nesbitt_algebra"
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

## Characteristic polynomials determine a semisimple algebra module

[Theorem ALG.1159](https://andrewodesky.com/rh/lean/Formalism.IrreducibleCountingLemmas.Z.brauer_nesbitt_algebra/)

Let $k$ be a field and $A$ a $k$-algebra, possibly noncommutative. Let $V,W$ be semisimple left $A$-modules, finite-dimensional over $k$, with compatible $k$-scalar structures. Suppose that for every $a\in A$, its $k$-linear actions on $V$ and $W$ have equal characteristic polynomials. Then $$V\simeq_A W.$$

**Matrix representations.**

Let $k$ be any field, $\Gamma$ a group, $a\ge0$, and $\rho,\rho':\Gamma\to\operatorname{GL}_a(k)$ semisimple representations. If $$\det(TI-\rho(g))=\det(TI-\rho'(g))\qquad(g\in\Gamma),$$ there is $P\in\operatorname{GL}_a(k)$ such that $$\rho'(g)=P^{-1}\rho(g)P\qquad(g\in\Gamma).$$

**Equal traces in characteristic zero.**

Let $k$ be a field of characteristic zero, $\Gamma$ a group, and $r,r':\Gamma\to\mathrm{GL}_n(k)$ semisimple representations, where $n\ge0$. If $$\operatorname{tr}r(g)=\operatorname{tr}r'(g)\qquad(g\in\Gamma),$$ then $r$ and $r'$ are isomorphic over $k$.
