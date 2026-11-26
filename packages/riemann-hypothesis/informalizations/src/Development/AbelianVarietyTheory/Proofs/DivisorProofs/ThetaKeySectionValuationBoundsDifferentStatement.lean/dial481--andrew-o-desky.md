---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaKeySectionValuationBoundsDifferentStatement.lean",
  "declarations": [
    "GlobalTheory.T.theta_key_section_valuation_bounds_different"
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

## Valuation bound for a normalized theta section

[Theorem ARAK.1149](https://andrewodesky.com/rh/lean/GlobalTheory.T.theta_key_section_valuation_bounds_different/)

Let $E$ be a CM number field, and choose the source's field, lattice, level, moduli and coefficient data, retaining all their defining conditions. Write $(p,q)$ for the lattice signature, $X$ for the smooth quasi-projective moduli scheme with its universal polarized family, and $F\subset\mathbb C$ for the coefficient number field. Suppose $p+q\ge1$. If $M$ is the principal level integer, assume $$3\le M/r^{v_r(M)}\qquad\text{for every rational prime }r.$$ Let $m_\tau$ be the multiplicity of the $\tau:E\hookrightarrow\mathbb C$ Lie eigenspace and choose an ordering of all these eigenspace coordinates. Let $\kappa$ be a theta normalization rule satisfying the source's change-of-frame, base-change, integral-unit and complex normalization conditions, described in the conventions below. Let $K$ be an invertible function rule on framed points of $X$ belonging to the section space of weight $4k$, where $k$ assigns exponent $1$ to every Lie-frame coordinate and exponent $-2$ to the theta-section coordinate. Suppose that over every characteristic-zero extension of $F$, evaluation of $K$ at any framed point equals $\kappa$ of every compatible polarized theta datum, with compatibility matching the theta section and the ordered Lie vectors. For each nonzero prime $w\subset\mathcal O_F$, and every valuation $v$ obtained from the source's algebraic integral framed-model points over complete discrete valuation rings above $w$, $$0\le v(K)\le4\sum_{\tau:E\hookrightarrow\mathbb C}m_\tau\operatorname{ord}_w\bigl(\tau(\mathfrak D_{E/\mathbb Q})\mathcal O_F\bigr).$$ Here the coefficient data supply the embeddings $\tau:E\hookrightarrow F$, and $\mathfrak D_{E/\mathbb Q}$ is the different.
