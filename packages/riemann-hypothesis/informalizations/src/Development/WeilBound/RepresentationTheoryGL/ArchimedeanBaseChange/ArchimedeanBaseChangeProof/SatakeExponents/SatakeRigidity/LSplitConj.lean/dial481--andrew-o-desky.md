---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/SatakeRigidity/LSplitConj.lean",
  "declarations": [
    "PositivityTheory.Rg.BcB.F.Rig.splitConj"
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

## Inversion of Satake parameters at conjugate split places

[Theorem AGR.1597](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.BcB.F.Rig.splitConj/)

Let $E$ be a CM number field and $\pi$ an automorphic representation of the rank-$n$ identity-form unitary group $U(I_n)$. Let $V_i$ be discrete automorphic representations of $\operatorname{GL}_{n_i}(\mathbb A_E)$, with $n_i>0$ and $\sum_i n_i=n$, and specify their irreducible local components and infinitesimal characters. Let $w,u$ be distinct finite places above the same split place of $E^+$. Assume $\pi$ is unramified at $w$. At both $w$ and $u$, assume a smooth irreducible subquotient of the local parabolic product of the $V_i$ occurs as the local component of $\pi$ under the respective split-place identifications with $\operatorname{GL}_n$.

Suppose all the $V_i$ are spherical at $w$ and $u$. If $B$ and $B'$ are the unions of their Satake multisets at these places, then $$B'=\{\alpha^{-1}:\alpha\in B\},$$ with multiplicities retained.
