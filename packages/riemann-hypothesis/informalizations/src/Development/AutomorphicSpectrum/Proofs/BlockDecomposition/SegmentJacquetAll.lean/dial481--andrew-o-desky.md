---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SegmentJacquetAll.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.SegCoarse.fineJac_all"
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

## Multiplicity and order of cuspidal Jacquet factors of a segment

[Theorem REP.1551](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.SegCoarse.fineJac_all/)

Assume ([Admissibility of smooth irreducible general linear representations](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.SmGLBridge.irreducibleAdmissible/)) and ([Unique irreducible subrepresentation of a segment](https://andrewodesky.com/rh/lean/PositivityTheory.RgGu.segmentRepresentation/)). Let $k$ be a nonarchimedean local field and $\Delta$ a segment of length $l$, whose irreducible factors in decreasing order are $\rho_1,\ldots,\rho_l$. Let $\pi$ be an irreducible representation of $\operatorname{GL}_N(k)$ admitting an equivariant surjection from $\rho_l\times\cdots\times\rho_1$ whose kernel equals every maximal proper subrepresentation of this induced product; the products are normalized parabolic inductions.

For an ordered tuple $\boldsymbol\tau=(\tau_1,\ldots,\tau_c)$ of irreducible smooth representations whose ranks sum to $N$, write $j_{\boldsymbol\tau}(\pi)$ for the multiplicity of $\tau_1\otimes\cdots\otimes\tau_c$ in the normalized Jacquet module for the corresponding ordered block parabolic. Then $$j_{(\rho_1,\ldots,\rho_l)}(\pi)=1.$$ If all $\tau_i$ are cuspidal and $j_{\boldsymbol\tau}(\pi)\ge1$, then $c=l$ and $\tau_i=\rho_i$ for every $i$.
