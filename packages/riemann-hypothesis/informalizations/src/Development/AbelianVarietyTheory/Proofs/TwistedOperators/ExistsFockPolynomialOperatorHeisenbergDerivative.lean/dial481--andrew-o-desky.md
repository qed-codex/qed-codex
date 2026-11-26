---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsFockPolynomialOperatorHeisenbergDerivative.lean",
  "declarations": [
    "GlobalTheory.ArchRec.DerFock.pure_deriv"
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

## A commutator identity differentiates polynomials in commuting operators

[Theorem ALG.0572](https://andrewodesky.com/rh/lean/GlobalTheory.ArchRec.DerFock.pure_deriv/)

Let $I$ be a finite set and $X$ any set. Let $\mathcal P\subseteq\mathbb C^X$ be closed under addition and complex scalar multiplication. Let $A_i,B:\mathbb C^X\to\mathbb C^X$ be maps, each additive and complex homogeneous when restricted to $\mathcal P$. Assume $A_i\mathcal P\subseteq\mathcal P$ and, for all $f\in\mathcal P$ and $i,j\in I$, $$A_iA_jf=A_jA_if,\qquad BA_jf=A_jBf+c_jf,$$ where $c_j\in\mathbb C$ are fixed. If $f\in\mathcal P$ and $Bf=0$, then for every $Q\in\mathbb C[T_i:i\in I]$, $$B\bigl(Q(A)f\bigr)=\left(\sum_{i\in I}c_i\frac{\partial Q}{\partial T_i}\right)(A)f.$$ Here $Q(A)f$ is obtained by applying the commuting $A_i$ to $f$ monomial by monomial.
