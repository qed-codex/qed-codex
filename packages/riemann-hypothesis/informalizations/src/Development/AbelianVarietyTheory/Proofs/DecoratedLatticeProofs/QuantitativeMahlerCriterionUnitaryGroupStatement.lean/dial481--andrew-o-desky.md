---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/QuantitativeMahlerCriterionUnitaryGroupStatement.lean",
  "declarations": [
    "GlobalTheory.T.quantitativeMahlerCriterion_unitaryGroup"
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

## A quantitative height bound from the absence of short vectors

[Theorem ARAK.1521](https://andrewodesky.com/rh/lean/GlobalTheory.T.quantitativeMahlerCriterion_unitaryGroup/)

Fix the following unitary adelic datum: a CM quadratic extension $E/F$, a nonsingular Hermitian matrix $J\in M_n(E)$, a self-dual full finitely generated $\mathcal O_E$-lattice $L\subset E^n$, and, at every infinite place $v$ of $F$, an embedding $\phi_v:E\hookrightarrow\mathbb C$ restricting to the chosen representing embedding of $v$ on $F$. Choose an invertible matrix $P_v$ with $P_v^*\phi_v(J)P_v=\operatorname{diag}(\varepsilon_{v,1},\ldots,\varepsilon_{v,n})$, where $\varepsilon_{v,i}\in\{1,-1\}$. Let $G_\infty=\prod_{v\mid\infty}U(\operatorname{diag}(\varepsilon_{v,i}))$, and let $G_f=U(J)(\mathbb A_{F,f})$ with the datum's topology.

There are $b\in\mathbb N$, $C\in\mathbb R$, and a compact set $K\subset G_f$ such that the following holds. If $y=(y_v)\in G_\infty$, $0<t\le1$, and $$t\le\max_{v,i}\left|\left(y_v^{-1}P_v^{-1}\phi_v(u)\right)_i\right|\quad(0\ne u\in\mathcal O_E^n),$$ then there is $\gamma\in U(J)(F)$ whose finite component belongs to $K$ and whose infinite component in the chosen coordinates satisfies $$|((\gamma_\infty y)_v)_{ij}|\,t^b\le C\qquad(v,i,j).$$
