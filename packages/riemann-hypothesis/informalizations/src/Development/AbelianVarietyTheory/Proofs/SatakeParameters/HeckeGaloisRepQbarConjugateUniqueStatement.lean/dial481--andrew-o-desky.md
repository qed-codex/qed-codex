---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/HeckeGaloisRepQbarConjugateUniqueStatement.lean",
  "declarations": [
    "GlobalTheory.T.heckeGaloisRepQbar_conjugate_unique"
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

## Conjugacy of two semisimple Galois representations with the same Hecke polynomials

[Theorem AGR.1015](https://andrewodesky.com/rh/lean/GlobalTheory.T.heckeGaloisRepQbar_conjugate_unique/)

Work in the source's full arithmetic unitary datum over a CM field $E$, and assume the strong-multiplicity-one package in the conventions below. Fix one of its coefficient-prime indices $i$, with prime $\ell$, excluded finite-place sets $S_i,Q_i$, and a permitted parameter $x$. For each split finite place $w\notin S_i\cup Q_i$ not over $\ell$, let $P_{x,w}(T)$ be the associated prescribed Hecke polynomial in $\overline{\mathbb Q}_\ell[T]$, of degree $n$.

Let $\rho,\rho':\operatorname{Gal}(\Omega/E)\to\operatorname{GL}_n(\overline{\mathbb Q}_\ell)$ be semisimple representations whose matrix-coefficient maps are continuous, with $\Omega$ the given algebraic closure of $E$. Assume that for every such $w$, every extension of its valuation to $\Omega$, and every Frobenius lift $\sigma$ for that extension, $$\det(T-\rho(\sigma))=P_{x,w}(T)=\det(T-\rho'(\sigma)).$$ There is $C\in\operatorname{GL}_n(\overline{\mathbb Q}_\ell)$ such that $$\rho'(g)=C^{-1}\rho(g)C\qquad(g\in\operatorname{Gal}(\Omega/E)).$$
