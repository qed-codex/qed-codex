---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TOrdVan.lean",
  "declarations": [
    "UpperTheory.V.Th.ordinary_vanishing_two_of_printed_hida"
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

## Ordinary polarized cocycles are coboundaries

[Theorem GC.0035](https://andrewodesky.com/rh/lean/UpperTheory.V.Th.ordinary_vanishing_two_of_printed_hida/)

Assume the source's classical automorphy and descent package in its rank-dependent version. Let $\ell$ be prime, let $L$ be a CM field with algebraic closure $\Omega$, and fix the source's ordinary deformation datum, a level $V$, a coefficient ring $O$, a residual representation of rank $2\le n\le4$, its universal ordinary determinant ring $B$, and $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$. Let $x$ be a point of $B$ arithmetic at an allowed weight, let $\rho$ be a continuous rank-$n$ representation of the datum's group $\Gamma_0$, and let $P\in\mathrm{GL}_n(\overline{\mathbb Q}_\ell)$. Assume the level's ramification set equals that of the datum, the residual admissibility condition, that the determinant at $x$ is the determinant of $\rho$, and that the pullback of $\rho$ to $G_L$ has the source's regular algebraic conjugate-self-dual automorphy property. Assume its matrices span all $\operatorname{Mat}_n(\overline{\mathbb Q}_\ell)$, it satisfies the integral polarized-form condition with $P$, and it is trivial on the designated subgroup $I_0$.

Let $\psi_{v,i}$ be the ordinary characters at $x$. Assume $\psi_{v,i}\ne\psi_{v,j}\chi_\ell$ for every local index $v$ and all $i,j$, where $\chi_\ell$ is the local cyclotomic character, and assume the source's regular-determinant condition. Every continuous cocycle $z:\Gamma_0\to\operatorname{Mat}_n(\overline{\mathbb Q}_\ell)$ satisfying $$z(gg')=z(g)+\rho(g)z(g')\rho(g)^{-1},\qquad Pz(cgc^{-1})=-z(g)^tP,$$ vanishing on the prescribed inertia subgroups, and satisfying the ordinary local condition, is a coboundary: $$z(g)=\rho(g)Y\rho(g)^{-1}-Y\quad(g\in\Gamma_0)$$ for some matrix $Y$. The ordinary local condition asks for a local upper-triangular basis for $\rho$ with diagonal $\psi_{v,i}$, in which $z$ after subtraction of a local coboundary is upper triangular and has zero diagonal on inertia.
