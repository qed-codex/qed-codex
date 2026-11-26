---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DeRhamRepresentationTensorComparison.lean",
  "declarations": [
    "GlobalTheory.Per.ExactMult.exact_hodge_add"
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

## Additivity of de Rham filtration dimensions

[Theorem PHT.1210](https://andrewodesky.com/rh/lean/GlobalTheory.Per.ExactMult.exact_hodge_add/)

Let $\ell$ be prime, let $K,L$ be finite extensions of $\mathbb Q_\ell$ in a fixed algebraic closure, and fix the compatible crystalline, de Rham and integral period-ring data of ([De Rham subrepresentations and strict quotient maps](https://andrewodesky.com/rh/lean/GlobalTheory.DRSubQuot.deRham_sub_quot/)). Let $$0\longrightarrow V_0\xrightarrow{\iota}V_1\xrightarrow{\pi}V_2\longrightarrow0$$ be an exact sequence of finite-dimensional $L$-linear $G_K$-representations with equivariant maps. If $V_1$ is de Rham for these data, then $V_0,V_2$ are de Rham. For every $\mathbb Q_\ell$-embedding $\tau:K\hookrightarrow L$ and $a\in\mathbb Z$, $$\dim_L\operatorname{Fil}^aD_{\mathrm{dR},\tau}(V_1)=\dim_L\operatorname{Fil}^aD_{\mathrm{dR},\tau}(V_0)+\dim_L\operatorname{Fil}^aD_{\mathrm{dR},\tau}(V_2),$$ $$\dim_L\operatorname{gr}^aD_{\mathrm{dR},\tau}(V_1)=\dim_L\operatorname{gr}^aD_{\mathrm{dR},\tau}(V_0)+\dim_L\operatorname{gr}^aD_{\mathrm{dR},\tau}(V_2).$$ A jump occurs at $a$ for $V_1$ exactly when it occurs for at least one of $V_0,V_2$.
