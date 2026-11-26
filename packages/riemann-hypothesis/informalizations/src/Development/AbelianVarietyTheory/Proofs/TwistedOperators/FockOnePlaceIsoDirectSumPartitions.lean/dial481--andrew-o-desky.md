---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/FockOnePlaceIsoDirectSumPartitions.lean",
  "declarations": [
    "GlobalTheory.OneFunctional.iso_directSum_fockOne"
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

## Decomposition of a one-place polynomial Fock representation

[Theorem REP.0201](https://andrewodesky.com/rh/lean/GlobalTheory.OneFunctional.iso_directSum_fockOne/)

Let $a,b\ge0$ and $\alpha,\beta\in\mathbb Z$. On $\mathcal P=\mathbb C[Z_{ij}:1\le i\le b,1\le j\le a]$, let $(g,h)\in U(a)\times U(b)$ act by $$((g,h)\cdot f)(Z)=(\det g)^\alpha(\det h)^\beta f(h^tZ\overline g).$$ As a complex representation of $U(a)\times U(b)$, $$\mathcal P\simeq\bigoplus_{\lambda}\left(\det^\alpha\otimes(V_a(\lambda)\circ\mathrm{conj})\right)\otimes\left(\det^\beta\otimes V_b(\lambda)\right).$$
