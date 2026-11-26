---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/PeakTraceBoundHolds.lean",
  "declarations": [
    "PositivityTheory.Rg.BcB.F.peak_trace_bound_holds"
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

## A character detected by bounds on power traces

[Theorem REP.1364](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.BcB.F.peak_trace_bound_holds/)

Let $A$ be a commutative complex star algebra, $I$ a nonempty finite set, and $R_s:A\to\mathcal B(H_s)$ star algebra homomorphisms on complex Hilbert spaces. Fix operators $\beta_s\in\mathcal B(H_s)$ commuting with every $R_s(g)$ and an integer $m\ge0$. Let $V$ be a finite-dimensional complex vector space, $\rho:A\to\operatorname{End}_{\mathbb C}(V)$ an algebra homomorphism, and $u\in\operatorname{End}_{\mathbb C}(V)$ commuting with $\rho(A)$. Let $p:A\to\mathbb C$ be a star algebra character and $a_0\in A$ with $p(a_0)\ne0$.

Assume that for every $g\in Aa_0$ there are $C\in\mathbb R$ and $N,j\in\mathbb N$ such that, for all sufficiently large integers $k$, $$\left|\operatorname{tr}\bigl((u\rho(g))^k\bigr)\right|\le C(1+k)^N\max_{s\in I}\left\|(\beta_s^mR_s(g))^{k-j}\right\|.$$ Here $k-j$ denotes truncated subtraction on natural numbers. Suppose also that some $v\ne0$ satisfies $uv=v$ and $\rho(g)v=p(g)v$ for every $g\in A$.

Then for some $s\in I$ the star subalgebra $$B_s=\operatorname{alg}^{*}_{\mathbb C}\bigl(R_s(A), (\beta_s^m)^*\beta_s^m\bigr)\subseteq\mathcal B(H_s)$$ has a star algebra character $\chi:B_s\to\mathbb C$ such that $$|\chi(b)|\le\|b\|,\qquad \chi(R_s(g))=p(g),\qquad \chi((\beta_s^m)^*\beta_s^m)\ne0.$$
