---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/ExistsPolyCoeff.lean",
  "declarations": [
    "GlobalTheory.IntegralEndLimit.exists_poly_coeff",
    "GlobalTheory.IntegralEndLimit.integral_of_limit"
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

## Closure of integral formal endomorphisms in their tangent matrices

[Theorem PHT.0723](https://andrewodesky.com/rh/lean/GlobalTheory.IntegralEndLimit.integral_of_limit/)

Let $C$ be a field of characteristic zero, let $v:C\to\mathbb R\cup\{+\infty\}$ be an additive valuation, and let $d\ge0$. Fix a tuple $\ell=(\ell_1,\ldots,\ell_d)\in C[[X_1,\ldots,X_d]]^d$ with constant term zero and linear term $X$. Assume there are series $F_i(X,Y)$ with constant term zero and all coefficients of valuation at least zero such that $$\ell(F(X,Y))=\ell(X)+\ell(Y).$$ Let $A\in M_d(C)$. Suppose that for every $r\in\mathbb R$ there exist $A'\in M_d(C)$ and $\varphi\in C[[X_1,\ldots,X_d]]^d$ with $$v(A_{ij}-A'_{ij})\ge r,\qquad\varphi(0)=0,\qquad v([X^\alpha]\varphi_i)\ge0,\qquad\ell(\varphi(X))=A'\ell(X).$$ Then there exists such an integral tuple $\varphi$ with $\ell(\varphi(X))=A\ell(X)$.

## Formal substitution coefficients depend polynomially on a matrix

[Theorem ALG.0703](https://andrewodesky.com/rh/lean/GlobalTheory.IntegralEndLimit.exists_poly_coeff/)

Let $C$ be a field, $d\ge0$, and let $l_1,\ldots,l_d\in C[[X_1,\ldots,X_d]]$ have zero constant coefficient. Given $f\in C[[X_1,\ldots,X_d]]$ and a multiindex $\alpha\in\mathbb N^d$, there is a polynomial $Q_\alpha\in C[T_{ab}:1\le a,b\le d]$ such that, for every matrix $A\in M_d(C)$, $$[X^\alpha]\,f\left(\sum_b A_{1b}l_b,\ldots,\sum_b A_{db}l_b\right)=Q_\alpha(A).$$
