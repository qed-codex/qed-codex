---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/WhittakerHeredityStatement.lean",
  "declarations": [
    "GlobalTheory.T.whittaker_heredity"
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

## Whittaker coinvariants of parabolic induction

[Theorem REP.1667](https://andrewodesky.com/rh/lean/GlobalTheory.T.whittaker_heredity/)

Let $k$ be a nonarchimedean local field and $\psi:k\to S^1$ a continuous nontrivial additive character. Let $d_1,\ldots,d_h\ge0$ with $\sum_a d_a=N$, and let $\pi_a$ be smooth complex representations of $\mathrm{GL}_{d_a}(k)$. Write $\pi_1\times\cdots\times\pi_h$ for normalized induction from the standard parabolic with these block sizes. Let $U_r$ be the upper unitriangular subgroup of $\mathrm{GL}_r(k)$ and $\psi_r(u)=\psi(\sum_{i=1}^{r-1}u_{i,i+1})$. For a representation $V$, set $$V_{U_r,\psi_r}=V/\langle uv-\psi_r(u)v:u\in U_r,\ v\in V\rangle_{\mathbb C}.$$ There is a complex-linear isomorphism $$(\pi_1\times\cdots\times\pi_h)_{U_N,\psi_N} \simeq\bigotimes_{a=1}^h(\pi_a)_{U_{d_a},\psi_{d_a}}.$$
