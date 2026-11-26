---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/HermitianFormFactor.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.norm_ball_volume_sharp"
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

## Polynomial volume growth for unitary matrix norm balls

[Theorem REP.0416](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.norm_ball_volume_sharp/)

Let $k,r\ge0$, $N=2r+k+1$, and let $H_{k,r}$ be the nondegenerate Hermitian matrix defined in the conventions below with $r$ hyperbolic pairs and a remaining diagonal block $\operatorname{diag}(1,\ldots,1,-1)$ with $k$ positive entries. Put $$G=\{g\in\operatorname{Mat}_N(\mathbb C):g^*H_{k,r}g=H_{k,r}\}.$$ Let $\mu$ be a nonzero Borel measure on the ambient matrix space, supported on $G$, invariant under left and right multiplication by $G$, and finite on compact sets. There is $C\in\mathbb R$ such that for every $R\ge1$, $$\mu\{g:\|g\|_{\mathrm F}\le R\}\le\max\{C R^{2(k+r)(r+1)},0\},$$ where $\|g\|_{\mathrm F}=(\sum_{i,j}|g_{ij}|^2)^{1/2}$.
