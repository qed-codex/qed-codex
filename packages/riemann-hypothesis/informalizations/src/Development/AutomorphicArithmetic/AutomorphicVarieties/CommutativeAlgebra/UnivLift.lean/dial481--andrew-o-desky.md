---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/UnivLift.lean",
  "declarations": [
    "UpperTheory.V.Alg.univ_lift"
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

## A universal ring for lifts with a fixed basis

[Theorem GC.1153](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.univ_lift/)

Let $\ell$ be prime and let $O$ be a complete Noetherian commutative local ring whose residue field $k$ is finite of characteristic $\ell$. Let $\Gamma$ be a profinite group such that $\operatorname{Hom}_{\mathrm{cont}}(H,\mathbb Z/\ell\mathbb Z)$ is finite for every open subgroup $H\subseteq\Gamma$. Let $I$ be a finite index set and let $\bar r:\Gamma\to M_I(k)$ be a locally constant multiplicative homomorphism preserving $1$. There exist a complete Noetherian commutative local $O$-algebra $R$, inducing an isomorphism on residue fields, and a lift $r:\Gamma\to M_I(R)$ continuous for the maximal-ideal topology, with the following property: for every complete Noetherian commutative local $O$-algebra $R'$ inducing an isomorphism on residue fields and every such continuous lift $r'$ of $\bar r$, there is a unique $O$-algebra homomorphism $f:R\to R'$ with $f\circ r=r'$ entry by entry.
