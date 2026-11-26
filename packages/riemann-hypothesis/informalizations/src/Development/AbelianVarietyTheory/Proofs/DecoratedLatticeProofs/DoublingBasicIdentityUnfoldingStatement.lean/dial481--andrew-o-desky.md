---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DoublingBasicIdentityUnfoldingStatement.lean",
  "declarations": [
    "GlobalTheory.T.doubling_basicIdentity_unfolding"
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

## The convergent doubling integral identity

[Theorem THETA.1651](https://andrewodesky.com/rh/lean/GlobalTheory.T.doubling_basicIdentity_unfolding/)

Assume the source's full arithmetic unitary datum, with CM extension $E/F$. Let $V$ be a Hermitian space of rank $n$ in this datum, let $G=U(V)(\mathbb A_F)$, and let $\widetilde G=U(V\oplus(-V))(\mathbb A_F)$ with doubling embedding $\iota:G\times G\to\widetilde G$. Choose an adelic frame $a$ that takes the Hermitian matrix to a diagonal matrix with entries $\pm1$ at each infinite place. Use its specified compact subgroup and determinant height $H_a$ on $\widetilde G$. Let $\mu:\mathbb A_E^\times\to S^1$ be a Hecke character, let $\operatorname{Re}s>n/2$, and let $\varphi$ be a continuous compact-finite section of the normalized degenerate principal series: for the Siegel parabolic $P$, with Levi determinant $b(p)$, $$\varphi(pg)=\mu(b(p))|b(p)|_{\mathbb A_E}^{\,s+n/2}\varphi(g).$$ Write $$\mathcal E_\varphi(g)=\sum_{\gamma\in P(F)\backslash U(V\oplus(-V))(F)}\varphi(\gamma g).$$ Assume that the spherical Eisenstein sum obtained from $H_a^{\,\operatorname{Re}s+n/2}$ has polynomial growth in the specified height on $\widetilde G$. Let $m$ be any Haar measure on $G$ and $\bar m$ its quotient measure on $[G]=U(V)(F)\backslash G$. Let $f_1,f_2:G\to\mathbb C$ be continuous, left $U(V)(F)$-invariant functions with rapid decay in every power of the specified quotient height, and assume $f_1$ is cuspidal. Put $$c(g)=\int_{[G]}f_1(xg)\overline{f_2(x)}\,d\bar m(x).$$ Then the double-integral integrand below descends to $[G]^2$, both displayed integrals converge absolutely, and $$\int_{[G]^2}\mathcal E_\varphi(\iota(g_1,g_2)) \overline{f_1(g_1)}f_2(g_2)\mu(\det g_2)^{-1}\, d\bar m(g_1)d\bar m(g_2) =\int_G\varphi(\iota(g,1))\overline{c(g)}\,dm(g).$$
