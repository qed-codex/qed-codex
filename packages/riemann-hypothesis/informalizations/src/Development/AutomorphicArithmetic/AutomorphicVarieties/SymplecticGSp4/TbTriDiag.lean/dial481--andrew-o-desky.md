---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/SymplecticGSp4/TbTriDiag.lean",
  "declarations": [
    "UpperTheory.V.GradeZeroInterpolatingElement.tanBK"
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

## Tangent cocycles satisfy the Bloch–Kato condition

[Theorem GC.1140](https://andrewodesky.com/rh/lean/UpperTheory.V.GradeZeroInterpolatingElement.tanBK/)

Let $\Omega$ be an algebraic closure of $\mathbb Q$, let $\ell$ be prime, and let $O\subset\overline{\mathbb Q}_\ell$ be a discrete valuation subalgebra finite over $\mathbb Z_\ell$. Fix the source's good four-dimensional ordinary symplectic deformation datum over $O$, and assume its local cohomology input package, both described in the conventions. Let $r:G_{\mathbb Q}\to M_4(\overline{\mathbb Q}_\ell)$ be a point of this datum. Let $$r_\epsilon:G_{\mathbb Q}\to M_4(\overline{\mathbb Q}_\ell[\epsilon]/\epsilon^2)$$ be a point of the same datum, with constant term $r$. A point here means specialization of a continuous matrix lift of the prescribed residual representation over a complete Noetherian local $O$-algebra, satisfying the datum's similitude, ramification, normalization, and prescribed local-component conditions. Write $r_\epsilon(g)=r(g)+\epsilon b(g)$ and put $z(g)=b(g)r(g^{-1})$. Then $$z(gh)=z(g)+r(g)z(h)r(g)^{-1},$$ and $z$ satisfies the Bloch–Kato local conditions for the adjoint representation at every place: its restriction to inertia at every finite prime other than $\ell$ is a coboundary, and at $\ell$ it satisfies the $V$-valued finite-cocycle condition defined in ([Finite local cocycles modulo a power are reductions of integral cocycles](https://andrewodesky.com/rh/lean/GlobalTheory.BKTorsionRed.mem_HfQ_iff_red/)) after a compatible embedding of $\Omega$ into $\overline{\mathbb Q}_\ell$. Moreover $$z(g)\in\mathfrak{sp}_4(\overline{\mathbb Q}_\ell)\qquad(g\in G_{\mathbb Q}),$$ for the datum's fixed symplectic form.
