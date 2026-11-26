---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/SmoothCompl.lean",
  "declarations": [
    "UpperTheory.V.Loc.smoothCompl"
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

## A power-series description of a formally smooth component

[Theorem ALG.0970](https://andrewodesky.com/rh/lean/UpperTheory.V.Loc.smoothCompl/)

Let $\ell$ be prime, $O$ a complete discrete valuation ring of characteristic zero, finite as a $\mathbb Z_\ell$-module, and $E=\operatorname{Frac}(O)$ a finite extension of $\mathbb Q_\ell$, with compatible scalar structures. Let $R$ be a complete noetherian local $O$-algebra whose structure map is local and induces a surjection on residue fields. Let $I\subseteq R$ be an ideal and $x:R\to O$ an $O$-algebra map with $I\subseteq\ker x$.

Assume the following lifting property. For finite-dimensional $E$-algebras $B,B'$ augmented to $E$ with nilpotent augmentation kernels, every surjective augmented $E$-algebra map $p:B\to B'$ and every $O$-algebra map $f':R\to B'$ with $f'(I)=0$ and augmentation equal to $R\xrightarrow{x}O\to E$ admit an $O$-algebra lift $f:R\to B$ with $f(I)=0$ and $pf=f'$.

There exist $n\ge0$, an ideal $P\supseteq I$, and an $O$-algebra map $\phi:R\to E[[T_1,\ldots,T_n]]$ such that:

1. $\ker\phi=P$ and the constant term of $\phi(a)$ is $x(a)$, viewed in $E$.
2. For every $N\ge0$ and $F\in E[[T_1,\ldots,T_n]]$, there are $a\in R$ and $c\in O\setminus\{0\}$ with $cF-\phi(a)\in(T_1,\ldots,T_n)^N$.
3. If $\phi(a)\in(T_1,\ldots,T_n)^N$, some $c\in O\setminus\{0\}$ satisfies $ca\in(\ker x)^N+P$.
4. Some $y\in R$ has $x(y)\ne0$ and $yP\subseteq I$.
5. $P$ is a minimal prime over $\sqrt I$, and for every minimal prime $Q$ over $\sqrt I$, $$Q\subseteq\ker x\quad\Longleftrightarrow\quad Q=P.$$
6. $\dim(R/P)=n+1$.
