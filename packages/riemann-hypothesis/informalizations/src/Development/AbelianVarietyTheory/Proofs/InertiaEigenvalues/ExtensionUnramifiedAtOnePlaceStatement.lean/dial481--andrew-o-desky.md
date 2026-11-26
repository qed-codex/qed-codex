---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExtensionUnramifiedAtOnePlaceStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_unramified_totallyComplex_ext_with_unity_roots"
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

## A totally complex extension with a prescribed residue degree

[Theorem ANT.1666](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_unramified_totallyComplex_ext_with_unity_roots/)

Let $E$ be a number field, $\Omega$ an algebraic closure, $g$ a prime, and $w$ a finite place of $E$. Fix a valuation ring $A\subseteq\Omega$ above $w$ and a continuous field isomorphism $\mathbb Q_g\simeq E_w$. For every $n>0$, there is a totally complex number field $E'$ with compatible embeddings $E\subseteq E'\subseteq\Omega$ and a finite place $w'$ of $E'$ induced by $A$ such that $$g\in\mathfrak p_{w'}\setminus\mathfrak p_{w'}^2,\qquad \#(\mathcal O_{E'}/\mathfrak p_{w'})=g^n.$$ The field $E'$ contains a primitive $(g^n-1)$-st root of unity, and every element of the inertia group of $\Omega/E$ associated with $A$ fixes $E'$ pointwise.
