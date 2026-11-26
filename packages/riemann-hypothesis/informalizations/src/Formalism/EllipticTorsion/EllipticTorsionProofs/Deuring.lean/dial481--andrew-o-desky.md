---
{
  "module": "src/Formalism/EllipticTorsion/EllipticTorsionProofs/Deuring.lean",
  "declarations": [
    "Formalism.ELL.deuring_model"
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

## A Deuring model with unit discriminant

[Theorem AV.0637](https://andrewodesky.com/rh/lean/Formalism.ELL.deuring_model/)

Let $K$ be an algebraically closed ultrametric normed field with $|3|=1$. For every $j\in K$ with $|j|\le1$, there is $a\in K$ with $|a|\le1$ such that the Weierstrass curve $$E_a:\quad y^2+axy+y=x^3$$ satisfies $$c_4(E_a)^3=j\Delta(E_a),\qquad |\Delta(E_a)|=1.$$
