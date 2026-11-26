---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsFiniteExtAbsIrrSubStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_finiteDimensional_ext_irrSub_absIrr"
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

## Absolute irreducibility after one finite coefficient extension

[Theorem REP.0432](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_finiteDimensional_ext_irrSub_absIrr/)

Let $K$ be a field, $\Gamma$ a group, $I$ a finite index set, and $a\ge0$. For every $i\in I$, let $\rho_i:\Gamma\to\operatorname{GL}_a(K)$ be a representation whose extension to an algebraic closure of $K$ is semisimple. There is a finite field extension $K'/K$ such that every irreducible invariant subspace of every $\rho_i\otimes_KK'$ is absolutely irreducible.
