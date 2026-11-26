---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/EtaleSpaceDescentLocalEquivalence.lean",
  "declarations": [
    "GlobalTheory.EtC.Descent.main"
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

## Etale cohomological equivalence from local lifting and vanishing

[Theorem AG.0596](https://andrewodesky.com/rh/lean/GlobalTheory.EtC.Descent.main/)

Let $R$ be a commutative ring, $F$ a sheaf of $R$-modules on the big étale site of schemes, and $T$ a category. Let $\mathcal C$ be a class of arrows of $T$ closed under composition. Let $X,X':T^{\mathrm{op}}\to\mathrm{sPSh}$ be functors to simplicial presheaves on schemes, with a natural map $a_U:X(U)\to X'(U)$.

Assume every arrow $g:U\to V$ in $\mathcal C$ has a common resolution as follows: there are a cosimplicial object $Y^\bullet$ of $T$, a coaugmentation $b:U\to Y^\bullet$, and $h:V\to Y^0$ with $hg=b^0$, such that, for every simplicial degree $k$, both augmented simplicial presheaves $$[m]\longmapsto X(Y^m)_k,\qquad [m]\longmapsto X'(Y^m)_k$$ have associated free étale $R$-module chain complexes quasi-isomorphic, by their augmentations, to those of $X(U)_k$ and $X'(U)_k$ respectively.

Suppose the following hold for every $U$ and every $n\in\mathbb Z$:

1. For each $x\in H^n(X(U),F)$ there are $g:U\to V$ in $\mathcal C$ and $y\in H^n(X'(V),F)$ with $a_V^*y=g^*x$.
2. If $y\in H^n(X'(U),F)$ has $a_U^*y=0$, some $g:U\to V$ in $\mathcal C$ satisfies $g^*y=0$.

Then $a_U^*:H^n(X'(U),F)\to H^n(X(U),F)$ is an isomorphism for every $U$ and $n$.
