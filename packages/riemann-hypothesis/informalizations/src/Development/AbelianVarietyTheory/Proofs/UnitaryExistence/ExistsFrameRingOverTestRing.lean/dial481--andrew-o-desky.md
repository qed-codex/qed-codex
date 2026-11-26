---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UnitaryExistence/ExistsFrameRingOverTestRing.lean",
  "declarations": [
    "GlobalTheory.exists_frameRing_testRing"
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

## A universal reduced algebra of invertible frames

[Theorem ALG.0361](https://andrewodesky.com/rh/lean/GlobalTheory.exists_frameRing_testRing/)

Let $K$ be a field, $J$ a finite set, $(m_j)_{j\in J}$ nonnegative integers, and $R$ a reduced finitely generated commutative $K$-algebra, given as a polynomial-ring quotient by a radical ideal. There exist another such algebra $A$, a $K$-algebra map $\pi:R\to A$, matrices $X_j\in M_{m_j}(A)$ with invertible determinants, and $s\in A^\times$ with the following property.

For every commutative $K$-algebra $T$, map $\psi:R\to T$, matrices $g_j\in M_{m_j}(T)$ with invertible determinants, and $a\in T^\times$, there is a unique $K$-algebra map $k:A\to T$ such that $$k\pi=\psi,\qquad k(X_j)=g_j\quad(j\in J),\qquad k(s)=a,$$ where $k$ acts entrywise on matrices.
