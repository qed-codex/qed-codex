---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SphericalParameterTransferAllFinitePlacesStatement.lean",
  "declarations": [
    "GlobalTheory.T.sphericalParameterTransfer_all_finitePlaces"
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

## Transfer of spherical parameters through a theta pairing

[Theorem THETA.0668](https://andrewodesky.com/rh/lean/GlobalTheory.T.sphericalParameterTransfer_all_finitePlaces/)

Assume the unramified Howe invariant-space theorem specified below. Fix the full arithmetic datum specified in ([The convergent doubling integral identity](https://andrewodesky.com/rh/lean/GlobalTheory.T.doubling_basicIdentity_unfolding/)), with CM extension $E/F$, Hermitian spaces $S,T$ with $\dim T=\dim S+t$, $t\ge0$, an additive character $\psi$, two adelic characters $\chi_S,\chi_T$, and a compatible Weil representation $\omega$ on theta functions on the associated adelic matrix space $W$. Let $v$ be any finite place of $F$, and assume $\chi_S,\chi_T$ are unramified at every place of $E$ above $v$. Choose $w\mid v$.

Let $U\subseteq\mathbb C^W$ be stable under the two local unitary groups through $\omega$, let $f\in U$ be the source's finite vacuum at $v$, and let $x$ be a spherical parameter vector of a complex representation $\rho$ of $U(S)(F_v)$ with parameter multiset $B$ at $w$. Let $\rho'$ be a complex representation of $U(T)(F_v)$ and let $b:U\times X\to X'$ be complex bilinear, satisfying $$b(\omega(g,h)u,\rho(g)y)=\rho'(h)b(u,y).$$ If $b(f,x)\ne0$, it is a spherical parameter vector for $\rho'$ with multiset $$\left\{\chi_S(\varpi_w)\chi_T(\varpi_w)^{-1}\beta:\beta\in B\right\} \ \sqcup\ \left\{\chi_S(\varpi_w)(Nw)^{(t-1)/2-i}:0\le i<t\right\}.$$
