---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/CardSpacedDetectedLe.lean",
  "declarations": [
    "GlobalTheory.SpacedDetected.card_spaced_detected_le"
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

## Counting spaced points detected by character sums

[Theorem ANT.0409](https://andrewodesky.com/rh/lean/GlobalTheory.SpacedDetected.card_spaced_detected_le/)

There is an absolute constant $C>0$ with the following property. Let $Q\ge2$ be an integer and let $\mathcal T$ be a finite set of triples $(q,\chi,\rho)$, where $1\le q\le Q$, $\chi$ is a primitive complex Dirichlet character modulo $q$, and $\rho\in\mathbb C$. Suppose each triple satisfies $$1-\frac1{400}\le\Re\rho\le1,\qquad |\Im\rho|\le Q,$$ $$\left|\sum_{Q^3<n\le Q^6}\left(\sum_{\substack{d\mid n\\d\le Q^3}}\mu(d)\right)\chi(n)n^{-\rho}\right|\ge\frac12,$$ where $\mu$ is the Möbius function. Suppose also that triples with the same $(q,\chi)$ and distinct $\rho,\rho'$ satisfy $|\Im\rho-\Im\rho'|\ge1$. Then $$|\mathcal T|\le C Q^{1/8}.$$
