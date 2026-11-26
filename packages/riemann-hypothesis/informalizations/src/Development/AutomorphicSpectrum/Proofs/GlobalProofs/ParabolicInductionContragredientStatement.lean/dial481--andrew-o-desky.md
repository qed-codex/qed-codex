---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/GlobalProofs/ParabolicInductionContragredientStatement.lean",
  "declarations": [
    "GlobalTheory.T.parabolic_induction_contragredient"
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

## Contragredient of normalized parabolic induction

[Theorem REP.1717](https://andrewodesky.com/rh/lean/GlobalTheory.T.parabolic_induction_contragredient/)

Let $k$ be a nonarchimedean local field, $n=\sum_{a\in A}n_a$ an ordered finite block decomposition, and $\rho$ a smooth complex representation of $M=\prod_{a\in A}\operatorname{GL}_{n_a}(k)$ on $W$. Let $P$ be the corresponding standard parabolic of $G=\operatorname{GL}_n(k)$, $K=\operatorname{GL}_n(\mathcal O_k)$, and $\mu$ any Haar measure on $G$, with its Borel measurable structure. Write $\rho^\vee$ for the smooth contragredient and $i_P^G$ for normalized induction.

There is a $G$-equivariant linear isomorphism $$\Phi:i_P^G(\rho^\vee)\xrightarrow{\sim}(i_P^G\rho)^\vee$$ satisfying, for all induced vectors $f',f$, $$\Phi(f')(f)=\int_K f'(k)(f(k))\,d\mu(k).$$
