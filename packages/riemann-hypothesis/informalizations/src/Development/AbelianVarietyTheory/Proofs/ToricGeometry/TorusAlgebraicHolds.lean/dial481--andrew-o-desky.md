---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ToricGeometry/TorusAlgebraicHolds.lean",
  "declarations": [
    "GlobalTheory.torusAlgebraic_holds"
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

## Algebraic realization of a polarized complex torus and its theta functions

[Theorem AV.0095](https://andrewodesky.com/rh/lean/GlobalTheory.torusAlgebraic_holds/)

Let $g\ge0$, $\tau\in M_g(\mathbb C)$ be symmetric with $\Im\tau$ positive definite, and $a,b\in\{0,\tfrac12\}^g$. Put $\Lambda=\mathbb Z^g+\tau\mathbb Z^g$ and $$\vartheta_{a,b}(z)=\sum_{m\in\mathbb Z^g}\exp\bigl(\pi i(m+a)^t\tau(m+a)+2\pi i(m+a)^t(z+b)\bigr).$$ There are a principally polarized complex abelian variety $(A,L)$ of dimension $g$, a holomorphic uniformization $u:\mathbb C^g\to A(\mathbb C)$ with kernel exactly $\Lambda$, and a section of $L$ represented by $\vartheta_{a,b}$. The differential of $u$ identifies $\mathbb C^g$ bijectively with the tangent vectors at the identity.

For every $N\ge0$, the uniformization identifies sections of $L^{\otimes N}$ bijectively with entire functions $f$ satisfying $$f(z+\tau m+n)=\exp\!\left(2\pi iN\bigl(a^tn-b^tm-\tfrac12m^t\tau m-m^tz\bigr)\right)f(z)\qquad(m,n\in\mathbb Z^g).$$ For every $N\ge3$, $L^{\otimes N}$ is very ample. Every complex-linear $F:\mathbb C^g\to\mathbb C^g$ with $F\Lambda\subseteq\Lambda$ is induced by an algebraic group endomorphism $\phi:A\to A$, with $u(Fz)=\phi(u(z))$.
