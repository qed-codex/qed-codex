---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/UnimodularIndex/PairwiseDisjointCosets.lean",
  "declarations": [
    "PI.UnimodIdxWork.unimodIdx_main"
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

## Right invariance of Haar measure from conjugate subgroup indices

[Theorem ALG.1095](https://andrewodesky.com/rh/lean/PI.UnimodIdxWork.unimodIdx_main/)

Let $G$ be a topological group with its Borel sigma-algebra and a sigma-finite left Haar measure $\mu$. Suppose there are open subgroups $U_n$ such that every neighborhood of $1$ contains some $U_n$. Let $K$ be a compact open subgroup such that, for every $x\in G$, $$[xKx^{-1}:xKx^{-1}\cap K]=[x^{-1}Kx:x^{-1}Kx\cap K].$$ Then $\mu$ is right invariant.
