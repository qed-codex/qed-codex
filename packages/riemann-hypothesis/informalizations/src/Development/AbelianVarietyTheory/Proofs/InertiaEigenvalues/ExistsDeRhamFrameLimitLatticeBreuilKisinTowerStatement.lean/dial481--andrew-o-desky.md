---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsDeRhamFrameLimitLatticeBreuilKisinTowerStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_deRhamFrame_limitLattice_breuilKisinTower"
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

## A limiting integral de Rham comparison frame

[Theorem PHT.1415](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_deRhamFrame_limitLattice_breuilKisinTower/)

Let $\ell$ be a rational prime, let $K/\mathbb Q_\ell$ be a finite extension in the source's local field model, and fix a full Breuil–Kisin period datum with a period element $\tau\in A_{\inf}$, the Witt period ring before its map to $B$. Write $\mathfrak S$ for its power-series ring, $E(u)$ for its Eisenstein element, $B$ for its Witt period ring, and $\iota:\mathfrak S\to B$ for its evaluation map. Assume $\varphi(\tau)=\operatorname{ev}(E(u))\tau$ and $\varphi(\tau)=\eta([\epsilon]-1)$ for a unit $\eta\in A_{\inf}$ and a compatible root-of-unity element $\epsilon$ satisfying the full period-element conditions of the source; here $\varphi$ is Frobenius, $\operatorname{ev}:\mathfrak S\to A_{\inf}$ is evaluation, and $[\epsilon]$ is its Teichmuller lift. Fix $d,N\ge0$ and $\rho:G_K\to\operatorname{GL}_d(\mathbb Z_\ell)$, where $G_K$ is the absolute Galois group of $K$ in the fixed algebraic closure.

Suppose there is a tower $\rho_j:G_K\to\operatorname{GL}_{d_j}(\mathbb Z_\ell)$ with matrices $\Pi_j\in M_{d,d_j}(\mathbb Z_\ell)$ and $f_j\in M_{d_j,d_{j+1}}(\mathbb Z_\ell)$ such that $\Pi_j\rho_j(g)\equiv\rho(g)\Pi_j\pmod{\ell^j}$ for every $g$, each $\Pi_j$ has a right inverse modulo $\ell^j$, each $f_j$ is exactly equivariant, and $$\Pi_jf_j\equiv\Pi_{j+1}\pmod{\ell^j}.$$ For every $j$, assume given a full comparison frame $F_j$ of bound $N$ for $\rho_j$, with period matrix $T_j\in\operatorname{GL}_{d_j}(B)$, satisfying the source's de Rham congruence conditions.

There is a full comparison frame $F_*$ of bound $N$ for $\rho$, with period matrix $T_*$, satisfying those same de Rham conditions. If every $F_j$ satisfies the crystalline congruence condition, then $F_*$ does too. There exists $r\ge0$ such that for every $n\ge0$ there are $m\ge n$ and matrices $R\in M_{d,d_m}(\mathfrak S)$, $G\in M_{d_m,d}(\mathfrak S)$ with $$\Pi_mT_m\equiv T_*\iota(R)\pmod{\ell^nB},\qquad RG\equiv\ell^rI_d\pmod{\ell^n\mathfrak S}.$$
