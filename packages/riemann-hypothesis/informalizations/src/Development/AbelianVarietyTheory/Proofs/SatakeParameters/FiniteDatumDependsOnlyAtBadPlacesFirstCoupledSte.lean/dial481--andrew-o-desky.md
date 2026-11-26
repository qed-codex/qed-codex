---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/FiniteDatumDependsOnlyAtBadPlacesFirstCoupledSte.lean",
  "declarations": [
    "GlobalTheory.TwV.AwayCpl.exists_approx"
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

## Simultaneous residue approximation in different frames

[Theorem ANT.0857](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_vector_prescribed_residues_in_frames/)

Let $E$ be a number field, $n\ge0$, and $S$ a finite set of nonzero prime ideals of $\mathcal O_E$. For each $\mathfrak p\in S$, choose an $E$-linear automorphism $f_{\mathfrak p}:E^n\to E^n$, a vector $y_{\mathfrak p}\in E^n$, and an integer $e_{\mathfrak p}\ge0$. Put $q_{\mathfrak p}=\#(\mathcal O_E/\mathfrak p)$. There is $y\in E^n$ such that $$f_{\mathfrak p}^{-1}y-y_{\mathfrak p}\in q_{\mathfrak p}^{\,e_{\mathfrak p}}(\mathcal O_{E,\mathfrak p})^n\qquad(\mathfrak p\in S),$$ where $\mathcal O_{E,\mathfrak p}$ is the localization of $\mathcal O_E$ at $\mathfrak p$.
