---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/Convolution/IntegrableConvolution/TypedEx.lean",
  "declarations": [
    "UpperTheory.ConvolutionTheory.L1.typedEx"
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

## Simultaneous local eigenvectors in a cuspidal summand

[Theorem AGR.0351](https://andrewodesky.com/rh/lean/UpperTheory.ConvolutionTheory.L1.typedEx/)

Let $K$ be a number field, $n\ge0$, $G^1=\{g\in\operatorname{GL}_n(\mathbb A_K):|\det g|_{\mathbb A_K}=1\}$, and $\mu$ a Haar measure on $G^1$. Let $V$ be a nonzero closed invariant subspace of the cuspidal part of $L^2(\operatorname{GL}_n(K)\backslash G^1)$, irreducible among closed invariant subspaces. For every finite place $w$, choose a compact open subgroup $J_w\le\operatorname{GL}_n(K_w)$ and a locally constant function $\chi_w:\operatorname{GL}_n(K_w)\to\mathbb C$ whose restriction to $J_w$ is a unitary character. Suppose $$J_w=\operatorname{GL}_n(\mathcal O_{K_w}),\qquad\chi_w=1$$ for all but finitely many $w$. If for each $w$ there is a nonzero $v_w\in V$ with $$\rho_w(j)v_w=\chi_w(j)v_w\qquad(j\in J_w),$$ then there is one nonzero $v\in V$ satisfying these equations for every $w$ simultaneously. Here $\rho_w(g)$ is right translation by the adele whose $w$-component is $g$ and whose other components are the identity.
