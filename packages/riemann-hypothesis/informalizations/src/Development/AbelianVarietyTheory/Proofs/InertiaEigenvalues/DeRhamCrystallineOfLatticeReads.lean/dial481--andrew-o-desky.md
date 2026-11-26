---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DeRhamCrystallineOfLatticeReads.lean",
  "declarations": [
    "GlobalTheory.ReadPass.crys_pass"
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

## Crystallinity passes to a representation covered by equivariant images

[Theorem PHT.0719](https://andrewodesky.com/rh/lean/GlobalTheory.ReadPass.crys_pass/)

Let $p$ be prime, let $K,L$ be finite extensions of $\mathbb Q_p$, and use the local period data specified below. Let $V$ be a finite-dimensional crystalline $\mathbb Q_p$-representation of $G_K$, and let $W=L^a$ have an $L$-linear $G_K$-action, where $a\ge0$. Suppose every $w\in W$ can be written as $F(v)$ for some $v\in V$ and some equivariant $\mathbb Q_p$-linear map $F:V\to W$, where $F$ may depend on $w$. Then $W$ is crystalline.
