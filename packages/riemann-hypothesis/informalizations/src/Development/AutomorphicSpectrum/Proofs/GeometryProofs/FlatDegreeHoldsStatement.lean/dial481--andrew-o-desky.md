---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/FlatDegreeHoldsStatement.lean",
  "declarations": [
    "GlobalTheory.T.FlatDegree_holds"
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

## The degree of a normalized flat CM generator

[Theorem ARAK.1251](https://andrewodesky.com/rh/lean/GlobalTheory.T.FlatDegree_holds/)

Let $E$ be a CM field and fix the source's full unitary moduli setup: a quadratic-discriminant parameter $d\ne0$, distinguished root and complex value, signature $(p,q)$, level, moduli scheme $X$, and coefficient field $K$ with its specified embedding in $\mathbb C$. Choose a finite list of embeddings $E\to\mathbb C$ of the required CM type, a compatible family of period uniformizations, and one member of that family. Let $U\subseteq X_K$ be a set, $\tau:E\to\mathbb C$ send the distinguished root to its distinguished complex value, and $\phi$ be a frame function: for every field-valued point of $X_K$, it assigns a scalar to a $p$-tuple and a $q$-tuple of tangent vectors. Let $\chi$ be a Dirichlet character modulo $d$ satisfying $\chi(m)=\bigl(\frac{-d}{m}\bigr)$ for every odd integer $m\ge1$, where the right side is the Jacobi symbol.

Suppose $\phi$ satisfies the source's flat-generator package on $U$ for the chosen uniformization member and $\tau$, and let $N$ be a system of logarithmic norms on $K$ satisfying its normalized Hodge-norm matching package for $\phi$. Then $N$ is adelic and $$\widehat{\deg}N=\frac{p-q}{2}\operatorname{Re}\log\Omega(E,\chi)+q\left(2\log\sqrt d-\log\operatorname{rd}_E\right),$$ where $\operatorname{rd}_E$ is the root discriminant and $\log\Omega(E,\chi)=\gamma+\log(2\pi/\operatorname{rd}_E)-L'(1,\chi)/L(1,\chi)$, with Euler's constant $\gamma$.
