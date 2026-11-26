---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/LevelCohomology/SoCocL.lean",
  "declarations": [
    "UpperTheory.V.X.So.soCocL"
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

## A local-to-global coboundary criterion for a negative cyclotomic twist

[Theorem GC.1139](https://andrewodesky.com/rh/lean/UpperTheory.V.X.So.soCocL/)

Fix a real constant $C$ and assume the condition in ([A uniform bound for second cyclotomic cohomology](https://andrewodesky.com/rh/lean/UpperTheory.V.LemmaK/)) with constant $C$, the condition in ([Normalized Poitou–Tate duality for finite Galois modules](https://andrewodesky.com/rh/lean/GlobalTheory.Published.PoitouTateDuality/)), all three conditions in ([Local cohomology conditions at finite primes](https://andrewodesky.com/rh/lean/ReciprocityTheory.Gal.LocalFiniteness/)), and the assertions of ([Local cohomology finiteness and dimension](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_locfin/)) and ([Local Tate duality](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_tate/)). Let $k$ be a number field, $\Omega$ an algebraic closure, and $G_k=\operatorname{Gal}(\Omega/k)$. Let $\ell$ be prime, and $O\subset\overline{\mathbb Q}_\ell$ a discrete valuation subalgebra finite over $\mathbb Z_\ell$. Let $\psi:G_k\to O^\times$ be a group homomorphism with open kernel, and let $e\ge1$ be an integer. Put $\eta=\chi_\ell^{-e}\psi^{-1}$, where $\chi_\ell$ is the cyclotomic character in $O^\times$. Let $z:G_k\to O$ be continuous for the maximal-ideal topology and satisfy $$z(gh)=z(g)+\eta(g)z(h).$$ Suppose that for every place $v\mid\ell$ there are a decomposition subgroup $D_v\subset G_k$ at $v$, a nonzero $a_v\in O$, and $m_v\in O$ such that $$a_vz(g)=\eta(g)m_v-m_v\qquad(g\in D_v).$$ Then there are a nonzero $a\in O$ and $m\in O$ such that $$az(g)=\eta(g)m-m\qquad(g\in G_k).$$
