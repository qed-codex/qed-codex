---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsAppellHumbertLineBundle.lean",
  "declarations": [
    "GlobalTheory.exists_isFactorAH_frame_of_unif"
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

## An Appell–Humbert frame on a fixed uniformization

[Theorem AV.0751](https://andrewodesky.com/rh/lean/GlobalTheory.exists_isFactorAH_frame_of_unif/)

Let $A/\mathbb C$ be an abelian variety with its commutative group structure, and fix $g\ge0$ and a holomorphic uniformization $u_0:\mathbb C^g\to A(\mathbb C)$ together with a holomorphic frame for the pullback of a reference line bundle $L_0$. For every line bundle $M$ on $A$, there are a holomorphic frame for $u_0^*M$, a Hermitian matrix $H\in M_g(\mathbb C)$, and a function $\chi:\Lambda\to\mathbb C$ with $|\chi(\lambda)|=1$, where $\Lambda=\ker u_0$, such that its local frame functions satisfy $$f_i(z)=\chi(\lambda)\exp\!\left(\pi z^tH\overline\lambda+\frac\pi2\lambda^tH\overline\lambda\right)f_i(z+\lambda).$$ This holds for every $\lambda\in\Lambda$ and every $z$ mapping into the corresponding trivializing open set of $M$.
