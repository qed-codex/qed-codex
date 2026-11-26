---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/PAdicWittLattices/SplitsBasicHolds.lean",
  "declarations": [
    "UpperTheory.Gal.G3.galInv_holds"
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

## Pullback image equals invariants on a finite Galois cover

[Theorem AG.1254](https://andrewodesky.com/rh/lean/UpperTheory.Gal.G3.galInv_holds/)

Let $B$ be a scheme and $R$ a field of characteristic zero. Let $T$ assign an $R$-vector space $T(X)$ to each $B$-scheme, with contravariant linear pullbacks respecting identity and composition. Assume that pullback along finite Galois covers is injective, and every finite etale map $s:Y\to Z$ has a linear trace $s_*:T(Y)\to T(Z)$ whose pullback, on every finite splitting family $\sigma_j:W\to Y$ over $c:W\to Z$, equals $\sum_j\sigma_j^*$.

Let $c:W\to Z$ be a finite Galois cover of $B$-schemes with finite group $G$ acting by $B$-morphisms $a_g:W\to W$. For every $y\in T(W)$, $$y\in\operatorname{im}\bigl(c^*:T(Z)\to T(W)\bigr)\quad\Longleftrightarrow\quad a_g^*y=y\text{ for all }g\in G.$$
