---
{
  "module": "src/Development/WeilBound/ThetaLifts/LeviDeterminants/ThetaBasic.lean",
  "declarations": [
    "PositivityTheory.ThKF0.thetaBasic"
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

## Continuity, invariance, and growth of theta series

[Theorem THETA.1448](https://andrewodesky.com/rh/lean/PositivityTheory.ThKF0.thetaBasic/)

Let $F,E$ be number fields with an $F$-automorphism $\sigma$ of $E$, and assume the source's full matched Weil pair conditions for a base datum, a Hermitian space $X$ of rank $n$ and signature $(r,s)$, a skew-Hermitian space $W$ of rank $d$ and signature $(r',s')$, a Schrodinger model, two splitting Hecke characters, and a Weil action $\omega$. For $\Phi\in\mathcal S(\mathbb A_F^{n\times d})$, let $\theta_\Phi(g,h)$ be the associated theta series on $U(X)(\mathbb A_F)\times U(W)(\mathbb A_F)$, and let $H_X,H_W$ be the restrictions of the fixed adelic general linear matrix heights.

The function $\theta_\Phi$ is continuous and satisfies $$\theta_\Phi(\gamma g,\gamma' h)=\theta_\Phi(g,h)\qquad(\gamma\in U(X)(F),\ \gamma'\in U(W)(F)).$$ There are $C\in\mathbb R$ and an integer $k\ge0$ such that $$|\theta_\Phi(g,h)|\le C\bigl(H_X(g)H_W(h)\bigr)^k\qquad\text{for all }g,h.$$ For any fixed finite adelic Schwartz–Bruhat function $\varphi$ and any $g,h$, the map $f\mapsto\theta_{f\otimes\varphi}(g,h)$ is continuous on the archimedean Schwartz space.
