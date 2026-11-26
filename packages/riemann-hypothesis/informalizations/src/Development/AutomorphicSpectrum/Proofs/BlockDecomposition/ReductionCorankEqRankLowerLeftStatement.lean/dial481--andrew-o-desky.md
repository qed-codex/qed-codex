---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ReductionCorankEqRankLowerLeftStatement.lean",
  "declarations": [
    "GlobalTheory.T.reduction_corank_eq_rank_lower_left"
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

## A block corank after an integral parabolic reduction

[Theorem ALG.0754](https://andrewodesky.com/rh/lean/GlobalTheory.T.reduction_corank_eq_rank_lower_left/)

Let $O$ be a discrete valuation ring with fraction field $L$, residue field $k$, and uniformizer $\varpi$. Let $n\ge0$ and $\kappa\in\operatorname{GL}_{2n}(O)$. Suppose $a,d\in\operatorname{GL}_n(L)$, $b\in M_n(L)$ and $\kappa'\in\operatorname{GL}_{2n}(O)$ satisfy $$\kappa\begin{pmatrix}1&0\\0&\varpi\,1\end{pmatrix} =\begin{pmatrix}a&b\\0&d\end{pmatrix}\kappa'.$$ Writing bars for reduction modulo the maximal ideal and using $n\times n$ blocks, one has $$n-\operatorname{rank}_k(\overline{\kappa'}_{22}) =\operatorname{rank}_k(\overline\kappa_{21}).$$
