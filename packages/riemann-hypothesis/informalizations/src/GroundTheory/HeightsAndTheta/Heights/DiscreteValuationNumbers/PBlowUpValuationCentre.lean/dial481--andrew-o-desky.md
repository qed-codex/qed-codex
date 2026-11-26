---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/DiscreteValuationNumbers/PBlowUpValuationCentre.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.NumbersDVR.exists_blowUp_centre"
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

## A valuation centre on a multihomogeneous blow-up

[Theorem AG.1042](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.NumbersDVR.exists_blowUp_centre/)

Let $O$ be a commutative ring, $K$ a finite set of blocks, $I_k$ arbitrary sets, and $J$ a finite set. Put $B=O[X_{ki}:k\in K,i\in I_k]$. Let $P\subseteq W$ be prime ideals, with $P$ multihomogeneous and $W$ relevant. Let $(u_j)_{j\in J}$ be forms of a common multidegree $N\in\mathbb N^K$, with at least one $u_j\notin P$. Put $L=\operatorname{Frac}(B/P)$.

Form $B'=B[Y_j:j\in J]$, regarding the $Y_j$ as one additional block, and let $$P'=\ker\bigl(B'\longrightarrow(B/P)[T],\ X_{ki}\mapsto\bar X_{ki},\ Y_j\mapsto\bar u_jT\bigr).$$ For any valuation ring $V\subseteq L$ containing $A(P,W)$ as defined below, there is a relevant multihomogeneous prime $W'\subset B'$ with $$P'\subseteq W',\qquad W'\cap B\subseteq W,\qquad A'(P,u,W')\subseteq V.$$
