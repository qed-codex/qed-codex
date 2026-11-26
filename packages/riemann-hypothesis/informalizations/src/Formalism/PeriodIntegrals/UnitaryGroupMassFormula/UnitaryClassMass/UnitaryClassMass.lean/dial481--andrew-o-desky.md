---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/UnitaryClassMass/UnitaryClassMass.lean",
  "declarations": [
    "PI.UnitaryGroupMassFormula.UJClassMass.hermitian_approximation"
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

## Simultaneous local matching of Hermitian lattices in a genus

[Theorem ANT.0560](https://andrewodesky.com/rh/lean/PI.UnitaryGroupMassFormula.UJClassMass.hermitian_approximation/)

Let $E/F$ be an extension of number fields with a nontrivial $F$-linear ring involution $\sigma$. Let $V$ be a finite-dimensional $E$-vector space with a nondegenerate Hermitian form $h$ relative to $\sigma$, and let $L_0\subseteq V$ be a full $\mathcal O_E$-lattice. Let $N\subseteq V$ be a full lattice in the genus of $L_0$: at every maximal ideal $\mathfrak p\subseteq\mathcal O_E$, an $E$-linear isometry of $h$ carries $(L_0)_{\mathfrak p}$ onto $N_{\mathfrak p}$. For every finite set $P$ of maximal ideals of $\mathcal O_E$, there is an $E$-linear isometry $\gamma$ of $h$ with $$(\gamma L_0)_{\mathfrak p}=N_{\mathfrak p}\qquad(\mathfrak p\in P).$$ The localizations are taken inside $V$.
