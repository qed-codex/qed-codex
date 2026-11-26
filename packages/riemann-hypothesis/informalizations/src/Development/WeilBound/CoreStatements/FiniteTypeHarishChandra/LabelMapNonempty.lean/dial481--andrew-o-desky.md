---
{
  "module": "src/Development/WeilBound/CoreStatements/FiniteTypeHarishChandra/LabelMapNonempty.lean",
  "declarations": [
    "ReciprocityTheory.Ty.Fin.GreenAll.cuspParam_all"
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

## Polynomial labels for cuspidal representations over a finite field

[Theorem REP.1577](https://andrewodesky.com/rh/lean/ReciprocityTheory.Ty.Fin.GreenAll.cuspParam_all/)

Let $K$ be any finite field, $q=|K|$, and $\overline K$ an algebraic closure. Fix a multiplicative map $\iota:\overline K\to\mathbb C$ preserving $1$ and injective on nonzero elements. Choose $g_d\in\overline K$ for $d\ge1$ with order $q^d-1$ and $$g_{de}^{(q^{de}-1)/(q^d-1)}=g_d\qquad(d,e\ge1).$$ For $d\ge1$, a label of a complex representation $\tau$ of $\operatorname{GL}_d(K)$ is a monic irreducible polynomial $P\in K[X]$, $P\ne X$, of degree $d$ with the following property. For every root $x$ of $P$, every matrix $\gamma$ with irreducible characteristic polynomial, every root $z$ of that polynomial and every $m\ge0$ with $g_d^m=z$, $$\operatorname{tr}\tau(\gamma)=(-1)^{d-1}\sum_{a=0}^{d-1}\iota(x)^{mq^a}.$$ Every irreducible cuspidal $\tau$ has a unique such label and $$\dim_{\mathbb C}\tau=\prod_{i=1}^{d-1}(q^i-1).$$ Every monic irreducible degree-$d$ polynomial other than $X$ labels an irreducible cuspidal representation, and two such representations with the same label are isomorphic. Cuspidal means that the fixed subspace of every proper parabolic unipotent radical is zero.
