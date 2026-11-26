---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsBasepointFreeSectionTupleAmpleArithStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_basepointFreeSectionTuple_ample_arith"
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

## Generating sections of a power of an ample arithmetic line bundle

[Theorem ARAK.1604](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_basepointFreeSectionTuple_ample_arith/)

Let $k$ be a commutative domain finite as a $\mathbb Z$-module, let $X$ be an integral scheme, and let $p:X\to\operatorname{Spec}k$ be projective. Assume $X\to\operatorname{Spec}\mathbb Z$ is flat and $\dim X=D+1$, where $D\ge0$. Fix a pair of metrized line bundles $(\overline L,\overline A)$ on $X$, each with compatible rational local trivializations, and suppose $L$ is ample. There are $e>0$ and $D+1$ global sections of $L^{\otimes e}$, represented by rational sections $s_0,\ldots,s_D\in k(X)$, such that $$\bigcup_{i=0}^{D}\{x\in X:s_i(x)\ne0\}=X.$$
