---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/MemNormGroupIffEverywhereNorm.lean",
  "declarations": [
    "GlobalTheory.IdeleNormChar.globalNormIndexTwo"
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

## The unique nontrivial quadratic norm character

[Theorem ANT.1511](https://andrewodesky.com/rh/lean/GlobalTheory.IdeleNormChar.globalNormIndexTwo/)

Let $E/F$ be a degree-two extension of number fields. There is a unique continuous character $\eta:\mathbb A_F^\times\to S^1$ satisfying $$\eta|_{F^\times}=1,\qquad \eta(N_{E/F}x)=1\quad(x\in\mathbb A_E^\times),\qquad \eta\ne1.$$ Here the adelic norm is the algebra norm on $\mathbb A_F\otimes_F E$, with its unit group identified with $\mathbb A_E^\times$.
