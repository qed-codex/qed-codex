---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/HeckeFubiniCompatibility/PGrowth.lean",
  "declarations": [
    "PositivityTheory.Rg.BcB.CG.growthOf"
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

## Growth of a convolution eigenfunction

[Theorem AGR.1278](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.BcB.CG.growthOf/)

Assume the basic height properties listed below for every CM number field and every matrix rank. Let $E$ be a CM number field and put $G_n=\mathrm{GL}_n(\mathbb A_E)$, for $n\ge0$. With the number-field local absolute values, define $$q_n(A)=\sum_{v\mid\infty}\log^+\max_{i,j}|A_{ij,v}|_v^2+\sum_{w\nmid\infty}\log^+\max_{i,j}|A_{ij,w}|_w,\qquad \lambda_n(g)=q_n(g)+q_n(g^{-1}),$$ where $\log^+(x)=\max(\log x,0)$, $\log0=0$, and an empty maximum is zero. Define $\lambda_n^{\mathrm{red}}(g)=\inf_{\gamma\in\mathrm{GL}_n(E)}\lambda_n(\gamma g)$.

Let $a,b\ge0$, $G=G_a\times G_b$, and $\Gamma=\mathrm{GL}_a(E)\times\mathrm{GL}_b(E)$. Fix a two-sided invariant measure $\mu$ on $G$ positive on nonempty open sets and locally finite, together with a fundamental domain $\mathcal F$ for $\Gamma$. Let $I$ be finite, $M\ge0$ an integer, $f_i:G\to\mathbb C$ continuous and left $\Gamma$-invariant, and $\Phi_{ij}:G\to\mathbb C$ continuous and compactly supported. Assume that, for each $i$, $$\int_{\mathcal F}\bigl(1+\lambda_a^{\mathrm{red}}(x_1)+\lambda_b^{\mathrm{red}}(x_2)\bigr)^{-2M}|f_i(x)|^2\,d\mu(x)<\infty.$$ If $c\in\mathbb C\setminus\{0\}$ satisfies $$\sum_{j\in I}\int_G\Phi_{ij}(y)f_j(xy)\,d\mu(y)=c f_i(x)\qquad(i\in I,\ x\in G),$$ there are real constants $C,N$ such that $$|f_i(x)|\le C\exp\bigl(N(\lambda_a(x_1)+\lambda_b(x_2))\bigr)\qquad(i\in I,\ x\in G).$$
