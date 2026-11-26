---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/IrredOfCharpolyEq.lean",
  "declarations": [
    "GlobalTheory.BrauerNesbittIrr.litBNIrr"
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

## Irreducibility determined by characteristic polynomials

[Theorem ALG.1472](https://andrewodesky.com/rh/lean/GlobalTheory.BrauerNesbittIrr.litBNIrr/)

Let $\Gamma$ be a group, $\ell$ a prime, and $a\ge0$. Suppose $\rho,\rho':\Gamma\to\operatorname{GL}_a(\overline{\mathbb F}_\ell)$ satisfy $$\det(T-\rho(g))=\det(T-\rho'(g))\qquad(g\in\Gamma).$$ If $\rho'$ is irreducible, then $\rho$ is irreducible.
