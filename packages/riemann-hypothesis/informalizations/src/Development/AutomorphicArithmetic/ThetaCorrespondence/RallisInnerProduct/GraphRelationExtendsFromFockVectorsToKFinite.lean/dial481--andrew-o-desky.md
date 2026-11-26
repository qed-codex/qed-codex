---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/RallisInnerProduct/GraphRelationExtendsFromFockVectorsToKFinite.lean",
  "declarations": [
    "UpperTheory.Lit.Rallis.T.siegelWeil_convergent_range_kFinite_thetaFun"
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

## Siegel–Weil value for compact-finite theta functions

[Theorem THETA.1696](https://andrewodesky.com/rh/lean/UpperTheory.Lit.Rallis.T.siegelWeil_convergent_range_kFinite_thetaFun/)

Assume the source's unitary Siegel–Weil theorem in the convergent range and its Weil-theta convergence statement. Fix its full arithmetic datum with CM extension $E/F$, an adelic additive character $\psi$, unitary spaces $A,B$, and a circle-valued character $\chi$. Let $\omega$ on the doubled oscillator space be a Weil datum for $(2A,B)$, additive character $\psi$, and splitting characters $(1,\chi)$. Put $a=\dim A$, $b=\dim B$, and assume $$a<b\le2a,\qquad a+\operatorname{WittIndex}(B)<b.$$ Choose a majorizing matrix $u$ for $A$ and assume Iwasawa decomposition for the associated maximal compact subgroup $K_u$ of $U(2A)(\mathbb A_F)$. Fix compatible archimedean coordinates, an additive Haar measure $\nu$ and fundamental domain $Y$ of covolume one for the rational oscillator lattice, and any Haar measure $m$ on $U(B)(\mathbb A_F)$.

For every permitted theta function $f$ whose $K_u$-orbit spans a finite-dimensional complex space, form the Siegel–Weil section $$F_f(g)=\int_Y(\omega(g,1)f)(\operatorname{lagr}(x))\,d\nu(x),\qquad s_0=(b-a)/2,$$ where $\operatorname{lagr}(x)=(x,-x)$ in the two summands of the doubled space. The Eisenstein family obtained by flat extension of $F_f$ from $s_0$ has holomorphic value at $s_0$ equal to $$g\longmapsto\operatorname{Avg}_{[U(B)]}\theta_{\omega,f}(g,h).$$
