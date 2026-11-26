---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/LowestKTypeCompressionFormulaOfStrictLowestKType.lean",
  "declarations": [
    "GlobalTheory.Jet.FormGapFree.formulaGap"
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

## A lowest-type coefficient formula under a parameter gap

[Theorem REP.0094](https://andrewodesky.com/rh/lean/GlobalTheory.Jet.FormGapFree.formulaGap/)

Let $n\ge0$, $\epsilon_i\in\{\pm1\}$ for $0\le i<n$, and $G=U(\operatorname{diag}(\epsilon))$ with maximal compact subgroup $K$. Let $\lambda_0>\cdots>\lambda_{n-1}$ with $\lambda_i-(n-1)/2\in\mathbb Z$. Let $\sigma$ on a complex inner product space satisfy the discrete-series conditions of parameter $\lambda$ in ([A nonzero discrete-series coefficient integral gives an intertwiner](https://andrewodesky.com/rh/lean/PositivityTheory.RgHe.LowestKTypeModel.ofInt/)), and let $S$ be its lowest compact-type subspace. Suppose $h\in\mathbb R$ satisfies $$h\le|\lambda_a-\lambda_b|\quad(\epsilon_a\ne\epsilon_b),\qquad120n\,\operatorname{rank}_{\mathbb R}(G)^{3/2}\le h.$$ Let $w\in S$ have norm one and compact-torus weight $\lambda+\rho_n-\rho_c$, with $\rho_n,\rho_c$ as in ([A nonzero discrete-series coefficient integral gives an intertwiner](https://andrewodesky.com/rh/lean/PositivityTheory.RgHe.LowestKTypeModel.ofInt/)). For $0\le i<n$ put $m_i=\lfloor\lambda_i+(n-1)/2-i\rfloor$, set $s_i=m_i-m_{i+1}$ for $i<n-1$ and $s_{n-1}=m_{n-1}$, and define $$\Phi_\lambda(g)=\prod_{i=0}^{n-1}\det(g_{0\le a,b\le i})^{-s_i}.$$ For every $X$ in the noncompact part of the Lie algebra and $u,v\in S$, $$\langle v,\sigma(e^X)u\rangle=\dim_{\mathbb C}S\int_K\Phi_\lambda(k^{-1}e^Xk)\langle v,\sigma(k)w\rangle\langle\sigma(k)w,u\rangle\,dk,$$ where $dk$ is the Haar probability measure on $K$.
