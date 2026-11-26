---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsFiniteEtaleLevelCoverOfPowEqOne.lean",
  "declarations": [
    "GlobalTheory.exists_finiteEtale_level_cover"
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

## A finite etale algebra representing a torsion-basis refinement

[Theorem AV.1009](https://andrewodesky.com/rh/lean/GlobalTheory.exists_finiteEtale_level_cover/)

Assume the two abelian-scheme law packages below. Let $o$ be a commutative ring, $N\ge1$, and $\zeta\in o^\times$ such that $N^2$ is invertible in $o$ and the image of $\zeta$ has exact order $N^2$ under every map from $o$ to a field. Let $R$ be a reduced Noetherian $o$-algebra, and let $(A,L)/R$ be a principally polarized abelian scheme of dimension $g$. Choose any indexed family of endomorphisms $(\alpha_j)_{j\in J}$ and sections $Q_1,\ldots,Q_{2g}\in A(R)[N]$ whose linear combinations give a unique parametrization of all geometric $N$-torsion points by $(\mathbb Z/N\mathbb Z)^{2g}$.

There is a finite étale $R$-algebra $R_1$, a principally polarized abelian scheme $(A_1,L_1)/R_1$ with endomorphisms $\alpha_{1,j}$, a symplectic full level-$N^2$ basis $P_1,\ldots,P_{2g}$, and a group-scheme pullback map $\psi_1:A_1\to A$, such that $L_1\simeq\psi_1^*L$, the endomorphisms commute with $\psi_1$, and $$\psi_1(NP_i)=Q_i|_{R_1}.$$ For every $R$-algebra $R'$ with another such object $(A',L',\alpha'_j,P'_i)$ and pullback map $\psi:A'\to A$, there is a unique $R$-algebra map $u:R_1\to R'$ for which $$\psi(P'_i)=\psi_1(P_i)|_{R'}\qquad(1\le i\le2g)$$ and $(A',L',\alpha'_j,P'_i)$ is a structured pullback of $(A_1,L_1,\alpha_{1,j},P_i)$ along $u$.
