---
{
  "module": "src/Formalism/GradedWeylDivisibility/DualWeylDominanceOf.lean",
  "declarations": [
    "Formalism.GradedWeylDivisibility.dualWeylPoint",
    "Formalism.GradedWeylDivisibility.dualWeylSat",
    "Formalism.GradedWeylDivisibility.fockPos",
    "Formalism.GradedWeylDivisibility.fockWeightOrth"
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

## Saturation of column-invariant polynomial modules

[Theorem ALG.0198](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeylSat/)

Let $R$ be a commutative integral domain, let $r,n\ge0$ be integers, and let $\nu\in\mathbb N^n$. Use the polynomial dual Weyl module $\nabla_\nu(R)$ of ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)).

For every $c\in R\setminus\{0\}$ and every $f\in R[X_{ai}:1\le a\le r,1\le i\le n]$, $$cf\in\nabla_\nu(R)\quad\Longrightarrow\quad f\in\nabla_\nu(R).$$

## Pointwise testing of universal column invariance

[Theorem ALG.0797](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeylPoint/)

Let $R$ be an infinite commutative integral domain, let $r,n\ge0$ be integers, and let $\nu\in\mathbb N^n$. Use the polynomial dual Weyl module $\nabla_\nu(R)$ of ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)).

For every $f\in R[X_{ai}:1\le a\le r,1\le i\le n]$, membership $f\in\nabla_\nu(R)$ is equivalent to the following two conditions: $f$ is homogeneous of degree $\nu_i$ in each column $i$, and for every $1\le l<j\le n$ and every $c\in R$, $f$ is unchanged as a polynomial by the simultaneous substitution $$X_{aj}\longmapsto X_{aj}+cX_{al}\qquad(1\le a\le r),$$ with all other columns fixed.

## Positivity of the factorial Hermitian pairing

[Theorem ALG.0837](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.fockPos/)

Let $I$ be any set and use $[\ ,\ ]_{\rm fac}$ from ([Bilinear factorial pairing of polynomials](https://andrewodesky.com/rh/lean/Formalism.L2.G.Model.TS.fockR/)) over $\mathbb C$. For a polynomial $f\in\mathbb C[X_i:i\in I]$, let $\overline f$ denote the polynomial obtained by conjugating every coefficient of $f$.

If $f\ne0$, then $$\operatorname{Re}[f,\overline f]_{\rm fac}>0,\qquad \operatorname{Im}[f,\overline f]_{\rm fac}=0.$$

## Orthogonality of distinct polynomial weights

[Theorem REP.0878](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.fockWeightOrth/)

Let $\Sigma$ be a set, $M$ a commutative additive monoid, and $w:\Sigma\to M$. Use $[\ ,\ ]_{\rm fac}$ from ([Bilinear factorial pairing of polynomials](https://andrewodesky.com/rh/lean/Formalism.L2.G.Model.TS.fockR/)) over $\mathbb C$. For polynomials $f,g\in\mathbb C[X_s:s\in\Sigma]$, let $\overline g$ denote the polynomial obtained by conjugating every coefficient of $g$, and define the Fischer pairing by $$[f,g]=[f,\overline g]_{\rm fac}.$$ If $f$ and $g$ are weighted homogeneous of distinct weights $\mu,\mu'\in M$, then $[f,g]=0$.
