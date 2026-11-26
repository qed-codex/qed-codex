---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DoublingZetaValueAtEisensteinHolomorphicPoint.lean",
  "declarations": [
    "GlobalTheory.Eis.zetaHolValueAt_of_eisValueAt"
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

## Doubling integrals at a holomorphic Eisenstein value

[Theorem THETA.1675](https://andrewodesky.com/rh/lean/GlobalTheory.Eis.zetaHolValueAt_of_eisValueAt/)

Fix the source's full arithmetic datum with CM extension $E/F$, a unitary space $V$ of rank $n$, a unitary Hecke character $\mu$ of its CM field, and a Haar measure on $U(V)(\mathbb A_F)$. Let $E(s,g)$ be the Siegel Eisenstein series attached to a section family $\Phi(s)$. Assume it is a convergent Eisenstein family for $\Re s>n/2$, has meromorphic continuation, and is holomorphic there for each $g$. Assume also the following uniform regularity condition at every $s_0$: for some $k\ge0$ and $r>0$, $(s-s_0)^kE(s,g)$ extends on $|s-s_0|<r$ to a function holomorphic in $s$, jointly continuous in $(s,g)$, and bounded uniformly by $C h(g)^N$ for some $C\in\mathbb R$, $N\ge0$.

Let $f_1,f_2$ be continuous, rationally invariant, rapidly decreasing functions on $U(V)(\mathbb A_F)$, where rapid decrease means $|f_i(g)|h_q(g)^M$ is bounded for every $M\ge0$. Assume the doubling integral converges and is rationally invariant for $\Re s>n/2$. If $E(s,g)$ has holomorphic value $E_0(g)$ at $s_0$, then $$Z(s)=\int_{[U(V)]^2}E(s,\iota(g_1,g_2))\overline{f_1(g_1)}f_2(g_2)\mu(\det g_2)^{-1}\,dg_1\,dg_2$$ has holomorphic value at $s_0$ equal to the same integral with $E_0$ in place of $E(s,\cdot)$; that integral is convergent and rationally invariant. Here $[U(V)]=U(V)(F)\backslash U(V)(\mathbb A_F)$ and $\iota$ is the doubling embedding.
