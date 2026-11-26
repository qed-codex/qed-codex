---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TorsionShapeOfTorsionCountsStatement.lean",
  "declarations": [
    "GlobalTheory.T.torsion_shape_of_torsion_counts"
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

## A cyclic quotient from bounds on torsion counts

[Theorem ALG.0988](https://andrewodesky.com/rh/lean/GlobalTheory.T.torsion_shape_of_torsion_counts/)

Let $O$ be a discrete valuation ring with finite residue field $k$ of cardinality $q$, let $\varpi$ be a uniformizer, and let $K=\operatorname{Frac}(O)$. Let $H$ be a submodule of an $O$-module. Suppose $a,d\ge0$ and an $O$-module $F$ with finite underlying set satisfy $$H\simeq (K/O)^a\times F.$$ Assume there is $C\in\mathbb N$ such that for every $n\ge1$, $$q^{nd}\le\#H[\varpi^n]\le Cq^{nd},\qquad \#H[\varpi]\le q^{d+1}.$$ There are a cyclic $O$-module $C_0$ and $O$-linear maps $$(K/O)^d\xrightarrow{\iota}H\xrightarrow{\pi}C_0$$ such that $\iota$ is injective and $\operatorname{im}\iota=\ker\pi$.
