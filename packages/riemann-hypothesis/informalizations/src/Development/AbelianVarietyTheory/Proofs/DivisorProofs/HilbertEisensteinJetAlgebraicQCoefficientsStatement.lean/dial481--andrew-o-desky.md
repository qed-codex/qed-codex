---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/HilbertEisensteinJetAlgebraicQCoefficientsStatement.lean",
  "declarations": [
    "GlobalTheory.T.hilbert_eisenstein_jet_algebraic_q_coefficients"
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

## Algebraic Fourier coefficients of normalized Hilbert Eisenstein jets

[Theorem ANT.1502](https://andrewodesky.com/rh/lean/GlobalTheory.T.hilbert_eisenstein_jet_algebraic_q_coefficients/)

Assume the Eisenstein expansion hypothesis stated below. Let $F$ be totally real of degree $h\ge2$, let $s\ge1$, $k=2s$, and $N>0$, and take an $\mathcal O_F$-submodule $L\subset F^2$ with $N\mathcal O_F^2\subset L\subset\mathcal O_F^2$. Assume there are rational numbers $z_C$ for the ideal classes of $F$ and partial zeta functions $Z_C$, holomorphic away from $1$ and equal to the ideal-class Dirichlet series on $\operatorname{Re}u>1$, with $Z_C(1-k)=z_C$.

For complex vectors $b,a$ indexed by real embeddings and $k\ne2$, let $G_{k,L}(b,a)$ be the unordered sum over nonzero vectors $(x,y)\in L$ modulo $\mathcal O_F^\times$ of $\prod_\sigma(\sigma(x)b_\sigma+\sigma(y)a_\sigma)^{-k}$, if this sum exists. For $k=2$, let $G_{2,L}(b,a)=H(0)$ if there is a function $H$ holomorphic on $\operatorname{Re}u>-1/2$ whose value for every $\operatorname{Re}u>0$ is the unordered sum regularized by the factor $|\prod_\sigma(\sigma(x)b_\sigma+\sigma(y)a_\sigma)|^{-2u}$. In either case set $G_{k,L}(b,a)=0$ if no such value exists. Put $$c_F(k)=((k-1)!)^h|\operatorname{disc}F|^{(k-1)/2},\qquad w=kh+2\sum_\sigma\kappa_\sigma$$ for any multi-index $\kappa_\sigma\ge0$. Let $C:\mathfrak H\to\mathbb C$ have an everywhere convergent expansion $C(\tau)=\sum_{m\ge0}a_m e^{2\pi i m\tau/N}$ with every $a_m$ algebraic over $\mathbb Q$. Define $$H(\tau)=(2\pi i)^{-w}\left.\partial_z^\kappa\left[c_F(k)G_{k,L}\bigl((\tau+z_\sigma(c\tau+t))_\sigma,(1+z_\sigma c)_\sigma\bigr)\right]\right|_{z=0},$$ where $c=(2\pi i)^2C(\tau)$ and $t=-2\pi i$. Then $H$ also has an everywhere convergent expansion $\sum_{m\ge0}b_m e^{2\pi i m\tau/N}$ with all $b_m$ algebraic over $\mathbb Q$.
