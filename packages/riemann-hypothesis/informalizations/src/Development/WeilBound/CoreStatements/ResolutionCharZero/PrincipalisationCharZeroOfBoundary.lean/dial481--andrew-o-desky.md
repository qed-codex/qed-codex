---
{
  "module": "src/Development/WeilBound/CoreStatements/ResolutionCharZero/PrincipalisationCharZeroOfBoundary.lean",
  "declarations": [
    "PositivityTheory.ResPlug.WeightsCompactStabilizer.principalisationCharZero_bot_closed"
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

## Principalization on a smooth separated scheme

[Theorem AG.1659](https://andrewodesky.com/rh/lean/PositivityTheory.ResPlug.WeightsCompactStabilizer.principalisationCharZero_bot_closed/)

Let $k$ have characteristic zero and let $X\to\operatorname{Spec}k$ be a quasi-compact separated smooth scheme of constant relative dimension $d\ge0$. Let $\mathcal I$ be an ideal sheaf on $X$ whose support contains no irreducible component of $X$. There exist a smooth $k$-scheme $X'$, a morphism $\pi:X'\to X$, and a closed subset $E'\subseteq X'$ such that $\pi$ is a finite sequence of blow-ups in smooth centers, starting with empty boundary and with each center having normal crossings with the accumulated boundary $E'$. The pulled-back ideal $\mathcal I\mathcal O_{X'}$ defines an effective Cartier divisor, its reduced support is a simple normal-crossing divisor, and $$\pi^{-1}(X\setminus\operatorname{Supp}\mathcal I) \xrightarrow{\ \sim\ }X\setminus\operatorname{Supp}\mathcal I.$$
