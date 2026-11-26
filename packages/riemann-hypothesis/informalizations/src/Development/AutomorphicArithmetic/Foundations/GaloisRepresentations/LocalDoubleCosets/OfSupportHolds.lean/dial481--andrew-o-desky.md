---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LocalDoubleCosets/OfSupportHolds.lean",
  "declarations": [
    "UpperTheory.Gal.LocD.locDesc_holds"
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

## A field-automorphism intertwiner acts by a scalar on a Jacquet module

[Theorem REP.0229](https://andrewodesky.com/rh/lean/UpperTheory.Gal.LocD.locDesc_holds/)

Let $E$ be a nonarchimedean local field, $n\ge0$, and $\sigma:E\simeq E$ a valuation-preserving automorphism with $\sigma^q=1$ for some integer $q\ge1$. Let $\pi$ be an irreducible complex representation of $\operatorname{GL}_n(E)$ that is a subquotient of the principal series induced by smooth characters $\omega_1,\ldots,\omega_n:E^\times\to\mathbb C^\times$, each fixed by $\sigma$. Suppose $A\ne0$ is a complex-linear operator with $$A\pi(g)=\pi(\sigma(g))A,$$ where $\sigma$ acts entrywise. Let $J=\pi_{N}$ be the Jacquet module for the upper unitriangular subgroup, with normalized diagonal action $J(t)$, $t\in(E^\times)^n$, and let $A_J$ be the induced operator.

The space $J$ is nonzero and finite-dimensional. Every character $\eta$ with nonzero simultaneous generalized eigenspace in $J$ has the form $$\eta(t)=\prod_i\omega_{w(i)}(t_i)$$ for a permutation $w$. There is $c\in\mathbb C^\times$ with $A_J=c\,\mathrm{id}$. If a continuous additive character $\psi:E\to\mathbb S^1$ is $\sigma$-invariant and a nonzero linear functional $\lambda$ satisfies $$\lambda(\pi(u)v)=\psi\!\left(\sum_{i=1}^{n-1}u_{i,i+1}\right)\lambda(v),\qquad\lambda\circ A=a\lambda,$$ then $a=c$.

For every nonzero diagonal-invariant subspace $U\subseteq J$, every diagonal element $t$, and every $k_0\ge0$, there is $k\ge k_0$ such that $J(t^k)A_J$ preserves $U$ and has nonzero trace on $U$.
