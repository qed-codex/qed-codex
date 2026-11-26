---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/ExistsSaturatedGoodVectorsSmallCorankStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_saturated_good_vectors_small_corank"
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

## Many integral vectors with a vanishing first coefficient

[Theorem PHT.0775](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_saturated_good_vectors_small_corank/)

Let $C$ be algebraically closed with an additive valuation $v:C\to\mathbb R\cup\{+\infty\}$, let $\ell$ be prime with $v(\ell)=1$, and put $O=\{c:v(c)\ge0\}$. Let $d\ge0$, let $I,J$ be finite sets, and choose a type function $t:I\sqcup J\to\mathbb Z/d\mathbb Z$ and an additive subgroup $$\mathcal T\subseteq\{x=(x_r)_{r\ge0}:x_r\in C^{I\sqcup J}\}$$ satisfying the conditions below. Fix $a\in\mathbb Z/d\mathbb Z$ and put $I_a=\{i\in I:t(i)=a\}$.

There exist $N\ge0$, vectors $w_1,\ldots,w_N\in O^I$ supported on $I_a$, and sequences $x^{(\nu)}\in\mathcal T$ such that $$x^{(\nu)}_0=(w_\nu,0),\qquad x^{(\nu)}_r(b)=0\ \text{if }t(b)\ne a+r,\qquad x^{(\nu)}_1|_I=0.$$ The matrix $W=(w_\nu(i))_{\nu,i}$ has a right inverse over $O$, and $$|I_a|\le N+|I_{a+1}|.$$
