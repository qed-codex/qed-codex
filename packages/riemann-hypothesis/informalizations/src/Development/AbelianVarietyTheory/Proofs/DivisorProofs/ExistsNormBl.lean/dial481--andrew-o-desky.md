---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsNormBl.lean",
  "declarations": [
    "GlobalTheory.NormBlowupField.exists_normBl"
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

## Normalized blowups away from an ideal's vanishing locus

[Theorem AG.1476](https://andrewodesky.com/rh/lean/GlobalTheory.NormBlowupField.exists_normBl/)

Let $k$ be a field of characteristic zero, let $Z\to\operatorname{Spec}k$ be projective with $Z$ normal, and let $\mathcal J$ be an ideal sheaf on $Z$. Let $W\subseteq Z$ be a dense open set disjoint from $\operatorname{Supp}(\mathcal O_Z/\mathcal J)$. There exist a normal scheme $S$, a morphism $\pi:S\to Z$, and an effective Cartier divisor $D$ on $S$, such that $S$ is projective over $k$, $\pi$ is proper, $\mathcal I_D=\mathcal J\mathcal O_S$, and $$\pi^{-1}(W)\xrightarrow{\sim}W,\qquad\overline{\pi^{-1}(W)}=S.$$ Moreover, $\pi$ factors through the blowup $Z_0=\operatorname{Bl}_{\mathcal J}Z$ by a finite map $\nu:S\to Z_0$ which is an isomorphism over some dense open subset $U\subseteq Z_0$, with $\nu^{-1}(U)$ dense in $S$.
