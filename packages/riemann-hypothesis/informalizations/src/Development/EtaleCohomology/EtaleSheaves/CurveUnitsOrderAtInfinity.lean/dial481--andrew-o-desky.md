---
{
  "module": "src/Development/EtaleCohomology/EtaleSheaves/CurveUnitsOrderAtInfinity.lean",
  "declarations": [
    "LateralTheory.E.CurveUnitsOrderAtInfinity.LeafUnits_of",
    "LateralTheory.E.CurveUnitsOrderAtInfinity.ordInfHom"
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

## A homomorphism controlling units at infinity

[Theorem AG.0467](https://andrewodesky.com/rh/lean/LateralTheory.E.CurveUnitsOrderAtInfinity.ordInfHom/)

Let $k$ be algebraically closed, let $B$ be a Dedekind domain finitely generated as a $k$-algebra, and let $g:k[T]\hookrightarrow B$ be an injective $k$-algebra homomorphism such that $B$ is finite as a $k[T]$-module. Put $L=\operatorname{Frac}B$ and $t=g(T)\in L$.

There are $n\ge0$ and a group homomorphism $\varphi:B^\times\to\mathbb Z^n$, with additive notation on the target, such that $$\varphi(u)=0\quad\Longrightarrow\quad u\text{ is integral over }k[t^{-1}]\subseteq L.$$

## Finiteness of units modulo powers

[Theorem AG.0428](https://andrewodesky.com/rh/lean/LateralTheory.E.CurveUnitsOrderAtInfinity.LeafUnits_of/)

Let $k$ be an algebraically closed field and $B$ a Dedekind domain that is a finitely generated $k$-algebra. For every integer $q\ge1$, the quotient $$B^\times/(B^\times)^q$$ is finite.
