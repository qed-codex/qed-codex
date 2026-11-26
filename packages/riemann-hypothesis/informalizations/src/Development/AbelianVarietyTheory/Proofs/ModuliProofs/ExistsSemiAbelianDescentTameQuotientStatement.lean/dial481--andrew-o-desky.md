---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsSemiAbelianDescentTameQuotientStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_semiAbelian_descent_tame_quotient"
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

## Descent of semiabelian data through a tame finite quotient

[Theorem AV.0672](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_semiAbelian_descent_tame_quotient/)

Fix the CM auxiliary datum for a CM number field $E$ specified in the conventions below. Let a finite group $\Gamma$ act on a scheme $X$, let $\pi:X\to X'$ be finite and affine, with $X'$ locally noetherian, and assume $\pi$ is invariant and identifies $\mathcal O_{X'}$ with the invariant subsheaf of $\pi_*\mathcal O_X$. Let $G\to X$ carry the semiabelian data below, and let $s:X\to\operatorname{Spec}R$ for a commutative ring $R$. Suppose $G\to\operatorname{Spec}R$ is quasi-projective, $X$ is reduced, and every generic point of $X$ lies in the abelian-fibre locus of $G$.

Suppose a group action of $\Gamma$ on the total scheme of $G$ lifts the given action on $X$, and each action map is a cartesian morphism of the semiabelian data over its action on $X$. At every geometric point $x:\operatorname{Spec}k\to X$, assume the order of its stabilizer is nonzero in $k$, and that each stabilizer element acts identically on the entire fibre $G_x$.

There are semiabelian data $G'\to X'$ and a cartesian morphism $\nu:G\to G'$ over $\pi$, preserving all these data, with $\nu\gamma=\nu$ for every $\gamma\in\Gamma$. The additional properties below descend if they hold for $G$ and its polarization bundle has the specified pushforward property.
