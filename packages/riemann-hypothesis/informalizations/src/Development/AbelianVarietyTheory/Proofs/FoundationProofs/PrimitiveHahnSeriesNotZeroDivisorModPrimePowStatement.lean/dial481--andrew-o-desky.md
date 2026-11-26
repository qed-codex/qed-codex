---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/PrimitiveHahnSeriesNotZeroDivisorModPrimePowStatement.lean",
  "declarations": [
    "GlobalTheory.T.primitiveHahnSeries_not_zeroDivisor_modPrimePow"
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

## Cancellation modulo prime powers for a primitive Hahn series

[Theorem ALG.1026](https://andrewodesky.com/rh/lean/GlobalTheory.T.primitiveHahnSeries_not_zeroDivisor_modPrimePow/)

Let $\Omega$ be an algebraic closure of $\mathbb Q$, let $\ell$ be prime, and let $A\subset\Omega$ be a valuation ring in which $\ell$ is a nonunit. Let $n\ge0$, $L\ge1$, and let $P,\phi\in\Omega((t^{\mathbb Q}))$ be Hahn series. Suppose all coefficients of $P$ and $\phi$ lie in $A$, at least one coefficient of $P$ is a unit of $A$, and $$P_r\ne0\ \Longrightarrow\ Lr\in\mathbb Z\qquad(r\in\mathbb Q).$$ If every coefficient of $\phi P$ lies in $\ell^nA$, then every coefficient of $\phi$ lies in $\ell^nA$.
