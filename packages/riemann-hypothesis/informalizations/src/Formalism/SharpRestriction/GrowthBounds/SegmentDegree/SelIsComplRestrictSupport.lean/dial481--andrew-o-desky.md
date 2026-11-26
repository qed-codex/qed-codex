---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/SegmentDegree/SelIsComplRestrictSupport.lean",
  "declarations": [
    "Formalism.MainNotions.SelectionLemmas.Pf.restSel"
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

## A direct summand spanned by selected polynomials

[Theorem ALG.0452](https://andrewodesky.com/rh/lean/Formalism.MainNotions.SelectionLemmas.Pf.restSel/)

Let $O$ be a discrete valuation domain with residue field $\kappa$, let $\Sigma$ be any set of variables, and let $S\subseteq\mathbb N^{(\Sigma)}$ be a finite set of monomials. Let $G\subseteq O[X_\sigma:\sigma\in\Sigma]$ consist of polynomials supported in $S$. There is an $O$-submodule $L$ of the polynomial ring such that $L\subseteq\operatorname{span}_O G$, $L$ is a direct summand of the polynomial ring, and $L$ has an $O$-basis consisting of elements of $G$. Moreover, $$\operatorname{rank}_O L=\dim_\kappa\operatorname{span}_\kappa\{\bar g:g\in G\},$$ where $\bar g$ denotes coefficientwise reduction modulo the maximal ideal of $O$.
