---
{
  "module": "src/Formalism/ThetaLogCoordinates/TraceIsometryWeights/SchurTraceProofs/InvInt.lean",
  "declarations": [
    "Formalism.InvariantFactorPaths.PW.invariant_integral_holds"
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

## An integral multiple of an invariant operator

[Theorem REP.1052](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.PW.invariant_integral_holds/)

Let $p$ be prime, $W$ a $\mathbb Q_p$-vector space, and $I$ an index set. Let $E_{ab}\in\operatorname{End}_{\mathbb Q_p}(W)$ satisfy $$[E_{ab},E_{cd}]=\delta_{bc}E_{ad}-\delta_{da}E_{cb}.$$ Let $M\subseteq W$ be an additive subgroup stable under $\mathbb Z_p$ and under $E_{ab}^k/k!$ for all $a\ne b$ and $k\ge0$. For an integer $\ell\ge0$ and a list $L$ of distinct indices in $I$, define $A_\ell(L)$ as below. Put $L_p(0)=0$ and $L_p(n)=\lfloor\log_p n\rfloor$ for integers $n\ge1$. Then $$p^{\binom{|L|}{2}L_p(\max\{\ell+|L|-1,0\})}\,A_\ell(L)u\in M\qquad(u\in M).$$
