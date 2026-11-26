---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UniformizationProofs/CardTorsionOverZero.lean",
  "declarations": [
    "GlobalTheory.GtCount.card_gtTors"
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

## Counting torsion in the generic extension attached to a polarization

[Theorem AV.0898](https://andrewodesky.com/rh/lean/GlobalTheory.GtCount.card_gtTors/)

Assume the source's two abelian-geometry law packages described below. Let $R$ be a Noetherian integral domain, let $(A,L)/R$ be a principally polarized abelian scheme of relative dimension $g$, and let $X$ be a free abelian group of finite rank $r$. Fix a homomorphism $c:X\to A(R)$, a rigidification, compatible cubical and symmetric structures on $L$, and generic trivializations of $c(x)^*L^{-1}$ for every $x\in X$, as in the source's preliminary degeneration datum.

Let $F$ be an algebraically closed extension of $\operatorname{Frac}R$, and let $G_F\to A_F$ be the extension by the split torus with character group $X$ attached to these data. For every integer $N\ge0$ whose image in $F$ is nonzero, $$\#G_F[N](F)=N^{2g+r},\qquad \#\{z\in G_F[N](F):z\mapsto0\text{ in }A_F\}=N^r.$$
