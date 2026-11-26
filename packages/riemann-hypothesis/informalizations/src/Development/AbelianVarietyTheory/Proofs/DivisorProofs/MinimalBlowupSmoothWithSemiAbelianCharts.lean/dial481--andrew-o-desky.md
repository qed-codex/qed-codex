---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/MinimalBlowupSmoothWithSemiAbelianCharts.lean",
  "declarations": [
    "GlobalTheory.SiegJoin.chartSt5_holds"
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

## Smoothness and polarized boundary charts of a normalized blow-up of a compactified Siegel moduli family

[Theorem AV.1.1765](https://andrewodesky.com/rh/lean/GlobalTheory.SiegJoin.chartSt5_holds/)

Let $g\ge1$ and let $n\ge3$ be odd. Put $R_n=\mathbb Z[\zeta_n,1/n]$ with $\zeta_n=e^{2\pi i/n}$. Let $\phi$ be an invariant function that satisfies the polarizing-fan condition and the no-self-intersection condition of ([Polarizing fan conventions for toroidal compactifications](https://andrewodesky.com/rh/lean/GlobalTheory.LocM.InvFun/)), for $\mathbb Z$ with the identity involution, in ranks at most $g$. Let $(A,P,\ell)/U$ be a Siegel moduli family of type $(g,n)$ over $R_n$, in the sense of ([Siegel moduli families and their level pairing](https://andrewodesky.com/rh/lean/GlobalTheory.ZM.SFam/)).

Let $Z$ be an $R_n$-scheme, $i:U\to Z$ a morphism and $L$ a line bundle on $Z$ such that $(Z,i,L)$ is a theta-integral compactification of $U$ with a semiabelian cover, in the sense of ([Theta-integral compactifications of a Siegel moduli family and semiabelian covers](https://andrewodesky.com/rh/lean/GlobalTheory.Poinc.IsThetaCompact/)). Let $d\ge1$ be an integer, and let $(S,\pi,j,B)$ be a normalized blow-up of $(Z,i)$ with boundary orders $d\phi$, in the sense of ([Normalized blow-ups of a compactified Siegel moduli family with prescribed boundary orders](https://andrewodesky.com/rh/lean/GlobalTheory.Poinc.Trait/)). Assume that $j:U\to S$ is an open immersion, and regard $S$ as an $R_n$-scheme through $\pi$.

Then:

1. $S$ is smooth over $R_n$ of relative dimension $g(g+1)/2$.
2. Every point of $S$ has a polarized chart with a semiabelian scheme for $(\phi,B,d)$, in the sense of ([Polarized boundary charts carrying a semiabelian scheme](https://andrewodesky.com/rh/lean/GlobalTheory.PolDeg.PreChart/)).
