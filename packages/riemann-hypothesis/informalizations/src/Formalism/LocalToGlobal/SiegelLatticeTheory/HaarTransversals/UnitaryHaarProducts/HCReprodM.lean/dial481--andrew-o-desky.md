---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/HCReprodM.lean",
  "declarations": [
    "Formalism.L2.SG.HCReprodM.hcReprodDSc"
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

## Reproducing a lowest compact-type vector by a compactly supported kernel

[Theorem REP.0426](https://andrewodesky.com/rh/lean/Formalism.L2.SG.HCReprodM.hcReprodDSc/)

Let $n\ge0$, $\varepsilon_1,\ldots,\varepsilon_n\in\{\pm1\}$, $\lambda\in\mathbb R^n$, and put $G=U(\operatorname{diag}(\varepsilon_i))$, $K=U(p)\times U(q)$. Let $\sigma$ be a strongly continuous irreducible unitary representation on a nonzero complex Hilbert space $H$, with every matrix coefficient square-integrable. Use positive roots $e_i-e_j$ for $i<j$, and let $\rho_c,\rho_n$ be their half-sums for equal and unequal signs. Put $\kappa=\lambda+\rho_n-\rho_c$.

Assume the $K$-type of highest weight $\kappa$ occurs, and for every occurring $K$-type of highest weight $\mu$, $$\|\kappa+2\rho_c\|^2\le\|\mu+2\rho_c\|^2.$$ For every $w$ in the span of all copies of the $K$-type $\kappa$, there is a continuous compactly supported $\alpha:G\to\mathbb C$ such that $g\mapsto\alpha(g)\sigma(g)w$ is Bochner integrable and $$\int_G\alpha(g)\sigma(g)w\,dg=w.$$ The measure $dg$ is the reference Haar measure $\mu^0_\varepsilon$ in ([Formal degree with compact-dual normalization](https://andrewodesky.com/rh/lean/PositivityTheory.RgFd.B.formalDegreeCompactDual/)) and the weight norm is the Euclidean norm.
