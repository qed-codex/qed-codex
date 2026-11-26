---
{
  "module": "src/Development/EtaleCohomology/WeilConjectures/ChevPf.lean",
  "declarations": [
    "LateralTheory.EWeil.ChevPf.Chev_of"
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

## Descending submodules eventually lie in every p-adic neighborhood

[Theorem PHT.0551](https://andrewodesky.com/rh/lean/LateralTheory.EWeil.ChevPf.Chev_of/)

Let $\ell$ be prime, let $M$ be a finitely generated $\mathbb Z_\ell$-module, and let $$K_0\supseteq K_1\supseteq K_2\supseteq\cdots$$ be submodules with $\bigcap_{j\ge0}K_j=0$. For every integer $N\ge0$, some $j\ge0$ satisfies $$K_j\subseteq\ell^N M.$$
