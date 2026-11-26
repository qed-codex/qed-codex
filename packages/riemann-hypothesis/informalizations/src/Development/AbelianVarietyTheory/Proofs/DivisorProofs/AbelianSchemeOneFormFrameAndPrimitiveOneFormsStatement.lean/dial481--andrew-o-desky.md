---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbelianSchemeOneFormFrameAndPrimitiveOneFormsStatement.lean",
  "declarations": [
    "GlobalTheory.T.abelianScheme_oneFormFrame_and_primitiveOneForms"
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

## Global one-forms on an abelian scheme

[Theorem AG.1669](https://andrewodesky.com/rh/lean/GlobalTheory.T.abelianScheme_oneFormFrame_and_primitiveOneForms/)

Let $R$ be a commutative ring and $A/R$ an abelian scheme smooth of constant relative dimension $g\ge0$. There exist finitely many global relative one-forms $\omega_1,\ldots,\omega_n$ and, for every affine open subset $T\subseteq A$, $\mathcal O(T)$-linear maps $$\delta_{i,T}:\Omega^1_{\mathcal O(T)/R}\longrightarrow\mathcal O(T)$$ compatible with restriction along inclusions of affine open subsets, such that $$\eta=\sum_{i=1}^n\delta_{i,T}(\eta)\,\omega_i|_T\quad(\eta\in\Omega^1_{\mathcal O(T)/R}).$$ Moreover every $\omega\in H^0(A,\Omega^1_{A/R})$ is primitive: $$m^*\omega=p_1^*\omega+p_2^*\omega,$$ where $m:A\times_RA\to A$ is addition and $p_1,p_2$ are the projections.
