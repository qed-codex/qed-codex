---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/SquareIdentityOfMatching.lean",
  "declarations": [
    "GlobalTheory.T.twisted_square_identity"
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

## Comparison of the two theta routes around a square

[Theorem THETA.1704](https://andrewodesky.com/rh/lean/GlobalTheory.T.twisted_square_identity/)

Assume the source's seven input packages: real Howe duality; local theta inputs; equality and local matching of the two Weil-model integrals; and, for the second square model, convergence, local matching, and agreement of theta integrals. There is $C_0\in\mathbb R$ such that for every $\varepsilon,C_F\in\mathbb R$ with $C_F\ge C_0$, there is $x_0$ for which the following holds for every full arithmetic datum of scale $x\ge x_0$ and exponent $\varepsilon$. Choose a finite group, its permitted family indexed by a set $T$, a coefficient number field, a compatible real representation datum and face satisfying the full Hida-setting conditions, and any associated grid with constants $(1,C_F,b)$, compatible Weil actions, frames, and real matching datum.

For each square $(i,j)$ of its $m\times m$ grid, let $P_{\mathrm{big}},P_{\mathrm{small}}$ be the polynomial tensor spaces for the paths through $(i+1,j+1)$ and $(i,j)$, from $(i,j+1)$ to $(i+1,j)$. There is a proper complex subspace $$R\subset P_{\mathrm{big}}\times P_{\mathrm{small}}$$ whose two coordinate projections are surjective. For every real matching datum with the same boundary vectors and relation $R$ at this square, and every $t\in T$, there is $c_t\in\mathbb C$ such that the following holds for every compatible system of Haar measures and fundamental domains, every pair of matched theta tensors $\Theta,\Theta'$, and every boundary pair $g,g_1$. There is a finitely supported function $z$ on the smaller intermediate group, with $\deg z=\sum_hz(h)\ne0$, such that both displayed integrands are integrable and $$\deg z\int_{\mathcal F_{\mathrm{big}}}K_{\mathrm{big}}(\Theta;g,g_1,u)\,du =c_t\int_{\mathcal F_{\mathrm{small}}}\sum_hz(h)K_{\mathrm{small}}(\Theta';g,g_1,uh)\,du.$$ Each $K$ is the contraction of the two theta kernels along its path, and matching of $\Theta,\Theta'$ includes the prescribed polynomial relation, local depth bounds, natural local vectors, and finite Fourier changes.
