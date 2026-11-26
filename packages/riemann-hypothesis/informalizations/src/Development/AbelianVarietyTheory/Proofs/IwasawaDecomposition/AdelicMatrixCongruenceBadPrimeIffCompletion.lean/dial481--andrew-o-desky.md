---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/AdelicMatrixCongruenceBadPrimeIffCompletion.lean",
  "declarations": [
    "GlobalTheory.Mem.Col2.AdT.AdelicValuationDictionary.exists_clear"
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

## Clearing adelic denominators away from a prescribed prime

[Theorem ANT.0713](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.Col2.AdT.AdelicValuationDictionary.exists_clear/)

Let $E$ be a number field, $\mathfrak p\subset\mathcal O_E$ a nonzero prime ideal, and $y=(y_{\mathfrak q})\in\mathbb A_{E,f}$. If $y_{\mathfrak p}\in\mathcal O_{E_{\mathfrak p}}$, there exists $s\in\mathcal O_E\setminus\mathfrak p$ such that $$s\,y_{\mathfrak q}\in\mathcal O_{E_{\mathfrak q}}\qquad\text{for every nonzero prime }\mathfrak q\subset\mathcal O_E.$$
