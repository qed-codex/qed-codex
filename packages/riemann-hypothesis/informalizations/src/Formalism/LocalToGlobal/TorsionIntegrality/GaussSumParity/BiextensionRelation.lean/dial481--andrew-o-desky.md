---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/GaussSumParity/BiextensionRelation.lean",
  "declarations": [
    "Formalism.L2.Th1.D.gramExists"
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

## An integral Frobenius-fixed factorization of a hyperbolic Gram matrix

[Theorem PHT.0691](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.D.gramExists/)

Let $K$ be an ultrametric normed field of characteristic zero, $l>2$ a prime, and $\sigma:K\to K$ a ring homomorphism. Assume $$|l|=l^{-1},\qquad |K^\times|\subset\{l^a:a\in\mathbb Z\},\qquad |\sigma(x)-x^l|\le l^{-1}\quad(|x|\le1).$$ Suppose $K$ contains a primitive $(l^2-1)$st root of unity. For every finite set $E$, there is a matrix $C=(c_{kx})$ indexed by $\{0,1\}\times E$ such that $$|c_{kx}|\le1,\qquad \sigma^2(c_{kx})=c_{kx},$$ and $$\sum_k c_{kx}\sigma(c_{kx'})= \begin{cases} 1,&x=(b,e),\ x'=(b',e),\ b\ne b',\\ 0,&\text{otherwise}. \end{cases}$$
