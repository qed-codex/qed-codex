---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/LowerBlockParameterTransferInvariantPairingStatement.lean",
  "declarations": [
    "GlobalTheory.T.lowerBlockParameter_transfer_invariantPairing"
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

## Transfer of a parahoric Hecke eigenvalue multiset

[Theorem REP.0716](https://andrewodesky.com/rh/lean/GlobalTheory.T.lowerBlockParameter_transfer_invariantPairing/)

Let $k$ be a nonarchimedean local field with residue cardinality $q$, normalized absolute value $|\cdot|$, and uniformizer $\varpi$. Let $a,d,t\ge0$. Let $\xi,\mu_S,\mu_T:k^\times\to\mathbb C^\times$ be characters, with $\xi$ trivial on $1+\mathfrak p_k$ and $\mu_S/\xi,\mu_T/\xi$ unramified. Put $m=a+d$ and $m'=a+d+t$.

On functions on $M_{m',m}(k)$ define $$\omega(g,h)f(z)=\mu_T(\det g)^{-1}\mu_S(\det h)|\det g|^{m'/2}|\det h|^{-m/2}f(h^{-1}zg).$$ Let $W$ be a complex vector subspace invariant under all these operators and containing $\Phi$, where $\Phi(z)=\xi(\det z_{11})$ if $z$ is integral, $\det z_{11}\in\mathcal O_k^\times$, and $z_{21}$ has entries in $\mathfrak p_k$, and $\Phi(z)=0$ otherwise. Blocks are taken with sizes $(a,d+t)$ by $(a,d)$.

Let $\rho,\rho'$ be complex representations of $\operatorname{GL}_m(k),\operatorname{GL}_{m'}(k)$ on arbitrary complex vector spaces $X,X'$, and let $b:W\times X\to X'$ be bilinear with $$b(\omega(g,h)f,\rho(g)y)=\rho'(h)b(f,y).$$ If $x\in X$ has the parahoric Hecke data $(\xi,B)$ defined below, where $B$ is a multiset of $d$ nonzero complex numbers, then $b(\Phi,x)$ has the corresponding data for lower-block size $d+t$ and multiset $$\{\beta\mu_S(\varpi)/\mu_T(\varpi):\beta\in B\}\ \sqcup\ \{\mu_S(\varpi)|\varpi|^{j-(t-1)/2}:0\le j<t\}.$$
