---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/AutomorphyLifting/SplitIrr.lean",
  "declarations": [
    "UpperTheory.V.Z.Win.UnlAll"
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

## Automorphy over imaginary quadratic fields and a class of four-dimensional l-adic representations of the Galois group of Q

[Definition / hypothesis AGR.D278](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Win.IsAutQA/)

This page defines a condition on a representation of $\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)$ with coefficients in $\overline{\mathbb Q}_\ell$, which asks that its restrictions to imaginary quadratic fields be attached to cuspidal automorphic representations, and a class $\mathcal R_4(\iota,e,M)$ of four-dimensional representations that satisfy it. The conditions from which both are built are those of ([Level, attachment and comparison conditions on l-adic Galois representations](https://andrewodesky.com/rh/lean/UpperTheory.V.Af.Level/)).

**Setting.** Let $\Omega$ be an algebraic closure of $\mathbb Q$ and $G=\operatorname{Gal}(\Omega/\mathbb Q)$; for a number field $F\subset\Omega$ write $G_F=\operatorname{Gal}(\Omega/F)$. Let $\ell$ be a prime, $\overline{\mathbb Q}_\ell$ an algebraic closure of $\mathbb Q_\ell$, $\iota:\overline{\mathbb Q}_\ell\to\mathbb C$ an isomorphism of fields, and $\epsilon_\ell:G\to\mathbb Z_\ell^\times\subset\overline{\mathbb Q}_\ell^\times$ the $\ell$-adic cyclotomic character. The following notions are those of ([Level, attachment and comparison conditions on l-adic Galois representations](https://andrewodesky.com/rh/lean/UpperTheory.V.Af.Level/)), formed with $\Omega$: representations $r:G\to\mathrm{GL}_n(\overline{\mathbb Q}_\ell)$, their irreducibility, isomorphism and restriction to $G_F$; the places $A$ of $\Omega$ above a prime and their decomposition groups $D_A$; representations that are triangular on $D_A$ with given diagonal characters; the field $\mathbb Q(\mu_M)\subset\Omega$; the level condition $\mathcal L_\ell(M;\mathbf m;r)$; attachment to a cuspidal automorphic representation; and the comparison condition $\mathcal W_F(\iota;r)$.

**Automorphy over imaginary quadratic fields.** A representation $r:G\to\mathrm{GL}_n(\overline{\mathbb Q}_\ell)$ satisfies the condition $\mathcal A^{\rm q}(\iota;r)$ if either $r$ is not continuous, or the following two assertions hold for every imaginary quadratic field $F\subset\Omega$ such that $r|_{G_F}$ is irreducible.

1. $r|_{G_F}$ is attached to a regular algebraic cuspidal automorphic representation of $\mathrm{GL}_n(\mathbb A_F)$.
2. The comparison condition $\mathcal W_F(\iota;r|_{G_F})$ holds.

**The class $\mathcal R_4(\iota,e,M)$.** Let $e\ge0$ and $M\ge1$ be integers. The class $\mathcal R_4(\iota,e,M)$ consists of the representations $r:G\to\mathrm{GL}_4(\overline{\mathbb Q}_\ell)$ with the following five properties.

1. $r$ is irreducible.
2. $\mathcal A^{\rm q}(\iota;r)$ holds.
3. $\mathcal L_\ell\bigl(M;(e+1,e,1,0);r\bigr)$ holds.
4. There are an integer $M'\ge1$, a character $\chi:G\to\overline{\mathbb Q}_\ell^\times$ that is trivial on $G_{\mathbb Q(\mu_{M'})}$, and a matrix $P\in\mathrm{GL}_4(\overline{\mathbb Q}_\ell)$ such that $${}^tr(s)\,P\,r(s)=\epsilon_\ell(s)^{e+1}\chi(s)\,P\qquad(s\in G).$$
5. $\ell$ divides $M$, and for every place $A$ of $\Omega$ above $\ell$ the representation $r$ is triangular on $D_A$ with diagonal characters $\kappa_1,\dots,\kappa_4$ such that $\kappa_i\ne\kappa_j\cdot\epsilon_\ell|_{D_A}$ for all $i,j$.
