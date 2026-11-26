---
{
  "module": "src/Formalism/LocalToGlobal/Divisibility/RecBridge.lean",
  "declarations": [
    "Formalism.L2.DIV.rhs_le_record"
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

## Numerical height and target comparison

[Theorem ARAK.0176](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.HtNums.le_hu/)

Use the numerical data, size conditions, weight conditions and notation of ([Numerical cancellation of slope and theta heights](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.RecNums.divIneq/)), including $H$, $H_{X,j}$, $M$ and $\mathcal R$.

**Averaged height comparison.** Let $A$ be a nonempty finite set, let $K_{j,s}$ be real numbers for $j\in J$ and $s\in A$, and let $h_P,l\in\mathbb R$. Assume the hypotheses of ([Averaged logarithmic bound for theta kernels](https://andrewodesky.com/rh/lean/Formalism.DivisorInequality.UniformCovolumeTail.stepDiSharp/)), with the same $J,\Sigma,A,r,\nu,\lambda,f,m,N,L,\Lambda,\ell,C_h$ and with its kernel bounds $K_{j,s}$. Assume also the hypotheses of ([Terminal period height with a source-prime saving](https://andrewodesky.com/rh/s/q9-terminal-period-height.html)), with the same $\Sigma,T,a_\rho,a,\Lambda,L,m,f,k,N,S,\eta,b',\ell$, terminal height $h_P$, and bounding constant $C=C_h$. In these two estimates, identify the source-prime constants $C_7=C_T$; distinguish the terminal error constant by writing $C_{\rm ev}$ for its $C_e$.

If $\sum_{j\in J}H_{X,j}\le l$, then $$h_P+\sum_{j\in J}\frac1{|A|}\sum_{s\in A}K_{j,s}-l\le H.$$

**Target comparison.** Let $C_D,C_{\rm abs}\in\mathbb R$ satisfy $$C_D\ge0,\qquad C_D\ge50C_0+10,\qquad C_D\ge60c_e,\qquad C_{\rm abs}\ge1.$$ Then $$\mathcal R\le M+C_D|T|a\Lambda+C_Dm(B_0+N_c)x^{C_{\rm abs}\varepsilon}.$$
