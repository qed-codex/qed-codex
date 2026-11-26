---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/DHol.lean",
  "declarations": [
    "PositivityTheory.Rg.Sw.Glob.dHol"
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

## Holomorphic parameter dependence of theta averages

[Theorem THETA.1259](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.Sw.Glob.dHol/)

Assume the absolute theta-convergence statement specified below. Fix the full arithmetic datum specified in ([The convergent doubling integral identity](https://andrewodesky.com/rh/lean/GlobalTheory.T.doubling_basicIdentity_unfolding/)), a Hermitian space $V$ of rank $m$, an integer $n\ge1$ with $n+\operatorname{WittIndex}(V)<m$, a compatible family $\theta$ of archimedean models, and a Haar measure $\nu$ on $U(V)(\mathbb A_F)$. Write $\mathcal M$ for its adelic matrix space of shape $m\times n$ and $\mathscr S_\theta(\mathcal M)$ for the Schwartz space consisting of finite linear combinations of products of archimedean Schwartz functions in the coordinates $\theta$ and finite-adelic locally constant compactly supported functions.

Let $P$ be a first-countable topological space, $U\subseteq\mathbb C$ open, and $\varphi:P\times\mathbb C\times\mathcal M\to\mathbb C$. Assume $\varphi(p,z,\cdot)\in\mathscr S_\theta(\mathcal M)$ for $z\in U$; $\varphi(p,\cdot,x)$ is holomorphic on $U$ for every $p,x$; $(p,z)\mapsto\varphi(p,z,x)$ is continuous on $P\times U$ for each $x$; and $(z,x)\mapsto\varphi(p,z,x)$ is continuous on $U\times\mathcal M$ for each $p$. For every $(p_0,z_0)\in P\times U$, assume a neighborhood $N$ and $M\in\mathscr S_\theta(\mathcal M)$ satisfy $|\varphi(p,z,x)|\le|M(x)|$ for $(p,z)\in N$ with $z\in U$ and all $x$.

Let $[U(V)]=U(V)(F)\backslash U(V)(\mathbb A_F)$ carry the induced automorphic measure, and define $$F(p,z)=⨍_{[U(V)]}\sum_\xi\varphi(p,z,h^{-1}\xi)\,dh,$$ where $\xi$ runs through $\operatorname{Mat}_{m\times n}(E)$. Then $F$ is continuous on $P\times U$, each $F(p,\cdot)$ is holomorphic, and for every $j\ge0$, $p\in P$, $z\in U$, $$\partial_z^jF(p,z)=⨍_{[U(V)]}\sum_\xi\partial_z^j\varphi(p,z,h^{-1}\xi)\,dh.$$
