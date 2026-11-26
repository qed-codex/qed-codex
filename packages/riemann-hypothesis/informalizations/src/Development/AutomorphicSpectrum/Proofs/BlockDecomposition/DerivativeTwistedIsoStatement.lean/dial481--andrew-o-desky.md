---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/DerivativeTwistedIsoStatement.lean",
  "declarations": [
    "GlobalTheory.T.derivative_twisted_iso"
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

## The determinant twist between two derivative conventions

[Theorem REP.1167](https://andrewodesky.com/rh/lean/GlobalTheory.T.derivative_twisted_iso/)

Let $k$ be a nonarchimedean local field, $\psi:k\to S^1$ an additive character, $n,j\ge0$, and $\pi$ any complex representation of $\operatorname{GL}_{n+j}(k)$. Let $D^j_\psi\pi$ be the unnormalized mirabolic derivative: for $j\ge1$, restrict to the mirabolic subgroup, apply the nontrivial twisted-coinvariant functor $\Phi^-_\psi$ $j-1$ times, and then the trivial-coinvariant functor $\Psi^-$. Define $\widetilde D^j_\psi$ in the same way, twisting the output of each $\Phi^-_\psi$ and $\Psi^-$ by $|\det|_k^{-1/2}$; for $j=0$, both derivatives are $\pi$. Then $$D^j_\psi\pi\simeq\widetilde D^j_\psi\pi\otimes|\det|_k^{j/2}$$ as representations of $\operatorname{GL}_n(k)$.
