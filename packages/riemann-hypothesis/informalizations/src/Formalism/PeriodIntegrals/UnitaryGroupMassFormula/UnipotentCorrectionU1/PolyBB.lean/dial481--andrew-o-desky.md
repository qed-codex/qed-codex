---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/UnipotentCorrectionU1/PolyBB.lean",
  "declarations": [
    "PI.UnitaryCorollaryDerivatives.pb_poly"
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

## Polynomial growth under mixed invariant derivatives

[Theorem REP.0741](https://andrewodesky.com/rh/lean/PI.UnitaryCorollaryDerivatives.pb_poly/)

Let $k,r,\kappa\ge0$ and $N=2r+k+1$. In the ordered basis $e_1,\ldots,e_r,u_1,\ldots,u_{k+1},f_r,\ldots,f_1$, let $H$ be the Hermitian form with $H(e_i,f_j)=\delta_{ij}$, middle diagonal $(1,\ldots,1,-1)$, and all other entries zero. Put $$G=\{g\in M_N(\mathbb C):g^*Hg=H\},\qquad\mathfrak g=\{X:X^*H+HX=0\}.$$ Let $P:M_N(\mathbb C)\to\mathbb C$ be a polynomial of total degree at most $\kappa$ in the matrix entries and their conjugates. Then $P$ is smooth over $\mathbb R$. For every $n\ge0$ there is $C_n\in\mathbb R$ such that $$|D_wP(g)|\le C_n\|g\|_F^\kappa\qquad(g\in G)$$ for every word $w$ of at most $n$ left or right derivatives with directions $X\in\mathfrak g$ whose entries have absolute value at most $1$.
