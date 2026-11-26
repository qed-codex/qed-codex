---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/QuasiIsoCechNerveChainsOfEtaleLocallySurjectiveStatement.lean",
  "declarations": [
    "GlobalTheory.T.quasiIso_cechNerveChains_of_etaleLocallySurjective"
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

## A Cech resolution from an etale-locally surjective presheaf map

[Theorem AG.0836](https://andrewodesky.com/rh/lean/GlobalTheory.T.quasiIso_cechNerveChains_of_etaleLocallySurjective/)

Let $R$ be a commutative ring and let $\phi:P\to Q$ be a morphism of set-valued presheaves on schemes. Suppose every section of $Q$ lifts etale locally: for each scheme $U$ and $y\in Q(U)$ there is an etale covering sieve on $U$ such that, for every $g:V\to U$ in that sieve, $Q(g)y$ belongs to $\phi_V(P(V))$.

Let $C_\bullet(\phi)$ be the Cech nerve, with $$C_n(\phi)=\underbrace{P\times_Q\cdots\times_QP}_{n+1\text{ factors}}.$$ Apply the free $R$-module etale sheaf functor degreewise and form the alternating-face complex, placing simplicial degree $n$ in cohomological degree $-n$. The augmentation $$R[C_\bullet(\phi)]\longrightarrow R[Q]$$ is a quasi-isomorphism, where $R[Q]$ on the right is in degree zero.
