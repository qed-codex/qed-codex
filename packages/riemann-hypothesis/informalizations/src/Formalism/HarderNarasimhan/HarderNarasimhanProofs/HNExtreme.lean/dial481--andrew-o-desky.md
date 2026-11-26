---
{
  "module": "src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/HNExtreme.lean",
  "declarations": [
    "Formalism.HN.polygon_extreme_slopes"
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

## Slope lists and ranks of threshold submodules

[Theorem ARAK.0147](https://andrewodesky.com/rh/lean/Formalism.HN.polygon_slopes_characterization/)

Let $R$ be a ring, $V$ an $R$-module, $E$ a finite-dimensional real inner product space, and $\rho:V\to E$ additive. Let $L\subseteq V$ be an $R$-submodule on which $\rho$ is injective, with discrete image. For $A\subseteq L$ put $r(A)=\operatorname{rk}_{\mathbb Z}\rho(A)$, $d(A)=-\log\operatorname{covol}\rho(A)$, and $\mu_0(A)=d(A)/r(A)$, with covolumes in the real span and zero rank assigned degree and slope zero. Let $\mu_{0,\max}(A)$ be the supremum of slopes of nonzero $R$-submodules of $A$, and let $\mu_{0,\min}(A)$ be the infimum of slopes of nonzero quotients obtained by orthogonal projection along saturated $R$-submodules. Saturation means intersection with the real span inside $\rho(A)$; empty extrema are assigned zero.

Put $$H_\theta(L)=\sum_{\substack{0\ne A\subseteq L\\\mu_{0,\min}(A)\ge\theta}}A,\qquad m=r(L),$$ and, for $0\le j<m$, define $$\lambda_j=\sup\{\theta\in\mathbb R:j<r(H_\theta(L))\},\qquad P(k)=\sum_{\substack{0\le j<m\\j<k}}\lambda_j\quad(k\in\mathbb N).$$ The list $\lambda_j$ is nonincreasing and satisfies $$\#\{j:\lambda_j\ge\theta\}=r(H_\theta(L)),\qquad\sum_{j=0}^{m-1}\lambda_j=d(L).$$ Every $R$-submodule $A\subseteq L$ satisfies $d(A)\le P(r(A))$, and every threshold submodule satisfies $$d(H_\theta(L))=P(r(H_\theta(L))).$$ If $L\ne0$, all list entries lie between $\mu_{0,\min}(L)$ and $\mu_{0,\max}(L)$, and each endpoint is attained by some list entry.
