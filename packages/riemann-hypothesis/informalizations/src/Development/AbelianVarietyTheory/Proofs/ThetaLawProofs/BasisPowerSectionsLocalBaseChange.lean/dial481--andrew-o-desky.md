---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/BasisPowerSectionsLocalBaseChange.lean",
  "declarations": [
    "GlobalTheory.KeyBasis.main"
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

## Bases of powers of a principal polarization commute with base change

[Theorem AV.0227](https://andrewodesky.com/rh/lean/GlobalTheory.KeyBasis.main/)

Assume the abelian-scheme law package specified in the conventions. Let $R$ be a commutative Noetherian local ring. Choose an abelian scheme $A/R$ of dimension $g\ge1$, a symmetric relatively ample line bundle $L$ with trivial translation kernel, a rigidification of $L$ at zero, a section $\theta$ nonzero on every fiber, and a basis of $\operatorname{Lie}(A/R)$. For every integer $l\ge1$, there is an $R$-basis of $H^0(A,L^{\otimes l})$ with $l^g$ elements.

For every such basis and every homomorphism $R\to R'$ of commutative rings, its pullback is a basis of $H^0(A',L'^{\otimes l})$ whenever the chosen data over $R'$ are identified with these pullbacks, including the group scheme, line bundle, rigidification, theta section and tangent basis.
