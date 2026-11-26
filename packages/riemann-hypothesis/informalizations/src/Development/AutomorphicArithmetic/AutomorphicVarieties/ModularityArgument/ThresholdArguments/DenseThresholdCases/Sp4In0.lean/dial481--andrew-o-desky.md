---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/Sp4In0.lean",
  "declarations": [
    "UpperTheory.V.HV.DescentVanishingReductions.sp4In0_alt"
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

## Finiteness and automorphy for the symplectic lifts of a sum of four characters

[Theorem AGR.1.1761](https://andrewodesky.com/rh/lean/UpperTheory.V.HV.DescentVanishingReductions.sp4In0_alt/)

Assume the fifteen statements of ([Hypothesis list D: fifteen assumed statements on cuspidal automorphic representations of general linear groups, base change, descent to unitary groups and Galois representations](https://andrewodesky.com/rh/lean/UpperTheory.V.Af.HypothesesH'/)).

Let $\Omega$ be an algebraic closure of $\mathbb Q$ and $G=\operatorname{Gal}(\Omega/\mathbb Q)$. Let $\chi$ be a primitive Dirichlet character and $(\nu,q,d)$ an auxiliary triple for $\chi$, with modulus $N$, in the sense of ([Auxiliary moduli of a primitive Dirichlet character and their characters](https://andrewodesky.com/rh/lean/Formalism.HC.PChar/)); that page defines the constants $N_\chi$, $o$, $p_K$, $h_K$ and $p_1$ of $\chi$ and the sets $\mathscr X_{\mathcal O}(e)$ of Dirichlet characters modulo $N$. Let $t\ge0$ be an integer such that $q$ and $d$ are both larger than each of the six numbers $$2t+1,\qquad N_\chi,\qquad o,\qquad p_K,\qquad h_K,\qquad p_1.$$ Let $\ell$ be an odd prime, let $\mathcal O\subset\overline{\mathbb Q}_\ell$ be a discrete valuation ring that contains $\mathbb Z_\ell$ and is a finitely generated $\mathbb Z_\ell$-module, let $e$ be an integer with $0<e<t$, and let $\psi\in\mathscr X_{\mathcal O}(e)$. Let $\mathfrak D$ be a datum for $(\Omega,\ell,\mathcal O)$ that is of case II or of case III for $\chi$, $(\nu,q,d)$, $e$ and $\psi$, in the sense of ([Symplectic lifts of a sum of four characters and their specializations](https://andrewodesky.com/rh/lean/UpperTheory.V.GradeZeroInterpolatingElement.Raw/)); that page defines the points of $\mathfrak D$, their weight-zero subalgebras, the specializations of $\mathfrak D$, and the block form and the corner of a $4\times4$ matrix. Then the following three assertions hold.

1. For every point $\rho$ of $\mathfrak D$, over a ring $R$, the weight-zero subalgebra $R_0(\rho)\subset R$ is a finitely generated $\mathcal O$-module.
2. Let $r$ be a specialization of $\mathfrak D$ such that $r(g)$ is of block form for every $g\in G$. Then the corners $r(g)^{\square}$, $g\in G$, do not span the $\overline{\mathbb Q}_\ell$-vector space $M_2(\overline{\mathbb Q}_\ell)$.
3. There is an isomorphism of fields $\iota:\overline{\mathbb Q}_\ell\to\mathbb C$ with the following property. Let $r$ be a specialization of $\mathfrak D$ such that the matrices $r(g)$, $g\in G$, span the $\overline{\mathbb Q}_\ell$-vector space $M_4(\overline{\mathbb Q}_\ell)$, and suppose that $r$ is continuous. Let $F\subset\Omega$ be an imaginary quadratic field such that the restriction of $r$ to $G_F=\operatorname{Gal}(\Omega/F)$ is irreducible. Then $r|_{G_F}$ is attached to a regular algebraic cuspidal automorphic representation of $\mathrm{GL}_4(\mathbb A_F)$, and the comparison condition $\mathcal W_F(\iota;r|_{G_F})$ holds.
