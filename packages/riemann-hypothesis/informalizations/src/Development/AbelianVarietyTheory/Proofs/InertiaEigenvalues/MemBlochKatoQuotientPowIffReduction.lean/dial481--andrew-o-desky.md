---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/MemBlochKatoQuotientPowIffReduction.lean",
  "declarations": [
    "GlobalTheory.BKTorsionRed.mem_HfQ_iff_red"
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

## Finite local cocycles modulo a power are reductions of integral cocycles

[Theorem GC.0376](https://andrewodesky.com/rh/lean/GlobalTheory.BKTorsionRed.mem_HfQ_iff_red/)

Fix a prime $\ell$, a local period datum $P$ with the period-ring, scalar-map and Galois-action structures in ([Exactness of crystalline invariants for regular period data](https://andrewodesky.com/rh/lean/GlobalTheory.RegularRing.dcrisExact/)), a finite extension $K/\mathbb Q_\ell$, and a finite extension $L/\mathbb Q_\ell$ with its finite-dimensional vector-space topology. Let $O$ be a discrete valuation domain with fraction field $L$ whose image in $L$ is open. Let $V$ be a finite-dimensional continuous $L$-representation of $G_K$ with a stable $O$-lattice $\Lambda$. Let $\varpi\in O$ and $r\ge0$, and suppose $\varpi^r\Lambda$ is stable. A map $c:G_K\to\Lambda/\varpi^r\Lambda$ belongs to the finite-cocycle submodule defined in the conventions below if and only if there is a continuous lattice-valued cocycle $a:G_K\to\Lambda$ whose associated $V$-valued cocycle is finite and whose reduction is exactly $c$.
