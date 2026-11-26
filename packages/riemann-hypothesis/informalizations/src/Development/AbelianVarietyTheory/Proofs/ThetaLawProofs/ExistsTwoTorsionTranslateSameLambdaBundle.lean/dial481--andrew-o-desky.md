---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ExistsTwoTorsionTranslateSameLambdaBundle.lean",
  "declarations": [
    "GlobalTheory.SameLam.exists_two_torsion_translate"
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

## Equal polarization bundles differ by a two-torsion translate

[Theorem AV.1151](https://andrewodesky.com/rh/lean/GlobalTheory.SameLam.exists_two_torsion_translate/)

Assume the abelian-scheme laws specified in the conventions below. Let $K$ be algebraically closed, and let $(A,L)$ and $(A',L')$ be abelian varieties with rigidified symmetric ample line bundles whose translation kernels are trivial, in the source's sense. Let $e:A'\simeq A$ be a group-scheme isomorphism. For such a bundle put $$\mathcal B_L=m^*L\otimes0^*L\otimes p_1^*L^{-1}\otimes p_2^*L^{-1}\quad\text{on }A\times A,$$ where $m$ is addition, $0$ the constant zero map, and $p_1,p_2$ the projections. Suppose $\mathcal B_{L'}\simeq(e\times e)^*\mathcal B_L$. Then there is $t\in A(K)$ with $2t=0$ and $$L'\simeq(\tau_t\circ e)^*L,$$ where $\tau_t$ is translation by $t$.
