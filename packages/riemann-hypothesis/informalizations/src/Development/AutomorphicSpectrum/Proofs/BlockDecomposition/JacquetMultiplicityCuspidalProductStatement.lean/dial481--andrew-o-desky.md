---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/JacquetMultiplicityCuspidalProductStatement.lean",
  "declarations": [
    "GlobalTheory.T.jacquet_multiplicity_cuspidal_product"
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

## Jacquet multiplicity in a product of cuspidal representations

[Theorem REP.1282](https://andrewodesky.com/rh/lean/GlobalTheory.T.jacquet_multiplicity_cuspidal_product/)

Assume ([Admissibility of smooth irreducible general linear representations](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.SmGLBridge.irreducibleAdmissible/)) universally over nonarchimedean local fields. Let $k$ be such a field, and let $x_1,\ldots,x_l$ and $y_1,\ldots,y_c$ be families of smooth irreducible cuspidal complex representations, where $x_a$ is a representation of $\mathrm{GL}_{n_a}(k)$ and $y_b$ of $\mathrm{GL}_{m_b}(k)$. Allow empty families and suppose $$\sum_{a=1}^{l}n_a=\sum_{b=1}^{c}m_b=N.$$ Let $\Pi=x_1\times\cdots\times x_l$ denote normalized parabolic induction to $\mathrm{GL}_N(k)$ and let $r_{(m_1,\ldots,m_c)}(\Pi)$ be its normalized Jacquet module for the standard ordered blocks of sizes $m_b$. Then $$\bigl[r_{(m_1,\ldots,m_c)}(\Pi):y_1\boxtimes\cdots\boxtimes y_c\bigr]=\#\{e:\{1,\ldots,c\}\simeq\{1,\ldots,l\}:y_b=x_{e(b)}\text{ for all }b\}.$$ The left side is Jordan–Holder multiplicity, with values in $\mathbb N\cup\{\infty\}$; equality on the right is equality of equivalence classes of irreducible representations.
