---
{
  "module": "src/Development/AutomorphicArithmetic/MeanSquareBounds/Kappa4Loglog.lean",
  "declarations": [
    "QH.kappa4"
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

## Logarithmic derivative from a fixed zero-free rectangle

[Theorem ANT.0166](https://andrewodesky.com/rh/lean/QH.kappa4/)

Fix $0<\varepsilon<1/52$ and a real constant $B>0$. There is $U_0\ge1$ such that for every real $U\ge U_0$, every real $Q$, every integer $N\ge1$ and every nonprincipal complex Dirichlet character $\chi$ modulo $N$, the following implication holds. If $$U^{\varepsilon/6}\le\log Q\le B U^{\varepsilon/5}(\log U)^2,\qquad N\le Q,$$ and $$L(s,\chi)\ne0\qquad(\Re s>399/400,\ |\Im s|\le Q),$$ then $$\left|\frac{L'}{L}(1,\chi)\right|\le4\log U.$$ The threshold $U_0$ depends only on $\varepsilon$ and $B$; primitivity is not assumed.
