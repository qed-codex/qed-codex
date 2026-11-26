---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ZetaIntegralEisensteinResidueStatement.lean",
  "declarations": [
    "GlobalTheory.T.zeta_integral_eisenstein_residue"
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

## Integrating the minus-one Laurent coefficient of an Eisenstein family

[Theorem ANT.1006](https://andrewodesky.com/rh/lean/GlobalTheory.T.zeta_integral_eisenstein_residue/)

Work in the source's full arithmetic unitary datum over a CM extension $E/F$. Let $V$ have rank $n$, put $G=U(V)(\mathbb A_F)$ and $\widetilde G=U(V\oplus(-V))(\mathbb A_F)$, and let $\iota:G\times G\to\widetilde G$ be the doubling embedding. Fix a circle-valued Hecke character $\mu$ of $\mathbb A_E^\times$ and a Haar measure $m$ on $G$, with quotient measure $\bar m$ on $[G]$.

Let $\Phi_s:\widetilde G\to\mathbb C$. For $\Re s>n/2$ assume $\Phi_s$ is left invariant under the rational Siegel subgroup and its Siegel Eisenstein sum $E(s,g)$ converges absolutely for every $g$ and is holomorphic in $s$. Assume each $E(\cdot,g)$ has meromorphic continuation. At every $s_0$, assume there are $k\ge0$, $r>0$, and a function $H(s,g)$, holomorphic in $s$ on $|s-s_0|<r$, jointly continuous there, satisfying $$H(s,g)=(s-s_0)^kE(s,g)\quad(s\ne s_0),\qquad |H(s,g)|\le C\operatorname{ht}(g)^N$$ for some fixed $C\in\mathbb R$, $N\ge0$ on that disc.

Let $f_1,f_2:G\to\mathbb C$ satisfy the source's rapid-decay conditions. Suppose for $\Re s>n/2$ the integrand in $$Z(s)=\int_{[G]^2}E(s,\iota(g_1,g_2))\overline{f_1(g_1)}f_2(g_2)\mu(\det g_2)^{-1}\,d\bar m(g_1)d\bar m(g_2)$$ descends to the quotient and is absolutely integrable. If $E_{-1}(g)$ is the coefficient of $(s-s_0)^{-1}$ in the continued Eisenstein family, then the continued $Z$ has coefficient $$[ (s-s_0)^{-1}]Z(s)=\int_{[G]^2}E_{-1}(\iota(g_1,g_2))\overline{f_1(g_1)}f_2(g_2)\mu(\det g_2)^{-1}\,d\bar m(g_1)d\bar m(g_2).$$
