---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/GaussSumParity/KummerThetaLogarithms/LubinTateLogIsArtinHasse.lean",
  "declarations": [
    "Formalism.L2.Th1.D.theta_homomorphism"
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

## A formal homomorphism from a prescribed logarithm

[Theorem PHT.0725](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.D.theta_homomorphism/)

Let $K$ be an ultrametric normed field of characteristic zero and let $p$ be prime with $|p|=p^{-1}$. Put $$\ell(T)=\sum_{j\ge0}\frac{T^{p^{2j}}}{p^j}.$$ Let $F(X,Y)$ have zero constant term, coefficients of norm at most $1$, and $\ell(F(X,Y))=\ell(X)+\ell(Y)$. For arbitrary $g_2,g_3,\varepsilon\in K$, let $G$ be the formal group of the Weierstrass equation $y^2=x^3-(g_2/4)x-g_3/4$, with normalized logarithm $l_G(T)=T+\cdots$ and its compositional inverse $e_G$. Put $$\theta(T)=e_G(\varepsilon\ell(T)).$$ Then $$l_G(\theta(T))=\varepsilon\ell(T),\qquad\theta(F(X,Y))=G(\theta(X),\theta(Y)).$$
