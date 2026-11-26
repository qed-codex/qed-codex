---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/ExistsIsLatticeFrameIsMajorantFrame.lean",
  "declarations": [
    "GlobalTheory.AdelicU.Frames.exists_isLatticeFrame_of_arch"
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

## Adelic lattice frames with prescribed infinite components

[Theorem ANT.1451](https://andrewodesky.com/rh/lean/GlobalTheory.AdelicU.Frames.exists_isLatticeFrame_of_arch/)

Let $E/F$ be an extension of number fields, $n\ge0$, and let $L\subset E^n$ be an $\mathcal O_E$-lattice. For each infinite place $w$ of $F$, choose $$c_w\in\operatorname{GL}_n(F_w\otimes_F E).$$ There exists $a\in\operatorname{GL}_n(\mathbb A_F\otimes_F E)$ whose component at every infinite place is $c_w$ and such that, at every finite place $v$ of $F$, $$y\in(\mathcal O_{F_v}\otimes_{\mathcal O_F}\mathcal O_E)^n \quad\Longleftrightarrow\quad a_v y\in L_v.$$ Here both modules are viewed in $(F_v\otimes_F E)^n$, and $L_v$ is the localized completed lattice.
