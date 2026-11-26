---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/NormalisedLocalInvariantExistsStatement.lean",
  "declarations": [
    "GlobalTheory.T.normalised_local_invariant_exists"
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

## A normalized local second-cohomology isomorphism

[Theorem GC.0568](https://andrewodesky.com/rh/lean/GlobalTheory.T.normalised_local_invariant_exists/)

Let $F$ be a number field with algebraic closure $\Omega$, let $\ell$ be prime, let $r>0$, and choose a primitive $\ell^r$th root of unity $\zeta\in\Omega$. Let $A\subseteq\Omega$ be a valuation ring over a finite prime $v$ of $F$, with decomposition and inertia groups $D_A,I_A$. There is a $\mathbb Z/\ell^r\mathbb Z$-linear isomorphism $$\operatorname{inv}_A:H^2(D_A,\mathbb Z/\ell^r\mathbb Z(1))\xrightarrow{\sim}\mathbb Z/\ell^r\mathbb Z$$ with this normalization. Let $\varpi\in\mathcal O_F$ satisfy $\varpi\in v\setminus v^2$, let $y\in\Omega$ satisfy $y^{\ell^r}=\varpi$, and let $\kappa,\chi:D_A\to\mathbb Z/\ell^r\mathbb Z$ satisfy $$g(y)=\zeta^{\widetilde{\kappa(g)}}y,\qquad\chi(gh)=\chi(g)+\chi(h),\qquad\chi|_{I_A}=0.$$ Assume $\chi(g)=1$ for every arithmetic Frobenius lift at $v$. For every $2$-cocycle $z$ with coefficients in $\mathbb Z/\ell^r\mathbb Z(1)$ whose values satisfy $$z(g,h)=\kappa(g)\chi(h),$$ one has $\operatorname{inv}_A([z])=1$. The tilde denotes the integer representative modulo $\ell^r$.
