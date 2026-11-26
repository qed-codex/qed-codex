---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ExistsCuspidalWithLabelStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_cuspidal_with_label"
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

## A cuspidal representation with a prescribed irreducible polynomial label

[Theorem REP.1495](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_cuspidal_with_label/)

Let $k$ be a finite field of cardinality $q$. Fix a multiplicative map $\iota:\bar k\to\mathbb C$ that is injective on nonzero elements, and elements $g_d\in\bar k$ of order $q^d-1$ for every $d\ge1$, satisfying $$g_{de}^{(q^{de}-1)/(q^d-1)}=g_d\qquad(d,e\ge1).$$ Let $d\ge1$ and let $P\in k[X]$ be monic and irreducible of degree $d$, with $P\ne X$. There is a finite-dimensional irreducible cuspidal complex representation $\pi$ of $\mathrm{GL}_d(k)$ with the following character values. For every root $x\in\bar k$ of $P$, every $\gamma\in\mathrm{GL}_d(k)$ with irreducible characteristic polynomial, every root $z$ of that polynomial, and every $m\ge0$ with $g_d^m=z$, $$\operatorname{tr}\pi(\gamma)=(-1)^{d-1}\sum_{a=0}^{d-1}\iota(x)^{m q^a}.$$ Cuspidal means that the fixed vectors of the unipotent radical of every proper parabolic subgroup are zero.
