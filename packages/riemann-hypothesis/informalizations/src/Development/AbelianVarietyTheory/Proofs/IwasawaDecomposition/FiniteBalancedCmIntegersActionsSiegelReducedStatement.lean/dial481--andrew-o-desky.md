---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/FiniteBalancedCmIntegersActionsSiegelReducedStatement.lean",
  "declarations": [
    "GlobalTheory.T.finite_balanced_cmIntegers_actions_siegelReduced"
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

## Finiteness of integral CM actions balanced by reduced forms

[Theorem ALG.1494](https://andrewodesky.com/rh/lean/GlobalTheory.T.finite_balanced_cmIntegers_actions_siegelReduced/)

Let $E$ be a CM number field with the CM field data specified below, and write $c\mapsto\bar c$ for its conjugation on $\mathcal O_E$. For every $n\ge0$, only finitely many unital ring homomorphisms $\rho:\mathcal O_E\to M_n(\mathbb Z)$ have the following property: there exist real numbers $d_i>0$ and an upper unitriangular real matrix $u$, with $|u_{ij}|\le1/2$ for $i<j$ and $d_i\le4d_{i+1}$, such that, putting $G=u^t\operatorname{diag}(d_i)u$, $$\rho(c)^tG=G\rho(\bar c)\qquad(c\in\mathcal O_E).$$
