---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/T2SpaceFiniteAdeleRingCmField.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.SplitTwo.haar_split"
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

## Splitting Haar measure with two equal factors

[Theorem REP.0374](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.SplitTwo.haar_split/)

Let $X$ be a topological group, and let $P,Q$ be locally compact second-countable topological groups. Equip them with their Borel measurable structures. Suppose $e:X\simeq(P\times P)\times Q$ is an isomorphism of topological groups and $\mu$ is a Haar measure on $X$. There are Haar measures $\mu_1$ on $P$ and $\mu_2$ on $Q$ such that $$e_*\mu=(\mu_1\otimes\mu_1)\otimes\mu_2.$$
