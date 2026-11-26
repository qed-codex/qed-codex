---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/RtCompl.lean",
  "declarations": [
    "UpperTheory.V.Loc.rtCompl"
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

## A twelve-variable completion chart at the rank-three base point

[Theorem PHT.0947](https://andrewodesky.com/rh/lean/UpperTheory.V.Loc.rtCompl/)

Assume the source's local cohomology input package: rational and finite-coefficient finiteness, Tate duality and Euler characteristics, and the local Bloch–Kato theorem. Let $\ell$ be prime, and let $O$ be a characteristic-zero discrete valuation domain, finite over $\mathbb Z_\ell$ and complete at its maximal ideal. Let $E=\operatorname{Frac}O$ be a finite extension of $\mathbb Q_\ell$, with the compatible scalar maps. Fix the rank-three local datum described below and its universal deformation ring $R$, universal representation $r$, and base-point homomorphism $x:R\to O$ specializing $r$ to $r_0$.

Form the ideals $J$ and $I$ and the set $\mathcal P$ specified below. Then $$\mathcal P=\{I\},$$ and there is an $O$-algebra homomorphism $\Phi:R\to E[[X_1,\ldots,X_{12}]]$ such that $\ker\Phi=I$ and $\Phi(a)(0)=x(a)$ for every $a\in R$. If $\mathfrak n=(X_1,\ldots,X_{12})$, then for every $N\ge0$:

- for every $f\in E[[X_1,\ldots,X_{12}]]$, there are $a\in R$ and $0\ne c\in O$ with $cf-\Phi(a)\in\mathfrak n^N$;
- if $\Phi(a)\in\mathfrak n^N$, there is $0\ne c\in O$ with $ca\in(\ker x)^N+I$.
