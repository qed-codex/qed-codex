---
{
  "module": "src/Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/SharpPoly.lean",
  "declarations": [
    "Formalism.L2.KerInert.SharpPolyP.sp_main"
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

## Removing determinant denominators from a Borel-covariant function

[Theorem ALG.0742](https://andrewodesky.com/rh/lean/Formalism.L2.KerInert.SharpPolyP.sp_main/)

Let $I$ be a finite set, $a\ge0$, and $\nu_{\tau,j}\in\mathbb N$ for $\tau\in I$, $1\le j\le a$. Suppose a function $F:(M_a(\mathbb C))^I\to\mathbb C$ satisfies $$F((x_\tau\beta_\tau)_\tau)=\left(\prod_{\tau\in I}\prod_{j=1}^a(\beta_\tau)_{jj}^{\nu_{\tau,j}}\right)F(x)$$ whenever every $x_\tau$ is invertible and every $\beta_\tau$ is invertible upper triangular. Let $N\ge0$, let $K_\tau\ge0$ with $\sum_\tau K_\tau=N$, and let $P$ be a polynomial in all matrix entries. If $$P(x)=F(x)\prod_{\tau\in I}\det(x_\tau)^{K_\tau}$$ whenever every $x_\tau$ is invertible, then there is a polynomial $Q$ in the same entries with $F(x)=Q(x)$ on that locus.
