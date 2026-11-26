---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiAbelianLieSeminegativeBis.lean",
  "declarations": [
    "GlobalTheory.Nef.semiAbelianLieSeminegative"
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

## Seminegativity of a semiabelian Lie bundle

[Theorem AV.0069](https://andrewodesky.com/rh/lean/GlobalTheory.Nef.semiAbelianLieSeminegative/)

Let $C$ be a smooth projective geometrically connected curve over a characteristic-zero field $k$, let $G\to C$ be a semiabelian scheme, and let $W$ be a vector bundle of rank $r$ with an injective morphism of sheaves $W\hookrightarrow\operatorname{Lie}(G/C)$. Then $$\deg_C\det W\le0.$$ A locally free cokernel is not assumed.
