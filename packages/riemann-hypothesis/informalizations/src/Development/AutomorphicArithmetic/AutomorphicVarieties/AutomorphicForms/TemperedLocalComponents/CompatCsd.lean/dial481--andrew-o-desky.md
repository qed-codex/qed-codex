---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/AutomorphicForms/TemperedLocalComponents/CompatCsd.lean",
  "declarations": [
    "UpperTheory.V.Af.compatCsd"
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

## Local comparison for an attached conjugate-self-dual representation

[Theorem AGR.1205](https://andrewodesky.com/rh/s/u3-csd-local-global-compatibility.html)

Assume the source's classical automorphy and descent package. Let $F$ be a CM field with algebraic closure $\Omega$, let $\ell$ be prime, let $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$, and let $n\ge1$. Let $\pi$ be a regular algebraic conjugate-self-dual cuspidal representation of $\mathrm{GL}_n(\mathbb A_F)$, and let $r:G_F\to\mathrm{GL}_n(\overline{\mathbb Q}_\ell)$ be continuous and semisimple. Suppose that at all but finitely many finite places its Frobenius eigenvalues agree through $\iota$ with the algebraically normalized Satake parameters of $\pi$.

For every finite place $w$, every local component $\pi_w$, every valuation of $\Omega$ above $w$, and every local reciprocity map satisfying the source's correspondence conditions, let $y_w$ be the parameter of the algebraically normalized $\pi_w$. If $w\nmid\ell$, then $y_w$ is a Weil--Deligne realization of $r$ in the source's sense. For every compatible local period and completion bridge at $w$, the resulting local representation is potentially semistable; writing $x_w$ for its parameter, if either $x_w$ or $y_w$ has characteristic polynomial $(T-1)^{\dim}$ on every commutator of Weil elements, then $$\det(T-x_w(g))=\det(T-y_w(g))\qquad\text{for every Weil element }g.$$
