---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/ThetaPointDeterminesAndEndDeterminedTorsion.lean",
  "declarations": [
    "GlobalTheory.thetaPtDetermines_and_endDeterminedOnTorsion"
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

## Rigidity from theta coordinates and from torsion

[Theorem AV.0536](https://andrewodesky.com/rh/lean/GlobalTheory.thetaPtDetermines_and_endDeterminedOnTorsion/)

The following two assertions hold for principally polarized abelian varieties supplied with the line bundles and normalizations in the conventions.

First, let $g,j\ge0$, let $n$ be an odd prime, and let $k\ge2$. Put $N=n^{2k}$ and $N'=n^jN$, and suppose $N^g g!<N'$. Let $K$ be algebraically closed with $n\ne0$ in $K$. Let $P=(A,L)$ and $P'=(A',L')$ have dimension $g$, with full level $N'^2$ structures for the same pairing parameter $\zeta\in K^\times$. If their theta coordinate vectors at parameter $N'$ are the same vector $$v:(\mathbb Z/N'^2\mathbb Z)^{2g}\to K,$$ then there is a polarized group-scheme isomorphism $\phi:A\to A'$ carrying every specified level basis point to its counterpart.

Second, let $g,c,M\ge0$ satisfy $4^g g!(2c)<M^2$. Let $K$ be algebraically closed with $M\ne0$ in $K$, and let $\phi:P\to P'$ be a polarized isomorphism of dimension $g$. Let $O$ be a ring with involution and $\rho,\rho'$ actions of $O$ on $P,P'$ for which the involution acts by Rosati adjoints. Suppose $a\in O$ admits $m\ge1$ and $b_1,\ldots,b_t\in O$ with $$(ma)^*(ma)+\sum_{i=1}^t b_i^*b_i=c.$$ If $\phi\rho(a)x=\rho'(a)\phi x$ for every $x\in A(K)$ killed by $M$, then $$\phi\rho(a)=\rho'(a)\phi.$$
