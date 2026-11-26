---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LelongLimitAtBranches.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.Lelong.lelongLimitAtBranches"
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

## Regularized logarithms along local branches

[Theorem AG.0047](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Lelong.lelongLimitAtBranches/)

Let $J,W\subset\mathbb C[x_1,\ldots,x_n]$, with $J$ prime and $\dim\mathbb C[x]/J=d+1$. Set $X=Z(J)$, $Y=Z(W)$, and $\ell(x)=\sum u_jx_j$, where $\ell\notin J$ and $W$ is a minimal prime over $J+(\ell)$. Let $q\in Y$. Let $\gamma_b:B(0,r_b)\subset\mathbb C^{d+1}\to X$, $1\le b\le m$, be injective holomorphic maps with $r_b>0$ and $\gamma_b(0)=q$. Assume that, near $q$, $X\cap\{\ell=0\}\subset Y$, the images of the $\gamma_b$ cover $X$, and $Y$ lies in every image of the slice $t_0=0$. Assume distinct branch images meet only where $\ell=0$.

Suppose $\ell(\gamma_b(t))=t_0^{e_b}H_b(t)$ throughout each ball, where $e_b\ge0$ and $H_b$ is holomorphic and nowhere zero. Suppose there is a linear map $\pi:\mathbb C^n\to\mathbb C^d$ for which the derivative at zero of $t\mapsto(t_0,\pi\gamma_b(t))$ is bijective for every $b$. Let $\phi_1,\ldots,\phi_d$ be real-valued functions smooth on a neighborhood of $X$.

There is a neighborhood $N$ of $q$ such that every real $C^\infty$ compactly supported $f$ with $\operatorname{supp}f\subset N$ satisfies $$\lim_{\varepsilon\downarrow0}\mathcal I_X\!\left(f;\tfrac12\log(|\ell|^2+\varepsilon),\phi_1,\ldots,\phi_d\right) =\left(\sum_{b=1}^m e_b\right)\mathcal I_Y(f;\phi_1,\ldots,\phi_d).$$ Here $\mathcal I_Z(f;\psi_1,\ldots,\psi_k)$ is the source's mixed curvature integral in dimension $k$, formed by summing the smooth sheets of a chosen finite linear projection; its density is $k!(2/\pi)^k$ times the real part of the mixed discriminant of the complex Hessians.
