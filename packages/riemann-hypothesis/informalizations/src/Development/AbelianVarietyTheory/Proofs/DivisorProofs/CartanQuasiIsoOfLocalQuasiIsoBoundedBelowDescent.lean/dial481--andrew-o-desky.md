---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/CartanQuasiIsoOfLocalQuasiIsoBoundedBelowDescent.lean",
  "declarations": [
    "GlobalTheory.CartanOne.cartan_one"
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

## Descent of a local cohomology isomorphism

[Theorem AG.0636](https://andrewodesky.com/rh/lean/GlobalTheory.CartanOne.cartan_one/)

Let $\mathcal T$ be a category with a class $\mathcal C$ of morphisms closed under composition, let $C,D:\mathcal T\to\operatorname{Ch}(\mathbf{Ab})$ be functors to integer-indexed cochain complexes, and let $\varphi:C\to D$ be natural. Suppose there is $b\in\mathbb Z$ such that $C^n(U)=D^n(U)=0$ for $n<b$ and every $U$.

Assume the cosimplicial refinement condition below. Suppose also that every cocycle in $D^n(U)$ becomes, after some morphism $U\to V$ in $\mathcal C$, cohomologous to the image of a cocycle in $C^n(V)$. Suppose that every cocycle of $C^n(U)$ whose image is a boundary in $D(U)$ becomes a boundary after some such morphism. Then $$H^n(C(U))\xrightarrow{\ H^n(\varphi_U)\ }H^n(D(U))$$ is an isomorphism for every $U$ and $n\in\mathbb Z$.
