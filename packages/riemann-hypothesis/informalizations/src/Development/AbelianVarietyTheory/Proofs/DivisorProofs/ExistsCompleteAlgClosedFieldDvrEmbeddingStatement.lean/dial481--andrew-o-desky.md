---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCompleteAlgClosedFieldDvrEmbeddingStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_complete_algClosed_field_dvr_embedding"
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

## A complete algebraically closed normed field containing a DVR fraction field

[Theorem PHT.0194](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_complete_algClosed_field_dvr_embedding/)

Let $V$ be a characteristic-zero discrete valuation domain, complete for its maximal ideal $\mathfrak m$, with finite residue field. There are a complete algebraically closed nontrivially normed ultrametric field $C$ of characteristic zero and a field embedding $\operatorname{Frac}(V)\hookrightarrow C$ such that $$|a|\le1\quad(a\in V),\qquad |a|<1\quad(a\in\mathfrak m).$$ Moreover, $C$ is isomorphic to $\mathbb C$ as a field.
