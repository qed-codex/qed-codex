---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/RigidBoundaryChartsForFanUnitaryDatum.lean",
  "declarations": [
    "GlobalTheory.RigChart.rigidForFan_holds"
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

## Unitary compactification with infinitesimally rigid boundary charts

[Theorem AV.1.0023](https://andrewodesky.com/rh/lean/GlobalTheory.RigChart.rigidForFan_holds/)

Every unitary moduli datum of signature $(p,q)$ with $p+q\ge1$, equipped with a fan satisfying ([Polarizing fan conventions for toroidal compactifications](https://andrewodesky.com/rh/lean/GlobalTheory.LocM.InvFun/)) over $\mathcal O_E$ in ranks at most $\min(p,q)$, has a smooth projective compactification with the following boundary and rigidity properties. The fields, level and polarization data are specified below.

Write $X/K$ for its open moduli scheme. There are a normal projective flat $K$-scheme $Y$, a dense open immersion $j:X\hookrightarrow Y$, a polarized semiabelian extension $G/Y$ of the universal family, an effective Cartier divisor $B$ on $Y$, and integers $d,k\ge1$, such that $Y/K$ is smooth of relative dimension $[E:\mathbb Q]pq/2$. The abelian locus of $G$ is $j(X)$, the reduced boundary $D=Y\setminus j(X)$ has simple normal crossings, and $\operatorname{Supp}B$ is disjoint from the abelian locus. If the determinant Hodge sheaf $\lambda$ of $G$ is invertible, then $$\lambda^{\otimes k}\otimes\mathcal O_Y(-B)\quad\hbox{is ample}.$$ Every boundary point has a polarized chart for $(\phi,B,d)$. Every closed boundary point has an infinitesimally rigid chart. These two chart conditions have the meanings below and are separate existence assertions.
