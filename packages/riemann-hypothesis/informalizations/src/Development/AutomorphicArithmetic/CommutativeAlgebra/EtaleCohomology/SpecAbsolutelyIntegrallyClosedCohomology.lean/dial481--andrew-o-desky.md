---
{
  "module": "src/Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/SpecAbsolutelyIntegrallyClosedCohomology.lean",
  "declarations": [
    "UpperTheory.Et.E2.n59",
    "UpperTheory.Et.E2.n72",
    "UpperTheory.Et.E2.secIso"
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

## A connected finite algebra over a Henselian local ring is local

[Theorem ALG.0204](https://andrewodesky.com/rh/lean/UpperTheory.Et.E2.n59/)

Let $A$ be a commutative Henselian local ring and $B$ a commutative $A$-algebra finite as an $A$-module. If $\operatorname{Spec}B$ is nonempty and connected, then $B$ is a local ring.

## An Artin-Rees intersection bound over a local ring

[Theorem ALG.0829](https://andrewodesky.com/rh/lean/UpperTheory.Et.E2.n72/)

Let $(A,\mathfrak m)$ be a Noetherian local commutative ring, let $M$ be an $A$-module, and let $N,P\subseteq M$ be submodules with $N$ finitely generated. There is an integer $k\ge1$ such that $$\mathfrak m^kN\cap P\subseteq\mathfrak mP.$$

## Natural trivializations of Tate twists from a primitive root

[Theorem AG.0304](https://andrewodesky.com/rh/lean/UpperTheory.Et.E2.secIso/)

Let $q\ge0$, $i\in\mathbb Z$, and $S$ be a scheme with $\zeta\in\Gamma(S,\mathcal O_S)$ such that $q$ is invertible and $\Phi_q(\zeta)=0$. For each $S$-scheme $X$, there is an additive isomorphism $$e_X:\operatorname{LC}(X,\mathbb Z/q\mathbb Z)\simeq H^0_{\mathrm{et}}(X,\mathbb Z/q\mathbb Z(i)),$$ natural in $X$: for every $S$-morphism $f:Y\to X$ and locally constant $g$, $$f^*(e_X(g))=e_Y(g\circ f).$$
