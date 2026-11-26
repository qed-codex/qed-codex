---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/SmallExtensionDualNumberFibreProductAffineMilnor.lean",
  "declarations": [
    "GlobalTheory.DualOpen.smallExt_fibre_ring"
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

## Two fiber product presentations of a small extension

[Theorem ALG.1066](https://andrewodesky.com/rh/lean/GlobalTheory.DualOpen.smallExt_fibre_ring/)

Let $C$ be a commutative local ring with maximal ideal $\mathfrak m$ and residue field $k$. Suppose $0\ne e\in\mathfrak m$ and $\mathfrak m e=0$. Write $D=k[\varepsilon]/(\varepsilon^2)$, let $r:C\to k$ be reduction, let $j:k\to D$ be the constant inclusion, and let $d:D\to k$ send $\varepsilon$ to zero.

There are a commutative ring $P$ and homomorphisms $i:C\to P$, $p,\sigma:P\to C$, and $q:P\to D$ satisfying $$pi=\sigma i=1_C,\qquad qi=jr.$$ The map $\operatorname{Spec}C\xrightarrow{\operatorname{Spec}\sigma}\operatorname{Spec}P$ is a surjective closed immersion. Both comparison homomorphisms $$P\xrightarrow{(p,\sigma)}C\times_{C/(e)}C,\qquad P\xrightarrow{(p,q)}C\times_kD$$ are isomorphisms, where the first fiber product uses the quotient map on each copy of $C$, and the second uses $r$ and $d$.
