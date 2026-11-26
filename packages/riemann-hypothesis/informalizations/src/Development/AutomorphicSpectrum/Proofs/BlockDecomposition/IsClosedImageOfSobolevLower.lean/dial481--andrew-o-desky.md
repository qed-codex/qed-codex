---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/IsClosedImageOfSobolevLower.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.SmoothClosed.isClosed_image_of_sobolev_lower"
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

## Closed image from lower bounds for Sobolev seminorms

[Theorem REP.1361](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.SmoothClosed.isClosed_image_of_sobolev_lower/)

Fix $n\ge0$, signs $\epsilon\in\{+1,-1\}^n$, $G=U(\operatorname{diag}\epsilon)$ and its real Lie algebra $\mathfrak g$. Let $H$ be a complex Hilbert space carrying an irreducible unitary representation $\sigma$ of $G$. Let $E$ be a complete Hausdorff complex vector space with a complete additive uniform structure, equipped with seminorms $(p_j)_{j\ge0}$ and the smooth module structure specified below $(\pi,d\pi)$ for $G$. Let $T:H\to E$ be complex linear and satisfy the smooth equivariant-map condition specified below.

For a finite list $S$ of finite lists of elements of $\mathfrak g$, let $\|w\|_{\sigma,S}$ be the Sobolev norm, equal to the sum of the norms of the iterated derivatives of $\sigma$ listed in $S$. Assume that for every such $S$ there is a continuous seminorm $q$ on $E$ with $$\|w\|_{\sigma,S}\le q(Tw)\qquad(w\in H^\infty),$$ where $H^\infty$ denotes the smooth-vector space. Then $T(H^\infty)$ is closed in $E$.
