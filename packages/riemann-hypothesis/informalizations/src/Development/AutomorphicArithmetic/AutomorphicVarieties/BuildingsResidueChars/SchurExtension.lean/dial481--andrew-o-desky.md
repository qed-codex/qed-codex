---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/BuildingsResidueChars/SchurExtension.lean",
  "declarations": [
    "UpperTheory.schur_extension"
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

## Equivalent restrictions differ by a character twist

[Theorem REP.0302](https://andrewodesky.com/rh/lean/UpperTheory.schur_extension/)

Let $\Gamma,\Gamma'$ be groups, $k$ an algebraically closed field, $n\ge0$, $r,r_1:\Gamma\to\operatorname{GL}_n(k)$ representations, and $\phi:\Gamma'\to\Gamma$ a homomorphism with normal image. Suppose $r\circ\phi$ is irreducible and $r_1\circ\phi\simeq r\circ\phi$. There is a character $\delta:\Gamma\to k^\times$ such that $$\delta\circ\phi=1,\qquad r_1\otimes\delta\simeq r.$$
