---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/PlaceJacHolds.lean",
  "declarations": [
    "PI.AprimeInfW.placeJac_holds"
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

## A Jacobian for a unitary orbit and its Hermitian normal space

[Theorem ALG.0903](https://andrewodesky.com/rh/lean/PI.AprimeInfW.placeJac_holds/)

Let $n,m\ge0$, let $J=\operatorname{diag}(\epsilon_1,\ldots,\epsilon_n)$ with $\epsilon_i\in\{1,-1\}$, and let $S\subseteq\{1,\ldots,n\}$ satisfy $n=m+|S|$. Let $w\in\operatorname{Mat}_{n\times m}(\mathbb C)$ have zero rows at $S$, and put $B=w^*Jw$; assume $\det B\ne0$. For finite sets $I,H$, choose real-linear parametrizations $$L:\mathbb R^I\longrightarrow\mathfrak l,\qquad A:\mathbb R^H\longrightarrow\operatorname{Herm}_m(\mathbb C),$$ onto the indicated spaces and preserving the squared Frobenius norm, where $$\mathfrak l=\{X:X^*J+JX=0,\ X_{ij}=0\ (i,j\in S)\}.$$ The real-linear map $$T(x,t)=L(x)w+\tfrac12wB^{-1}A(t)$$ satisfies $$T_*(dx\,dt)=\frac{2^{nm}}{|\det B|^{|S|}}\,dY.$$
