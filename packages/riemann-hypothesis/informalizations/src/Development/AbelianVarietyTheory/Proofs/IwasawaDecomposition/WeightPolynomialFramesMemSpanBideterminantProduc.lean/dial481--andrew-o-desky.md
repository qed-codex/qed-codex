---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/WeightPolynomialFramesMemSpanBideterminantProduc.lean",
  "declarations": [
    "GlobalTheory.Mem.WeightBideterminants.weightPolynomial_mem_span_bideterminantProducts"
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

## Weight polynomials after left multiplication are spanned by products of minors

[Theorem REP.0709](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.WeightBideterminants.weightPolynomial_mem_span_bideterminantProducts/)

Let $K$ be an infinite field, $\phi:K\to L$ a homomorphism to a field, $I$ a finite set, $N\ge0$, and $\nu_\tau:\{1,\ldots,N\}\to\mathbb N$ for $\tau\in I$. Let $Q$ be a polynomial over $K$ in the entries of matrices $(Y_\tau)_{\tau\in I}$ such that, for every family of invertible upper triangular matrices $\beta_\tau$ over $K$, $$Q((Y_\tau\beta_\tau)_\tau)= \left(\prod_{\tau,j}(\beta_\tau)_{jj}^{\nu_\tau(j)}\right)Q((Y_\tau)_\tau).$$ For arbitrary matrices $M_\tau\in M_N(L)$, the function $$(Y_\tau)_\tau\longmapsto(\phi Q)((M_\tau Y_\tau)_\tau)$$ is in the $L$-linear span of functions $\prod_\tau g_\tau(Y_\tau)$ of the following form. For each $\tau$, choose a finite list of sizes $0\le s_{\tau,k}\le N$ and increasing row lists $I_{\tau,k}$ of length $s_{\tau,k}$ with $$\#\{k:s_{\tau,k}\ge j\}=\nu_\tau(j)\qquad(1\le j\le N).$$ Then $$g_\tau(Y)=\prod_k\det Y_{I_{\tau,k},\,\{1,\ldots,s_{\tau,k}\}}.$$
