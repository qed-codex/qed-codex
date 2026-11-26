---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/FockMinimalKTypeSecondMemberStatement.lean",
  "declarations": [
    "GlobalTheory.T.fock_minimal_KType_second_member"
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

## Joint harmonics detect a minimal compact type of a theta quotient

[Theorem REP.0521](https://andrewodesky.com/rh/lean/GlobalTheory.T.fock_minimal_KType_second_member/)

Let $p,q,r,s\ge0$ and let $M_1,M_2$ be the algebraic modules for $\mathfrak{gl}_{p+q}(\mathbb C)$ and $\mathfrak{gl}_{r+s}(\mathbb C)$ described below. Suppose $M_2$ is nonzero and irreducible, and all its compact highest-weight spaces are finite-dimensional. Let $$f:\mathcal P\to M_1\otimes_{\mathbb C}M_2$$ be nonzero and intertwine both Fock Lie algebra actions with the respective tensor-factor actions. Let $\mu'$ be an occurring rational compact highest weight of $M_2$ minimizing $$d(\nu)=\sum_{i=1}^r|\nu_i-(p-q)/2|+\sum_{j=1}^s|\nu_{r+j}+(p-q)/2|$$ among all occurring compact highest weights. There are a rational compact weight $\mu$ and a joint harmonic polynomial $P$ which is a highest-weight vector of weights $\mu,\mu'$ for the two actions, and $f(P)\ne0$. Moreover, for every polynomial $Q$ of compact type $\mu'$ under the second action, $$f(Q)\in f\bigl(\langle\mathcal H_{\mu'}\rangle_{\mathfrak{gl}_{p+q}}\bigr),$$ where $\mathcal H_{\mu'}$ consists of joint harmonics of that second compact type and the brackets mean the smallest submodule for the first Lie algebra action containing this set.
