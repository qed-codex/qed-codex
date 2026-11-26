---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/CubicalLineBundles/HomDerivDescendsToNumberField.lean",
  "declarations": [
    "GlobalTheory.HomDerivDescent.exists_descent"
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

## Descent of a complex homomorphism of polarized abelian varieties

[Theorem AV.0846](https://andrewodesky.com/rh/lean/GlobalTheory.HomDerivDescent.exists_descent/)

Assume the theta-uniformization package of ([Theta functions for a principally polarized complex abelian variety](https://andrewodesky.com/rh/lean/GlobalTheory.thetaUnifAV_closed/)) and the polarized-base-change package in the conventions below. Let $k\subseteq\mathbb C$ be a number field and let $(A,L_A)$ and $(B,L_B)$ be principally polarized abelian varieties over $k$, with symmetric ample polarization bundles rigidified at zero. Choose complex base-change models $(A_{\mathbb C},L_{A,\mathbb C})$ and $(B_{\mathbb C},L_{B,\mathbb C})$, including their projection maps to $A,B$ and isomorphisms of the pulled-back line bundles.

Every homomorphism of complex group varieties $f_{\mathbb C}:A_{\mathbb C}\to B_{\mathbb C}$ descends over some intermediate field $k\subseteq K\subseteq\mathbb C$ finite over $k$. More precisely, there are polarized base-change models $A_K,B_K$, their projections to $A,B$, compatible projections $A_{\mathbb C}\to A_K$, $B_{\mathbb C}\to B_K$, and a group homomorphism $f_K:A_K\to B_K$. The composite projections agree with the chosen complex projections, and $$\operatorname{pr}_{B_K}\circ f_{\mathbb C}=f_K\circ\operatorname{pr}_{A_K}.$$
