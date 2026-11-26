---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/HeightProofs/FieldSizeAdjoinKthRoot.lean",
  "declarations": [
    "GlobalTheory.FieldSize.sz_sup_adjoin_root"
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

## Degree and root discriminant after adjoining a root

[Theorem ANT.0896](https://andrewodesky.com/rh/lean/GlobalTheory.FieldSize.sz_sup_adjoin_root/)

Let $F\subseteq\mathbb C$ be a number field and let $a,b\in\mathbb R$ satisfy $$\log[F:\mathbb Q]\le a,\qquad \frac{\log|\operatorname{disc}(F)|}{[F:\mathbb Q]}\le b.$$ Let $k\ge1$, $0\ne y\in F$, and let $I\subseteq F$ be an $\mathcal O_F$-submodule with $I^k=\mathcal O_F y$. If $z\in\mathbb C$ satisfies $z^k=y$, then $F(z)$ is a number field and $$\log[F(z):\mathbb Q]\le a+\log k,\qquad \frac{\log|\operatorname{disc}(F(z))|}{[F(z):\mathbb Q]}\le b+\log k.$$
