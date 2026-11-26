---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BlochKatoReductionsOrthogonalModPowStatement.lean",
  "declarations": [
    "GlobalTheory.T.blochKato_reductions_orthogonal_mod_pow"
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

## Orthogonality of reduced finite local cocycles

[Theorem GC.1312](https://andrewodesky.com/rh/lean/GlobalTheory.T.blochKato_reductions_orthogonal_mod_pow/)

Let $l$ be a prime, $K/\mathbb Q_l$ a finite extension in the chosen algebraic closure, and fix the source's local period datum at $K$. Assume its full rational Bloch–Kato orthogonality condition: for every permitted finite-dimensional coefficient field and every nondegenerate cyclotomic-equivariant dual pair with the first representation de Rham, a continuous $1$-cocycle is finite exactly when its cup products with all finite cocycles of the dual representation are continuous coboundaries, in either order.

Let $L/\mathbb Q_l$ be finite, equipped with its finite-dimensional vector-space topology as a topological ring, and let $\mathcal O$ be a discrete valuation domain with fraction field $L$, embedded as an open subring of $L$. Choose a stable lattice $L_1\subset L(1)$ whose underlying submodule is $\mathcal O$. Let $V,V'$ be finite-dimensional continuous $L$-linear representations of $G_K$, with the compatible scalar and vector-space topologies, and let $\Lambda,\Lambda'$ be stable lattices. Let $m:V\times V'\to L$ be a nondegenerate bilinear pairing with equal dimensions, satisfying $$m(gx,gy)=\chi_l(g)m(x,y),\qquad \Lambda'=\{y\in V':m(\Lambda,y)\subset\mathcal O\},$$ where $\chi_l$ is the $l$-adic cyclotomic character. Assume $V$ is de Rham.

For any $a\in\mathcal O$ and integer $r\ge0$, assume $a^r\Lambda$ and $a^r\Lambda'$ are stable. Let $c:G_K\to\Lambda/a^r\Lambda$ and $c':G_K\to\Lambda'/a^r\Lambda'$ be reductions of integral-valued finite cocycles, up to coboundaries in their quotient representations. Fix set-theoretic sections of the quotient maps and use them to choose lattice-valued representatives $\widetilde c,\widetilde c'$ of $c,c'$. Put $$z(g,h)=(a^{-1})^r m\bigl(\widetilde c(g),\,g\widetilde c'(h)\bigr)\in L,$$ where the inverse is taken in $L$ and $0^{-1}=0$. Then the image of $z$ in $L(1)/L_1$ is a $2$-coboundary.
