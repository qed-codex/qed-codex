---
{
  "module": "src/Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/AdelicEisensteinSeries/IsGrowFormEvAt.lean",
  "declarations": [
    "PositivityTheory.SiegelWeilFormula.Aeis.eisBLW"
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

## Meromorphic Eisenstein families tested by growth functionals

[Theorem AGR.1245](https://andrewodesky.com/rh/lean/PositivityTheory.SiegelWeilFormula.Aeis.eisBLW/)

Let $E/F$ be number fields and choose an $F$-linear endomorphism $\sigma$ and base data satisfying the good-base package in the conventions. Let $n\ge1$, let $Y$ be its rank-$n$ space datum, and let $G$ be the associated doubled unitary group. Choose a unitary Hecke character $\chi$ of $E$ whose restriction to the embedded $\mathbb A_F^\times$ is the $c$th power of the quadratic character of $E/F$ for some $c\ge0$. Choose a doubled frame, its standard compact subgroup $K$, and an Iwasawa height $a:G(\mathbb A_F)\to\mathbb R$ satisfying the frame, compact-subgroup and height packages in the conventions. Let $s_1\in\mathbb C$ and let $f:G(\mathbb A_F)\to\mathbb C$ be continuous and right $K$-finite, with $$f(px)=\chi(\det t)|\det t|_{\mathbb A_E}^{s_1+n/2}f(x)$$ for every Siegel-parabolic element $p$ with Levi coordinate $t$. Put $f_s(x)=a(x)^{s-s_1}f(x)$ and form the Eisenstein terms indexed by rational Siegel-parabolic cosets.

There is a family $\widehat E(s,x)$ such that, in some right half-plane, the Eisenstein terms have sum $\widehat E(s,x)$ and $s\mapsto\widehat E(s,x)$ is holomorphic for every $x$. For every $s_0\in\mathbb C$, there are $k\ge0$, a neighborhood $U$ of $s_0$, and a family $H(s)$ of moderate-growth functions such that $$H(s)(x)=(s-s_0)^k\widehat E(s,x)\qquad(s\in U,\ s\ne s_0,\ x\in G(\mathbb A_F)).$$ For every growth functional $\mu$, $s\mapsto\mu(H(s))$ is holomorphic on $U$. Here moderate-growth functions are the complex span of continuous functions bounded in absolute value by a nonnegative integral power of the source's doubled-group height; a growth functional is complex-linear and bounded on each set $\{h:|h(x)|\le\operatorname{ht}(x)^N\text{ for all }x\}$.
