---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsContractionIsometricDiscreteSeriesFockStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_contraction_isometric_discreteSeries_fock"
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

## A contraction from a polynomial Fock model to discrete series

[Theorem THETA.1286](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_contraction_isometric_discreteSeries_fock/)

Let $p,q,r,s\ge0$, and fix the source's real group data for signatures $(p,q)$, $(r,s)$, and $(pr+qs,ps+qr)$. Fix its compatible polynomial Fock model $\mathcal P=\mathbb C[Z_{ab}]$ with $(p+q)(r+s)$ variables, Hilbert completion $\mathcal H_F$, and the resulting representation $\omega$ of the first two groups. Let $\pi_1,\pi_2$ be discrete-series data for those groups on Hilbert spaces $\mathcal H_1,\mathcal H_2$, with prescribed Harish–Chandra module embeddings. Suppose there is a continuous complex-bilinear map $T:\mathcal H_1\times\mathcal H_2\to\mathcal H_F$ such that $$\langle T(x,y),T(x',y')\rangle=\langle x,x'\rangle\langle y,y'\rangle,\qquad \omega(g,h)T(x,y)=T(\pi_1(g)x,\pi_2(h)y).$$ There is a map $B:\mathcal P\times\mathcal H_2\to\mathcal H_1$, complex-linear in its first variable and conjugate-linear in its second, such that:

1. For every $P\in\mathcal P$ there is $c_P\in\mathbb R$ with $\|B(P,y)\|\le c_P\|y\|$ for every $y$.
2. Every $B(P,y)$ lies in the image of the prescribed Harish–Chandra module of $\pi_1$, and for every $y\ne0$ some $P$ has $B(P,y)\ne0$.
3. Writing $d\omega_1,d\omega_2$ for the polynomial Fock Lie actions, one has, for $X\in\mathfrak u(p,q)$ and $Y\in\mathfrak u(r,s)$, $$\left.\frac{d}{dt}\right|_{t=0}\pi_1(\exp(tX))B(P,y)=B(d\omega_1(X)P,y),$$ $$\left.\frac{d}{dt}\right|_{t=0}B(P,\pi_2(\exp(tY))y)=-B(d\omega_2(Y)P,y).$$
