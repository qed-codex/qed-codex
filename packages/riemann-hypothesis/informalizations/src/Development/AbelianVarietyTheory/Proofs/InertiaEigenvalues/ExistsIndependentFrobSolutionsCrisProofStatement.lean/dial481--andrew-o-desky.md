---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsIndependentFrobSolutionsCrisProofStatement.lean",
  "declarations": [
    "GlobalTheory.T.existsIndependentFrobSolutionsCris_proof"
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

## Independent crystalline Frobenius solutions with a filtration relation

[Theorem PHT.0331](https://andrewodesky.com/rh/lean/GlobalTheory.T.existsIndependentFrobSolutionsCris_proof/)

Let $\ell$ be prime and fix the local crystalline, de Rham and integral period data, with their Fontaine-ring identifications, specified in ([Hodge jumps under uniform trace approximation](https://andrewodesky.com/rh/lean/GlobalTheory.LimitTop.closedAtL/)). Let $h\ge2$ and $\mu_0,\ldots,\mu_{h-1}\in B_{\mathrm{dR}}$ satisfy $$\mu_i\in\operatorname{Fil}^0B_{\mathrm{dR}}\quad\text{for all }i,\qquad\mu_i\notin\operatorname{Fil}^1B_{\mathrm{dR}}\quad\text{for at least one }i.$$ There are $b_0,\ldots,b_{h-1}\in B_{\mathrm{cris}}$, linearly independent over $\mathbb Q_\ell$, such that $$b_j\in B_{\mathrm{cris}}^+,\qquad\varphi^h(b_j)=\ell b_j,\qquad \sum_{i=0}^{h-1}\mu_i\,\iota\bigl(\varphi^i(b_j)\bigr)\in\operatorname{Fil}^1B_{\mathrm{dR}}\quad(0\le j<h).$$
