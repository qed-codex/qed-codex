---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/ComplementarySeries/ComplementaryOf.lean",
  "declarations": [
    "PositivityTheory.RgGu.NR.complementary_of"
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

## Unitarisability along an exponential family

[Theorem REP.1368](https://andrewodesky.com/rh/lean/PositivityTheory.RgGu.NR.complementary_of/)

Assume the following finite-dimensional signature principle. For every finite-dimensional complex space $W$, a surjection $\iota:I\to I$, and operators $A_i(s)$ weakly continuous in $s\in\mathbb R$, suppose that for all $s\ge0$ the family $(A_i(s))$ is irreducible and admits a nonzero Hermitian form with $$B_s(A_i(s)v,w)=B_s(v,A_{\iota(i)}(s)w).$$ If such a form is positive definite at $s=0$, every nonzero Hermitian form satisfying this relation at any $s\ge0$ is either positive definite or negative definite.

Let $G$ be a topological group, $K\subseteq G$ an open compact subgroup, and $\pi_s$ complex representations on one vector space $V$, indexed by $s\in\mathbb R$. Assume $\pi_s|_K=\pi_0|_K$, and that for every $g\in G$, $v\in V$ there are finitely many $r_i\in\mathbb R$ and $v_i\in V$ such that $$\pi_s(g)v=\sum_i e^{r_i s}v_i\qquad(s\in\mathbb R).$$ For every $s\ge0$, assume $\pi_s$ is smooth, admissible, irreducible and admits a nonzero invariant sesquilinear form. If $\pi_0$ is unitarisable, so is every $\pi_s$ for $s\ge0$.
