---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SelfDualVol.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.GunrVol.selfDualVol"
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

## Volume of a self-annihilating compact open subgroup

[Theorem ANT.0349](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.GunrVol.selfDualVol/)

Let $V$ be an abelian topological group with its Borel measurable structure, $\mu$ a measure on $V$, and $\chi:V\times V\to\mathbb C$. Assume $\mu$ is self-dual for $\chi$ in the convention below. Let $L\le V$ be compact and open. Suppose $$\chi(x+x',y)=\chi(x,y)\chi(x',y),$$ that $x\mapsto\chi(x,y)$ is continuous for every $y$, and that $$\bigl(\chi(x,y)=1\text{ for every }x\in L\bigr)\quad\Longleftrightarrow\quad y\in L.$$ Then $\mu(L)=1$.
