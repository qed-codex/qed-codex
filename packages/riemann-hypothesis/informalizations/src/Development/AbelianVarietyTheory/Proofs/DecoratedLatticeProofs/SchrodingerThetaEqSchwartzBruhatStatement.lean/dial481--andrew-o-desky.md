---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SchrodingerThetaEqSchwartzBruhatStatement.lean",
  "declarations": [
    "GlobalTheory.T.schrodingerTheta_eq_schwartzBruhat"
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

## Schrodinger realization of adelic theta functions

[Theorem THETA.1726](https://andrewodesky.com/rh/lean/GlobalTheory.T.schrodingerTheta_eq_schwartzBruhat/)

Fix the source's complete global theta datum, in particular its CM extension $E/F$ and the prescribed forms and archimedean embeddings. Let $\psi$ be a continuous unitary nontrivial character of $\mathbb A_F/F$ whose infinite part is $\exp(-2\pi i\sum_\tau\tau(x))$, and choose a compatible family of infinite embeddings. Let $A,B$ be Hermitian spaces permitted by this datum. Put $V=M_{\operatorname{rank}B,\operatorname{rank}A}(\mathbb A_F\otimes_F E)$ and $\Gamma=M_{\operatorname{rank}B,\operatorname{rank}A}(E)$. Choose additive Haar measure $\nu$ and an additive fundamental domain $\mathcal Y$ for $\Gamma$ with $\nu(\mathcal Y)=1$.

On the doubled space associated to $A\oplus(-A)$ and $B$, consider complex functions satisfying rational Heisenberg quasi-periodicity, continuity, smoothness along every finite-dimensional real archimedean translation, and invariance under finite translations from an open additive subgroup. Apply the source's mixed-model transform and evaluate its second coordinate at zero; denote the resulting function on $V$ by $S(f)$.

Every $S(f)$ is a Schwartz–Bruhat function on $V$: it is a finite sum of products of a Schwartz function in the prescribed infinite coordinates and a locally constant compactly supported function on the finite adeles. Every such Schwartz–Bruhat function equals $S(f)$ for some $f$ satisfying the stated theta-function conditions, and $$S(f)=S(f')\quad\Longrightarrow\quad f=f'.$$
