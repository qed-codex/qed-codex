---
{
  "module": "src/Development/WeilBound/CoreStatements/PublishedTheorems/PoitouTateDuality/PtfsSha.lean",
  "declarations": [
    "PositivityTheory.Lit1.PTN.perfectQZ_of_found"
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

## A perfect pairing between global localization kernels

[Theorem GC.1215](https://andrewodesky.com/rh/lean/PositivityTheory.Lit1.PTN.perfectQZ_of_found/)

Let $X,Y$ be abelian groups. Suppose there are a number field $K\subset\overline{\mathbb Q}$, a finite set $S$ of finite places of $K$, a nonzero integer $N\ge0$, and a finite discrete continuous $G_{K,S}$-module $A$ killed by $N$. Here $G_{K,S}$ allows ramification only in $S$. Assume $S$ contains all places dividing $N$, and either $N$ is odd or $K$ is totally complex. Fix embeddings $\overline{\mathbb Q}\hookrightarrow\overline{K_v}$ over $K$ for $v\in S$. Put $A^\vee=\operatorname{Hom}(A,\mu_N)$ with its induced Galois action, and define $$\mathrm{Ш}_S^i(M)=\ker\left(H^i(G_{K,S},M)\longrightarrow\prod_{v\in S}H^i(G_{K_v},M)\right).$$ If $Y\simeq\mathrm{Ш}_S^1(A)$ and $X\simeq\mathrm{Ш}_S^2(A^\vee)$ as abelian groups, then $X,Y$ are finite and there is a biadditive pairing $$P:X\times Y\longrightarrow\mathbb Q/\mathbb Z$$ inducing bijections $X\simeq\operatorname{Hom}(Y,\mathbb Q/\mathbb Z)$ and $Y\simeq\operatorname{Hom}(X,\mathbb Q/\mathbb Z)$.
