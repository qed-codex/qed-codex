---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/TypeIdempotentConstantTermVanishStatement.lean",
  "declarations": [
    "GlobalTheory.T.typeIdempotent_constantTerm_vanish"
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

## Vanishing constant terms after convolution with a finite type

[Theorem REP.0415](https://andrewodesky.com/rh/lean/GlobalTheory.T.typeIdempotent_constantTerm_vanish/)

Let $k$ be a nonarchimedean local field, $r=a+b$ with $a,b>0$, and $\tau$ an irreducible finite-dimensional complex representation of $\mathrm{GL}_r(\kappa_k)$. Assume $\tau$ has no nonzero vector fixed by the unipotent radical of the standard parabolic of block sizes $(a,b)$. Choose Haar measure $\mu$ on $G=\mathrm{GL}_r(k)$, and let $e_\tau$ be its inflated type idempotent. For any locally constant compactly supported $\phi:G\to\mathbb C$, put $f=e_\tau*\phi$ or $f=\phi*e_\tau$. Let $P$ be any parabolic subgroup of $G$, with unipotent radical $N$, contained in a conjugate of the standard $(a,b)$ parabolic. For every Haar measure $\nu$ on $N$ and all $x,y\in G$, the function $u\mapsto f(xuy)$ is integrable and $$\int_N f(xuy)\,d\nu(u)=0.$$
