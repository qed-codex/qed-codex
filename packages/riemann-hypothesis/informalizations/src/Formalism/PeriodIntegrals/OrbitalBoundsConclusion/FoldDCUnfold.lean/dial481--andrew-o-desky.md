---
{
  "module": "src/Formalism/PeriodIntegrals/OrbitalBoundsConclusion/FoldDCUnfold.lean",
  "declarations": [
    "fold_dc_unfold"
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

## Unfolding a product of two subgroup sums

[Theorem REP.0472](https://andrewodesky.com/rh/lean/fold_dc_unfold/)

Let $G$ be a measurable group with measurable multiplication and left-invariant measure $\mu$. Let $\Gamma\subseteq G$ be countable and let $S,S'\subseteq\Gamma$ be subgroups. Choose representatives $D$ for $S\backslash\Gamma$, $D'$ for $S'\backslash\Gamma$, and $R$ for $S\backslash\Gamma/S'$, all as subsets of $\Gamma$. Let $F_\Gamma$ be a fundamental domain for $\Gamma$ on $G$. For each $r\in R$, let $F_r$ be a fundamental domain for $S\cap rS'r^{-1}$.

If $g,h:G\to[0,\infty]$ are measurable, with $g(sx)=g(x)$ for $s\in S$ and $h(s'x)=h(x)$ for $s'\in S'$, then $$\int_{F_\Gamma}\left(\sum_{\delta\in D}g(\delta x)\right)\left(\sum_{\delta'\in D'}h(\delta'x)\right)d\mu(x) =\sum_{r\in R}\int_{F_r}g(x)h(r^{-1}x)\,d\mu(x).$$ All sums and integrals are extended nonnegative ones.
