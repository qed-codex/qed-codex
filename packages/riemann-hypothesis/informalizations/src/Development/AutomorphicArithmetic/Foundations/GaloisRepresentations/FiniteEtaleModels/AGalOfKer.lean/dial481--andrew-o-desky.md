---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/FiniteEtaleModels/AGalOfKer.lean",
  "declarations": [
    "UpperTheory.Gal.FiniteEtaleModels.galOfKer_holds"
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

## A split finite kernel gives a Galois cover of abelian schemes

[Theorem AV.1603](https://andrewodesky.com/rh/lean/UpperTheory.Gal.FiniteEtaleModels.galOfKer_holds/)

Let $S$ be a scheme and $A,B$ commutative group schemes that are abelian schemes over $S$. Let $\psi:A\to B$ and $\psi':B\to A$ be group homomorphisms and $\kappa\ge0$ satisfy $$\psi'\circ\psi=[\kappa]_A,\qquad\psi\circ\psi'=[\kappa]_B,$$ and assume $\kappa$ is a unit in $\Gamma(S,\mathcal O_S)$. Let $H\subseteq A(S)$ be a finite subgroup contained in $\ker\psi$. Suppose that for every algebraically closed field $\Omega$ and every $z:\operatorname{Spec}\Omega\to S$, evaluation $H\to A(\Omega)$ is injective and its image is exactly $\ker(\psi:A(\Omega)\to B(\Omega))$. Then $\psi$ is a Galois cover with group $H$ acting by translations.
