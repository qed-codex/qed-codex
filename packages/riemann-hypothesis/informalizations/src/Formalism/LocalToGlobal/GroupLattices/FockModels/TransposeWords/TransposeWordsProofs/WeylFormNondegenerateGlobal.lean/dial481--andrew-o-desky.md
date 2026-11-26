---
{
  "module": "src/Formalism/LocalToGlobal/GroupLattices/FockModels/TransposeWords/TransposeWordsProofs/WeylFormNondegenerateGlobal.lean",
  "declarations": [
    "Formalism.L2.G.Model.TS.dual_weyl_inclusion",
    "Formalism.L2.G.Model.TS.nondegenerate_over_field",
    "Formalism.L2.G.Model.TS.weyl_form_nondegenerate_global"
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

## An integral pairing test for a dual Weyl lattice

[Theorem REP.0383](https://andrewodesky.com/rh/lean/Formalism.L2.G.Model.TS.dual_weyl_inclusion/)

Let $O$ be a domain with fraction field $K$ of characteristic zero, let $0\le n\le r$ be integers, and let $\nu=(\nu_1,\ldots,\nu_n)$ be a weakly decreasing list of nonnegative integers. Use the dual Weyl module $\nabla_\nu$, the Weyl module $\Delta_\nu$ and the highest-weight polynomial $v_\nu$ of ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)). Regard $\nabla_\nu(O)$ and $\Delta_\nu(O)$ as submodules of $K[x_{ij}:1\le i\le r,1\le j\le n]$ by coefficient inclusion.

Use $\langle P,Q\rangle=[P,Q]_{\rm fac}$ from ([Bilinear factorial pairing of polynomials](https://andrewodesky.com/rh/lean/Formalism.L2.G.Model.TS.fockR/)). If $Q\in\nabla_\nu(K)$ and $$\langle P,Q\rangle\in O\langle v_\nu,v_\nu\rangle\qquad(P\in\Delta_\nu(O)),$$ then $Q\in\nabla_\nu(O)$.

## Nondegeneracy of the factorial pairing on column-highest polynomials

[Theorem REP.0434](https://andrewodesky.com/rh/lean/Formalism.L2.G.Model.TS.nondegenerate_over_field/)

Let $K$ be a field of characteristic zero, let $0\le n\le r$ be integers, and let $\nu_1\ge\cdots\ge\nu_n\ge0$ be integers. Use the polynomial dual Weyl module $\nabla_\nu(K)$ of ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)).

On $K[X_{ai}:1\le a\le r,1\le i\le n]$, use $\langle P,Q\rangle=[P,Q]_{\rm fac}$ from ([Bilinear factorial pairing of polynomials](https://andrewodesky.com/rh/lean/Formalism.L2.G.Model.TS.fockR/)). If $Q\in\nabla_\nu(K)$ and $\langle P,Q\rangle=0$ for every $P\in\nabla_\nu(K)$, then $Q=0$.

## A nondegenerate form controlling an integral dual Weyl module

[Theorem REP.0564](https://andrewodesky.com/rh/lean/Formalism.L2.G.Model.TS.weyl_form_nondegenerate_global/)

Let $O$ be a commutative local domain with characteristic-zero fraction field $K$, and let $p$ be prime with $p$ not a unit in $O$. Let $0\le n\le r$ be integers and let $\nu=(\nu_1,\ldots,\nu_n)$ be a weakly decreasing list of nonnegative integers. For $R=O,K$, put $D_R=\nabla_\nu(R)$ as in ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)), using the $r\times n$ matrix of variables $Z=(z_{ij})$. Regard $D_O$ as an $O$-submodule of $D_K$ through coefficient inclusion.

There is a $K$-bilinear form $B$ on the entire polynomial space over $K$ such that:

1. For every $g\in M_r(K)$ and polynomials $P,Q$, $$B(P(gZ),Q(Z))=B(P(Z),Q(g^tZ)).$$
2. If $Q\in D_K$ and $B(P,Q)=0$ for every $P\in D_K$, then $Q=0$.
3. If $Q\in D_K$ and $B(P,Q)\in O$ for every $P\in D_O$, then $Q\in D_O$.
4. For every integer $l\ge0$ such that either all $\nu_i\le l$, or $n=r$ and $\nu_i\le\nu_j+l$ for all $i,j$, $$B(P,p^{e(p,r,l)}Q)\in O\qquad(P,Q\in D_O).$$
5. If all $\nu_i=0$, then $B(P,Q)\in O$ for $P,Q\in D_O$.
