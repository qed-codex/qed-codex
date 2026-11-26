---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/PlugPairs.lean",
  "declarations": [
    "MainStatements.Tam.Plug.tamagawa_pairs_compatible"
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

## An upper bound for a normalized unitary quotient volume

[Theorem ANT.0076](https://andrewodesky.com/rh/lean/MainStatements.Tam.Plug.tamagawa_number_upper_bound/)

Assume the full published Hodge-bundle theorem package in ([Uniform bounds for generators of integral cusp-form lattices](https://andrewodesky.com/rh/lean/GlobalTheory.T.short_generator_norm_comparison/)). Fix the full CM unitary parameter datum in ([The convergent doubling integral identity](https://andrewodesky.com/rh/lean/GlobalTheory.T.doubling_basicIdentity_unfolding/)), with numerical parameters $f,r,n_V$, level integers $g_0,g_1$, root discriminant $\mathrm{rd}_E$, and logarithmic $L$-value parameter $\delta$. Choose a level-change system with a base point satisfying the source's compatibility package, an index $0\le i<m$ in its list of unitary spaces, and a local level representation $P$ of rank parameter $r$. Let $V_i$ be the associated Hermitian space, $K_i$ the induced finite-level subgroup, and $\mu,\mathcal F$ satisfy the source's measurable-fundamental-domain package for $U(V_i)$ at level $K_i$.

Let $L\in\mathbb R$ satisfy $$frn_V\le e^L,\qquad W_i\le e^{2L}\text{ for every }i,\qquad \log(g_0g_1)\le30L,\qquad\log\mathrm{rd}_E+|\delta|\le2L,$$ where $W_i$ is the sum, over its archimedean weights, of the absolute values of each weight coordinate plus the specified stage shift. If $v(\mathcal F)$ is the real value of $\mu(\mathcal F)$ when finite, and zero when infinite, then $$\log v(\mathcal F)\le fr^2\log(r+3)+119fr^2L.$$ Here $\log0=0$.
