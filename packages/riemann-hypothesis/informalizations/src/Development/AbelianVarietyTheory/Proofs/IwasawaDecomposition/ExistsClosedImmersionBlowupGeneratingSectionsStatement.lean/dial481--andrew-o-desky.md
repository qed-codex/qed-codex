---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsClosedImmersionBlowupGeneratingSectionsStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_closedImmersion_blowup_generatingSections"
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

## A blowup embedded using generating sections

[Theorem AG.1127](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_closedImmersion_blowup_generatingSections/)

Let $R$ be a commutative Noetherian ring, $X\to\operatorname{Spec}R$ projective, $\mathcal J$ an ideal sheaf on $X$, and $b:X'\to X$ its blowup. Let $L$ be a line bundle with a trivializing open cover and sections $s_0,\ldots,s_m$. Suppose that on every affine open contained in a trivialization, the local coefficient functions of the $s_i$ generate $\mathcal J$. There is an $R$-morphism $c:X'\to\mathbb P_R^m$ such that $$(b,c):X'\longrightarrow X\times_R\mathbb P_R^m$$ is a closed immersion. On each intersection of a pulled-back trivialization with $c^{-1}\{T_i\ne0\}$, its coordinate functions satisfy $$b^*s_j=c^*(T_j/T_i)\,b^*s_i\qquad(0\le j\le m).$$
