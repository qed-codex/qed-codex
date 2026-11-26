---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/SymplecticGSp4/GeAlgTop.lean",
  "declarations": [
    "_private.Development.AutomorphicArithmetic.AutomorphicVarieties.SymplecticGSp4.GeAlgTop.0.UpperTheory.V.GradeZeroInterpolatingElement.geAlg_iff"
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

## Matrix units in the span of a representation

[Theorem ALG.1319](https://andrewodesky.com/rh/lean/_private.Development.AutomorphicArithmetic.AutomorphicVarieties.SymplecticGSp4.GeAlgTop.0.UpperTheory.V.GradeZeroInterpolatingElement.geAlg_iff/)

Let $H$ be a group, $K$ a field, and $\rho:H\to M_4(K)$ a homomorphism of multiplicative monoids. Write $E_{ij}$ for the matrix units and $A=\operatorname{span}_K\{\rho(g):g\in H\}$. Assume $E_{ii}\in A$ for every $i\in\{0,1,2,3\}$. Then, for every $i,j$, $$E_{ij}\in A\quad\Longleftrightarrow\quad\text{there exists }g\in H\text{ with }\rho(g)_{ij}\ne0.$$
