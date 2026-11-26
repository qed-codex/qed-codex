---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/UnitaryClassFiniteness/LatticeClassesFiniteRefinement.lean",
  "declarations": [
    "PI.UnitaryGroupMassFormula.UJClassFin.lattice_classes_finite_refinement"
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

## Finiteness of definite Hermitian additive lattice classes

[Theorem ANT.0510](https://andrewodesky.com/rh/lean/PI.UnitaryGroupMassFormula.UJClassFin.lattice_classes_finite_refinement/)

Let $E$ be a number field and $\sigma:E\to E$ a ring homomorphism satisfying $$\tau(\sigma(a))=\overline{\tau(a)}\qquad(a\in E,\ \tau:E\hookrightarrow\mathbb C).$$ Let $J\in M_m(E)$ have $\tau(J)$ positive definite for every complex embedding, and put $H(x,y)=\sum_{i,j}\sigma(x_i)J_{ij}y_j$. Fix positive integers $D,T,c_0$. There are only finitely many orbits, under $\{g\in\operatorname{GL}_m(E):\sigma(g)^tJg=J\}$, of additive subgroups $\Lambda\subset E^m$ satisfying all of the following:

1. $c_0a\Lambda\subseteq\Lambda$ for every $a\in\mathcal O_E$.
2. $k\mathcal O_E^m\subseteq\Lambda$ for some positive integer $k$.
3. $DH(x,y)\in\mathcal O_E$ for all $x,y\in\Lambda$.
4. If $y\in E^m$ has $DH(x,y)\in\mathcal O_E$ for every $x\in\Lambda$, then $Ty\in\Lambda$.
