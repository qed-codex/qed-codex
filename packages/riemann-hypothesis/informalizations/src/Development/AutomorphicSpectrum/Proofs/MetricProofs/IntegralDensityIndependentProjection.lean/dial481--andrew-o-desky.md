---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/MetricProofs/IntegralDensityIndependentProjection.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.Pub.CxPosIndep.cx_posPart_indep"
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

## Projection independence for complex positive sheet integrals

[Theorem AG.1129](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Pub.CxPosIndep.cx_posPart_indep/)

Let $K$ be a nonempty finite set, let $I_k$ be finite sets, and let $Q\subset\mathbb C[z_{k,i}]$ be a multihomogeneous prime such that for each $k$ some $z_{k,i}\notin Q$. Suppose $$\dim\mathbb C[z]/Q=e+|K|.$$ Let $C$ be its complex zero set with every block nonzero, and put $s(z)=(\prod_kz_{k,i_k})_{(i_k)\in\prod_k I_k}$. Let $\Psi,\Psi':\mathbb C^{\prod_k I_k}\to\mathbb C^{e+1}$ be linear and nonzero on every $s(z)$ with $z\in C$. For $1\le j\le e$, choose a smooth function $h_j>0$ on the nonzero-block locus with integer multidegree $a_j\in\mathbb Z^K$: $$h_j((c_kz_{k,i}))=\prod_k|c_k|^{a_{j,k}}h_j(z)\quad(c_k\ne0).$$ Let $g:\mathbb C^{\coprod_k I_k}\to\mathbb R$ be measurable and invariant under these block scalings. For $y\in\mathbb C^e$, sum over $w\in s(C)$ with $\Psi w=(1,y)$. If this projection has a local holomorphic lift $\gamma$ through $w$, let $D_\Psi(y,w)$ be $g(\gamma(y))$ times the density of $\bigwedge_jdd^c\log h_j(\gamma(y))$, where $dd^c=(i/\pi)\partial\bar\partial$; set it to zero when no lift exists. Then $$\int_{\mathbb C^e}\sum_w\max\{D_\Psi(y,w),0\}\,dy=\int_{\mathbb C^e}\sum_w\max\{D_{\Psi'}(y,w),0\}\,dy.$$ Both are extended nonnegative integrals, and each sum uses its own projection's fiber.
