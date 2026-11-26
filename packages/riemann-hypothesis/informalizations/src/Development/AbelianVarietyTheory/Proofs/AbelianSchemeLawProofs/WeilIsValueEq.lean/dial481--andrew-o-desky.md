---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/AbelianSchemeLawProofs/WeilIsValueEq.lean",
  "declarations": [
    "GlobalTheory.PairingLevels.weilIs_mul_iff"
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

## Compatibility of Weil pairings with multiplication

[Theorem AV.1234](https://andrewodesky.com/rh/lean/GlobalTheory.PairingLevels.weilIs_mul_iff/)

Assume bijectivity of pullback $\Gamma(S,\mathcal O_S)\to\Gamma(A,\mathcal O_A)$ for every abelian scheme $A/S$, existence of a generating trivialization of the theta construction of every line bundle on a polarized abelian scheme, local lifting of every torsion point to the associated theta group, and existence and uniqueness of the scalar in each Weil-pairing relation.

Let $(A,L)$ be a polarized abelian scheme over a scheme $S$, let $T\to S$ be a scheme, and let $k,l\ge0$. Suppose $kl$ is a unit in $\Gamma(T,\mathcal O_T)$. For $x,y\in A(T)$ with $[kl]x=0$ and $[k]y=0$, and every $c\in\Gamma(T,\mathcal O_T)^\times$, $$e_{kl,L}(x,y)=c\quad\Longleftrightarrow\quad e_{k,L}([l]x,y)=c,$$ where $e_{n,L}$ is the scalar commutator pairing defined through the theta group of $L^{\otimes n}$.
