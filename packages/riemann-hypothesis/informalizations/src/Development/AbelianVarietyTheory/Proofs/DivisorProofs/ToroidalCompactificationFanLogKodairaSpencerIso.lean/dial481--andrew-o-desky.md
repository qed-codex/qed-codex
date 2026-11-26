---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ToroidalCompactificationFanLogKodairaSpencerIso.lean",
  "declarations": [
    "GlobalTheory.TorKSField.toroidalForFanKS"
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

## Toroidal compactification of unitary moduli with a logarithmic Kodaira–Spencer isomorphism

[Theorem AV.1.1760](https://andrewodesky.com/rh/lean/GlobalTheory.TorKSField.toroidalForFanKS/)

Fix moduli data of signature $(p,q)$ with $p+q\ge1$, in the sense of ([Unitary toroidal models and boundary charts](https://andrewodesky.com/rh/lean/GlobalTheory.MumfordChart.HasChart/)): a CM field $E$ with the elements $r,w\in\mathcal O_E$ and $r_0\in\mathbb C$ chosen there, a polarized $\mathcal O_E$-lattice of signature $(p,q)$, a level, a moduli scheme for these data, and a coefficient field $K\subset\mathbb C$. Let $X$ be the moduli scheme after base change to $K$. Let $\phi$ be an invariant function that satisfies the polarizing-fan condition and the no-self-intersection condition of ([Polarizing fan conventions for toroidal compactifications](https://andrewodesky.com/rh/lean/GlobalTheory.LocM.InvFun/)), for $\mathcal O_E$ with CM conjugation, in ranks at most $\min(p,q)$.

Then there are a model $(Y,j,G)$ of $X$, an effective Cartier divisor $B$ on $Y$, and integers $d,k\ge1$ with the five properties below. Here $j:X\hookrightarrow Y$ is the open immersion of the model, $G/Y$ is its semiabelian scheme, and $D=Y\setminus j(X)$ is the boundary with its reduced structure.

1. **Smoothness.** The scheme $Y$ is smooth over $K$ of relative dimension $[E:\mathbb Q]pq/2$, and $D$ has simple normal crossings.
2. **Support.** The support of $B$ is contained in $D$.
3. **Boundary charts.** Every point of $D$, closed or not, has a polarized boundary chart for $(\phi,B,d)$.
4. **Ampleness.** If the determinant Hodge presentation $\lambda$ of $G$ is a line bundle, then $\lambda^{\otimes k}\otimes\mathcal O_Y(-B)$ is ample.
5. **Kodaira–Spencer isomorphism.** The $K$-scheme $Y$, the semiabelian scheme $G$ with its polarization line bundle, and the open subset $j(X)\subseteq Y$ satisfy the logarithmic Kodaira–Spencer condition of ([Flag models and logarithmic Kodaira–Spencer maps](https://andrewodesky.com/rh/lean/GlobalTheory.CompHS.TorFlag/)).
