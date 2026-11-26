---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/IsIntegralZpowOfPowEqOne.lean",
  "declarations": [
    "GlobalTheory.MemberLatFull.fullLat_of"
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

## A full lattice from denominator clearing and a norm-product bound

[Theorem ARAK.0760](https://andrewodesky.com/rh/lean/GlobalTheory.MemberLatFull.fullLat_of/)

Let $K$ be a number field, $R$ a commutative $K$-algebra, and $C\subseteq R$ a finite-dimensional $K$-linear subspace. For each finite prime $\mathfrak p$ of $K$, let $\mathcal V_{\mathfrak p}$ be a collection of valuation functions as specified below. Define $$\Lambda=\{f\in C:v(f)\ge0\text{ for every }\mathfrak p\text{ and }v\in\mathcal V_{\mathfrak p}\}.$$ For each embedding $\tau:K\hookrightarrow\mathbb C$, choose a norm $N_\tau$ on $C$ satisfying $N_\tau(af)=|\tau(a)|N_\tau(f)$. Suppose $B\in\mathbb R$ satisfies $$\sum_{\tau:K\hookrightarrow\mathbb C}\log N_\tau(f)\ge-B\qquad(0\ne f\in\Lambda).$$ Suppose also that for every $f\in C$ there is $0\ne t\in\mathcal O_K$ such that $tf\in\Lambda$. Then $\Lambda$ is finitely generated over $\mathcal O_K$ and its $K$-linear span is $C$.
