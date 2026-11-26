---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/RCocompactPfKer.lean",
  "declarations": [
    "Formalism.L2.SG.Pf.RCoc.kerBaseChange_holds"
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

## A kernel projector valid after every field extension

[Theorem ALG.0566](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Pf.RCoc.kerBaseChange_holds/)

Let $K,L$ be fields, let $\iota:K\hookrightarrow L$, let $M,P$ be finite index sets, and let $A\in M_{M,P}(K)$. There is $Q\in M_P(K)$ such that $$AQ=0,$$ and, for every $z\in L^P$, $$\iota(A)z=0\quad\Longrightarrow\quad\iota(Q)z=z.$$ The maps $\iota(A),\iota(Q)$ apply $\iota$ entrywise.
