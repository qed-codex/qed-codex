---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/WeierstrassTwoTorsion/CompInv.lean",
  "declarations": [
    "Formalism.L2.Th1.A.logSer"
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

## Formal logarithms and Taylor expansions for Weierstrass curves

[Definition / hypothesis PHT.D105](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.A.logSer/)

Let $K$ be a field of characteristic zero and let $W/K$ have Weierstrass equation $$y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6.$$ Let $w_W(T)\in K[[T]]$ be the unique series with $w_W(0)=0$ and $$w_W=T^3+a_1Tw_W+a_2T^2w_W+a_3w_W^2+a_4Tw_W^2+a_6w_W^3.$$ Set $$\omega_W(T)=\left(1-a_1T-a_2T^2-2a_3w_W(T)-2a_4Tw_W(T)-3a_6w_W(T)^2\right)^{-1}.$$ The normalized formal logarithm is $$\mathcal L_W(T)=\int_0^T\omega_W(U)\,dU.$$ It has constant coefficient zero and linear coefficient one.

For a prime $\ell$, let $\mathbb C_\ell$ be the completion of an algebraic closure of $\mathbb Q_\ell$. Take $K=\mathbb C_\ell$, a field isomorphism $\iota:\mathbb C\simeq\mathbb C_\ell$, and a curve $W/K$ as above. For an entire function $f:\mathbb C\to\mathbb C$, define its transported Taylor expansion in the logarithmic coordinate by $$\mathcal T_{\iota,W}(f)(T)=\sum_{n\ge0}\iota\left(\frac{f^{(n)}(0)}{n!}\right)\mathcal L_W(T)^n.$$
