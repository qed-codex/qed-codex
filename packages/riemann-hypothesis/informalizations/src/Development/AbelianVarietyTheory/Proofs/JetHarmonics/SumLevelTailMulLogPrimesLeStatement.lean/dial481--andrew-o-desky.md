---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/SumLevelTailMulLogPrimesLeStatement.lean",
  "declarations": [
    "GlobalTheory.T.sum_level_tail_mul_log_primes_le"
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

## A weighted prime sum for odd level tails

[Theorem ANT.0459](https://andrewodesky.com/rh/lean/GlobalTheory.T.sum_level_tail_mul_log_primes_le/)

For integers $k\ge1$ and $\ell\ge2$, define $$t(k,\ell)=\sup\{\ell^{-i}:i\ge3\text{ odd},\ k^{3/2}<\ell^i\}.$$ Then $$t(k,\ell)\le\ell^{-3},\qquad t(k,\ell)<k^{-3/2},\qquad k<\ell^2\Longrightarrow t(k,\ell)=\ell^{-3}.$$ For every finite set $Q$ of rational primes, $$\sum_{p\in Q}t(k,p)\log p\le\frac{20}{k}.$$
