---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/QuadraticSemicharacters/CayleyGaussianIntegrals/TripleSumEighthOf.lean",
  "declarations": [
    "Formalism.L2.Th1.H.TripleSumEighth_of"
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

## The eighth power of a nonzero triple theta sum is positive

[Theorem ALG.0990](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.H.TripleSumEighth_of/)

Assume the two universal phase and Gauss-sum assertions specified below. Let $V$ be a complex vector space, $H:V\times V\to\mathbb C$ a Hermitian form linear in the first argument, and $E(x,y)=\operatorname{Im}H(x,y)$. Let $\Lambda_1,\Lambda_2,\Lambda_3\subseteq V$ be additive subgroups self-dual for $E$, with all six relative indices finite. Let $\alpha:V\to\mathbb C$ restrict to a sign-valued semicharacter on each $\Lambda_i$: $$\alpha(x)\in\{1,-1\},\qquad\alpha(x+y)=\alpha(x)\alpha(y)e^{\pi iE(x,y)}\qquad(x,y\in\Lambda_i).$$ Choose finite transversals $S_2$ for $\Lambda_2/(\Lambda_1\cap\Lambda_2)$ and $S_3$ for $\Lambda_3/(\Lambda_2\cap\Lambda_3)$, and put $$\psi(z,y)=\alpha(z)\alpha(y)\alpha(z+y)e^{-\pi iE(z,y)},\qquad A=\sum_{z\in S_3}\sum_{\substack{y\in S_2\\z+y\in\Lambda_1}}\psi(z,y).$$ If $A\ne0$, then $A^8$ is a positive real number.
