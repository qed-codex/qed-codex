---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SegreChartIntegralHolds.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.SegreChart.Chart.AreaFormulaInjSet",
    "GlobalTheory.CompanionTheory.Ar.SegreChart.Chart.PtsPosPartProjIndep"
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

## The Hausdorff area formula for an injective restriction

[Theorem AG.0810](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.SegreChart.Chart.AreaFormulaInjSet/)

Let $E,F$ be finite-dimensional real inner product spaces with their Borel measurable structures, and put $k=\dim_{\mathbb R}E$. Let $U\subseteq E$ be open, $f:E\to F$ be continuously differentiable on $U$, and $A\subseteq U$ measurable. If $f$ is injective on $A$, then $$\mathcal H^k(f(A))=\int_A J_k(Df_x)\,d\mathcal H^k(x).$$

## Independence of positive sheet integrals from projection

[Theorem ARAK.1723](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.SegreChart.Chart.PtsPosPartProjIndep/)

Let $K$ be a nonempty finite set, $(I_k)$ finite coordinate sets, and $P\subseteq\mathbb Z[x_{k,i}]$ a relevant multihomogeneous prime with $P\cap\mathbb Z=0$ and $$\dim\mathbb Z[x]/P=e+1+|K|.$$ Let $C_P$ be the complex zero set with every coordinate block nonzero, and let $s(z)=(\prod_kz_{k,i_k})_{(i_k)}$ be its Segre coordinates. Let $\Psi,\Psi':\mathbb C^{\prod_k I_k}\to\mathbb C^{e+1}$ be linear, both nonzero on $s(C_P)$.

Choose smooth positive Hermitian metric functions $h_1,\ldots,h_e$ on the nonzero-block locus: for integer multidegrees $a_j\in\mathbb Z^K$ they satisfy $h_j(cz)=\prod_k|c_k|^{a_{j,k}}h_j(z)$ under nonzero block scalings. Let $g$ be a measurable real function on the coordinate space invariant under all these scalings.

For $y\in\mathbb C^e$, sum over $w\in s(C_P)$ with $\Psi w=(1,y)$. On a local holomorphic lift $\gamma$ of this projection through $w$, let $D_\Psi(y,w)$ be $g(\gamma(y))$ times the Lebesgue density of $\bigwedge_{j=1}^e dd^c\log h_j(\gamma(t))$, with $dd^c=(i/\pi)\partial\bar\partial$; set this value to zero where no local lift exists. Define $D_{\Psi'}$ in the same way. Then, as extended nonnegative integrals, $$\int_{\mathbb C^e}\sum_w\max\{D_\Psi(y,w),0\}\,dy =\int_{\mathbb C^e}\sum_w\max\{D_{\Psi'}(y,w),0\}\,dy.$$ Each sum uses the fiber of its own projection.
