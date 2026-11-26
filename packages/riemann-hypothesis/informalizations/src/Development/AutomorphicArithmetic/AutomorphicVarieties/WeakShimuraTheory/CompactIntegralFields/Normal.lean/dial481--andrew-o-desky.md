---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/WeakShimuraTheory/CompactIntegralFields/Normal.lean",
  "declarations": [
    "UpperTheory.V.Ws.normal"
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

## Symplectic diagonalization over a complete local ring

[Theorem ALG.0263](https://andrewodesky.com/rh/lean/UpperTheory.V.Ws.normal/)

Let $R$ be a commutative local ring complete for its maximal ideal $\mathfrak m$, with $2\in R^\times$. Index matrices by $0,1,2,3$, put $s=(1,1,-1,-1)$, and define $$(X^\#)_{ij}=s_i s_j X_{3-j,3-i}.$$ Let $\nu\in R^\times$ and $g\in M_4(R)$ satisfy $$g^\#g=\nu I_4,\qquad g_{ij}\in\mathfrak m\ (i\ne j),\qquad g_{ii}-g_{jj}\in R^\times\ (i\ne j).$$ There exists $u\in M_4(R)$ such that $$u^\#u=I_4,\qquad u\equiv I_4\pmod{\mathfrak m},\qquad u^\#gu\text{ is diagonal}.$$ If $g$ preserves the coordinate subspaces indexed by $\{0,2\}$ and $\{1,3\}$, then $u$ can be chosen to preserve both as well.
