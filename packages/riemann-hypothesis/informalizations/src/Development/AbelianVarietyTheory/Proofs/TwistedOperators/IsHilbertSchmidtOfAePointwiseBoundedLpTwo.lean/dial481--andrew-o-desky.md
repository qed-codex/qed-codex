---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/IsHilbertSchmidtOfAePointwiseBoundedLpTwo.lean",
  "declarations": [
    "GlobalTheory.isHilbertSchmidt_of_ae_bounded"
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

## A pointwise bound implies the Hilbert–Schmidt property

[Theorem ALG.1628](https://andrewodesky.com/rh/lean/GlobalTheory.isHilbertSchmidt_of_ae_bounded/)

Let $(X,\nu)$ be a finite measure space, $H$ a complex Hilbert space, and $T:H\to L^2(X,\nu)$ a bounded complex-linear map. Suppose there is $C\in\mathbb R$ such that, for every $v\in H$, $$|(Tv)(x)|\le C\|v\|\quad\text{for almost every }x.$$ Then $T$ is Hilbert–Schmidt: for an orthonormal basis $(e_i)$ of $H$, $$\sum_i\|Te_i\|_{L^2}^2<\infty.$$ The exceptional null set may depend on $v$.
