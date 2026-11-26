---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/AdmissibleParabolicInductionStatement.lean",
  "declarations": [
    "GlobalTheory.T.admissible_parabolic_induction"
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

## Admissibility of a parabolic product

[Theorem REP.1414](https://andrewodesky.com/rh/lean/GlobalTheory.T.admissible_parabolic_induction/)

Let $k$ be a nonarchimedean local field with its valuation and topology. Let $c,n\ge0$, let $N_1,\ldots,N_c\ge0$ satisfy $\sum_iN_i=n$, and let $\sigma_i$ be smooth irreducible complex representations of $\operatorname{GL}_{N_i}(k)$. The normalized parabolic induction $$\operatorname{Ind}_{P}^{\operatorname{GL}_n(k)}(\sigma_1\boxtimes\cdots\boxtimes\sigma_c)$$ from the standard block parabolic $P$ is admissible: its fixed vectors under every compact open subgroup form a finite-dimensional complex vector space.
