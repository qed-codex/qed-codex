---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/BranchNormalisationHoldsStatement.lean",
  "declarations": [
    "GlobalTheory.T.branch_normalisation_holds"
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

## Normalization of a reduced complex curve germ by its branches

[Theorem AG.1461](https://andrewodesky.com/rh/lean/GlobalTheory.T.branch_normalisation_holds/)

Let $I\subset\mathbb C[x_1,\ldots,x_n]$, $q\in\mathbb C^n$, and let $c_1,\ldots,c_m$ be one-dimensional holomorphic branches of $V(I)$ at $q$, as defined in the conventions, with $m>0$. Suppose $I$ is radical after localization at $q$, the branch images cover $V(I)$ in a neighborhood of $q$, and distinct images meet only at $q$. Let $A=(\mathbb C[x]/I)_q$ and let $\widetilde A$ be its integral closure in its total fraction ring. Then $\dim A=1$.

If $\operatorname{ord}_{t=0}f(c_b(t))<\infty$ for every branch $b$, the image of $f$ in $A$ is a non-zero-divisor. There is a bijection $b\mapsto\mathfrak m_b$ from the branches to $\operatorname{MaxSpec}\widetilde A$ such that $$\ell_A(\widetilde A/\mathfrak m_b)=1,\qquad \operatorname{ord}_{\widetilde A_{\mathfrak m_b}}(f)=\operatorname{ord}_{t=0}f(c_b(t))$$ for every polynomial $f$; orders may equal infinity.
