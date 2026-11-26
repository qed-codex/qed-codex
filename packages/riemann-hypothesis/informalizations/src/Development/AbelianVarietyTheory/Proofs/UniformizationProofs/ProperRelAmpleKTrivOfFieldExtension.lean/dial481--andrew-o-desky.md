---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UniformizationProofs/ProperRelAmpleKTrivOfFieldExtension.lean",
  "declarations": [
    "GlobalTheory.AmpleDescent.proper_relAmple_kTriv_of_fieldExtension"
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

## Descent of properness and line-bundle properties across a field extension

[Theorem AV.0696](https://andrewodesky.com/rh/lean/GlobalTheory.AmpleDescent.proper_relAmple_kTriv_of_fieldExtension/)

Let $K\to K'$ be a field homomorphism. Let $G$ be a smooth, quasi-compact, separated group scheme over $K$ and $G'$ a group scheme over $K'$, with a group-compatible Cartesian identification $G'\simeq G\times_K K'$. Let $L,L'$ be line bundles on $G,G'$ and assume $L'\simeq L|_{G'}$. If $G'$ is proper, $L'$ is relatively ample, and $L'$ has trivial translation kernel in the sense below, then $G$ is proper, $L$ is relatively ample, and $L$ has trivial translation kernel.
