---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/LogAbsVpOfNormalised.lean",
  "declarations": [
    "GlobalTheory.HTLat.eigQuotLat",
    "GlobalTheory.HTLat.eigSubLat"
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

## Eigenspace submodules and integral frames

[Definition / hypothesis AV.D024](https://andrewodesky.com/rh/lean/GlobalTheory.EigenSplit.eigenSub/)

An action on a vector space gives eigenspace intersections and, when the coefficient algebra splits, projected submodules. Integral frames describe a submodule within the span of chosen vectors.

**Eigenspace intersections.** Let $O$ and $\Lambda$ be commutative rings, let $C$ be a field with a specified homomorphism $\iota:O\to C$, and let $V$ be a $C$-vector space, viewed as an $O$-module through this homomorphism. Fix a ring homomorphism $\rho:\Lambda\to\operatorname{End}_C(V)$ and an $O$-submodule $X\subseteq V$. For a ring homomorphism $\chi:\Lambda\to C$, put $$V_\chi=\{x\in V:\rho(a)x=\chi(a)x\text{ for every }a\in\Lambda\},\qquad X^{\mathrm{sub}}_\chi=X\cap V_\chi.$$

**Projected submodules.** Let $I$ be an index set and let $\sigma_i:\Lambda\to C$, for $i\in I$, be ring homomorphisms such that $$\alpha:C\otimes_{\mathbb Z}\Lambda\longrightarrow C^I,\qquad \alpha(c\otimes a)_i=c\sigma_i(a),$$ is bijective. Here $C^I$ is the algebra of all functions $I\to C$, with pointwise operations. For each $i$, let $e_i$ be the inverse image under $\alpha$ of the function equal to $1$ at $i$ and $0$ elsewhere. Extend $\rho$ to the $C$-algebra homomorphism $$\widetilde\rho:C\otimes_{\mathbb Z}\Lambda\longrightarrow\operatorname{End}_C(V),\qquad \widetilde\rho(c\otimes a)(x)=c\rho(a)x.$$ The eigenspace projection and projected submodule at $i$ are $$\pi_i=\widetilde\rho(e_i),\qquad X^{\mathrm{quot}}_i=\pi_i(X)=\{\pi_i(x):x\in X\}.$$

**Integral frames.** For an $O$-submodule $Y\subseteq V$ and a finite tuple $w_1,\ldots,w_n\in V$, the integral-frame condition is that the vectors are $C$-linearly independent and $$\sum_{i=1}^n Ow_i=Y\cap\operatorname{span}_C\{w_1,\ldots,w_n\}.$$ For the empty tuple, both spans are zero.

**Scalar-extension submodules.** Let $p$ be a rational prime, suppose $O$ is a $\mathbb Z_p$-algebra, and suppose the map $O\to C$ respects the $\mathbb Z_p$-algebra structures. For a $\mathbb Z_p$-module $T$ with an action $\Lambda\to\operatorname{End}_{\mathbb Z_p}(T)$, set $$V=C\otimes_{\mathbb Z_p}T,\qquad X=\operatorname{im}\left(O\otimes_{\mathbb Z_p}T\longrightarrow V\right),\qquad o\otimes t\longmapsto \iota(o)\otimes t,$$ The induced action on $V$ is $\rho(a)(c\otimes t)=c\otimes at$. Its eigenspace intersections and projected submodules have the definitions above.
