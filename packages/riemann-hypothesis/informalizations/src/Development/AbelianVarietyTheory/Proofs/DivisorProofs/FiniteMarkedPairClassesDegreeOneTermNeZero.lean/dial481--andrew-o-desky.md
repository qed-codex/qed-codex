---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/FiniteMarkedPairClassesDegreeOneTermNeZero.lean",
  "declarations": [
    "GlobalTheory.LKCx.FiniteClassIntegralRoots.finite_pol_marked'"
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

## Finiteness of marked minimal polynomials with bounded denominators

[Theorem AGR.1134](https://andrewodesky.com/rh/lean/GlobalTheory.LKCx.FiniteClassIntegralRoots.finite_pol_marked'/)

Let $p$ be prime and fix the unitary central-simple-algebra data at $p$ described in the conventions below. Write $F$ for its CM field, $C$ for its central simple $F$-algebra of dimension $n^2$, $*$ for its involution of the second kind, and $\psi_v:C\to M_n(\mathbb C)$ for its archimedean realizations with nonsingular Hermitian matrices $H_v$. Suppose exactly one infinite place has signature $(1,n-1)$; the other places have signature $(0,n)$. A pair consists of $\beta,\gamma\in C^\times$ and $c\in\mathbb Q^\times$ satisfying $$\beta^*=\beta,\qquad\gamma\beta\gamma^*=c\beta,$$ with the minimal polynomial of $\gamma$ over $F$ separable of degree $n$. Require that $\beta$ be carried by $x\beta x^*$ to a scalar unit over the finite adeles away from $p$, and to $1$ over $\mathbb R\otimes_{\mathbb Q}C$. Call the pair marked if for some infinite place $v$ of signature $(1,n-1)$ there are $\mu\in\mathbb C$ and $x\in\mathbb C^n$ with $$\psi_v(\gamma)x=\mu x,\qquad\operatorname{Re}\bigl(x^*H_v\psi_v(\beta^{-1})x\bigr)>0.$$ For every integer $N>0$, the set of minimal polynomials over $F$ of $\gamma$ in marked pairs for which both $N\gamma$ and $N\gamma^{-1}$ are integral over $\mathbb Z$ is finite.
