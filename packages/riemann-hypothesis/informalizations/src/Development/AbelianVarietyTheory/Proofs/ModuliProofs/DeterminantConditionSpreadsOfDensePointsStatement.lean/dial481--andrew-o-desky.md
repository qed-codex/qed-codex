---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/DeterminantConditionSpreadsOfDensePointsStatement.lean",
  "declarations": [
    "GlobalTheory.T.determinantCondition_spreads_of_dense_points"
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

## A PEL tangent multiplicity condition spreads from a dense set

[Theorem AV.0871](https://andrewodesky.com/rh/lean/GlobalTheory.T.determinantCondition_spreads_of_dense_points/)

Fix the unitary PEL datum in the conventions over a CM field $E$, with prime $d\equiv7\pmod{16}$, $\alpha\in\mathcal O_E$ satisfying $\alpha^2=-d$, and signature $(p,q)$. Let $S$ be a reduced scheme and $G\to S$ a smooth commutative group scheme of constant relative dimension $g$, with an action of $\mathcal O_E$. Let $o$ be a commutative ring, $s:S\to\operatorname{Spec}o$, and $\rho\in o$ with $\rho^2=-d$.

For an algebraically closed characteristic-zero field $K$, a point $x:\operatorname{Spec}K\to S$ and $\beta:o\to K$ with $s\circ x=\operatorname{Spec}\beta$, impose the condition that for every $\tau:\mathcal O_E\to K$, the $\tau$-eigenspace of $\operatorname{Lie}(G_x)$ has dimension $p$ if $\tau(\alpha)=\beta(\rho)$, and dimension $q$ otherwise. If the union of the images of all such $x$ satisfying this condition is dense in $S$, then every such pair $(x,\beta)$ satisfies it.
