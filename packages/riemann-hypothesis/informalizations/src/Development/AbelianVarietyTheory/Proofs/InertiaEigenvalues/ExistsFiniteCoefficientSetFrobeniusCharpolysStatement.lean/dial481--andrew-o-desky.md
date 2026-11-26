---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsFiniteCoefficientSetFrobeniusCharpolysStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_finite_coefficient_set_frobenius_charpolys"
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

## A finite set of coefficients controlling a field of definition

[Theorem AGR.0641](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_finite_coefficient_set_frobenius_charpolys/)

Fix a prime $\ell$, a field isomorphism $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$, a number field $E$ with algebraic closure $\Omega$, an integer $a\ge0$, a dense subset $U\subseteq\Gamma=\operatorname{Gal}(\Omega/E)$, and polynomials $p_\gamma\in\mathbb C[T]$ for $\gamma\in\Gamma$.

There is a finite set $S\subseteq\mathbb C$ with the following property. Let $K\subseteq\overline{\mathbb Q}_\ell$ be any intermediate field over $\mathbb Q_\ell$ containing $\iota^{-1}(S)$. If $\rho:\Gamma\to\operatorname{GL}_a(\overline{\mathbb Q}_\ell)$ is semisimple, its matrix-entry map is continuous, and $$\iota\bigl(\det(T-\rho(\gamma))\bigr)=p_\gamma\qquad(\gamma\in U),$$ then there is $P\in\operatorname{GL}_a(\overline{\mathbb Q}_\ell)$ such that every entry of $P^{-1}\rho(\gamma)P$ belongs to $K$ for every $\gamma\in\Gamma$.
