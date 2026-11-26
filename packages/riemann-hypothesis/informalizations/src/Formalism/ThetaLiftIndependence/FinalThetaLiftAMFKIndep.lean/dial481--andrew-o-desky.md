---
{
  "module": "src/Formalism/ThetaLiftIndependence/FinalThetaLiftAMFKIndep.lean",
  "declarations": [
    "Formalism.ThetaLiftIndependence.final_gaussOp"
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

## Inverse identities for finite-field Gauss operators

[Theorem REP.0687](https://andrewodesky.com/rh/s/s10-finite-field-gauss-operators.html)

Let $\mathbb F$ be a finite field, $V$ a complex vector space, $\psi:\mathbb F\to\mathbb C^\times$ a nontrivial additive character, and $\rho:\mathbb F^\times\to\operatorname{End}_{\mathbb C}(V)$ a multiplicative monoid homomorphism. Define $$G=\sum_{a\in\mathbb F^\times}\psi(a)\rho(a),\qquad G^\vee=\sum_{a\in\mathbb F^\times}\psi(-a)\rho(a^{-1}).$$ If $v\in V$ satisfies $\sum_{a\in\mathbb F^\times}\rho(a)v=0$, then $$GG^\vee v=|\mathbb F|\,v,\qquad G^\vee Gv=|\mathbb F|\,v.$$
