---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/CoefficientCongruenceOfTwistedValues.lean",
  "declarations": [
    "GlobalTheory.KZ.CoefVal.coeff_cg_of_values"
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

## Coefficient divisibility from torsion values of truncations

[Theorem PHT.1049](https://andrewodesky.com/rh/lean/GlobalTheory.KZ.CoefVal.coeff_cg_of_values/)

Let $\ell$ be prime and let $O\subseteq\overline{\mathbb Q}_\ell$ be a discrete valuation $\mathbb Z_\ell$-subalgebra finite as a $\mathbb Z_\ell$-module. Let $F(T)=\sum_{n\ge0}a_nT^n\in O[[T]]$ and let $k,m_1\ge0$ be integers. Suppose that for every $m\ge m_1$ and every primitive $\ell^m$-th root of unity $z$, $$\left|\sum_{0\le n<\ell^{3m}}a_n(z-1)^n\right|_\ell\le |\ell|_\ell^k.$$ Then $|a_n|_\ell\le|\ell|_\ell^k$ for every $n\ge0$.
