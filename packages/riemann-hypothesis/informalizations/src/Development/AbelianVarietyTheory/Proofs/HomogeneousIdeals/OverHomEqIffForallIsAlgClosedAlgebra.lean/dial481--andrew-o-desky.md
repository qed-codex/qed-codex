---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/HomogeneousIdeals/OverHomEqIffForallIsAlgClosedAlgebra.lean",
  "declarations": [
    "GlobalTheory.WeierstrassCurve.exists_eq_ptHom",
    "GlobalTheory.WeierstrassCurve.exists_unit_smul_of_minors",
    "GlobalTheory.WeierstrassCurve.ptOver_eq_ptOver_iff"
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

## Unimodular vectors with vanishing two by two minors differ by a unit

[Theorem ALG.0956](https://andrewodesky.com/rh/lean/GlobalTheory.WeierstrassCurve.exists_unit_smul_of_minors/)

Let $A$ be a commutative ring, $I$ a finite set, and $P,Q\in A^I$. Suppose the coordinates of each vector generate the unit ideal and $$P_iQ_j=P_jQ_i\qquad(i,j\in I).$$ There is $u\in A^\times$ such that $Q_i=uP_i$ for every $i\in I$.

## Equality of projective Weierstrass points

[Theorem AG.0995](https://andrewodesky.com/rh/lean/GlobalTheory.WeierstrassCurve.ptOver_eq_ptOver_iff/)

Let $R$ be a commutative ring, $A$ a commutative $R$-algebra, and $W$ a Weierstrass equation over $R$. Let $P,Q\in A^3$ satisfy the homogenized Weierstrass equation of $W_A$, and suppose the coordinates of each triple generate the unit ideal of $A$. Let $[P],[Q]:\operatorname{Spec}A\to W$ be the resulting points over $\operatorname{Spec}R$. Then $$[P]=[Q]\quad\Longleftrightarrow\quad Q=uP\text{ for some }u\in A^\times.$$

## Homogeneous coordinates for a Weierstrass point over a local ring

[Theorem AG.1022](https://andrewodesky.com/rh/lean/GlobalTheory.WeierstrassCurve.exists_eq_ptHom/)

Let $R$ be a commutative ring, $W$ a Weierstrass equation over $R$, $A$ a commutative local ring, and $\rho:R\to A$ a ring homomorphism. Every $R$-morphism $\operatorname{Spec}A\to W$ is represented by a triple $(X,Y,Z)\in A^3$ generating the unit ideal and satisfying $$Y^2Z+a_1XYZ+a_3YZ^2=X^3+a_2X^2Z+a_4XZ^2+a_6Z^3,$$ where the coefficients are mapped from $R$ to $A$ through $\rho$.
