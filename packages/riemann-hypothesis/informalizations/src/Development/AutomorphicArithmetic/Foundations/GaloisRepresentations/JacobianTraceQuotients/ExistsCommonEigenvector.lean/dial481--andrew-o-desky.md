---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/JacobianTraceQuotients/ExistsCommonEigenvector.lean",
  "declarations": [
    "UpperTheory.Gal.Join.twExp"
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

## An invariant eigencharacter detected by a twisted trace

[Theorem REP.0624](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Join.twExp/)

Let $T$ be a commutative group, $X$ a complex vector space, $\rho:T\to\operatorname{GL}(X)$ a representation, and $P\subseteq X$ a finite-dimensional $T$-invariant subspace. Let $s:T\to T$ be a group automorphism and $A:X\to X$ a linear map preserving $P$, with $$A\rho(t)=\rho(s(t))A\qquad(t\in T).$$ If, for some $t_1\in T$, $$\operatorname{tr}\bigl((\rho(t_1)A)|_P\bigr)\ne0,$$ then there are a character $\chi:T\to\mathbb C^\times$ and $0\ne y\in P$ such that $$\chi(s(t))=\chi(t),\qquad \rho(t)y=\chi(t)y\quad(t\in T).$$
