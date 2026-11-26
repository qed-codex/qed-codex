---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsAdaptedQuasiLogBasisPDivGroupLieDualStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_adapted_quasiLog_basis_pDivGroup_lieDual"
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

## An adapted quasi-logarithm basis for a p-divisible group

[Theorem PHT.1707](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_adapted_quasiLog_basis_pDivGroup_lieDual/)

Let $p$ be prime, $C$ an algebraically closed field of characteristic zero with a real-valued nonnegative valuation, and $O\subseteq C$ its valuation ring. Assume $O$ is a domain, $p$ is not a unit in $O$, and $O$ is $p$-adically complete. Let $G$ be a $p$-divisible group over $O$ and choose a $d$-variable formal-coordinate chart of $G$, with formal group law $\mu$ and finite-level evaluation maps $\operatorname{ev}_n:O[[T_1,\ldots,T_d]]\to\mathcal O(G[p^n])$ as in the source.

Let $E$ be a commutative $O$-algebra with $O\hookrightarrow E$, with $p$ invertible, and such that each $x\in E$ satisfies $p^kx\in O$ for some $k\ge0$. Assume every integer prime to $p$ is invertible in $O$ and $O$ has no $p$-torsion. A quasi-logarithm is a series $f\in E[[T]]$ with zero constant term, integral linear coefficients, and integral additive defect $f(\mu(T,S))-f(T)-f(S)$.

There exist $k\ge0$, quasi-logarithms $e_1,\ldots,e_{d+k}$ and an $O$-basis $l_1,\ldots,l_k$ of $\operatorname{Lie}(G^\vee)$ such that every quasi-logarithm has a unique expression modulo $O[[T]]$ as an $O$-linear combination of the $e_i$. For $i\le d$, $e_i$ is exactly additive for $\mu$ and has linear term $T_i$.

For $j\le k$, put $\Delta_n e_{d+j}=p^n e_{d+j}-e_{d+j}([p^n]_\mu T)$. Each $\Delta_n e_{d+j}$ is integral. For every invariant differential $\omega$ of $G^\vee$, every Cartier-dual character $\varphi$ on $G[p^n]$ whose differential is the level-$n$ component of $\omega$, and every integral series $s$ mapping to $\Delta_n e_{d+j}$ in $E[[T]]$, $$l_j(\omega)\equiv\varphi(\operatorname{ev}_n(s))\pmod{p^nO}.$$
