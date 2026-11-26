---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/CharpolyEqOfIsNilpotentSub.lean",
  "declarations": [
    "GlobalTheory.WeilDeligne.IsFrobSS",
    "GlobalTheory.WeilDeligne.exists_isFrobSS"
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

## Semisimplification of a smooth Weil–Deligne pair

[Theorem AGR.1601](https://andrewodesky.com/rh/lean/GlobalTheory.WeilDeligne.exists_isFrobSS/)

Let $E$ be a number field, $\Omega$ an algebraic closure, and $A\subset\Omega$ a valuation ring above a nonzero prime $w$ of $E$. Write $W$ for its Weil group, $I$ for inertia, $q=Nw$ and $\deg:W\to\mathbb Z$ for the Frobenius-degree map. Let $V$ be a finite-dimensional complex vector space, $\rho:W\to\operatorname{GL}(V)$ a representation whose inertia kernel is open, and $N\in\operatorname{End}_{\mathbb C}(V)$ nilpotent, satisfying $$\rho(g)N=q^{\deg g}N\rho(g).$$ There is a representation $\rho^{\mathrm{ss}}$ on $V$ with open inertia kernel, such that every $\rho^{\mathrm{ss}}(g)$ is semisimple, $$\rho^{\mathrm{ss}}(g)N=q^{\deg g}N\rho^{\mathrm{ss}}(g),$$ and, for every $g\in W$, $\rho(g)$ commutes with $\rho^{\mathrm{ss}}(g)$ and $\rho(g)-\rho^{\mathrm{ss}}(g)$ is nilpotent.

## The Weil-Deligne parameter of an l-adic representation at a finite place not above l

[Definition / hypothesis AGR.D106](https://andrewodesky.com/rh/lean/GlobalTheory.WeilDeligne.wdOf/)

Let $E$ be a number field, $\overline E$ an algebraic closure of $E$ and $G_E=\operatorname{Gal}(\overline E/E)$. Let $v$ be a finite place of $E$ and $A$ a valuation ring of $\overline E$ lying over $v$. Let $\ell$ be a prime that does not lie in $v$, let $\iota:\overline{\mathbb Q}_\ell\to\mathbb C$ be an isomorphism of fields, and let $r:G_E\to\mathrm{GL}_n(\overline{\mathbb Q}_\ell)$ be a homomorphism, $n\ge0$. The Weil group $W$ of $A$, its inertia subgroup $I$, the degree $\deg:W\to\mathbb Z$, Weil-Deligne representations of $W$ and their isomorphism classes are those of ([Hypothesis: existence of a reciprocity map for GL\_n over the completions of number fields, with a restricted list of properties](https://andrewodesky.com/rh/lean/UpperTheory.Zero.LLC.RecTExists/)).

**Monodromy data.** A *monodromy datum* for $r$ at $A$ is a triple $(t,\phi,M)$ in which

- $t:I\to\mathbb Z_\ell$ is a continuous surjective homomorphism to the additive group $\mathbb Z_\ell$;
- $\phi\in W$ has $\deg\phi=1$;
- $M$ is a nilpotent $n\times n$ matrix over $\overline{\mathbb Q}_\ell$ such that $r(s)=\exp(t(s)M)$ for every $s$ in some open subgroup of $I$.

The exponential of a nilpotent matrix is the finite sum of its exponential series. For a monodromy datum $(t,\phi,M)$ and $g\in W$, the element $i_g=\phi^{-\deg g}g$ lies in $I$; put $$R_0(g)=\iota\bigl(r(g)\exp(-t(i_g)M)\bigr),\qquad N_0=\iota(M),$$ where $\iota$ is applied to each matrix entry, so that $R_0(g)$ and $N_0$ are complex $n\times n$ matrices.

**Frobenius semisimplification.** A Weil-Deligne representation $(R,N)$ of $W$ on $\mathbb C^n$ is a *Frobenius semisimplification* of $(R_0,N_0)$ if $N=N_0$ and, for every $g\in W$, the matrix $R(g)$ commutes with $R_0(g)$ and $R_0(g)-R(g)$ is nilpotent. Since every $R(g)$ is semisimple, $R(g)$ is then the semisimple part of $R_0(g)$.

**The parameter.** Consider the isomorphism classes of the Weil-Deligne representations that are Frobenius semisimplifications of $(R_0,N_0)$ for some monodromy datum $(t,\phi,M)$ for $r$ at $A$. There is at most one such class: it does not depend on the monodromy datum. The *Weil-Deligne parameter* $\operatorname{WD}_{A,\iota}(r)$ of $r$ at $A$ is this class if it exists, and otherwise the class of $\mathbb C^n$ with the trivial action of $W$ and $N=0$. The class exists whenever $r$ is continuous.
