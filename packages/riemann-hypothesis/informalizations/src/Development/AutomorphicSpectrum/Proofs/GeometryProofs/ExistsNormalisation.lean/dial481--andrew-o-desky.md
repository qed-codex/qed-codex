---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/ExistsNormalisation.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.NormEx.exists_normalisation"
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

## A finite normalization model after a finite field extension

[Theorem AG.0805](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.NormEx.exists_normalisation/)

Let $o$ be a commutative ring essentially of finite type over $\mathbb Z$, $\Omega$ an $o$-algebra which is a field, $x=(x_c)_{c\in I}$ a finite coordinate family in $\Omega$, and $(X,\xi,s)$ a coordinate model for $x$ in the sense below. Let $\Omega'/\Omega$ be a finite field extension with a compatible $o$-algebra structure.

There are a finite coordinate family $y$ in $\Omega'$, a coordinate model $(X',\xi',s')$ for $y$, and a finite morphism $f:X'\to X$ such that $$f\circ\xi'=\xi\circ\operatorname{Spec}(\Omega'\leftarrow\Omega).$$ Every regular-image local ring $R'_{p'}\subseteq\Omega'$ is integrally closed in $\Omega'$. For every point $p\in X$, let $B_p$ be the integral closure in $\Omega'$ of the image of $R_p$. The points $p'\in X'$ above $p$ correspond bijectively to the maximal ideals $\mathfrak m$ of $B_p$, with $$R'_{p'}=(B_p)_{\mathfrak m}.$$
