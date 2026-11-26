---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SobolevSpaceCompleteStatement.lean",
  "declarations": [
    "GlobalTheory.T.sobolev_space_complete"
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

## Completeness of the space with all right derivatives in L2

[Theorem REP.0317](https://andrewodesky.com/rh/lean/GlobalTheory.T.sobolev_space_complete/)

Assume ([A local Sobolev inequality on the complex general linear group](https://andrewodesky.com/rh/lean/GlobalTheory.T.sobolev_inequality_on_group/)), restated in the conventions. Fix $n\ge0$, a Haar measure $\mu$ on $G=\operatorname{GL}_n(\mathbb C)$, and a complex Hilbert space $V$. Let $a_k:M_n(\mathbb C)\to V$ be smooth on $G$, with $D_wa_k\in L^2(G,\mu;V)$ for every finite word $w$ in the real matrix basis $\{E_{ij},iE_{ij}\}$. Suppose $(D_wa_k)_k$ is Cauchy in $L^2$ for every $w$. There is $b:M_n(\mathbb C)\to V$, smooth on $G$, with every $D_wb\in L^2$, such that $$D_wa_k\longrightarrow D_wb\text{ in }L^2\quad\text{for every }w,\qquad a_k(g)\longrightarrow b(g)\quad(g\in G).$$
