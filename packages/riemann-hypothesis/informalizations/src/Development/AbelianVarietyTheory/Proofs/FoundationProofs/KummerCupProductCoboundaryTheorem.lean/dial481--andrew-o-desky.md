---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/KummerCupProductCoboundaryTheorem.lean",
  "declarations": [
    "GlobalTheory.KummerCob.thmA"
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

## A Kummer cup product with a primitive vanishing on inertia

[Theorem GC.0905](https://andrewodesky.com/rh/lean/GlobalTheory.KummerCob.thmA/)

Let $k$ be an algebraically closed field of characteristic zero, $K$ a finite extension of $k(t)$ with compatible $k[t]$-algebra structure, and $A$ the integral closure of $k[t]$ in $K$. Let $\Omega$ be an algebraic closure of $K$, $N\ge1$, and $\zeta\in\Omega$ a primitive $N$th root of unity. For $a,b\in A^\times$, choose $\alpha,\beta\in\Omega$ with $\alpha^N=a$, $\beta^N=b$. Define $\kappa_\alpha,\kappa_\beta:G_K\to\mathbb Z/N\mathbb Z$ by $$g(\alpha)/\alpha=\zeta^{\kappa_\alpha(g)},\qquad g(\beta)/\beta=\zeta^{\kappa_\beta(g)}.$$ Both maps are locally constant homomorphisms to the additive group. There is a locally constant $\eta:G_K\to\mathbb Z/N\mathbb Z$ such that $$\kappa_\alpha(g)\kappa_\beta(h)=\eta(h)-\eta(gh)+\eta(g)\qquad(g,h\in G_K),$$ and $\eta(g)=0$ for every inertia element $g$ at every valuation ring of $\Omega$ containing $A$.
