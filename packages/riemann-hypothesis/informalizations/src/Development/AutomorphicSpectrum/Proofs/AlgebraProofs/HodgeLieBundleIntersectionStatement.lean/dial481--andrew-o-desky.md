---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/AlgebraProofs/HodgeLieBundleIntersectionStatement.lean",
  "declarations": [
    "GlobalTheory.T.hodge_lie_bundle_intersection"
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

## A relative power-sum intersection identity for scaled lattice bundles

[Theorem ARAK.0948](https://andrewodesky.com/rh/lean/GlobalTheory.T.hodge_lie_bundle_intersection/)

Let $O$ be a discrete valuation domain, $\Omega$ an $O$-algebra that is a field, and $X$ a flat integral multiprojective model of relative dimension $d$, specified by a tuple of homogeneous coordinates $x$ in $\Omega$ and satisfying the model conditions below. Let $\mathcal L,W,\Lambda$ be rank-$r$ chart lattice bundles in one $\Omega$-vector space, $M,M'$ rank-$s$ chart lattice bundles in another, and $H,T$ rank-$n$ chart lattice bundles in a third. Suppose $0\ne w\in O$ and, on every nonzero coordinate chart, $$\mathcal L\subseteq W\subseteq\Lambda,\qquad\mathcal L=w\Lambda.$$ Assume $M,M'$ have the same generic lattice span, as do $H,T$, and that compatible lattice relations represent an exact sequence of quotients $$0\longrightarrow\Lambda/W\longrightarrow H/T\longrightarrow M/M'\longrightarrow0.$$

Let $1\le k\le d+1$, let $L_1,\ldots,L_q$ be arbitrary integral multidegrees for the projective factors, and let $Q\in\mathbb Z[Y_1,\ldots,Y_q]$ be homogeneous of degree $d+1-k$. Using the flag-intersection conventions below, $$C_k(\mathcal L,W;L,Q)+C_k(M,M';L,Q) =C_k(H,T;L,Q)-k\,I_w(\mathcal L;p_{k-1},L,Q).$$
