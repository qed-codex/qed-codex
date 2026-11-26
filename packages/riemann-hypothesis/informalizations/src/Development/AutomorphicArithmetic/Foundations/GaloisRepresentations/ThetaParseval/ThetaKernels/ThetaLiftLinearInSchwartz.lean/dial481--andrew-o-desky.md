---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/ThetaLiftLinearInSchwartz.lean",
  "declarations": [
    "UpperTheory.thetaLift_linear_in_schwartz"
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

## Sesquilinearity of the theta lift

[Theorem THETA.1701](https://andrewodesky.com/rh/lean/UpperTheory.thetaLift_linear_in_schwartz/)

Assume the source's full theta-tool package. Let $F,E$ be number fields with an $F$-automorphism $\sigma$, and fix a base datum, spaces $X,W$ of dimensions $n,d\ge0$, a Schrödinger model $M$, circle-valued splitting characters $\chi_X,\chi_W$, and a Weil action $\omega$. Assume the source's definite-pair conditions: the base satisfies its CM, imaginary-quadratic-subfield, finite-unramifiedness, and local-character conditions, $X$ satisfies the Hermitian signature-and-lattice package of signature $(n,0)$, $W$ satisfies the skew-Hermitian signature-and-lattice package of signature $(d,0)$ (both including integral duality, Cartan involutions, and prescribed split bases), the model has rational Darboux coordinates, compatible nonzero local vacuum vectors standard almost everywhere, a Haar measure and rational fundamental domain, and the two Hecke characters restrict to $\eta^n,\eta^d$ respectively, where $\eta$ is the quadratic character determined by membership in $F^\times N_{E/F}(\mathbb A_E^\times)$.

Write $\mathcal S$ for the prescribed adelic Schwartz space and $\mathcal A$ for the continuous complex-valued functions on $U(X)(\mathbb A_F)$ invariant on the left under $U(X)(F)$. If $L(\Phi,\phi)$ is the model's theta lift, then for $\Phi,\Phi'\in\mathcal S$, $\phi,\phi'\in\mathcal A$, and $c\in\mathbb C$, $$L(\Phi+\Phi',\phi)=L(\Phi,\phi)+L(\Phi',\phi),\quad L(c\Phi,\phi)=cL(\Phi,\phi),$$ $$L(\Phi,\phi+\phi')=L(\Phi,\phi)+L(\Phi,\phi'),\quad L(\Phi,c\phi)=\overline cL(\Phi,\phi).$$
