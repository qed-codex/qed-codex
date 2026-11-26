---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/HeckeGaloisCriteria/EvPowLeExp.lean",
  "declarations": [
    "UpperTheory.GalC.etaSum_le_add",
    "UpperTheory.GalC.sum_val_le"
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

## Summing integer valuations over coefficient places

[Theorem ANT.0171](https://andrewodesky.com/rh/lean/UpperTheory.GalC.sum_val_le/)

Fix the source's arithmetic datum and the finite support of coefficient places. At a twisted place $v$, set $$a_v={\log\operatorname{Norm}(\mathfrak p_v)\over[K:\mathbb Q]}e_v,$$ where $K$ is the coefficient field, $e_v$ its ramification index over the residue prime $p_v$, and twisted means that the local Hecke type differs from the distinguished type. For every integer $H\ge1$, $$\sum_{v\ \mathrm{twisted}}a_vv_{p_v}(H)\le\log H.$$ Consequently, for any $d\ge0$, any real values $u_v$, and any lift index $j$, if $\eta_j(v)\le u_v+dv_{p_v}(H)$ at every twisted coefficient place, then $$\eta_j\le\sum_{v\ \mathrm{twisted}}a_vu_v+d\log H.$$ All sums over coefficient places are restricted to the specified finite support, and $\eta_j=\sum a_v\eta_j(v)$.
