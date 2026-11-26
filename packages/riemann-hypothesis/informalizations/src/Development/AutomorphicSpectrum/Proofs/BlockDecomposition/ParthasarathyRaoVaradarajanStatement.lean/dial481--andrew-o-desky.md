---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ParthasarathyRaoVaradarajanStatement.lean",
  "declarations": [
    "GlobalTheory.T.parthasarathy_rao_varadarajan"
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

## A highest weight after tensoring with a Clifford module

[Theorem REP.0745](https://andrewodesky.com/rh/lean/GlobalTheory.T.parthasarathy_rao_varadarajan/)

For every $n\ge0$ there are a finite set $I$ and matrices $c_{ab}\in M_I(\mathbb C)$, $1\le a,b\le n$, with $$c_{ab}c_{de}+c_{de}c_{ab}=2\delta_{ae}\delta_{bd},\qquad c_{ab}^*=c_{ba}.$$ Put $$S_{ab}=\frac12\sum_e c_{ae}c_{eb}-\delta_{ab}\frac n2\,1.$$ Let $V$ be a complex inner-product space, and let $K_{ab}\in\operatorname{End}_{\mathbb C}(V)$ satisfy $$[K_{ab},K_{cd}]=\delta_{bc}K_{ad}-\delta_{da}K_{cb},\qquad\langle K_{ab}x,y\rangle=\langle x,K_{ba}y\rangle.$$ Suppose a finite-dimensional subspace $T\subseteq V$ is stable under every $K_{ab}$ and contains a nonzero highest-weight vector $v$ of weight $\nu\in\mathbb Z^n$. Define operators on $V^I$ by $$(Y_{ab}x)_i=K_{ab}x_i+\sum_j(S_{ab})_{ij}x_j.$$ There are a permutation $w$ of $\{1,\ldots,n\}$ and a nonzero highest-weight vector for $Y$ of weight $$\eta_i=\nu_{w(i)}-\frac{n+1-2w(i)}2,$$ with $\eta_1\ge\cdots\ge\eta_n$.
