---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/CommutingOperatorsUniformCokernelStatement.lean",
  "declarations": [
    "GlobalTheory.T.commuting_operators_uniform_cokernel"
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

## An operator power annihilates a graded-tower cokernel

[Theorem ALG.0973](https://andrewodesky.com/rh/lean/GlobalTheory.T.commuting_operators_uniform_cokernel/)

Let $R$ be a commutative ring, $I=(\rho_1,\ldots,\rho_g)$ a finitely generated ideal, and $A$ a linearly ordered set. For $e\ge0$, $t\in\mathbb Z$ and finite $S\subseteq A$, let $T_{e,t,S}$ be $R$-modules, with linear maps $$r_{e,t,S,S'}:T_{e,t,S}\to T_{e,t,S'}\quad(S\subseteq S'),\qquad p_{e,t,S}:T_{e+1,t,S}\to T_{e,t,S},$$ $$x_{j,e,t,S}:T_{e,t,S}\to T_{e,t+1,S}\quad(j\in A).$$ Assume the $x_j$ commute in successive degrees. Assume also, whenever $S\ne\varnothing$:

1. $p$ commutes with $r$ and with every $x_j$.
2. $r x_j-x_j r$ has image in $I T_{e,t+1,S'}$ for $S\subseteq S'$.
3. Each $p_{e,t,S}$ is surjective, with kernel $I^{e+1}T_{e+1,t,S}$.
4. $I^{e+1}T_{e,t,S}=0$.

Put $G_e(S)=\bigoplus_{t\in\mathbb Z}T_{e,t,S}$, with $X_j$ acting by $x_j$, and let $[a]_t$ denote the inclusion of $a\in T_{e,t,S}$. Suppose that for every $e,t,S,j$ with $S\ne\varnothing$ and every $b\in T_{e,t,S\cup\{j\}}$, there are $k\ge0$, $t'\in\mathbb Z$ and $a\in T_{e,t',S}$ such that in $G_e(S\cup\{j\})$, $$[r_{e,t',S,S\cup\{j\}}a]_{t'}=X_j^k[b]_t.$$ Define $$K_{e,t,S}=\ker p_{e,t,S},\qquad M(S)=\bigoplus_{e\ge0}\bigoplus_{t\in\mathbb Z}K_{e,t,S}.$$ The maps $x_j$ restrict to $K_{e,t,S}$, and $r$ induces $r_M:M(S)\to M(S\cup\{j\})$. For every nonempty finite $S$, every $j\in A$ and every $b\in M(S\cup\{j\})$, there is $k\ge0$ such that $$X_j^kb\in\operatorname{im}r_M.$$
