---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/NormLeTsumOfCubeFourierCoeffLe.lean",
  "declarations": [
    "GlobalTheory.phKoecher"
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

## Boundedness on a Siegel half-space away from its boundary

[Theorem AGR.1432](https://andrewodesky.com/rh/lean/GlobalTheory.phKoecher/)

Let $g\ge2$ and $N\ge1$ be integers. Write $\mathfrak H_g$ for the complex symmetric $g\times g$ matrices with positive definite imaginary part. Suppose $F:\mathfrak H_g\to\mathbb C$ is holomorphic and satisfies $$F(\tau+NB)=F(\tau)\qquad(B\in M_g(\mathbb Z),\ B^t=B),$$ and $$F(U\tau U^t)=F(\tau)\qquad(U\in\operatorname{SL}_g(\mathbb Z),\ U\equiv I_g\pmod N).$$ For every real $c>0$ there is a real $K$ such that $$|F(\tau)|\le K\qquad\text{whenever }\tau\in\mathfrak H_g\text{ and }\Im\tau-cI_g\text{ is positive semidefinite}.$$
