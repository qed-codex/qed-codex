---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/ExistsIsKum.lean",
  "declarations": [
    "GlobalTheory.CNorm.exists_isKum"
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

## A cyclic Kummer extension from a non-power

[Theorem ANT.1262](https://andrewodesky.com/rh/lean/GlobalTheory.CNorm.exists_isKum/)

Let $p$ be prime, $F$ a field of characteristic zero, $\zeta\in F$ a primitive $p$th root of unity, and $\delta\in F$ with $r^p\ne\delta$ for every $r\in F$. There are a field extension $E/F$, an element $\theta\in E$, and an $F$-automorphism $\sigma$ of $E$ such that $$\theta^p=\delta,\qquad \sigma(\theta)=\zeta\theta,\qquad F[\theta]=E.$$
