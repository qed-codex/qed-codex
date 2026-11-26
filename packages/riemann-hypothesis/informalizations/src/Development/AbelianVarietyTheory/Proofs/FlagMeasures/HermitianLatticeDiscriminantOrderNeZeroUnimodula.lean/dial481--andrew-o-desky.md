---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/HermitianLatticeDiscriminantOrderNeZeroUnimodula.lean",
  "declarations": [
    "GlobalTheory.Mass.DiscOrder.main"
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

## Discriminants, indices and local self-duality of Hermitian lattices

[Theorem ANT.0328](https://andrewodesky.com/rh/lean/GlobalTheory.Mass.DiscOrder.main/)

Let $K$ be a number field with involution $a\mapsto\bar a$ satisfying the conditions below, let $V$ be finite-dimensional over $K$, and let $h:V\times V\to K$ be nondegenerate Hermitian, conjugate-linear in the first variable. For an integral full $\mathcal O_K$-lattice $M$, put $$M^\#=\{y\in V:h(x,y)\in\mathcal O_K\text{ for all }x\in M\},\qquad d(M)=[M^\#:M].$$ Then $d(M)\ne0$, and $d(M)=1$ if and only if $M=M^\#$. If $M\subseteq M'$ is another integral full lattice, then $[M':M]\ne0$ and $$d(M)=d(M')[M':M]^2.$$ Every lattice in the genus of $M$ is integral and has discriminant $d(M)$. For every maximal ideal $P\subseteq\mathcal O_K$, if $d(M)\notin P$ then $M$ is self-dual after the localization described below. If $M\subseteq M'$ are integral full lattices and $M$ is self-dual at $P$, their localizations at $P$ agree.
