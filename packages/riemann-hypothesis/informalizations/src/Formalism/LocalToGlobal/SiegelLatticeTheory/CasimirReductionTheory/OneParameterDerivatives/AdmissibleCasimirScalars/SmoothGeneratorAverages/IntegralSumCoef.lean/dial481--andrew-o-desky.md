---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/CasimirReductionTheory/OneParameterDerivatives/AdmissibleCasimirScalars/SmoothGeneratorAverages/IntegralSumCoef.lean",
  "declarations": [
    "Formalism.L2.SG.Pf.admitted.c7"
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

## Finite dimension from uniformly small displacement

[Theorem REP.0539](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Pf.admitted.c7/)

Let $G=U(p,q)$, with a fixed Haar measure $\mu$, and let $\rho$ be a unitary representation with continuous orbit maps on a complex Hilbert space $H$. Suppose there is $d>0$ such that, for all $v,w,v',w'\in H$, the product below is integrable and $$\int_G\langle w,\rho(g)v\rangle\,\overline{\langle w',\rho(g)v'\rangle}\,d\mu(g)=\frac{\langle v',v\rangle\langle w,w'\rangle}{d}.$$ If $W\subseteq H$ is a complex subspace and $U$ is a neighborhood of the identity satisfying $$\|\rho(g)v-v\|\le\tfrac12\|v\|\qquad(g\in U,\ v\in W),$$ then $W$ is finite-dimensional.
