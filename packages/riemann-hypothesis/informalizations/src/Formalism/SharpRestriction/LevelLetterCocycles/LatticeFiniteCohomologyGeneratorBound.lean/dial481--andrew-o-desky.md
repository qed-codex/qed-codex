---
{
  "module": "src/Formalism/SharpRestriction/LevelLetterCocycles/LatticeFiniteCohomologyGeneratorBound.lean",
  "declarations": [
    "Formalism.MainNotions.RamifiedCoefficientChains.len_step_of_ker"
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

## A quotient-length bound from a kernel containment

[Theorem ALG.0886](https://andrewodesky.com/rh/lean/Formalism.MainNotions.RamifiedCoefficientChains.len_step_of_ker/)

Let $O$ be a principal ideal domain, let $M,Q$ be $O$-modules, and let $A,B,P\subseteq M$ be submodules. If an $O$-linear map $u:B\to Q$ satisfies $\ker u\subseteq A\cap B$, then $$\operatorname{length}_O\bigl(B/(B\cap(A+P))\bigr)\le\operatorname{length}_O(Q).$$
