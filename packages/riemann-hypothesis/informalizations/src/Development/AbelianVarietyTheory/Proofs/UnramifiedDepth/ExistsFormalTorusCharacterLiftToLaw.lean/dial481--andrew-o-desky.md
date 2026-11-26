---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/ExistsFormalTorusCharacterLiftToLaw.lean",
  "declarations": [
    "GlobalTheory.ChF.Lift.exists_char_lift"
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

## Formal characters extending independent torus tangent directions

[Theorem PHT.0436](https://andrewodesky.com/rh/lean/GlobalTheory.ChF.Lift.exists_char_lift/)

Let $p$ be prime, $C$ an algebraically closed characteristic-zero field with a nonnegative real-valued valuation, and $O\subseteq C$ its valuation ring. Assume $p$ is not a unit in $O$ and $O$ is $p$-adically complete. Let $F$ be a commutative $d$-dimensional formal group law over $O$ satisfying the torsion condition below. Suppose $$J:\widehat{\mathbb G}_m^r\longrightarrow F$$ is a homomorphism of formal group laws whose $d\times r$ linear coefficient matrix $B$ has a left inverse over $O$. For each $1\le i\le r$, there is a series $u_i\in O[[T_1,\ldots,T_d]]$ such that $$u_i(0)=1,\qquad u_i(F(T,S))=u_i(T)u_i(S),\qquad B^t\nabla u_i(0)=e_i,$$ where $e_i$ is the $i$th coordinate vector of $O^r$.
