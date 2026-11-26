---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/LogarithmicSubstitution/DivLaw.lean",
  "declarations": [
    "Formalism.L2.Th1.B.LDiv.div_law"
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

## Integral divisibility from vanishing along a formal inverse

[Theorem PHT.0885](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.B.LDiv.div_law/)

Let $K$ be a characteristic-zero ultrametric normed field. Let $F,G\in K[[X,Y]]$ and $\lambda,\iota\in K[[T]]$ satisfy $$F(0,0)=0,\quad \lambda(0)=0,\quad [T]\lambda=1,\quad \lambda(F(X,Y))=\lambda(X)+\lambda(Y),\qquad \iota(0)=0,\quad \lambda(\iota(T))=-\lambda(T).$$ Suppose every coefficient of $F$, $G$, and $\iota$ has norm at most one. If $G(X,\iota(X))=0$, there is $Q\in K[[X,Y]]$ with every coefficient of norm at most one such that $G=FQ$.
