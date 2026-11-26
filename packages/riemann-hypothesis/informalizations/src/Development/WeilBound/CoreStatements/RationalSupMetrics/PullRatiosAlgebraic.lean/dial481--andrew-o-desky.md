---
{
  "module": "src/Development/WeilBound/CoreStatements/RationalSupMetrics/PullRatiosAlgebraic.lean",
  "declarations": [
    "MultiProjectiveCoordinates.grid_separation"
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

## A finite set of evaluations detecting integral sections quantitatively

[Theorem ARAK.0093](https://andrewodesky.com/rh/lean/MultiProjectiveCoordinates.grid_separation/)

Let $K$ be a finite set of finite coordinate blocks $I_k$, $\Omega$ a field, and $y=(y_{k,i})\in\Omega^{\coprod I_k}$. Put $P=\ker(\mathbb Z[X_{k,i}]\to\Omega[T_k],\ X_{k,i}\mapsto y_{k,i}T_k)$. Suppose $P$ is an arithmetic-variety ideal of relative dimension $D\ge0$ in the sense stated in the conventions, and every element of $\Omega$ is a ratio of evaluations at $y$ of integral multihomogeneous polynomials of equal multidegree, with nonzero denominator. Let $(a,h)$ be a smooth Hermitian multidegree, with $a\in\mathbb Z^K$ and positive homogeneous metric $h$. For each $\tau\ge0$, define $$\Lambda_\tau=\{s\in\Omega:s\prod_k y_{k,c_k}^{-\tau a_k}\text{ is integral over }\mathbb Z[y_{k,i}/y_{k,c_k}]\text{ for every }c\text{ with all }y_{k,c_k}\ne0\}.$$ There is $C\ge0$ such that for every $\tau$ there is a finite set $Z_\tau$ of nonzero complex coordinate tuples satisfying $P$ with these properties. For every $s\in\Lambda_\tau$ and $z\in Z_\tau$, there are integral multihomogeneous $g,h_1$ with degree difference $\tau a$, $g(y)=s h_1(y)$ and $h_1(z)\ne0$. For every nonzero $s\in\Lambda_\tau$, one can choose such $z,g,h_1$ with $$|g(z)|\ge e^{-C(\tau+1)}h(z)^\tau|h_1(z)|.$$
