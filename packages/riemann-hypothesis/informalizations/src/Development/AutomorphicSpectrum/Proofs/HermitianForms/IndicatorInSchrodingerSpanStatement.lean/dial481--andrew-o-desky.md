---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/HermitianForms/IndicatorInSchrodingerSpanStatement.lean",
  "declarations": [
    "GlobalTheory.T.self_dual_lattice_filtration_character"
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

## A self-dual Haar measure from dual compact open filtrations

[Theorem THETA.0620](https://andrewodesky.com/rh/lean/GlobalTheory.T.self_dual_lattice_filtration_character/)

Let $V$ be a locally compact, second countable Hausdorff abelian topological group, equipped with its Borel sigma algebra. Let $\chi:V\times V\to\mathbb C$ be continuous and satisfy $$\chi(x+x',y)=\chi(x,y)\chi(x',y),\qquad\chi(x,y)=\chi(y,x),\qquad|\chi(x,y)|=1.$$ Let $(L_n)_{n\in\mathbb Z}$ and $(D_n)_{n\in\mathbb Z}$ be compact open subgroups with $L_n$ decreasing, $\bigcup_n L_n=\bigcup_n D_n=V$, and with some $L_n$ contained in every neighborhood of zero. Suppose $$D_n=\{y:\chi(x,y)=1\ \forall x\in L_n\},\qquad L_n=\{x:\chi(x,y)=1\ \forall y\in D_n\}.$$ There is an additive Haar measure $\mu$ on $V$ such that $$\widehat{\widehat f}(y)=f(-y),\qquad\widehat f(y)=\int_V f(x)\chi(x,y)\,d\mu(x),$$ for every locally constant compactly supported $f:V\to\mathbb C$ and every $y\in V$.
