---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/UnramifiedGaloisHomsBoundedClassNumberOfArtinRecStatement.lean",
  "declarations": [
    "GlobalTheory.T.unramifiedGaloisHoms_bounded_classNumber_of_artinReciprocity"
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

## The class number bounds unramified first cohomology

[Theorem GC.1114](https://andrewodesky.com/rh/lean/GlobalTheory.T.unramifiedGaloisHoms_bounded_classNumber_of_artinReciprocity/)

Assume global Artin reciprocity in the normalization below. Let $E$ be a number field, $\Omega$ an algebraic closure, and choose a valuation ring of $\Omega$ above every finite place of $E$, defining inertia subgroups $I_v\subseteq G_E$. Let $\ell$ be prime and $O$ a discrete valuation domain finite over $\mathbb Z_\ell$. Assume $\ell\ne2$ or $E$ has no real places. Let $M$ be an $O$-module isomorphic to $\operatorname{Frac}(O)/O$, endowed with the trivial $G_E$-action.

If $S\subseteq H^1(G_E,M)$ is an $O$-submodule whose classes admit locally constant cocycle representatives and whose restriction to each $I_v$ is zero, then $$\operatorname{length}_O S\le\operatorname{length}_O(O/\ell O)\,v_\ell(h_E),$$ where $h_E$ is the class number. Lengths are allowed to be infinite.
