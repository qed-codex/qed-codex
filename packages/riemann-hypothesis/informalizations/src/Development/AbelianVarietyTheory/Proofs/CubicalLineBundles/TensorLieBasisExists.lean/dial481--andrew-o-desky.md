---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/CubicalLineBundles/TensorLieBasisExists.lean",
  "declarations": [
    "GlobalTheory.SerreLie.exists_lie_tensor"
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

## Tangent vectors of a tensor construction on commutative group schemes

[Theorem AV.0950](https://andrewodesky.com/rh/lean/GlobalTheory.SerreLie.exists_lie_tensor/)

Let $O\to R$ be a homomorphism of commutative rings and let $M$ be a finitely generated projective $O$-module. Let $G,A$ be commutative group schemes over $R$ with $O$-actions, and suppose natural $O$-linear isomorphisms $$M\otimes_O G(T)\simeq A(T)$$ are specified for every $R$-scheme $T$. Write $\iota_m:G\to A$ for the map induced by $m\in M$, and $\phi_A:A\to A$ for that induced by $\phi\in\operatorname{End}_O(M)$. Suppose $\operatorname{Lie}(G)$ has an $R$-basis consisting of one vector $v$, and the differential of the $O$-action sends $v$ to $cv$ for every $c\in O$, using $O\to R$ on the right.

There is an injective map $\Phi:R\otimes_O M\to A(R[\epsilon]/\epsilon^2)$ whose image is exactly the tangent vectors at the identity, with $$\Phi(y+z)=\Phi(y)\Phi(z),\qquad\Phi(cy)=c\Phi(y)\quad(c\in R),$$ $$\Phi(1\otimes m)=d\iota_m(v),\qquad\Phi((1\otimes\phi)y)=\phi_A(\Phi(y)).$$
