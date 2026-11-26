---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeckeAlgebras/OrdinaryHeckeCharacters/HiComm.lean",
  "declarations": [
    "UpperTheory.V.Hi.hiComm"
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

## Commuting Hecke operators on finite free ordinary spaces

[Theorem AGR.1693](https://andrewodesky.com/rh/lean/UpperTheory.V.Hi.hiComm/)

Let $L$ be a number field with algebraic closure $\Omega$, $\ell$ a prime, $n\ge0$, and $\mathcal O\subset\overline{\mathbb Q}_\ell$ a discrete valuation $\mathbb Z_\ell$-algebra finite over $\mathbb Z_\ell$. Fix the source's full ordinary-Hecke setting and assume its structural axiom package. Let $A$ be a complete Noetherian local commutative $\mathcal O$-algebra such that $\mathcal O\to A$ is local and surjective on residue fields. Let $\theta$ be an $A^\times$-valued character of the setting's torus satisfying the weight package: continuity in the prescribed sense and the free-action condition at every allowed level.

At every tuple $K$ of compact open subgroups at the auxiliary finite places, the ordinary module $M^{\mathrm{ord}}(\theta,K)$ is finite free over $A$, is preserved by every prescribed spherical and ordinary Hecke operator $T_i$, and these operators commute on it: $$T_iT_jv=T_jT_iv\qquad(v\in M^{\mathrm{ord}}(\theta,K)).$$ For every list $a_i\in\mathcal O$, the corresponding localized module $M^{\mathrm{ord}}(\theta,a,K)$ has the same finite freeness, stability, and commutativity properties.
