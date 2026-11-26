---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/GlobalProofs/GagaSections.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Gaga.gagaSections"
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

## Algebraization of holomorphic line bundle sections

[Theorem AG.1645](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Gaga.gagaSections/)

Let $X$ be a smooth proper scheme over $\mathbb C$, and let $L$ be an algebraic line bundle with trivializing open cover $(U_i)$ and transition functions $g_{ij}$. Suppose functions $h_i:X(\mathbb C)\to\mathbb C$ are holomorphic on $U_i(\mathbb C)$ and satisfy $$h_i(x)=g_{ij}(x)\,h_j(x) \qquad(x\in(U_i\cap U_j)(\mathbb C)).$$ Here holomorphy means that $h_i\circ y$ is holomorphic for every holomorphic map $y:B\to U_i(\mathbb C)$ from an open set $B\subseteq\mathbb C^m$, for every $m\ge0$. There exists an algebraic global section $s\in H^0(X,L)$ whose expression in each trivialization is $h_i$ on $U_i(\mathbb C)$.
