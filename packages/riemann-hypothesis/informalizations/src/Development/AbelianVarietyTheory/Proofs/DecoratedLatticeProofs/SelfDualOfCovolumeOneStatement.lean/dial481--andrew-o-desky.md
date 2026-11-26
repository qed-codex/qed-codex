---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SelfDualOfCovolumeOneStatement.lean",
  "declarations": [
    "GlobalTheory.T.selfDual_of_fundamentalDomain_volume_eq_one"
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

## Fourier inversion from a lattice of covolume one

[Theorem ALG.1279](https://andrewodesky.com/rh/lean/GlobalTheory.T.selfDual_of_fundamentalDomain_volume_eq_one/)

Let $G$ be a second-countable locally compact Hausdorff abelian topological group, with its Borel measurable structure. Let $\Gamma\subseteq G$ be a discrete subgroup, and suppose that a compact set $K\subseteq G$ meets every translate of $\Gamma$. Let $B:G\times G\to\mathbb C$ be symmetric, continuous in its first variable, and satisfy $$B(x+x',y)=B(x,y)B(x',y),\qquad |B(x,y)|=1.$$ Assume $$\bigl[B(\gamma,x)=1\text{ for all }\gamma\in\Gamma\bigr]\iff x\in\Gamma,$$ and that $\gamma\in\Gamma$ and $B(\gamma,x)=1$ for all $x\in G$ imply $\gamma=0$. Let $\mu$ be an additive Haar measure and $\mathcal F$ an additive fundamental domain for $\Gamma$ with $\mu(\mathcal F)=1$. For every continuous compactly supported $\Phi:G\to\mathbb C$ whose transform $$\widehat\Phi(y)=\int_G\Phi(x)B(x,y)\,d\mu(x)$$ is integrable, one has $$\int_G\widehat\Phi(y)B(y,z)\,d\mu(y)=\Phi(-z)\qquad(z\in G).$$
