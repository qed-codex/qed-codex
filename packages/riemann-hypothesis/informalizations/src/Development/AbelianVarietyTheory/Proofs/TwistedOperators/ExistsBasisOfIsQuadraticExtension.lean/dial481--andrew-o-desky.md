---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsBasisOfIsQuadraticExtension.lean",
  "declarations": [
    "GlobalTheory.QuadSymbol.normTheorem"
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

## The local-global norm criterion for a quadratic extension

[Theorem ANT.1660](https://andrewodesky.com/rh/lean/GlobalTheory.QuadSymbol.normTheorem/)

Let $L/K$ be a quadratic extension of number fields. For every $t\in K^\times$, $$t\in N_{L/K}(L^\times) \quad\Longleftrightarrow\quad t\in N_{(L\otimes_K K_v)/K_v}\bigl((L\otimes_K K_v)^\times\bigr) \ \text{for every finite or infinite place }v\text{ of }K.$$
