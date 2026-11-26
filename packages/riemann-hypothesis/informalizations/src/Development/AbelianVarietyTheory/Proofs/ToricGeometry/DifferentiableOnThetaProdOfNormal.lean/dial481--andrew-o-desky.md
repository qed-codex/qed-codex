---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ToricGeometry/DifferentiableOnThetaProdOfNormal.lean",
  "declarations": [
    "GlobalTheory.thetaHolo_of_domainOpen_of_mTest"
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

## Joint holomorphy of the theta series from normal convergence

[Theorem AV.1482](https://andrewodesky.com/rh/lean/GlobalTheory.thetaHolo_of_domainOpen_of_mTest/)

For each finite index set of size $g$, put $$\mathcal D_g=\{\tau\in M_g(\mathbb C):\operatorname{Im}\tau+(\operatorname{Im}\tau)^T\text{ is positive definite}\}.$$ Assume $\mathcal D_g$ is open for every $g$. Assume also that for every $a\in\mathbb R^g$ and compact $K\subseteq\mathbb C^g\times\mathcal D_g$ there is a summable family $(u_l)_{l\in\mathbb Z^g}$ of real numbers such that, for all $b\in\mathbb R^g$, $(z,\tau)\in K$ and $l\in\mathbb Z^g$, $$\left|\exp\left(2\pi i\left[\tfrac12(l+a)^T\tau(l+a)+(l+a)^T(z+b)\right]\right)\right|\le u_l.$$ Then for every $a,b\in\mathbb R^g$ the function $$\theta[a,b](z,\tau)=\sum_{l\in\mathbb Z^g}\exp\left(2\pi i\left[\tfrac12(l+a)^T\tau(l+a)+(l+a)^T(z+b)\right]\right)$$ is jointly complex differentiable on $\mathbb C^g\times\mathcal D_g$.
