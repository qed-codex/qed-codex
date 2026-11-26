---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/MetricProofs/ConvergenceStatementHoldsStatement.lean",
  "declarations": [
    "GlobalTheory.T.convergence_statement_holds"
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

## Convergence of regularized curvature integrals

[Theorem ARAK.1443](https://andrewodesky.com/rh/lean/GlobalTheory.T.convergence_statement_holds/)

Let $X$ be a compact Hausdorff complex manifold of dimension $e\ge0$, with a finite holomorphic atlas and its Borel measurable structure. Let $\Theta,L$ be smooth local potential systems, with $\Theta$ strictly positive. Let $s$ be a holomorphic section for $L$, with a specified simple normal crossings presentation of its zero set $D$ by finitely many components and nonnegative integral multiplicities. Normalize $\log\|s\|_L\le0$. Off $D$ put $$r=\exp(1)-2\log\|s\|_L.$$ Fix local potential systems $\theta_i$, real functions $\phi_i$, and regularizations $\phi_{i,t}$ for $1\le i\le e$, with real constants $C_5,C,t_0$. Assume the full singular-weight and regularization conditions below. Each $\theta_i$ is smooth, $\phi_i$ is smooth off $D$, $\theta_i+\phi_i$ has nonnegative Levi form there, and $$-C_5\log r\le\phi_i\le C_5\qquad\text{off }D.$$ Assume $0<t_0<1$. Put $\epsilon(t)=C\log\log(1/t)/\log(1/t)$. For $0<t\le t_0$, require $\phi_{i,t}$ smooth on $X$ and $$-C\log\log(1/t)\le\phi_{i,t}\le C,\qquad\phi_i\le\phi_{i,t}\quad\text{off }D,$$ with nonnegative Levi form for $\theta_i+\phi_{i,t}+\epsilon(t)\Theta$. Off $D$ require $$\phi_{i,t}\le\phi_i+t^{1/3}+\epsilon(t)r,$$ and, wherever $r\le\log(1/t)$, require the stronger upper bound $\phi_{i,t}\le\phi_i+t^{1/3}+\epsilon(t)$. For $0<t\le t'\le t_0$, require on all of $X$ $$\phi_{i,t}\le\phi_{i,t'}+C\epsilon(t').$$ Assume also $\phi_{i,t}\to\phi_i$ in $C^2$ uniformly on every compact subset of every coordinate chart outside $D$.

Let $g:X\to\mathbb R$ and $g_t:X\to\mathbb R$ be functions, with $g_t$ continuous off $D$ for every real $t$. Suppose there is $C_6\in\mathbb R$ such that $|g_t|\le C_6\log r$ off $D$ for every $t$, and $g_t\to g$ locally uniformly off $D$ as $t\downarrow0$. Let $\mu_t$ and $\mu$ be the mixed curvature measures of $(\theta_i+\phi_{i,t}+\Theta)_i$ and $(\theta_i+\phi_i+\Theta)_i$, respectively, in the normalization of ([Measure associated with positive mixed potentials](https://andrewodesky.com/rh/lean/ReciprocityTheory.AnForm.M.maMeasure_thm/)), with the singular measure defined by its densities off $D$. Then $\mu$ is finite, its total mass equals the smooth mixed curvature integral for $(\theta_i+\Theta)_i$, $g$ is $\mu$-integrable, $g_t$ is $\mu_t$-integrable for all sufficiently small positive $t$, and $$\lim_{t\downarrow0}\int_Xg_t\,d\mu_t=\int_Xg\,d\mu.$$
