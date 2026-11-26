---
{
  "module": "src/Formalism/LocalToGlobal/PairingIndexBounds/HalvesRecursion/BoundedHalfModels/AdicBoxOpenness/CentralCharacterLocalHolds.lean",
  "declarations": [
    "Formalism.L2.PairingIndexBounds.Rec.good_duality_holds"
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

## Detecting membership by the opposite summand of a self-dual group

[Theorem ALG.0832](https://andrewodesky.com/rh/lean/Formalism.L2.PairingIndexBounds.Rec.good_duality_holds/)

Let $V$ be a complex vector space and let $H:V\times V\to\mathbb C$ be Hermitian, complex-linear in its first argument. Put $E(x,y)=\operatorname{Im}H(x,y)$. Let $A,B,\Lambda\subseteq V$ be additive subgroups. Assume $$E(A,A)\subseteq\mathbb Z,\qquad E(B,B)\subseteq\mathbb Z,\qquad \Lambda\subseteq(\Lambda\cap A)+(\Lambda\cap B),$$ and assume that every $w\in V$ satisfying $E(w,\Lambda)\subseteq\mathbb Z$ belongs to $\Lambda$. Then $$a\in A,\ E(a,B\cap\Lambda)\subseteq\mathbb Z\quad\Longrightarrow\quad a\in\Lambda,$$ $$b\in B,\ E(b,A\cap\Lambda)\subseteq\mathbb Z\quad\Longrightarrow\quad b\in\Lambda.$$
