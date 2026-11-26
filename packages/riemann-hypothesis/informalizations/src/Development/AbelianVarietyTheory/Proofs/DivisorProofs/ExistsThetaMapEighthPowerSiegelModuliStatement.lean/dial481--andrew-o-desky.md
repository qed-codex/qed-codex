---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsThetaMapEighthPowerSiegelModuliStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_thetaMap_eighthPower_siegelModuli"
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

## A symmetric theta-coordinate map on Siegel moduli

[Theorem AV.1446](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_thetaMap_eighthPower_siegelModuli/)

Let $g\ge1$ and let $n\ge3$ be odd. Put $R=\mathbb Z[\zeta_n,1/n]\subset\mathbb C$, with a chosen primitive root $\zeta_n$. Let $F$ be a Siegel moduli family of dimension $g$ and level $n$ over $R$, with the full family conditions of ([A polarized eightfold power over a Siegel moduli family](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_polarised_E8ThetaPower_over_moduli/)) and base $X$. Let $W\in M_8(\mathbb Z)$ satisfy $$(W+W^t)\text{ is positive definite over }\mathbb R,\qquad\det(W+W^t)=1.$$ Let $(A,L)$ be a polarized abelian scheme over $X$ of relative dimension $8g$, with the following full polarization package: $L$ is symmetric, rigidified and relatively ample, and a translation whose difference line bundle is locally trivial on the base is the identity section. Fix a generating rigidification of $L$ at its identity. Assume the full product-polarization condition of ([A polarized eightfold power over a Siegel moduli family](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_polarised_E8ThetaPower_over_moduli/)): after identifying the Siegel family over $X$, the group scheme $A$ is its eighth power, with projections and line bundle isomorphism prescribed by the Poincare pairing and the coefficients $W_{ab}$. Let $m\ge3$ be odd and a unit in $R$.

There exist $N\ge0$ and an $R$-morphism $f:X\to\mathbb P_R^N$ such that $$N+1=m^{32g}.$$ Put $M=m^{32g}$. At every field-valued point of $X$, whenever $c_1,\ldots,c_M$ are the normalized theta values from a generating theta section and a complete, nonrepeating list of the $m^2$-torsion points in the rigidified theta construction specified in the conventions below, the projective coordinates of $f$ are $$\left[e_1(c)^{M!}:e_2(c)^{M!/2}:\cdots:e_M(c)^{M!/M}\right],$$ where $e_j$ is the $j$th elementary symmetric polynomial. Completeness of a torsion list is required after every extension to an algebraically closed field.
