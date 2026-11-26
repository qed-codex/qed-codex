---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/UnitaryGroupRealPointsEquivPiIndefiniteUnitary.lean",
  "declarations": [
    "GlobalTheory.Mem.InfGroup.real_points"
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

## Archimedean points of a unitary group as a product of real Lie groups

[Theorem REP.0957](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.InfGroup.real_points/)

Let $E/F$ be a CM extension with conjugation $\sigma$, and let $J\in M_M(E)$. Choose a finite family of embeddings $\tau_i:E\hookrightarrow\mathbb C$, one for each infinite place of $E$, and homomorphisms $\theta_i:\mathbb A_{F,\infty}\otimes_FE\to\mathbb C$ satisfying $$\theta_i(1\otimes x)=\tau_i(x),\qquad a\longmapsto\theta_i(a\otimes1)\text{ is continuous}.$$ For each $i$, suppose $J_i=\tau_i(J)$ has signature $(P_i,Q_i)$ and choose an $(P_i+Q_i)\times M$ matrix $A_i$ with $$A_i^*\operatorname{diag}(1_{P_i},-1_{Q_i})A_i=J_i.$$ There is a topological group isomorphism $$e:U(J)(\mathbb A_{F,\infty})\simeq\prod_iU(P_i,Q_i)$$ such that $$e(g)_iA_i=A_i\theta_i(g)\qquad(g\in U(J)(\mathbb A_{F,\infty}),\ i).$$ The homomorphisms in the last identity act entrywise on matrices.
