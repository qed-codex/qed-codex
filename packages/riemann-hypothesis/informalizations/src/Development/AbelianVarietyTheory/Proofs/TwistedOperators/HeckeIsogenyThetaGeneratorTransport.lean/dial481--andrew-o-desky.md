---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/HeckeIsogenyThetaGeneratorTransport.lean",
  "declarations": [
    "GlobalTheory.ThetaTransport.existsUnique_trace_isThGen"
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

## A unique theta trace transports a section generator

[Theorem AV.1599](https://andrewodesky.com/rh/lean/GlobalTheory.ThetaTransport.existsUnique_trace_isThGen/)

Fix the source's CM moduli package: a CM number field $E$, its integral datum and level, a moduli scheme $X$ with universal group and rigidified polarization line bundle, and a coefficient datum $c$ with number field $F_c$. Write $M'$ for the level integer used in the split-prime condition and $g=([E:\mathbb Q]/2)(p_0+q_0)$, where $p_0,q_0$ are the two signature ranks of the integral datum. Let $\Omega$ be an algebraically closed $F_c$-algebra field and let $x,x'\in X(\Omega)$, with $x$ over the coefficient point specified by $c$. Denote the universal fibres by $A_x,A_{x'}$ and their line bundles by $L_x,L_{x'}$.

Let $p$ be prime, $\mathfrak p\subset\mathcal O_E$ maximal, $p\in\mathfrak p$, $\mathfrak p+\bar{\mathfrak p}=\mathcal O_E$, and $p\nmid M'$. Let $i\ge0$ and let $C\subseteq A_x(\Omega)$ satisfy the Hecke-kernel conditions in the conventions. Let $\Psi:A_x\to A_{x'}$ be over $\Omega$, preserve the identity and group law, commute with $\mathcal O_E$, and be surjective on $\Omega$-points with kernel $C$. Assume $x,x'$ have the same base point, $\Psi$ raises Weil-pairing values to their $p^2$ powers at every order prime to $p$, and it carries both specified level maps to their multiples by $p$.

If every section of $L_x$ has a unique expression $a s$ with $a\in\Omega$ for a section $s$, then there is a unique theta-trace section $s'$ of $L_{x'}$ along $\Psi$, and every section of $L_{x'}$ has a unique expression $a s'$. Here a theta trace means the following: after a rigidified isomorphism $\Psi^*L_{x'}\simeq L_x^{\otimes p^2}$, its pullback is the sum of translates of the normalized multiplication pullback $[p]^*s$ by representatives of $\ker\Psi$ modulo its $p$-torsion, using theta-group lifts compatible with the rigidified isomorphism.
