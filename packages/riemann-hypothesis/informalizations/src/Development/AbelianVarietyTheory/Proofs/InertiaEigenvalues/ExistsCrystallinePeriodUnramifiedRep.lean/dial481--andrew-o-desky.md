---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsCrystallinePeriodUnramifiedRep.lean",
  "declarations": [
    "GlobalTheory.UnrPer.exists_period_unramified",
    "GlobalTheory.UnrPer.exists_solution"
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

## An invariant crystalline period matrix for an unramified representation

[Theorem PHT.0310](https://andrewodesky.com/rh/lean/GlobalTheory.UnrPer.exists_period_unramified/)

Let $\ell$ be prime and fix compatible local period-ring data, integral tilt data, and their identifications with Fontaine's rings, as specified in the conventions below. Let $K/\mathbb Q_\ell$ be finite inside the chosen algebraic closure, let $U=\mathbb Q_\ell^{\mathrm{ur}}$ be its chosen maximal unramified subfield, and let $$\rho:G_K\to\operatorname{GL}_n(U)$$ be continuous entrywise. Suppose there is $r\ge1$ such that every element of $U$ fixed by $\mathrm{Frob}^r$ lies in $K$, and every matrix entry of every $\rho(g)$ is fixed by $\mathrm{Frob}^r$. Suppose $$\rho|_{I_K}=1,\qquad|\rho(g)_{ij}-\delta_{ij}|_\ell<1\quad(g\in G_K).$$ There is $Q\in\operatorname{GL}_n(B)$ such that $$\rho(g)\,g(Q)=Q\qquad(g\in G_K),$$ where $B$ is the crystalline ring in the chosen datum and $U$ is embedded in $B$.

## Trivializing a matrix cocycle over Witt vectors

[Theorem PHT.0313](https://andrewodesky.com/rh/lean/GlobalTheory.UnrPer.exists_solution/)

Let $p$ be prime, $R$ a perfect integral domain of characteristic $p$, and $G$ a compact topological group acting by ring automorphisms $\rho(g)$ on $R$. Suppose every $y\in R$ with $y^{p^m}=y$ for some $m\ge1$ is fixed by all $g$ in some neighborhood of $1$. Put $$J=\{g\in G:\rho(g)y=y\text{ whenever }y^{p^m}=y,\ m\ge1\}.$$ Write $g\cdot Q$ for entrywise Witt-vector extension of $\rho(g)$ to matrices over $W_p(R)$. Let $A:G\to M_n(W_p(R))$, for $n\ge0$, satisfy $$A(gh)=A(g)(g\cdot A(h)),\qquad A(g)\equiv I\pmod p.$$ For every $N\ge0$, assume there is an open set containing $J$ on which $A(g)\equiv I\pmod{p^N}$. Then there is $Q\in M_n(W_p(R))$ with unit determinant and $$A(g)(g\cdot Q)=Q\qquad(g\in G).$$
