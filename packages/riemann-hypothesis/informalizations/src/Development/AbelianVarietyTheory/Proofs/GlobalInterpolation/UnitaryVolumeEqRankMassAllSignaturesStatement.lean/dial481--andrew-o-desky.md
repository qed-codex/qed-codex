---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/UnitaryVolumeEqRankMassAllSignaturesStatement.lean",
  "declarations": [
    "GlobalTheory.T.unitary_volume_eq_rank_mass_all_signatures"
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

## Unitary volumes and standard lattice masses in all signatures

[Theorem ARAK.1412](https://andrewodesky.com/rh/lean/GlobalTheory.T.unitary_volume_eq_rank_mass_all_signatures/)

Choose an arithmetic datum satisfying ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), with CM field $E$ and positive volume assignment $\operatorname{vol}$. Assume the volume-normalization condition in ([The adelic volume ratio on removing a unit vector](https://andrewodesky.com/rh/lean/GlobalTheory.VolRatioUnfold.volumeRatio_of_unfolding/)). Hermitian spaces with recorded lattice data have the generic meaning in ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)). For every nonnegative integer $n$, put $$M_E(n)=\operatorname{mass}(h_{\mathrm{std}},\mathcal O_E^n),\qquad h_{\mathrm{std}}(x,y)=\sum_i\overline{x_i}y_i,$$ using the definition of mass in ([A common Hermitian mass constant in every positive rank](https://andrewodesky.com/rh/lean/Formalism.HermitianLattices.Ext.L3.massConst_all/)).

For every such Hermitian space $W$ whose Gram matrix has its recorded signature $(P,Q)$ at every complex embedding of $E$, $$\operatorname{vol}(W)=M_E(P+Q).$$
