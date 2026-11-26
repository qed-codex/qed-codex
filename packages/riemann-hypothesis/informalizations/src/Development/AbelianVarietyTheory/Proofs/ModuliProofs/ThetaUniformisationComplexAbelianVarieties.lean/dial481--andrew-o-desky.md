---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/ThetaUniformisationComplexAbelianVarieties.lean",
  "declarations": [
    "GlobalTheory.thetaUnifAV_closed"
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

## Theta functions for a principally polarized complex abelian variety

[Theorem AV.1663](https://andrewodesky.com/rh/lean/GlobalTheory.thetaUnifAV_closed/)

Let $A/\mathbb C$ be an abelian variety of dimension $g$, with a rigidified symmetric ample line bundle $L$ defining a principal polarization, and choose a nonzero generator of its fiber at the identity. There exist a surjective holomorphic group homomorphism $e:\mathbb C^g\to A(\mathbb C)$ with discrete kernel $\Lambda$ spanning $\mathbb C^g$ over $\mathbb R$, a positive-definite Hermitian matrix $M$, and $\chi:\Lambda\to\mathbb C$ with $|\chi(\lambda)|=1$. Put $H(z,w)=z^TM\overline w$. In algebraic trivializations of $L$, there are compatible nowhere-zero holomorphic functions $f_i$ trivializing $e^*L$, agreeing with the chosen generator at $0$, such that $$f_i(z)=\chi(\lambda)e^{\,\pi H(z,\lambda)+\pi H(\lambda,\lambda)/2}f_i(z+\lambda).$$ The differential of $e$ identifies $\mathbb C^g$ bijectively with the algebraic tangent space of $A$ at the identity. Every algebraic group endomorphism of $A$ lifts through $e$ to a complex-linear endomorphism of $\mathbb C^g$.

For every $n\ge0$, the sections $s\in H^0(A,L^{\otimes n})$ correspond bijectively to entire functions $\theta:\mathbb C^g\to\mathbb C$ satisfying $$\theta(z+\lambda)= \left(\chi(\lambda)e^{\,\pi H(z,\lambda)+\pi H(\lambda,\lambda)/2}\right)^n\theta(z),$$ by $s_i(e(z))=\theta(z)f_i(z)^n$ in each trivialization. There is an integer bilinear form $E:\Lambda\times\Lambda\to\mathbb Z$ with $$E(a,b)=\operatorname{Im}H(a,b)$$ whose map $\Lambda\to\operatorname{Hom}_{\mathbb Z}(\Lambda,\mathbb Z)$ is bijective. For every $k>0$, the Weil pairing attached to $L$ on $A[k]$ satisfies, with the following sign convention, $$e_k^L\bigl(e(a/k),e(b/k)\bigr) =\exp\!\left(-\frac{2\pi i\,E(a,b)}{k}\right)\qquad(a,b\in\Lambda).$$
