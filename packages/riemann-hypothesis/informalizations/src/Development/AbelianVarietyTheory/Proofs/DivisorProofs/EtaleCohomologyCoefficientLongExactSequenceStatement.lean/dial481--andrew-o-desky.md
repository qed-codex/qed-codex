---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/EtaleCohomologyCoefficientLongExactSequenceStatement.lean",
  "declarations": [
    "GlobalTheory.T.etaleCohomology_coefficient_longExactSequence"
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

## Long exact cohomology sequences for short exact coefficient sequences

[Theorem AG.1607](https://andrewodesky.com/rh/lean/GlobalTheory.T.etaleCohomology_coefficient_longExactSequence/)

Let $R$ be a commutative ring and $$0\longrightarrow\mathcal F_1\xrightarrow{i}\mathcal F_2\xrightarrow{p}\mathcal F_3\longrightarrow0$$ a short exact sequence in the category of sheaves of $R$-modules on the big étale site. Fix injective resolutions $I^\bullet(\mathcal F_j)$ as in ([Mayer–Vietoris for simplicial presheaves on the etale site](https://andrewodesky.com/rh/lean/GlobalTheory.EtC.mayerVietoris/)). There is a degree-one cocycle $$z:I^\bullet(\mathcal F_3)\longrightarrow I^\bullet(\mathcal F_1)[1]$$ such that for every complex of sheaves $K^\bullet$ and every $n\in\mathbb Z$ the sequence $$H^n\operatorname{Hom}^\bullet(K,I(\mathcal F_1))\xrightarrow{i_*}H^n\operatorname{Hom}^\bullet(K,I(\mathcal F_2))\xrightarrow{p_*}H^n\operatorname{Hom}^\bullet(K,I(\mathcal F_3))\xrightarrow{z_*}H^{n+1}\operatorname{Hom}^\bullet(K,I(\mathcal F_1))\xrightarrow{i_*}H^{n+1}\operatorname{Hom}^\bullet(K,I(\mathcal F_2))$$ is exact at its three interior terms.
