---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/AnnihilatorModels/IdealSplitHolds.lean",
  "declarations": [
    "UpperTheory.Gal.crystallineComparison.Mod.chainLoc_holds",
    "UpperTheory.Gal.crystallineComparison.Mod.idealSplit_holds",
    "UpperTheory.Gal.crystallineComparison.Mod.ringHomog_holds"
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

## Dimension of an Artin algebra with transitive automorphisms on its points

[Theorem ALG.0441](https://andrewodesky.com/rh/lean/UpperTheory.Gal.crystallineComparison.Mod.ringHomog_holds/)

Let $\kappa$ be algebraically closed and $B$ a finite-dimensional commutative $\kappa$-algebra. Fix a $\kappa$-algebra homomorphism $\varepsilon_0:B\to\kappa$ and suppose $\ker\varepsilon_0$ is prime. Assume that for every $\kappa$-algebra homomorphism $\varepsilon:B\to\kappa$ there is $\alpha\in\operatorname{Aut}_\kappa(B)$ with $\varepsilon=\varepsilon_0\circ\alpha$. Then $$\dim_\kappa B=\#\operatorname{Hom}_{\kappa\text{-alg}}(B,\kappa)\cdot\dim_\kappa B_{\ker\varepsilon_0}.$$

## Approximation by one modulo an ideal power

[Theorem ALG.0602](https://andrewodesky.com/rh/lean/UpperTheory.Gal.crystallineComparison.Mod.idealSplit_holds/)

Let $A$ be a Dedekind domain, $\mathfrak a\subseteq A$ an ideal, and $0\ne x\in A$. For every integer $\rho\ge0$, there are an integer $m\ge0$ and $\alpha\in A$ such that $$\alpha\equiv1\pmod{\mathfrak a^\rho},\qquad \alpha\mathfrak a^m\subseteq xA.$$

## Ideals in a finite local algebra with principal maximal ideal

[Theorem ALG.0773](https://andrewodesky.com/rh/lean/UpperTheory.Gal.crystallineComparison.Mod.chainLoc_holds/)

Let $k$ be a field and $A$ a commutative local $k$-algebra that is finite-dimensional over $k$. Assume there is a $k$-algebra homomorphism $\epsilon:A\to k$. If the maximal ideal of $A$ is $(t)$, then every ideal $J\subseteq A$ satisfies $$\dim_k(A/J)=q\quad\Longrightarrow\quad J=(t^q)\qquad(q\ge0).$$
