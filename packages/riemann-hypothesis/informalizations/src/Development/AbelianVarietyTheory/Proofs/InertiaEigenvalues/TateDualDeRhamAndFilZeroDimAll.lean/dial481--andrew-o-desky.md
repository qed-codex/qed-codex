---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TateDualDeRhamAndFilZeroDimAll.lean",
  "declarations": [
    "GlobalTheory.TateDualFil.tateDual"
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

## De Rham Tate duals and their zeroth filtration

[Theorem PHT.1195](https://andrewodesky.com/rh/lean/GlobalTheory.TateDualFil.tateDual/)

Let $\ell$ be prime, $K/\mathbb Q_\ell$ and $L/\mathbb Q_\ell$ finite extensions, and fix local period data identified with Fontaine's period rings as specified in the conventions. Let $V,V'$ be finite-dimensional $L$-linear representations of $G_K$ of equal dimension, and let $m:V\times V'\to L$ be a bilinear pairing nondegenerate in both variables. Suppose $$m(gx,gy)=\chi_\ell(g)m(x,y)\qquad(g\in G_K),$$ where $\chi_\ell$ is the cyclotomic character in these period data. If $V$ is de Rham, then $V'$ is de Rham and $$\dim_L\operatorname{Fil}^0D_{\mathrm{dR}}(V')+ \dim_L\operatorname{Fil}^0D_{\mathrm{dR}}(V)=\dim_LD_{\mathrm{dR}}(V).$$
