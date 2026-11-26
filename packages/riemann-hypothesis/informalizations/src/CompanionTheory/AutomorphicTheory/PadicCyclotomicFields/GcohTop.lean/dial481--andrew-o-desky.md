---
{
  "module": "src/CompanionTheory/AutomorphicTheory/PadicCyclotomicFields/GcohTop.lean",
  "declarations": [
    "CompanionTheory.LocalTateOrthogonality.Gcoh.top_locfin",
    "CompanionTheory.LocalTateOrthogonality.Gcoh.top_tate"
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

## Local cohomology finiteness and dimension

[Theorem GC.0131](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_locfin/)

Let $\ell$ be prime, $K/\mathbb Q_\ell$ a finite extension in a fixed algebraic closure, $r>0$, and $M$ a finite discrete $\mathbb Z/\ell^r\mathbb Z$-module with continuous action of $G_K$, the absolute Galois group of $K$. Then $H^i(K,M)$ is finite for $i=0,1,2$, and $$H^i(K,M)=0\qquad(i\ge3).$$

## Local Tate duality

[Theorem GC.0133](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_tate/)

Let $\ell$ be prime, $K/\mathbb Q_\ell$ finite, $r>0$, and $M$ a finite discrete $\mathbb Z/\ell^r\mathbb Z$-module with continuous action of $G_K$, the absolute Galois group of $K$. Put $M^\vee(1)=\operatorname{Hom}_{\mathbb Z/\ell^r\mathbb Z}(M,\mathbb Z/\ell^r\mathbb Z)(1)$, with the contragredient and cyclotomic actions. There is an isomorphism $$H^2(K,\mathbb Z/\ell^r\mathbb Z(1))\simeq\mathbb Z/\ell^r\mathbb Z,$$ and cup products give perfect pairings $$H^i(K,M)\times H^{2-i}(K,M^\vee(1))\longrightarrow H^2(K,\mathbb Z/\ell^r\mathbb Z(1)),\qquad i=0,1,2.$$ Perfectness means that each induced map to the corresponding linear dual is bijective, in both orders also for the degree-one pairing.
