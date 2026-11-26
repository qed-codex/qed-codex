---
{
  "module": "src/CompanionTheory/HarishChandraModules/KFiniteAnalyticVectors/HaarBumpFunctions/PoulsenSmoothVectorsDense.lean",
  "declarations": [
    "CompanionTheory.D.gk.Poul.poulsen_smooth_vectors_dense"
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

## Invariant forms on smooth discrete series vectors

[Theorem REP.1431](https://andrewodesky.com/rh/lean/CompanionTheory.D.gk.Poul.poulsen_smooth_vectors_dense/)

Let $k,r\ge0$, put $n=2r+k+1$, and let $G$ be the real unitary group on $\mathbb C^n$ whose form has $r$ hyperbolic pairs and middle block $\operatorname{diag}(1_k,-1)$. Let $R,R'$ be unitary representation models on complex Hilbert spaces, satisfying the discrete-series conditions of ([Discrete series with a prescribed lowest compact type](https://andrewodesky.com/rh/lean/CompanionTheory.RgDs.B.classUsed/)) for the same sign pattern $\varepsilon$ and parameters $\mu,\mu'\in\mathbb R^n$, respectively. Write $R^\infty,(R')^\infty$ for their smooth vectors. Call a form $B$ admissible here if on smooth vectors it is linear in its first argument, conjugate-linear in its second, diagonally $G$-invariant, and bounded by $$|B(x,y)|\le C\Bigl(\sum_{D\in\mathcal D}\|dR(D)x\|\Bigr)\Bigl(\sum_{D'\in\mathcal D'}\|dR'(D')y\|\Bigr)$$ for some real $C$ and finite lists $\mathcal D,\mathcal D'$ of words in $\mathfrak g$.

Every admissible form on $R^\infty\times R^\infty$ has the form $B(x,y)=c\langle y,x\rangle$ for some $c\in\mathbb C$. For every admissible form on $R^\infty\times(R')^\infty$, either it is zero on all smooth-vector pairs, or there exists a unitary complex-linear isomorphism $U:R\simeq R'$ with $UR(g)=R'(g)U$ for every $g\in G$.
