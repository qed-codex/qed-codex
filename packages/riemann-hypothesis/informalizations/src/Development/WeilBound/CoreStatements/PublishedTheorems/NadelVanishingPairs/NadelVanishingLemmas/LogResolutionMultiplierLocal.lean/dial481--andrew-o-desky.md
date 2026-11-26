---
{
  "module": "src/Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/LogResolutionMultiplierLocal.lean",
  "declarations": [
    "GlobalTheory.Discrepancy.kltAt_lcAt_iff_of_isLogRes"
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

## Testing local klt and log canonical conditions on a resolution

[Theorem AG.1184](https://andrewodesky.com/rh/lean/GlobalTheory.Discrepancy.kltAt_lcAt_iff_of_isLogRes/)

Let $k$ have characteristic zero, and let $p:X\to\operatorname{Spec}k$ be projective with $X$ normal, integral, and locally Noetherian of dimension $n$. Let $\Delta:X\to\mathbb Q$, let $\eta$ be a nonzero rational top-degree differential form, let $m\ge1$, and let $G$ be a Cartier divisor encoding $m(K_X(\eta)+\Delta)$ in the following local sense: whenever $g$ is a local equation for $G$ at $x$, and $v$ is a divisorial valuation whose valuation ring equals $\mathcal O_{X,z}$ for a point $z$ specializing to $x$, $$v(g)=m\bigl(\operatorname{ord}_v(\eta)+\Delta(z)\bigr).$$ Let $Y$ be integral and locally Noetherian and $s:Y\to X$ dominant, inducing an isomorphism of function fields. Assume $Y/k$ is smooth of relative dimension $n$ and projective, $K$ is the Cartier divisor of the pulled-back form $s^*\eta$, and a closed subset $B\subset Y$ has simple normal crossings and contains the support of $s^*G-mK$.

Write $D=s^*G-mK$, and let $\operatorname{mult}_wD$ be the order of a local equation for $D$ at $w$. For every $x\in X$, $$\begin{aligned} (X,\Delta)\text{ is klt at }x &\ \Longleftrightarrow\ \operatorname{mult}_wD<m\quad\text{for every }w\in Y\text{ with }s(w)\rightsquigarrow x,\\ (X,\Delta)\text{ is log canonical at }x &\ \Longleftrightarrow\ \operatorname{mult}_wD\le m\quad\text{for every }w\in Y\text{ with }s(w)\rightsquigarrow x. \end{aligned}$$ Here $y\rightsquigarrow x$ means that $x$ is a specialization of $y$; the two local singularity conditions mean that all divisorial discrepancies over $x$ are $>-1$ and $\ge-1$, respectively.
