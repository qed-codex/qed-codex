---
{
  "module": "src/Development/WeilBound/CoreStatements/PublishedTheorems/GlobalFiniteness/VanishAll.lean",
  "declarations": [
    "PositivityTheory.Lit1.GFVanish.vanishAll"
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

## Vanishing of global Galois cohomology above degree two

[Theorem GC.1214](https://andrewodesky.com/rh/lean/PositivityTheory.Lit1.GFVanish.vanishAll/)

Let $F$ be a number field with algebraic closure $\Omega$, let $\ell$ be prime, and let $r>0$. Assume $\ell\ne2$ or $F$ is totally complex. Let $S$ be a finite set of finite places of $F$ containing every place above $\ell$, and let $G_{F,S}$ be the Galois group of the maximal extension of $F$ in $\Omega$ unramified outside $S$. Let $M$ be a finite discrete $\mathbb Z/\ell^r\mathbb Z$-module with a continuous $G_{F,S}$-action. Then $$H^n(G_{F,S},M)=0\qquad(n\ge3).$$
