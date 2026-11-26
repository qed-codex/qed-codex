---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/WeilRepresentationIntertwinesHeisenbergStatement.lean",
  "declarations": [
    "GlobalTheory.T.weilRepresentation_intertwines_heisenberg"
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

## Heisenberg covariance of the local Weil representation

[Theorem REP.1690](https://andrewodesky.com/rh/lean/GlobalTheory.T.weilRepresentation_intertwines_heisenberg/)

Use the data of ([Local Weil data and action formulas](https://andrewodesky.com/rh/lean/GlobalTheory.KSp.IsKW/)), and let $\kappa\in\mathbb C$ and a complex-linear representation $\omega$ of $G$ on $\mathcal S(V)$ satisfy the local Weil action formulas.

For $w=(a,b)\in M_{\alpha,\nu\sqcup\nu}(E)$, define the Heisenberg operator by $$[H_{\psi,Q}(a,b)\phi](x)=\psi\bigl(\beta_Q(x,b)+\tfrac12\beta_Q(a,b)\bigr)\phi(x+a).$$ Then, for every $g\in G$ and $w\in M_{\alpha,\nu\sqcup\nu}(E)$, $$H_{\psi,Q}(w)\,\omega(g)=\omega(g)\,H_{\psi,Q}(wg).$$
