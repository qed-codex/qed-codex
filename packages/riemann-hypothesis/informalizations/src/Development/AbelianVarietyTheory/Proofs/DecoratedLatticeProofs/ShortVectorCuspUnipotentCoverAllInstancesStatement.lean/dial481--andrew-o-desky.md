---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ShortVectorCuspUnipotentCoverAllInstancesStatement.lean",
  "declarations": [
    "GlobalTheory.T.shortVectorCuspUnipotentCover_all_instances"
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

## Unipotent approximation in the presence of a short integral vector

[Theorem ARAK.1553](https://andrewodesky.com/rh/lean/GlobalTheory.T.shortVectorCuspUnipotentCover_all_instances/)

Fix the full adelic unitary lattice datum in ([A canonical flag from normalized lattice sizes](https://andrewodesky.com/rh/lean/GlobalTheory.PointFlag.flag_spec/)) for a CM extension $E/F$, a nondegenerate Hermitian form $J$ on $E^n$, a self-dual integral lattice and compatible archimedean signature frames $P_v$. Write $G_\infty,G_f$ for its infinite and finite groups, and $G(F)$ for the embedded rational group. For $y\in G_\infty$ and $u\in E^n$, put $$V_y(u)_v=y_v^{-1}P_v^{-1}\sigma_v(u),\qquad\|V_y(u)\|_\infty=\max_{v,i}|V_y(u)_{v,i}|.$$ For every neighborhood $U$ of $1$ in $G_f$, there are $s_0,\eta_0>0$ and $C\in\mathbb R$ such that the following holds. If $0<\eta\le\eta_0$ and some nonzero $u\in\mathcal O_E^n$ satisfies $$\|V_y(u)\|_\infty\le s_0\eta^{n+1},$$ then there is a nonzero rational totally isotropic subspace $W\subseteq E^n$ such that, for every $m\in G_\infty$ with $(m,1)$ in the adelic unipotent radical associated with $W$, one can find $\gamma\in G(F)$ with $\gamma_f\in U$ and $$\max_{v,i,j}\left|\bigl(y^{-1}(\gamma_\infty m)y-1\bigr)_{v,ij}\right|\le C\eta.$$
