---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/DiscreteValuationNumbers/PPolynomialLocalizedLength.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.NumbersDVR.PolynomialLocalizedLength.full"
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

## Localized quotient length is unchanged by adjoining a polynomial variable

[Theorem ALG.1750](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.NumbersDVR.PolynomialLocalizedLength.full/)

Let $R$ be a commutative ring, $\mathfrak q\subseteq R$ a prime ideal, and $I\subseteq R$ an ideal. Write $\mathfrak qR[X]$ and $IR[X]$ for their extensions to the polynomial ring. Then $$\operatorname{length}_{R[X]_{\mathfrak qR[X]}}\left((R[X]/IR[X])_{\mathfrak qR[X]}\right) =\operatorname{length}_{R_{\mathfrak q}}\left((R/I)_{\mathfrak q}\right).$$
