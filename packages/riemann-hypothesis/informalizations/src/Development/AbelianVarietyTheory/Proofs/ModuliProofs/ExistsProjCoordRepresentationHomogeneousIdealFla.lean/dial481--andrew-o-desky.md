---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsProjCoordRepresentationHomogeneousIdealFla.lean",
  "declarations": [
    "GlobalTheory.ProjFlat.exists_projRep_flat"
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

## A projective model for homogeneous equations with an eventual flatness criterion

[Theorem AG.0774](https://andrewodesky.com/rh/lean/GlobalTheory.ProjFlat.exists_projRep_flat/)

Let $R$ be a commutative ring, let $\Sigma$ be finite, and let $I\subset R[X_i:i\in\Sigma]$ be an ideal containing every homogeneous component of each of its elements. Fix $d\ge0$. There exist a scheme $Z$, a morphism $s:Z\to\operatorname{Spec}R$, a line bundle $M$ on $Z$, and sections $t_i\in\Gamma(Z,M)$ with the following properties.

For every commutative $R$-algebra $R'$ and every tuple $(a_i)\in(R')^\Sigma$ generating the unit ideal and annihilating all equations in $I$, there is a unique $R$-morphism $x:\operatorname{Spec}R'\to Z$ for which $x^*M$ has a trivialization identifying $x^*t_i$ with $a_i$. Conversely, every such morphism and trivialization give a tuple generating the unit ideal and annihilating $I$.

If $\Sigma\ne\varnothing$, then $s$ is projective. If $I$ is finitely generated, then $s$ is locally of finite presentation. If $$\bigl(R[X_i]/I\bigr)_e\text{ is flat over }R\qquad(e\ge d),$$ then $s$ is flat.
