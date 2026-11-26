---
{
  "module": "src/Development/AutomorphicArithmetic/CommutativeAlgebra/LeafH0Holds.lean",
  "declarations": [
    "UpperTheory.leafH0_holds"
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

## Zeroth Tate-twisted cohomology over an algebraically closed field

[Theorem AG.0683](https://andrewodesky.com/rh/lean/UpperTheory.leafH0_holds/)

Assume the étale foundation package below. Let $q>0$, let $\Omega$ be an algebraically closed field in which $q$ is invertible, and let $i\in\mathbb Z$. Then $H^0_{\mathrm{et}}(\operatorname{Spec}\Omega,\mathbb Z/q(i))$ is finite. For every connected scheme $X$ and every morphism $c:X\to\operatorname{Spec}\Omega$, pullback is a bijection $$c^*:H^0_{\mathrm{et}}(\operatorname{Spec}\Omega,\mathbb Z/q(i)) \longrightarrow H^0_{\mathrm{et}}(X,\mathbb Z/q(i)).$$
