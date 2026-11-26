---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/MirabolicPsiMinusExactStatement.lean",
  "declarations": [
    "GlobalTheory.T.mirabolic_psi_minus_exact"
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

## Exactness of ordinary mirabolic coinvariants

[Theorem REP.0522](https://andrewodesky.com/rh/lean/GlobalTheory.T.mirabolic_psi_minus_exact/)

Let $k$ be a nonarchimedean local field and $n\ge0$. Let $$P=\left\{\begin{pmatrix}a&b\\0&1\end{pmatrix}:a\in\operatorname{GL}_n(k),\ b\in k^n\right\},\qquad U=\left\{\begin{pmatrix}1&b\\0&1\end{pmatrix}:b\in k^n\right\}.$$ Let $V_1\xrightarrow{f}V_2\xrightarrow{g}V_3$ be equivariant linear maps of smooth complex $P$-representations, exact at $V_2$. The induced sequence of ordinary $U$-coinvariants is exact at $(V_2)_U$: $$\operatorname{im}(f_U)=\ker(g_U).$$
