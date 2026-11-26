---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/RealDescent/LyingOverPrimes/InertThin.lean",
  "declarations": [
    "PositivityTheory.Rg.BcB.Desc.inertThin_holds"
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

## Summability over nonsplit primes of a CM field

[Theorem ANT.1588](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.BcB.Desc.inertThin_holds/)

Let $E$ be a CM number field and $E^+$ its maximal totally real subfield. Then $$\sum_{\substack{\mathfrak p\subset\mathcal O_E\text{ nonzero prime}\\\mathfrak p\text{ lies over a nonsplit prime of }E^+}}\frac1{N_{E/\mathbb Q}\mathfrak p}<\infty.$$ Here nonsplit includes inert and ramified primes in $E/E^+$.
