---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsIsMeasDef.lean",
  "declarations": [
    "GlobalTheory.Mem.DefiniteMeasure.exists_probHaar"
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

## The probability Haar measure on a definite unitary group

[Theorem REP.0240](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.DefiniteMeasure.exists_probHaar/)

Let $p,q\ge0$ satisfy $p=0$ or $q=0$, and let $G=U(p,q)$ with its usual matrix topology and Borel measurable structure. There exists a Haar measure $\nu$ on $G$ such that, for every Borel measure $m$ on $G$, $$m\text{ is a Haar probability measure}\quad\Longleftrightarrow\quad m=\nu.$$
