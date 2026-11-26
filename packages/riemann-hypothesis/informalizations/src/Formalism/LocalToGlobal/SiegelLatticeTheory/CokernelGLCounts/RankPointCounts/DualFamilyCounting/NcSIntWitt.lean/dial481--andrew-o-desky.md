---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcSIntWitt.lean",
  "declarations": [
    "Formalism.L2.SG.Pf.NcS.IntWittPf.integral_witt_almost_everywhere"
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

## Integral transitivity on tuples with a fixed nonsingular Gram matrix

[Theorem ANT.0606](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Pf.NcS.IntWittPf.integral_witt_almost_everywhere/)

Let $E/F$ be a CM extension of number fields with conjugation $\sigma$, and let $J\in M_n(E)$ be nondegenerate and $\sigma$-Hermitian. Fix a tuple $X_0=(x_1,\ldots,x_a)\in(E^n)^a$ whose Gram matrix $G$ for $J$ is nonsingular, and an $\mathcal O_E$-lattice $\Lambda\subset E^n$. Choose an $F$-basis $b_1,\ldots,b_d$ of $E$.

For all but finitely many finite places $v$ of $F$, every tuple $X\in((F_v\otimes_FE)^n)^a$ with coefficients integral in the basis $(b_i)$ and with Gram matrix equal to the image of $G$ is of the form $$X=kX_0$$ for some $k\in U(J)(F_v)$ stabilizing the completed lattice $\Lambda_v$.
