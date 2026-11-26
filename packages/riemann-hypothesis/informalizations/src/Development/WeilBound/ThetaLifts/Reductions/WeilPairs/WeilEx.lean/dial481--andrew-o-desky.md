---
{
  "module": "src/Development/WeilBound/ThetaLifts/Reductions/WeilPairs/WeilEx.lean",
  "declarations": [
    "PositivityTheory.ThKW.weilEx"
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

## Existence of the adelic Weil action

[Theorem THETA.1683](https://andrewodesky.com/rh/lean/PositivityTheory.ThKW.weilEx/)

Let $E/F$ be a CM extension of number fields with conjugation $\sigma$. Fix a base datum consisting of an adelic additive character $\psi$, embeddings over all infinite places, two infinity-weight lists, selected split places and embeddings, and a distinguished split place. Assume $E/\mathbb Q$ is Galois, $E/F$ is unramified at finite places, $\psi$ is standard, and its local characters are unramified at the selected places and all inert places; every inert residue cardinality is odd and exceeds three.

Let $X,W$ have dimensions $n,d\ge0$ and satisfy the source's Hermitian and skew-Hermitian signature-and-lattice packages for signatures $(r,s)$ and $(r',s')$. Let $M$ be any Schrödinger model satisfying its compatibility conditions with $\psi$. For any circle-valued Hecke characters $\chi_X,\chi_W$ of $E$ with $$\chi_X|_{\mathbb A_F^\times}=\eta^n,\qquad \chi_W|_{\mathbb A_F^\times}=\eta^d,$$ there is a Weil action $\omega$ in $M$ for the characters $(\psi,\chi_X,\chi_W)$. Here $\eta$ is the character of ([The unique nontrivial quadratic norm character](https://andrewodesky.com/rh/lean/GlobalTheory.IdeleNormChar.globalNormIndexTwo/)), given by membership in $F^\times N_{E/F}(\mathbb A_E^\times)$.
