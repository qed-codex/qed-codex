---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/HilbertEisensteinFourierExpansionSupport.lean",
  "declarations": [
    "GlobalTheory.HilbFam.fourier_with_support"
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

## Integral Fourier coefficients with totally positive support

[Theorem ANT.0648](https://andrewodesky.com/rh/lean/GlobalTheory.HilbFam.fourier_with_support/)

Let $F$ be a totally real number field of degree $d$ and absolute discriminant $D$, let $k\ge0$, and let $\mathfrak a,\mathfrak b$ be nonzero invertible fractional ideals. Put $\omega_{\mathfrak a}=D^{1/2}N\mathfrak a$, $c_k=((k-1)!)^dD^{(k-1)/2}$, and $$q^\xi(z)=\exp\left(2\pi i\sum_{\tau:F\hookrightarrow\mathbb R}\tau(\xi)z_\tau\right).$$ Suppose $G:(\mathbb C)^d\to\mathbb C$ has the product expansion specified below. There are a function $Z:\mathbb C\to\mathbb C$ representing the partial zeta function of $[\mathfrak a]^{-1}$ and coefficients $a_\xi\in\mathbb C$ such that $$a_0=2^{-d}Z(1-k),\qquad a_\xi\in\mathbb Z\quad(\xi\ne0),$$ $$a_\xi\ne0,\ \xi\ne0\ \Longrightarrow\ \xi\in\mathfrak a\mathfrak b\text{ and }\tau(\xi)>0\text{ for every }\tau,$$ and, for every $\operatorname{Im}z_\tau>0$, the family indexed by $F$ is summable with $$\sum_{\xi\in F}a_\xi q^\xi(z)=c_kG(z)/\omega_{\mathfrak a}^{k}.$$
