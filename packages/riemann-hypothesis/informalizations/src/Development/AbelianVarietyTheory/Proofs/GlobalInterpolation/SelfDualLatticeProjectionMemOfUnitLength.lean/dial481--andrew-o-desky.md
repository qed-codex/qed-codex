---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/SelfDualLatticeProjectionMemOfUnitLength.lean",
  "declarations": [
    "GlobalTheory.SelfDualLatticeSplit.unit_vector_splits"
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

## Splitting off a vector of unit Hermitian length

[Theorem ALG.1144](https://andrewodesky.com/rh/lean/GlobalTheory.SelfDualLatticeSplit.unit_vector_splits/)

Let $E/F$ be a CM extension of number fields with involution $\sigma$, and let $J\in M_M(E)$ be nondegenerate and Hermitian. For a nonzero prime $v$ of $\mathcal O_F$, put $E_v=F_v\otimes_FE$ and let $O_v$ be the integral closure of $\mathcal O_{F_v}$ in $E_v$. Write $h(x,y)=\bar x^tJy$ on $E_v^M$. Let $L$ be a finitely generated $O_v$-submodule spanning $E_v^M$ with $$L=\{y\in E_v^M:h(z,y)\in O_v\text{ for every }z\in L\}.$$ If $x\in L$ and $h(x,x)b=1$ for some $b\in O_v$, then $$L=O_vx+(L\cap x^\perp),\qquad x^\perp=\{y:h(x,y)=0\}.$$ Moreover $L\cap x^\perp$ is finitely generated, spans $x^\perp$ over $E_v$, and is self-dual within $x^\perp$ for the restricted form.
