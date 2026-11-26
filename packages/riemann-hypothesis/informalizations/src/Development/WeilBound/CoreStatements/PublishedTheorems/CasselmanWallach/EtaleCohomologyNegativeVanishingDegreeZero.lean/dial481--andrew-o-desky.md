---
{
  "module": "src/Development/WeilBound/CoreStatements/PublishedTheorems/CasselmanWallach/EtaleCohomologyNegativeVanishingDegreeZero.lean",
  "declarations": [
    "PositivityTheory.CWB.identity_operator_filtration",
    "PositivityTheory.CWB.matrix_symmetric_power",
    "PositivityTheory.CWB.power_traces_nilpotent"
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

## Dyadic moment inequality for a symmetric operator

[Theorem ALG.1146](https://andrewodesky.com/rh/lean/PositivityTheory.CWB.matrix_symmetric_power/)

Let $W$ be a complex inner product space and let $P:W\to W$ be a complex linear endomorphism satisfying $\langle Px,y\rangle=\langle x,Py\rangle$ for all $x,y$. If $\|x\|=1$ and $\operatorname{Re}\langle x,Px\rangle\ge0$, then for every integer $j\ge0$, $$\bigl(\operatorname{Re}\langle x,Px\rangle\bigr)^{2^j}\le\operatorname{Re}\langle x,P^{2^j}x\rangle.$$

## Growth of filtered Lie algebra operators on Casimir eigenspaces

[Theorem REP.1172](https://andrewodesky.com/rh/lean/PositivityTheory.CWB.identity_operator_filtration/)

Let $V$ be a complex inner product space, $n\ge0$, and $\varepsilon:\{1,\ldots,n\}\to\{+,-\}$. Let operators $E_{ab}$ satisfy the $\mathfrak{gl}_n$ commutator relations and the signed adjoint relations $$[E_{ab},E_{cd}]=\delta_{bc}E_{ad}-\delta_{da}E_{cb},\qquad \langle E_{ab}x,y\rangle=s_{ab}\langle x,E_{ba}y\rangle,$$ where $s_{ab}=1$ for equal signs and $-1$ otherwise. Assume there is no proper nonzero subspace invariant under all $E_{ab}$. Put $$C_K=\sum_{\varepsilon(a)=\varepsilon(b)}E_{ab}E_{ba},$$ and assume its real-eigenvalue eigenvectors span $V$, and that the span of its eigenvectors with eigenvalue at most $R$ is finite-dimensional for every $R\in\mathbb R$. Let $U_k$ be the complex span of words of length at most $k$ in the $E_{ab}$, including the empty word. For each $k\ge0$ and $u\in U_k$, there is a constant $C\ge0$ such that $$\|uv\|\le C(\sqrt{1+\mu})^k\|v\|\qquad(\mu\ge0,\ C_Kv=\mu v).$$

## Vanishing power traces imply nilpotence

[Theorem ALG.1326](https://andrewodesky.com/rh/lean/PositivityTheory.CWB.power_traces_nilpotent/)

Let $R$ be a commutative $\mathbb Q$-algebra, let $n\ge0$, and let $N\in M_n(R)$. If $$\operatorname{tr}(N^{k+1})=0\qquad\text{for every integer }k\ge0,$$ then $N^n=0$.
