---
{
  "module": "src/Formalism/PeriodIntegrals/OrbitalBoundsConclusion/UnitaryDense.lean",
  "declarations": [
    "unitaryGroupDense_holds"
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

## The unitary group is Zariski dense in matrix space

[Theorem ALG.0496](https://andrewodesky.com/rh/lean/unitaryGroupDense_holds/)

Let $n\ge0$ and let $P\in\mathbb C[X_{ij}:1\le i,j\le n]$. If $$P(U)=0\qquad\text{for every }U\in M_n(\mathbb C)\text{ with }U^*U=I_n,$$ then $P=0$. Here $U^*$ is the conjugate transpose.
