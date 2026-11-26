---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TorsionCocycleUniformizerPowSmulMemStatement.lean",
  "declarations": [
    "GlobalTheory.T.torsionCocycle_uniformizer_pow_smul_mem"
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

## A common denominator for representatives of a torsion cocycle

[Theorem GC.0537](https://andrewodesky.com/rh/lean/GlobalTheory.T.torsionCocycle_uniformizer_pow_smul_mem/)

Let $\ell$ be prime, $K/\mathbb Q_\ell$ finite, and $L/\mathbb Q_\ell$ finite with its vector-space topology. Let $O\subseteq L$ be an open discrete valuation ring with fraction field $L$, and let $V$ be a finite-dimensional continuous $L$-linear representation of $G_K$. Let $T\subseteq V$ be a $G_K$-stable $O$-lattice and $\varpi\in O$ irreducible. Let $c:G_K\to V/T$ be a locally constant cocycle for the induced action: $$c(gh)=c(g)+g\,c(h).$$ For the fixed choice $s:V/T\to V$ of representatives used to lift quotient classes, there is $r\ge0$ such that $$\varpi^r s(c(g))\in T\qquad(g\in G_K).$$
