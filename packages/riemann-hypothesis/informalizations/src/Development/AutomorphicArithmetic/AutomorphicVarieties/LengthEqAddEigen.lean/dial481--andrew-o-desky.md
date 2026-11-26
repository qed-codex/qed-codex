---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/LengthEqAddEigen.lean",
  "declarations": [
    "UpperTheory.V.shaLen_eq_add",
    "UpperTheory.V.vvle_of_parts"
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

## Recombining localization eigenspaces

[Theorem ALG.0165](https://andrewodesky.com/rh/lean/UpperTheory.V.vvle_of_parts/)

Let $E$ be a CM number field, $t\in\mathbb N$, and $B_2,B_-,B_+\in\mathbb R$. For a prime $\ell$ and $r\ge1$, let $\mathcal S_{\ell,r}(E)$ be the localization kernel defined in ([Bound for localization kernels](https://andrewodesky.com/rh/lean/UpperTheory.One.vwin_of_row/)). For odd $\ell$, let $\mathcal S_{\ell,r}(E)^+$ and $\mathcal S_{\ell,r}(E)^-$ be the eigenspaces of the natural complex-conjugation action with eigenvalues $(-1)^r$ and $(-1)^{r+1}$ respectively. Assume, uniformly for every algebraic closure and compatible local coefficient data, that all the lengths below are finite and $$\sum_{1\le r<t}\operatorname{length}_{\mathbb Z_2}\mathcal S_{2,r}(E)\le B_2,$$ and, for every finite set $\mathcal P$ of odd primes, $$\sum_{\ell\in\mathcal P}\log\ell\sum_{1\le r<t}\operatorname{length}_{\mathbb Z_\ell}\mathcal S_{\ell,r}(E)^\pm\le B_\pm.$$ Then all the lengths $\operatorname{length}_{\mathbb Z_\ell}\mathcal S_{\ell,r}(E)$ with $1\le r<t$ are finite, and every finite set $\mathcal P$ of primes satisfies $$\sum_{\ell\in\mathcal P}\log\ell\sum_{1\le r<t}\operatorname{length}_{\mathbb Z_\ell}\mathcal S_{\ell,r}(E)\le B_2\log2+B_-+B_+.$$
