---
{
  "module": "src/Formalism/DistinguishedUnitIdeals/DistinguishedOrderProofs/PolynomialEvaluationValuation.lean",
  "declarations": [
    "Formalism.ExponentWindows.E.factorial_valuation_holds"
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

## Exact divisibility of powers of a principal unit

[Theorem ALG.1070](https://andrewodesky.com/rh/lean/Formalism.ExponentWindows.E.factorial_valuation_holds/)

Let $O$ be a commutative local ring, let $\ell\ge3$ be prime, and suppose $\ell$ is not a unit in $O$. Let $u,x\in O^\times$ satisfy $u=1+\ell x$. For every nonzero integer $m$ there is a unit $\varepsilon\in O^\times$ such that $$1-u^m=\varepsilon\ell^{1+v_\ell(m)}.$$
