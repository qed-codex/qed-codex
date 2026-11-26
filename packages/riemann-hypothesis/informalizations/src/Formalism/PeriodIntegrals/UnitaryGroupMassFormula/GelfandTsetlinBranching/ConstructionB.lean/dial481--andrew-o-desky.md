---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/GelfandTsetlinBranching/ConstructionB.lean",
  "declarations": [
    "PI.WGB.stable_complement_exists"
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

## Stable complements in a polynomial branching module

[Theorem REP.0678](https://andrewodesky.com/rh/lean/PI.WGB.stable_complement_exists/)

Let $n+1=N$, and let $\lambda_1\ge\cdots\ge\lambda_N$ be integers. Put $d=\lambda_N$ and $\nu_j=\lambda_j-d$. Let $V_\lambda\subset\mathbb C[X_{ij}:1\le i,j\le N]$ consist of the polynomials of column multidegree $\nu$ invariant under every formal operation adding a scalar multiple of column $a$ to column $b$ for $a<b$. Give it the action $$\rho_\lambda(g)f(X)=\det(g)^d f(g^{\mathsf T}X) \qquad(g\in\operatorname{GL}_N(\mathbb C)).$$ If $W\subset V_\lambda$ is a complex subspace stable under $\rho_\lambda(\operatorname{diag}(h,1))$ for $h\in\operatorname{GL}_n(\mathbb C)$, it has a stable complement: there is $W'\subset V_\lambda$ with $$W+W'=V_\lambda,\qquad W\cap W'=0.$$
