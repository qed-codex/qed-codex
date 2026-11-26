---
{
  "module": "src/CompanionTheory/AutomorphicTheory/ProductFormulaTheory/GrothendieckRingPolynomial/TriSupportedLe.lean",
  "declarations": [
    "CompanionTheory.Groth.triAut"
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

## Invertibility of a polynomial map triangular in natural-number weights

[Theorem ALG.0457](https://andrewodesky.com/rh/lean/CompanionTheory.Groth.triAut/)

Let $\Sigma$ be any set, $w:\Sigma\to\mathbb N$, and $\psi:\mathbb Z[X_s:s\in\Sigma]\to\mathbb Z[X_s:s\in\Sigma]$ a ring homomorphism. Suppose for every $s\in\Sigma$, $$\psi(X_s)=\varepsilon_sX_s+P_s,\qquad\varepsilon_s\in\{1,-1\},$$ where every variable $X_t$ occurring in $P_s$ has $w(t)<w(s)$. Then $\psi$ is bijective.
