---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/Convolution/NormCharacterPowers/BcSumD.lean",
  "declarations": [
    "UpperTheory.ConvolutionTheory.R.bcSum_holds"
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

## A logarithmic-series identity for a cyclic splitting pattern

[Theorem ANT.0509](https://andrewodesky.com/rh/lean/UpperTheory.ConvolutionTheory.R.bcSum_holds/)

Let $l\ge1$ be an integer, $u:W'\to W$, $q:W\to\mathbb N$ with $q_v\ge1$, $q':W'\to\mathbb N$, $f:W'\to\mathbb N$, and $c:W\to\mathbb C$. Suppose $q'_w=q_{u(w)}^{f_w}$, and for each $v\in W$ at least one of the following splitting conditions holds: the fibre $u^{-1}(v)$ has cardinality $l$, every $f_w=1$ on it, and $c_v=1$; or the fibre has cardinality one, $f_w=l$ there, and $c_v$ is a primitive $l$th root of unity.

Let $\alpha_{v,a},\beta_{v,b},\xi_{w,a'},\zeta_{w,b'}$ be complex numbers indexed by arbitrary finite sets $A,B,A',B'$. Assume, for every $w$ and integer $k\ge0$, $$\sum_{a'}\xi_{w,a'}^k=\sum_a\alpha_{u(w),a}^{f_wk},\qquad\sum_{b'}\zeta_{w,b'}^k=\sum_b\beta_{u(w),b}^{f_wk}.$$ For $\sigma\in\mathbb R$, define $$S(q;\alpha,\beta;\sigma)=\sum_{v\in W}\sum_{m\ge1}\frac{(\sum_a\alpha_{v,a}^m)\,\overline{(\sum_b\beta_{v,b}^m)}\,q_v^{-\sigma m}}m.$$ If the summands defining $S(q;\alpha,\beta;\sigma)$ are absolutely summable, then those defining $S(q';\xi,\zeta;\sigma)$ are absolutely summable and $$S(q';\xi,\zeta;\sigma)=\sum_{j=0}^{l-1}S(q;\alpha,c^j\beta;\sigma),$$ where $(c^j\beta)_{v,b}=c_v^j\beta_{v,b}$.
