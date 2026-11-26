---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/TameFunctionalVacuumIrreducibilityStatement.lean",
  "declarations": [
    "GlobalTheory.T.tame_functional_vacuum_irreducibility"
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

## Detection of a functional by translates of one vacuum vector

[Theorem THETA.1233](https://andrewodesky.com/rh/lean/GlobalTheory.T.tame_functional_vacuum_irreducibility/)

Fix the source's arithmetic CM and Hermitian-space datum, a standard adelic additive character $\psi$ with parameter $-1$, and two of its Hermitian spaces $S,T$. Write $W$ for the associated oscillator space, $h(w)$ for its Heisenberg action, and $[w,u]$ for the symplectic pairing. Let $\Gamma\subset W$ be an additive subgroup. Let $\mathcal V_\Gamma$ be the theta functions $f$ such that $h(2u)f=f$ for $u\in\Gamma$ and $h(u)f=f$ whenever $u\in\Gamma$ is supported in a split idempotent component. Put $$\Gamma^\perp=\{w:\psi([w,2u])=1\ (u\in\Gamma),\quad\psi([w,u])=1\text{ for every such split-component }u\}.$$ Let $\ell$ be a functional on functions on $W$, complex-linear on the theta functions. Assume that for each theta function $f$, $w\mapsto\ell(h(w)f)$ is continuous and bounded, and that $\ell$ commutes with every integrable average of Heisenberg translates that is again a theta function, for every s-finite measure. If $0\ne f_0\in\mathcal V_\Gamma$ and $\ell(h(w)f_0)=0$ for every $w\in\Gamma^\perp$, then $\ell(f)=0$ for every $f\in\mathcal V_\Gamma$.
