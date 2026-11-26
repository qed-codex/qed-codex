---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/MultiplicativeLargeSieveStatement.lean",
  "declarations": [
    "GlobalTheory.T.sum_norm_sq_primitive_char_sum_le"
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

## A large sieve inequality for primitive Dirichlet characters

[Theorem ANT.0392](https://andrewodesky.com/rh/lean/GlobalTheory.T.sum_norm_sq_primitive_char_sum_le/)

Let $Q\ge1$ and $M,N\ge0$ be integers and $a:\mathbb N\to\mathbb C$. Then $$\sum_{q=1}^{Q}\ \sum_{\substack{\chi\bmod q\\\chi\ \mathrm{primitive}}} \left|\sum_{M<n\le M+N}a(n)\chi(n)\right|^2 \le\bigl(Q^2+2\pi N\bigr)\sum_{M<n\le M+N}|a(n)|^2.$$
