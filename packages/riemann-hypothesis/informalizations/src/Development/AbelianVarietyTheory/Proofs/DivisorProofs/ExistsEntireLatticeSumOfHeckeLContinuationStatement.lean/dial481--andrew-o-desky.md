---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsEntireLatticeSumOfHeckeLContinuationStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_entire_latticeSum_of_heckeL_continuation"
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

## Entire continuation of a CM lattice sum

[Theorem ANT.1342](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_entire_latticeSum_of_heckeL_continuation/)

Assume the following global continuation statement: for every CM field $E$, every CM type $(\varphi_i)_{i\in I}$, every integer family $(m_i)$ not identically zero, and every unitary Hecke character of infinity type $2m_i$, its Euler product agrees for $\operatorname{Re}z>1$ with an entire function.

Let $E$ be a CM field, $F=E^+$, and $(\varphi_i)_{i\in I}$ a CM type. Suppose $E/F$ is unramified at all finite places. Let $s\ge1$ and $\kappa_i\ge0$ be integers, and let $\mathfrak f\mid\mathfrak c$ be nonzero ideals of $\mathcal O_F$. Assume $\mathfrak f\ne\mathcal O_F$ and the base-conductor condition on $\mathfrak f$ specified below. Let $\chi$ be a unitary Hecke character of infinity type $2(\kappa_i+s)$, trivial in its finite part on $\widehat{\mathcal O}_{\mathfrak c}^{\times}$, where $$\mathcal O_{\mathfrak c}=\mathcal O_F+\mathfrak c\mathcal O_E,$$ and the hat denotes closure in the finite adeles of $E$. For any finite idele $y$, put $$L_y=\{x\in E:xy^{-1}\in\widehat{\mathcal O}_{\mathfrak c}\}.$$ There is an entire $S:\mathbb C\to\mathbb C$ such that for $\operatorname{Re}z+s>1$, $$S(z)=\sum_{[x]\in(L_y\setminus\{0\})/\mathcal O_F^{\times}} \prod_{i\in I}\varphi_i(x)^{-(2s+\kappa_i)}\overline{\varphi_i(x)}^{\kappa_i}|\varphi_i(x)|^{-2z},$$ with convergence in the unordered-sum sense, using a fixed choice of one representative of each class.
