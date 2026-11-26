---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/AlgebraicModularFormsStrongMultiplicityOneStatement.lean",
  "declarations": [
    "GlobalTheory.T.algebraic_modular_forms_strong_multiplicity_one"
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

## Local matching determines an irreducible algebraic modular representation

[Theorem AGR.0992](https://andrewodesky.com/rh/lean/GlobalTheory.T.algebraic_modular_forms_strong_multiplicity_one/)

Let $L$ be a CM number field, $F=L^+$, $n\ge0$, and $G=U(I_n)$ over $F$. Let $W$ be a finite-dimensional complex vector space with an irreducible representation $\rho$ of $G(F)$ whose matrix coefficients, in some basis, are polynomials in the complex-embedding coordinates of rational matrices. Let $S_1,S_2$ be nonzero irreducible right-translation subspaces of the algebraic modular forms with coefficients $W$.

Assume the following local matching conditions.

1. For every split-place embedding $L\hookrightarrow F_v$, choose the associated place $w$ of $L$. There are isomorphic smooth irreducible representations $\sigma_1,\sigma_2$ of $\operatorname{GL}_n(L_w)$, each admitting an injective linear map into $S_i$ that intertwines the action of every adelic element supported at $v$, using a continuous identification $F_v\simeq L_w$ extending the chosen embedding.
2. For every finite place $v$ of $F$ with no such embedding, there are $w\mid v$, local coordinates as below, and $\alpha\in\mathbb C^{\lfloor n/2\rfloor}$ such that each $S_i$ contains a nonzero vector $f_i$ fixed by a subgroup $U_i\subseteq G(\mathbb A_{F,f})$. On elements supported at $v$, membership in $U_i$ is exactly membership in the standard integral subgroup. Every spherical local Hecke function $h$ acts on $f_i$ by the same scalar $\mathcal S_\alpha(h)$.

Then $S_1\simeq S_2$ as representations of $G(\mathbb A_{F,f})$.
