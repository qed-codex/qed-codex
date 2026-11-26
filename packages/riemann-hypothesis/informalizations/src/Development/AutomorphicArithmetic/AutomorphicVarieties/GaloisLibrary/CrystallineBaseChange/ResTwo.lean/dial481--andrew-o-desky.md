---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/CrystallineBaseChange/ResTwo.lean",
  "declarations": [
    "UpperTheory.V.Br.resTwo"
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

## Irreducibility and uniqueness under quadratic restriction

[Theorem REP.0574](https://andrewodesky.com/rh/lean/UpperTheory.V.Br.resTwo/)

Let $\Gamma,\Gamma'$ be groups, $k$ an algebraically closed field of characteristic zero, $\phi:\Gamma'\to\Gamma$ a homomorphism, and $\delta:\Gamma\to k^\times$ a character such that $$\ker\delta=\operatorname{im}\phi,\qquad\delta(g)\in\{1,-1\}\quad(g\in\Gamma).$$ For every $n\ge0$ and representation $r:\Gamma\to\operatorname{GL}_n(k)$:

1. If $r$ is irreducible and $r\not\simeq r\otimes\delta$, then $r\circ\phi$ is irreducible.
2. For every $r':\Gamma\to\operatorname{GL}_n(k)$, if $r\circ\phi$ is irreducible and $r\circ\phi\simeq r'\circ\phi$, then $r'\simeq r$ or $r'\simeq r\otimes\delta$.

Here $(r\otimes\delta)(g)=\delta(g)r(g)$.
