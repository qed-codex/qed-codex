---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DefiniteUnitaryQuotientCompactFundamentalDomainStatement.lean",
  "declarations": [
    "GlobalTheory.T.definite_unitary_quotient_compact_fundamentalDomain"
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

## A bounded measurable fundamental domain for a definite unitary quotient

[Theorem AGR.0912](https://andrewodesky.com/rh/lean/GlobalTheory.T.definite_unitary_quotient_compact_fundamentalDomain/)

Fix the full arithmetic datum specified in ([The convergent doubling integral identity](https://andrewodesky.com/rh/lean/GlobalTheory.T.doubling_basicIdentity_unfolding/)) over a CM extension $E/F$ and a Hermitian space $V$ in its space package. Suppose the assigned signature at every embedding $E\hookrightarrow\mathbb C$ agrees with the Gram matrix and equals $(\dim_E V,0)$. Put $G=U(V)$. For every Haar measure $\mu$ on $G(\mathbb A_F)$, the rational subgroup $G(F)$ is cocompact, and there are a measurable fundamental domain $X$ for its left action and a compact set $C\subseteq G(\mathbb A_F)$ such that $X\subseteq C$.
