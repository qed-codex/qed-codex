---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/WeylFormulaCompact/DimStep.lean",
  "declarations": [
    "PI.WeylForKWork.dimension_induction_holds"
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

## Dimensions under two commuting compact unitary actions

[Theorem REP.0589](https://andrewodesky.com/rh/lean/PI.WeylForKWork.dimension_induction_holds/)

Let $H$ be a complex inner-product space with strongly continuous unitary actions of $U(p)$ and $U(q)$ whose operators commute. Let $S\subseteq H$ be finite-dimensional and invariant under both actions, with no simultaneous invariant subspaces other than $0$ and $S$. Let $0\ne X,Y\subseteq S$, with $X$ invariant and irreducible for $U(p)$ and $Y$ invariant and irreducible for $U(q)$. Then $$\dim_{\mathbb C}S=\dim_{\mathbb C}X\,\dim_{\mathbb C}Y.$$ The integers $p,q$ may be zero.
