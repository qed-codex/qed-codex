---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/FiniteAbsLeOneMulMemRange.lean",
  "declarations": [
    "GlobalTheory.phHolo_of_phKoecher"
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

## Constancy of invariant holomorphic Siegel functions from a boundedness input

[Theorem THETA.1391](https://andrewodesky.com/rh/lean/GlobalTheory.phHolo_of_phKoecher/)

Assume the following boundedness assertion for every genus $g\ge2$ and integer $N\ge1$: a holomorphic function $F$ on Siegel upper half-space $\mathfrak H_g$ invariant under $\tau\mapsto\tau+NB$ for every integral symmetric $B$, and under $\tau\mapsto U\tau U^{\mathsf T}$ for every $U\in\mathrm{SL}_g(\mathbb Z)$ with $U\equiv1\pmod N$, is bounded on every region $\operatorname{Im}\tau\ge cI$ with $c>0$.

Then for every $g\ge2$, every holomorphic function $H:\mathfrak H_g\to\mathbb C$ invariant under the action $\tau\mapsto(A\tau+B)(C\tau+D)^{-1}$ for every $\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\in\operatorname{Sp}_{2g}(\mathbb Z)$ is constant: $$H(\tau)=z\qquad(\tau\in\mathfrak H_g)$$ for some $z\in\mathbb C$.
