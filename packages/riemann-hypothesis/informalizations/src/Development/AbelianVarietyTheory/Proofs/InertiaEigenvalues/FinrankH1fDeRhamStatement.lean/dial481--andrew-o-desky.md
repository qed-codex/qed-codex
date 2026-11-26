---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/FinrankH1fDeRhamStatement.lean",
  "declarations": [
    "GlobalTheory.T.finrank_H1f_de_rham"
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

## Dimension of finite local cohomology for a de Rham representation

[Theorem PHT.1385](https://andrewodesky.com/rh/lean/GlobalTheory.T.finrank_H1f_de_rham/)

Let $\ell$ be prime, $K/\mathbb Q_\ell$ a finite extension, and $L/\mathbb Q_\ell$ a finite coefficient extension with its vector-space topology. Let $\mathcal O\subset L$ be a discrete valuation ring with fraction field $L$ and open image in $L$. Use local crystalline, de Rham, and integral period data identified with Fontaine's rings as in ([An invariant crystalline period matrix for an unramified representation](https://andrewodesky.com/rh/lean/GlobalTheory.UnrPer.exists_period_unramified/)). Let $V$ be a finite-dimensional continuous $L$-linear representation of $G_K$, with compatible $\mathcal O$- and $\mathbb Q_\ell$-module structures, and assume $V$ is de Rham.

Let $H_f^1(K,V)$ be continuous cocycles becoming coboundaries in $V\otimes_{\mathbb Q_\ell}B_{\mathrm{cris}}$, modulo coboundaries, as in ([Finite local cocycles modulo a power are reductions of integral cocycles](https://andrewodesky.com/rh/lean/GlobalTheory.BKTorsionRed.mem_HfQ_iff_red/)). This space is finite-dimensional over $L$, and $$\dim_L H_f^1(K,V)=\dim_L V^{G_K}+\dim_L D_{\mathrm{dR}}(V)-\dim_L\bigl(D_{\mathrm{dR}}(V)\cap\mathrm{Fil}^0(V\otimes_{\mathbb Q_\ell}B_{\mathrm{dR}})\bigr).$$
