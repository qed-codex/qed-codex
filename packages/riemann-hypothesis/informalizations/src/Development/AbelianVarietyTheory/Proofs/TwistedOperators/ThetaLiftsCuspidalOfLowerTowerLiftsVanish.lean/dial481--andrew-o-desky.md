---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ThetaLiftsCuspidalOfLowerTowerLiftsVanish.lean",
  "declarations": [
    "GlobalTheory.PairLift.cuspAll_of_lowAll"
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

## Cuspidality from vanishing of lower theta lifts

[Theorem THETA.1394](https://andrewodesky.com/rh/lean/GlobalTheory.PairLift.cuspAll_of_lowAll/)

Fix the source's full arithmetic datum and chosen family of unitary discrete-series models. Assume its theta-lift input package and the following lower-tower vanishing assertion, for every permitted pair of archimedean signed parameters and splitting-character exponents: every theta lift to a unitary space obtained by lowering both signature entries by $i\ge1$ vanishes, for all source automorphic realizations, smooth vectors, and permitted theta functions.

For any such parameter pair, let $V,W$ be the permitted unitary spaces, with the prescribed discrete-series models on both sides. Choose a compatible family of infinite-place embeddings and additive character, a Weil action with splitting characters of the prescribed exponents, a Haar measure on $U(W)(\mathbb A)$ and a fundamental domain for $U(W)(F)$. For any automorphic realization $F_0$ in the source's multiplicity space with empty prescribed finite-place set and trivial character, any smooth tensor vector $v$, and any permitted theta function $f$, the lift $$g\longmapsto\int_{[U(W)]}\theta_{\omega,f}(g,h)F_0(v)(h)\,dh$$ is a cuspidal automorphic function on $U(V)(\mathbb A)$.
