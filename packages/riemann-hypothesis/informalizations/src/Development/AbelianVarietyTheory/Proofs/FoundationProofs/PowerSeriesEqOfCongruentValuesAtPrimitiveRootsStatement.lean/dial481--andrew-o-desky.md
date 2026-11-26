---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/PowerSeriesEqOfCongruentValuesAtPrimitiveRootsStatement.lean",
  "declarations": [
    "GlobalTheory.T.powerSeries_eq_of_congruent_values_at_primitiveRoots"
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

## Rigidity from congruent values at prime-power roots of unity

[Theorem PHT.0583](https://andrewodesky.com/rh/lean/GlobalTheory.KZ.autoPin_congr/)

Let $\ell$ be prime and let $O\subseteq\overline{\mathbb Q}_\ell$ be a discrete valuation $\mathbb Z_\ell$-subalgebra finite as a $\mathbb Z_\ell$-module. Let $A,B\in O[[T]]$ with $B\ne0$, let $u\in\overline{\mathbb Q}_\ell$ satisfy $|u|_\ell=1$, and let $w_m\in\overline{\mathbb Q}_\ell$ satisfy $$|w_m|_\ell=1,\qquad|w_{m+1}-w_m|_\ell\le|\ell|_\ell^m\quad(m\ge0).$$ For $F=\sum_na_nT^n$, put $$F_N(z)=\sum_{0\le n<N}a_n(z-1)^n.$$ Suppose $c_0,m_0\ge0$ are integers and, for every $m\ge m_0$ and every primitive $\ell^m$th root $z$, $$\left|A_{\ell^{3m}}(z)-w_mu^mB_{\ell^{3m}}(z)\right|_\ell\le |\ell|_\ell^{\max\{\lfloor m/2\rfloor-c_0,0\}}.$$ Then $u=1$. Moreover, for every integer $k\ge0$, some $m_1$ satisfies $$|a_n-w_mb_n|_\ell\le|\ell|_\ell^k\qquad(m\ge m_1,\ n\ge0),$$ where $a_n,b_n$ are the coefficients of $A,B$.
