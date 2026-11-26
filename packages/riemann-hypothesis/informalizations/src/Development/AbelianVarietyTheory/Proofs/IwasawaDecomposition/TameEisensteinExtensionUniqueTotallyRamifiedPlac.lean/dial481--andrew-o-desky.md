---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/TameEisensteinExtensionUniqueTotallyRamifiedPlac.lean",
  "declarations": [
    "GlobalTheory.TameRecPlace.main"
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

## The unique place in a tame uniformizer-root extension

[Theorem ANT.0354](https://andrewodesky.com/rh/lean/GlobalTheory.TameRecPlace.main/)

Let $E$ be a number field, $\Omega/E$ a field extension, $v$ a nonzero prime of $\mathcal O_E$, and $A\subseteq\Omega$ a valuation ring above $v$. Put $q=|\mathcal O_E/v|$ and choose $\varpi\in v\setminus v^2$. Let $\pi\in\Omega$ satisfy $$\pi^{q-1}=\varpi,$$ and assume $L=E(\pi)\subseteq\Omega$ is finite over $E$, with its number-field structure. There is exactly one prime $W$ of $\mathcal O_L$ above $v$. The valuation ring $A$ lies above $W$, the prime $W$ has residue cardinality $|\mathcal O_L/W|=q$, and the image of $\pi$ in $L_W$ is a uniformizer.
