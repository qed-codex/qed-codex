---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/LocalLanglands/LocalCentralUnits/TameUniq.lean",
  "declarations": [
    "UpperTheory.Zero.LLC.tameUniq"
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

## Uniqueness of a tame parameter with fixed determinant

[Theorem REP.1698](https://andrewodesky.com/rh/lean/UpperTheory.Zero.LLC.tameUniq/)

Let $E$ be a number field, $\Omega/E$ an algebraic closure, $A$ a valuation ring above a finite place $w$, $p$ a prime, and $K/\mathbb F_p$ a field extension. Suppose $n\ge1$, $|\mathcal O_E/w|=p$, $[K:\mathbb F_p]=n$, and $R:I_w\to K^\times$ is surjective with open kernel, trivial on wild inertia, and satisfies $$R(\sigma t\sigma^{-1})=R(t)^p\qquad(\deg\sigma=1).$$ Let $\theta:K^\times\to\mathbb C^\times$ have $n$ distinct Frobenius conjugates. Suppose a complex Weil–Deligne parameter $V$ has inertia characteristic polynomial $$P_{V,t}(T)=\prod_{j=0}^{n-1}\bigl(T-\theta(R(t)^{p^j})\bigr)\qquad(t\in I_w).$$ Then the same formula holds with $\theta^{p^j}$ in place of $\theta$ for every $j\ge0$. Every other character $\theta'$ giving this formula for $V$ equals $\theta^{p^j}$ for some $0\le j<n$. If $V,V'$ are irreducible tame Weil–Deligne parameters, $V'$ has the displayed inertia polynomial, and $\det V(\sigma)=\det V'(\sigma)$ for every $\sigma\in W_w$, then $V'=V$.
