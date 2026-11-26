---
{
  "module": "src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameHermSharpB.lean",
  "declarations": [
    "Formalism.HN.frameB_hnStep"
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

## Lattice submodules selected by a slope threshold

[Theorem ARAK.0148](https://andrewodesky.com/rh/lean/Formalism.HN.frameB_hnStep/)

Let $R$ be a ring, $V$ an $R$-module, $E$ a finite-dimensional real inner product space, and $\rho:V\to E$ an additive map. Let $L\subseteq V$ be an $R$-submodule on which $\rho$ is injective, with $\rho(L)$ discrete. For $A\subseteq L$ write $r(A)=\operatorname{rk}_{\mathbb Z}\rho(A)$ and $d(A)=-\log\operatorname{covol}\rho(A)$, with covolume in its real span and $d(0)=0$. Write $\mu_0(A)=d(A)/r(A)$, assigning zero to division by zero. A submodule $A\subseteq L$ is saturated when $\rho(A)=\rho(L)\cap\operatorname{span}_{\mathbb R}\rho(A)$. Define $\mu_{0,\min}(A)$ as the infimum of slopes of nonzero quotients of $\rho(A)$ obtained by orthogonal projection along saturated submodules, with the empty infimum assigned zero.

For every $\theta\in\mathbb R$, define the $R$-submodule $$H_\theta(L)=\sum_{\substack{0\ne A\subseteq L\\\mu_{0,\min}(A)\ge\theta}}A.$$ Then $H_\theta(L)$ is saturated in $L$, and, when it is nonzero, $\mu_{0,\min}(H_\theta(L))\ge\theta$. Every nonzero $A\subseteq L$ with $\mu_{0,\min}(A)\ge\theta$ lies in $H_\theta(L)$. Moreover, every $A$ with $H_\theta(L)\subsetneq A\subseteq L$ satisfies $$d(A)-d(H_\theta(L))<\theta\bigl(r(A)-r(H_\theta(L))\bigr).$$
