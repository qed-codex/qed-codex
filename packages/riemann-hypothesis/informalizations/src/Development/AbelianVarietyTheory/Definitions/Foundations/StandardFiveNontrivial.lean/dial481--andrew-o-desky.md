---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Foundations/StandardFiveNontrivial.lean",
  "declarations": [
    "GlobalTheory.BadShare.Basic.countAt_of_trace_eq_zero"
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

## Ranks of convolution projections from vanishing traces

[Theorem REP.0861](https://andrewodesky.com/rh/lean/GlobalTheory.BadShare.Basic.countAt_of_trace_eq_zero/)

Let $p_1,p_2$ be primes, $N\ge0$, and $I_1,I_2$ finite sets. Put $$G=\operatorname{GL}_N(\mathbb F_{p_1})^{I_1}\times\operatorname{GL}_N(\mathbb F_{p_2})^{I_2}.$$ Let $\rho:G\to\operatorname{GL}(V)$ be a representation on a nonzero finite-dimensional complex vector space. Say that a tuple is unipotent if every matrix in it is unipotent. Assume $$\operatorname{tr}\rho(\gamma)=0$$ whenever $\gamma\ne1$ and at least one of its two tuples is unipotent.

There is $c>0$ such that, for every function $e:G\to\mathbb C$ with $e*e=e$ and $e(\gamma^{-1})=\overline{e(\gamma)}$, if its support consists entirely of elements with unipotent first tuple, or entirely of elements with unipotent second tuple, then $$\dim_{\mathbb C}\operatorname{im}\left(\sum_{\gamma\in G}e(\gamma)\rho(\gamma)\right)=c\,\operatorname{Re}e(1).$$
