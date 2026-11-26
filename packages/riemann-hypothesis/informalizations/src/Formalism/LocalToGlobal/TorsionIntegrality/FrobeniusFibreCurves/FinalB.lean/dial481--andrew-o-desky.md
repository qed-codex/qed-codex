---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/FinalB.lean",
  "declarations": [
    "Formalism.L2.Th1.B.jetsThree"
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

## Integral higher derivatives in a formal logarithmic coordinate

[Theorem PHT.0645](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.B.jetsThree/)

Let $K$ be an ultrametric normed field of characteristic zero. Let $F\in K[[X,Y]]$ have zero constant term and all coefficients of norm at most $1$, and let $\ell\in K[[X]]$ satisfy $$\ell(0)=0,\qquad\ell'(0)=1,\qquad \ell(F(X,Y))=\ell(X)+\ell(Y).$$ For $f\in K[[X]]$, put $$H(X,Y)=f(F(X,Y))-f(X)-f(Y),$$ $$A(X,Y,Z)=H(F(X,Y),Z)-H(X,Z)-H(Y,Z).$$ Assume $A(0,0,0)=0$ and every coefficient of $\exp(A)$ has norm at most $1$. With $D=(\ell')^{-1}\frac{d}{dX}$, one has $$|(D^n f)(0)|\le1\qquad(n\ge3).$$
