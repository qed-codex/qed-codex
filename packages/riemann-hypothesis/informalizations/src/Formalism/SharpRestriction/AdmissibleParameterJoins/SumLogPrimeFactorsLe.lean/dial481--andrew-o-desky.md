---
{
  "module": "src/Formalism/SharpRestriction/AdmissibleParameterJoins/SumLogPrimeFactorsLe.lean",
  "declarations": [
    "Formalism.MainNotions.J.mu_frac",
    "Formalism.MainNotions.J.sum_log_primes_le"
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

## Sum of logarithms of primes up to an integer

[Theorem ANT.1737](https://andrewodesky.com/rh/lean/Formalism.MainNotions.J.sum_log_primes_le/)

For every integer $N\ge0$, $$\sum_{\substack{p\le N\\p\text{ prime}}}\log p\le N\log4.$$

## Mean slope under multiplication by a fractional ideal

[Theorem ARAK.1734](https://andrewodesky.com/rh/lean/Formalism.MainNotions.J.mu_frac/)

Let $K$ be a totally complex number field with a ring involution, and let $V$ be a finite-dimensional $K$-space with a chosen basis and a positive definite Hermitian metric at each infinite place. Let $\mathfrak a$ be a nonzero fractional ideal of $K$, and let $M,N\subseteq V$ be $\mathcal O_K$-submodules such that $$N=\mathfrak aM:=\operatorname{span}_{\mathcal O_K}\{av:a\in\mathfrak a,\ v\in M\}.$$ Suppose $N$ is finitely generated and nonzero. Then $$\mu(N)=\mu(M)-\frac{2\log\operatorname{Norm}(\mathfrak a)}{[K:\mathbb Q]}.$$
