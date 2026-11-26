---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/ClosedAtL.lean",
  "declarations": [
    "GlobalTheory.LimitTop.closedAtL"
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

## Hodge jumps under uniform trace approximation

[Theorem PHT.0117](https://andrewodesky.com/rh/lean/GlobalTheory.LimitTop.closedAtL/)

Let $E$ be a number field, $\ell$ prime, $a\ge1$, and $r:G_E\to\mathrm{GL}_a(\overline{\mathbb Q}_\ell)$ continuous and semisimple. Fix a place $v$ of $E$ and a place of $\overline E$ above it. Assume the following compatible local data:

1. A finite extension $K/\mathbb Q_\ell$, an embedding $j:\overline E\hookrightarrow\overline{\mathbb Q}_\ell$ with $j(E)\subset K$ dense, and a topological group isomorphism from the chosen decomposition group to $G_K$ such that $j(gx)=g(jx)$ under this isomorphism, and $x$ belongs to the chosen valuation ring of $\overline E$ if and only if $|j(x)|_\ell\le1$.
2. A finite coefficient field $L/\mathbb Q_\ell$ containing the images of all embeddings of $K$, and a topological $\mathbb Z_\ell$-algebra identified with $\mathcal O_L$ by a continuous ring isomorphism with continuous inverse.
3. Crystalline and de Rham period rings, with their coefficient maps, Galois actions, Frobenius, inclusion, filtrations, cyclotomic period and character, identified with Fontaine's $B_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$. The identifications preserve the $\mathbb Z_\ell$ maps, Galois actions, Frobenius, inclusion and every filtration step; algebraic scalars lift to $B_{\mathrm{dR}}^+$ with their usual residue. The cyclotomic period is the logarithm of the compatible system of roots of unity.
4. Integral period data from $A_{\mathrm{inf}}=W(\mathcal O_{\mathbb C_\ell}^{\flat})$, compatible with the norm-preserving Galois action and Frobenius, the chosen roots of unity, the inclusion in $B_{\mathrm{cris}}$ and the de Rham filtration. The map to $B_{\mathrm{cris}}$ is injective and agrees with the usual Teichmüller lifts of prime-to-$\ell$ roots of unity; its image lies in filtration zero, and membership in filtration one is divisibility by $\sum_{i=0}^{\ell-1}[\epsilon^{1/\ell}]^i$.
5. The global-to-local maps induce these period structures on the decomposition group. All semistability, crystalline, de Rham and jump conditions below are interpreted using these data.

Fix integer multisets $J_\tau$ for embeddings $\tau:E\to\overline{\mathbb Q}_\ell$ and a set $\mathcal C$ of continuous representations of rank $a$. Suppose that for every $\eta>0$ there are a finite $F\subset\mathcal C$ and scalars $c_\rho\in\overline{\mathbb Q}_\ell$ such that $$\left|\operatorname{tr}r(g)-\sum_{\rho\in F}c_\rho\operatorname{tr}\rho(g)\right|_\ell\le\eta\qquad(g\in G_E).$$ Assume every $\rho\in\mathcal C$ is semistable on the chosen decomposition group and has jumps $J_\tau$ whenever $\tau$ extends to an embedding $K\to L'$ for a finite coefficient extension $L'/\mathbb Q_\ell$, with the extension agreeing with $j$ on $E$. Then $r$ is de Rham there and has those same jumps for every such embedding. If every $\rho\in\mathcal C$ is crystalline there, then $r$ is crystalline there.
