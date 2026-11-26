---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StabilizerVolume/HenselCountHolds.lean",
  "declarations": [
    "PI.VolStabS.henselCount_holds"
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

## A measure identity for congruence fibres of a nonlinear map

[Theorem ALG.0844](https://andrewodesky.com/rh/lean/PI.VolStabS.henselCount_holds/)

Let $V,X$ be topological abelian groups equipped with their Borel sigma-algebras and additive Haar measures $\mu,\nu$. Let $(\Lambda_n)_{n\ge0}$ and $(H_n)_{n\ge0}$ be families of compact open additive subgroups of $V$ and $X$, respectively, with $\Lambda_{n+1}\subseteq\Lambda_n$. Let $D:V\to X$ be an additive homomorphism satisfying $D(\Lambda_n)=H_n$ for every $n$.

Let $G:V\to X$ be any map and $y\in V$. Suppose that for every $n\ge0$, $Z\in\Lambda_0$ and $W\in\Lambda_n$, $$G(y+Z+W)-G(y+Z)-D(W)\in H_{n+1}.$$ For every $n\ge0$ and $h\in X$ with $h-G(y)\in H_0$, $$\mu\{Z\in\Lambda_0:G(y+Z)-h\in H_n\}\,\nu(H_0) =\mu(\Lambda_0)\,\nu(H_n).$$
