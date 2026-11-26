---
{
  "module": "src/Formalism/GL3MeanSquares/HookFormulaTorsion/IntegralInverse.lean",
  "declarations": [
    "Formalism.HermitianLattices.ExpSeriesBivariate.integralInverse_statement"
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

## Inversion of formal coordinates over a commutative ring

[Theorem ALG.0435](https://andrewodesky.com/rh/lean/GlobalTheory.ChartInv.exists_isInvPair/)

Let $k$ be a commutative ring, $d\ge0$, and $\varphi=(\varphi_1,\ldots,\varphi_d)\in k[[T_1,\ldots,T_d]]^d$ have zero constant term. If the determinant of its linear coefficient matrix is a unit in $k$, there is $\psi\in k[[T_1,\ldots,T_d]]^d$ with zero constant term such that $$\varphi(\psi(T))=T,\qquad\psi(\varphi(T))=T.$$

In particular, let $K$ be an ultrametric normed field and $I$ a finite set. Let $T_i\in K[[X_j:j\in I]]$ have zero constant term and all coefficients of norm at most $1$. Put $J_{ij}=[X_j]T_i$. If there is $J'\in M_I(K)$ with $$JJ'=1,\qquad\|J'_{ij}\|\le1,$$ then there are series $S_i$, also with zero constant term and all coefficients of norm at most $1$, such that $$T_i(S(X))=X_i,\qquad S_i(T(X))=X_i\qquad(i\in I).$$
