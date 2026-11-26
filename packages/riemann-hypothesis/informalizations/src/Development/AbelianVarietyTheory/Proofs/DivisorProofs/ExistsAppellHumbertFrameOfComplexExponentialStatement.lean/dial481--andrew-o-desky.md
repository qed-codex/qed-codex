---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsAppellHumbertFrameOfComplexExponentialStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_appellHumbertFrame_of_complexExponential"
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

## Appell-Humbert frames for a prescribed complex exponential

[Theorem AV.0714](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_appellHumbertFrame_of_complexExponential/)

Let $A/\mathbb C$ be a commutative abelian variety of dimension $g$, let $M$ be a line bundle on $A$, and let $e:\mathbb C^g\to A(\mathbb C)$ be a surjective holomorphic group homomorphism whose differential at zero is a bijection onto the algebraic tangent space. There are a discrete $\mathbb Z$-submodule $\Lambda=\ker e$ spanning $\mathbb C^g$ over $\mathbb R$, a Hermitian matrix $H\in M_g(\mathbb C)$, and $\chi:\Lambda\to\mathbb C$ with $|\chi(\lambda)|=1$, together with a nowhere-zero holomorphic frame of $e^*M$, such that in each algebraic trivialization of $M$ its representing function $f_i$ satisfies $$f_i(z)=\chi(\lambda)\exp\left(\pi z^tH\overline\lambda+\frac\pi2\lambda^tH\overline\lambda\right)f_i(z+\lambda)\qquad(\lambda\in\Lambda).$$
