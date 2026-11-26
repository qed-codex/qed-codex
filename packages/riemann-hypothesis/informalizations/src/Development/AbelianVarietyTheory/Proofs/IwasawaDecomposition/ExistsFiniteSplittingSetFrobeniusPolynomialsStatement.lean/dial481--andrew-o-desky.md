---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsFiniteSplittingSetFrobeniusPolynomialsStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_finite_splitting_set_frobeniusPolynomials"
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

## A finite coefficient set forcing absolute irreducibility of constituents

[Theorem AGR.0243](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_finite_splitting_set_frobeniusPolynomials/)

Fix a prime $\ell$, a field isomorphism $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$, a number field $E$, an algebraic closure $\Omega/E$, and $n\ge0$. Let $\Gamma=\operatorname{Gal}(\Omega/E)$, let $U\subseteq\Gamma$ be dense, and prescribe a polynomial $p_\gamma\in\mathbb C[T]$ for every $\gamma\in\Gamma$.

There is a finite set $S\subseteq\mathbb C$ with this property. Let $O$ be a discrete valuation domain finite as a $\mathbb Z_\ell$-module, endowed with a ring topology defined by its maximal ideal, and let $K=\operatorname{Frac}O$. Let $j:K\to\overline{\mathbb Q}_\ell$ be a field embedding whose composite with $\mathbb Z_\ell\to O\to K$ is the usual inclusion. Suppose $$S\subseteq\iota(j(K)).$$ For every homomorphism $r:\Gamma\to\operatorname{GL}_n(O)$ whose matrix-entry map is continuous, whose representation on $K^n$ is semisimple, and for which $$\iota\bigl(j(\det(T-r(\gamma)))\bigr)=p_\gamma\qquad(\gamma\in U),$$ every irreducible invariant subspace of $K^n$ is absolutely irreducible.
