---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/DiscreteValuationNumbers/AssemblyCN.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.NumbersDVR.HilbFnCut.full",
    "GroundTheory.Heights₂.Heights.NumbersDVR.PrimeFiltration.full"
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

## Hilbert functions after a regular homogeneous cut

[Theorem ALG.1258](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.NumbersDVR.HilbFnCut.full/)

Let $F$ be a field, $K$ a finite set, and $I_k$ finite coordinate sets. Give $R=F[X_{k,i}]$ its block multigrading. Let $J\subseteq R$ be a multihomogeneous ideal and $x\in R$ multihomogeneous of degree $e\in\mathbb N^K$. Assume $xy\in J$ implies $y\in J$ for every $y\in R$. For $m\in\mathbb Z^K$, let $h_J(m)$ be the dimension of the degree-$m$ part of $R/J$, interpreted as zero outside nonnegative multidegrees. Then $$h_{J+(x)}(m)=h_J(m)-h_J(m-e)\qquad(m\in\mathbb Z^K).$$

## Prime decomposition of multigraded Hilbert functions and local lengths

[Theorem ALG.1291](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.NumbersDVR.PrimeFiltration.full/)

Let $F$ be a field, $K$ a finite set, and $I_k$ a finite set for each $k\in K$. Give $A=F[X_{k,i}:k\in K,\ i\in I_k]$ the block multigrading $\deg X_{k,i}=e_k$. For a multihomogeneous ideal $J$, put $h_J(m)=\dim_F(A/J)_m$ for $m\in\mathbb Z^K$ with nonnegative coordinates, and $h_J(m)=0$ otherwise. For a prime ideal $W$, put $$\lambda_W(J)=\operatorname{length}_{A_W}(A/J)_W\in\mathbb N\cup\{\infty\}.$$ There is a finite list $(P_a,s_a)_{a=1}^{t}$, with repetitions allowed, such that each $P_a$ is a multihomogeneous prime containing $J$, each $s_a\in\mathbb N^K$, and $$h_J(m)=\sum_{a=1}^{t}h_{P_a}(m-s_a)\quad(m\in\mathbb Z^K),\qquad \lambda_W(J)=\sum_{a=1}^{t}\lambda_W(P_a)\quad(W\text{ prime}).$$
