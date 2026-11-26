---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/AbelianSchemeLawProofs/UnramExtLaw.lean",
  "declarations": [
    "GlobalTheory.unramExt_law"
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

## Lifting a finite separable residue field extension

[Theorem ALG.1562](https://andrewodesky.com/rh/lean/GlobalTheory.unramExt_law/)

Let $V$ be a discrete valuation ring complete for its maximal-ideal topology, and let $k'/k_V$ be a finite separable extension of its residue field. There are a complete discrete valuation ring $W$ and a finite injective local homomorphism $V\to W$ that is formally unramified, together with an isomorphism $$e:k_W\simeq k'$$ such that, for every $v\in V$, $e(\overline v)$ is the image of the residue of $v$ under the given map $k_V\to k'$.
