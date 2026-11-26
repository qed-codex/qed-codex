---
{
  "module": "src/Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/CuspDiscreteDecompositionOfTraceClass.lean",
  "declarations": [
    "GlobalTheory.CuspSpectrum.isDiscreteSum_of_repOp"
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

## Discrete decomposition from compact integrated operators

[Theorem REP.1240](https://andrewodesky.com/rh/lean/GlobalTheory.CuspSpectrum.isDiscreteSum_of_repOp/)

Let $G$ be a group with a topology and measurable structure for which open sets are measurable. Let $H$ be a complex Hilbert space and $\rho:G\to\mathcal B(H)$ a homomorphism by bounded complex-linear operators such that $\|\rho(g)v\|=\|v\|$ for every $g,v$, and $g\mapsto\rho(g)v$ is continuous for every $v$. Let $\mu$ be a measure finite on compact sets, and put $$\rho(f)v=\int_G f(g)\rho(g)v\,d\mu(g).$$ Suppose that for each nonzero $v\in H$ there is a continuous compactly supported $f:G\to\mathbb C$ such that $\rho(f)$ is compact and $\rho(f)v\ne0$. Then $H$ is a Hilbert direct sum of irreducible subrepresentations of $\rho$, and every irreducible unitary representation occurs with finite multiplicity.
