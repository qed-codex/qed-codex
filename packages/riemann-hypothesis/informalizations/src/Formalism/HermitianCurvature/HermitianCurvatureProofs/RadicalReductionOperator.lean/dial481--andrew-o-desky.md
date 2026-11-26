---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/RadicalReductionOperator.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.local_logarithm_unitary"
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

## A local logarithm in a unitary stabilizer

[Theorem REP.0747](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.local_logarithm_unitary/)

Let $k,r\ge0$ and $N=2r+k+1$. In the ordered basis $e_1,\ldots,e_r,u_1,\ldots,u_{k+1},f_r,\ldots,f_1$, let $H$ have $H(e_i,f_j)=\delta_{ij}$, middle diagonal $(1,\ldots,1,-1)$, and all other entries zero. Let $z\in\operatorname{span}_{\mathbb C}(u_1,\ldots,u_{k+1})$ satisfy $z^*Hz<0$. Put $$U_z=\{g:g^*Hg=H,\ ge_i=e_i,\ gf_i=f_i\ (1\le i\le r),\ gz=z\}.$$ There are an open neighborhood $O$ of $1$ in $M_N(\mathbb C)$ and a map $\Lambda:M_N(\mathbb C)\to M_N(\mathbb C)$ smooth over $\mathbb R$ on $O$ such that, for $g\in O\cap U_z$, $$\exp\Lambda(g)=g,\qquad\Lambda(g)^*H+H\Lambda(g)=0,$$ $$\Lambda(g)e_i=\Lambda(g)f_i=0\quad(1\le i\le r),\qquad\Lambda(g)z=0.$$
