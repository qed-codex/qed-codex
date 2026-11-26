---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ExistsUniqueChernClassNilpotentBase.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.CrystallineChernClass.existsUnique_crystalline_chern_class"
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

## Existence and uniqueness of a divided-power Chern class

[Theorem PHT.0466](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.CrystallineChernClass.existsUnique_crystalline_chern_class/)

Let $O,R,\Lambda$ be commutative rings, let $I\subseteq R$ carry divided powers $\gamma$, let $p\ge1$, and fix maps $q:X\to\operatorname{Spec}O$, $\kappa:O\to R/I$, and $c:\Lambda\to R$. Let a line bundle be given by a smooth surjective cover $f:Y\to X$ and invertible transition functions $u(a,b)$, natural under pullback and satisfying $u(a,b)u(b,d)=u(a,d)$. Assume the open subsets of $X$ on which $f$ admits a section cover $X$. Let $N\ge0$ satisfy $N!=0$ in $R$.

There is a unique class $x\in H^2(\mathcal C,\mathcal O_\Lambda)$ with the following characterization. On every diagram of divided-power thickenings equipped with lifts to $Y$ and unit lifts of its transition functions, the divided-power logarithms of the transition defects form a cocycle, and its cohomology class is the restriction of $x$.
