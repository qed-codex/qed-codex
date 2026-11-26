---
{
  "module": "src/Formalism/SizeWindowBrackets/ChainSlopeWindows/TraceConjTransposeMulSelf.lean",
  "declarations": [
    "Formalism.LFunctionChainParameters.HilbertSchmidtNormSquare.compressDiagDefectBound",
    "Formalism.LFunctionChainParameters.HilbertSchmidtNormSquare.compressTraceSquareBound"
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

## Second moments after isometric restriction

[Theorem ALG.1746](https://andrewodesky.com/rh/lean/Formalism.LFunctionChainParameters.HilbertSchmidtNormSquare.compressTraceSquareBound/)

Let $I$ be a finite set, let $D,d_u,r_u$ be nonnegative integers for $u\in I$, and give the complex coordinate spaces their Euclidean norms. Let $$A_u:\mathbb C^{d_u}\longrightarrow\mathbb C^D,\qquad V_u:\mathbb C^{r_u}\longrightarrow\mathbb C^{d_u},\qquad V_u^*V_u=I_{r_u}.$$ Here $T^*$ is the adjoint of a linear map $T$. For nonnegative real weights $\gamma_u$, put $$K_{uu'}=\sqrt{\gamma_u\gamma_{u'}}A_u^*A_{u'},\qquad \widetilde A_u=A_uV_u,\qquad Q=\sum_{u\in I}\gamma_u\widetilde A_u\widetilde A_u^*,$$ $$R_d=\sum_{u\in I}d_u,\qquad R_r=\sum_{u\in I}r_u,\qquad \|T\|_{\rm HS}^2=\operatorname{tr}(T^*T).$$ Let $D_*,\sigma,\eta_0,\eta_1,e_0,\alpha$ be real numbers satisfying $$D_*>0,\qquad0<\sigma\le1/20,\qquad D_*/\sigma\le R_d,$$ $$-1\le\eta_0\le\sigma/2,\qquad\eta_1\le\sigma/2,\qquad e_0\ge0,\qquad\sqrt{e_0}\le\sigma/2,\qquad0\le\alpha\le1/4.$$ Assume $$\|K_{uu'}\|_{\rm HS}^2\le(1+\eta_0)d_ud_{u'}/D_*\quad(u\ne u'),\qquad \|K_{uu}-I_{d_u}\|_{\rm HS}^2\le e_0d_u\quad(u\in I),$$ $$D\le(1+\eta_1)D_*,\qquad \sum_{u\in I}(d_u-r_u)\le\alpha R_d.$$ Then $$R_r\ge(1-\alpha)R_d,$$ $$\sum_{u\in I}\|\gamma_u\widetilde A_u^*\widetilde A_u-I_{r_u}\|_{\rm HS}^2\le2e_0R_r,$$ $$\operatorname{tr}(Q^2)\le(1+5\sigma+3\sqrt\alpha)\frac{(\operatorname{tr}Q)^2}{D}.$$
