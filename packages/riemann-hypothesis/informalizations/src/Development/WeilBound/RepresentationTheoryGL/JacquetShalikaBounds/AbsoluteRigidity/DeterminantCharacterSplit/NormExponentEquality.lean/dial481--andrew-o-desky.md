---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/JacquetShalikaBounds/AbsoluteRigidity/DeterminantCharacterSplit/NormExponentEquality.lean",
  "declarations": [
    "PositivityTheory.RgJS.norm_exponent_equality"
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

## Unitary cuspidal classes are imaginary norm twists of normalized forms

[Theorem REP.1642](https://andrewodesky.com/rh/lean/PositivityTheory.RgJS.norm_exponent_equality/)

Let $E$ be a totally complex number field. There is a family of Hecke characters $\nu_t$, $t\in\mathbb R$, unramified at every finite place $w$, with $$\nu_{t,w}(\varpi_w)=q_w^{-it},\qquad q_w=|\mathcal O_E/\mathfrak p_w|,$$ such that every unitary cuspidal automorphic isomorphism class $\pi$ of $\operatorname{GL}_m(\mathbb A_E)$, $m\ge1$, can be written $$\pi=[\pi_0]\otimes\nu_t$$ for some cuspidal automorphic subrepresentation $\pi_0$ and some $t\in\mathbb R$. Here $\pi_0$ is normalized: its forms are invariant under $z(x)$, the scalar $e^xI_m$ at every infinite place and the identity at every finite place, for every $x\in\mathbb R$.
