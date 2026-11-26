---
{
  "module": "src/Formalism/GradedWeylDivisibility/StatementA.lean",
  "declarations": [
    "Formalism.GradedWeylDivisibility.dualWeyl",
    "Formalism.GradedWeylDivisibility.rowAct",
    "Formalism.GradedWeylDivisibility.weyl"
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

## Polynomial Weyl modules and row substitutions

[Definition / hypothesis REP.D247](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)

Let $R$ be a commutative ring, let $r,n\ge0$ be integers, and let $\nu=(\nu_1,\ldots,\nu_n)$ be a list of nonnegative integers. Use variables $X_{ai}$ with $1\le a\le r$ and $1\le i\le n$.

The polynomial dual Weyl module $\nabla_\nu(R)$ consists of the polynomials in $R[X_{ai}]$ homogeneous of degree $\nu_i$ in column $i$ and invariant, for each pair $i<j$, under the simultaneous column substitution $$X_{aj}\longmapsto X_{aj}+tX_{ai}\qquad(1\le a\le r).$$ Invariance means equality in the polynomial ring $R[X_{ai},t]$. The zero polynomial is included.

For a matrix $g\in M_r(R)$, row substitution $A_g$ is the $R$-algebra homomorphism defined by $$A_g(X_{ai})=\sum_{b=1}^r g_{ab}X_{bi}.$$ We also write $g\cdot P=A_gP$.

For $1\le a,b\le r$ and $k\in\mathbb N$, define $D_{ab}^{(k)}P$ to be the coefficient of $t^k$ after replacing $X_{bi}$ by $X_{bi}+tX_{ai}$ in $P$, for every column $i$.

Suppose now that $n\le r$. Put $\nu_{n+1}=0$ and define $$v_\nu=\prod_{i=1}^n\det(X_{ab})_{1\le a,b\le i}^{\max\{\nu_i-\nu_{i+1},0\}}.$$ The module $\Delta_\nu(R)$ is the $R$-span of all finite iterates of the operators $D_{ab}^{(k)}$ applied to $v_\nu$, including $v_\nu$ itself.

For weakly decreasing $\nu$, the polynomial $v_\nu$ is the highest-weight polynomial and $\Delta_\nu(R)$ is the polynomial Weyl module.
