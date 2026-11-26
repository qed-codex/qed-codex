---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsIntegralLogHomDiagonalOfLimitStatement.lean",
  "declarations": [
    "GlobalTheory.T.isIntegralLogHom_diagonal_of_limit"
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

## Integral formal homomorphisms from limits of diagonal eigenvalues

[Theorem PHT.0839](https://andrewodesky.com/rh/lean/GlobalTheory.T.isIntegralLogHom_diagonal_of_limit/)

Let $C$ be a characteristic-zero field with an additive valuation $v:C\to\mathbb R\cup\{\infty\}$, and put $\mathcal O_v=\{x:v(x)\ge0\}$. Fix $d\ge0$ and formal series $\ell=(\ell_1,\ldots,\ell_d)$ and $F$ as in the conventions. Let $I$ be finite and $$U\in M_{d\times I}(\mathcal O_v),\qquad L\in M_{I\times d}(\mathcal O_v),\qquad UL=I_d.$$ Fix $t=(t_i)_{i\in I}\in C^I$. Suppose that for every real $r$ there are $t'\in C^I$, $A\in M_d(C)$, and $\phi\in\mathcal O_v[[X_1,\ldots,X_d]]^d$ with zero constant term such that $$\ell(\phi(X))=A\ell(X),\qquad AU_i=t'_iU_i,\qquad v(t'_i-t_i)\ge r\quad(i\in I),$$ where $U_i$ is column $i$ of $U$. Then there is $\phi\in\mathcal O_v[[X_1,\ldots,X_d]]^d$ with zero constant term satisfying $$\ell(\phi(X))=U\operatorname{diag}(t)L\,\ell(X).$$
