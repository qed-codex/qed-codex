---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/InfinitesimalCharacterLimits/IsometrySymmetry/IsoVSymm.lean",
  "declarations": [
    "PositivityTheory.Rg.BcB.SpectralAccumulation.FiniteDiscreteTypes.finDisc"
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

## Finiteness of discrete automorphic types under a uniform exponent gap

[Theorem AGR.1539](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.BcB.SpectralAccumulation.FiniteDiscreteTypes.finDisc/)

Let $E$ be a CM field, $N\ge0$, $\mu$ a Borel Haar measure on $G=\operatorname{GL}_N(\mathbb A_E)$, $K_f\subseteq\operatorname{GL}_N(\mathbb A_{E,f})$ open, and $W$ a finite-dimensional complex subspace of functions on the standard maximal compact subgroup at infinity. Fix $R\in\mathbb R$ and $\epsilon>0$. Say a smooth function has type $(K_f,W)$ if it is right $K_f$-invariant and each right translate restricted to the infinite compact subgroup lies in $W$. Assume there are $\alpha\in C_c(G)$ and $\delta>0$ such that every automorphic function $f$ of this type whose generated one-dimensional space has infinitesimal parameters bounded by $R$ satisfies $$\int_G\alpha(y)f(xy)\,d\mu(y)=s_f f(x),\qquad |s_f|\ge\delta.$$

Then there are finitely many isomorphism classes of nonzero irreducible discrete automorphic subspaces $V$ with a nonzero vector of type $(K_f,W)$, all infinitesimal parameters of absolute value at most $R$, and the following gap. For $0<r<N$, let $\operatorname{Exp}_r(V)$ be the exponential eigenvalues in the span of split-torus translates of constant terms along the $(r,N-r)$ parabolic; normalize the torus by $\operatorname{diag}(e^t1_r,1_{N-r})$ at all infinite places. Require $$\frac{\operatorname{Re}c}{[E:\mathbb Q]}-\frac{r(N-r)}2\le-\epsilon r(N-r) \qquad(c\in\operatorname{Exp}_r(V)).$$ Isomorphisms intertwine the finite adelic and archimedean infinitesimal actions.
