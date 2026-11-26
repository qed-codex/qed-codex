---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/EigenvalueSeparation/AlmostEverywhereEigen/OrthogonalKeepingHolds.lean",
  "declarations": [
    "PositivityTheory.Rg.BcB.E2.spec_holds"
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

## A spectral model concentrated near a character

[Theorem REP.1264](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.BcB.E2.spec_holds/)

Let $H$ be a complex Hilbert space, $B$ a commutative unital complex $*$-algebra, $R:B\to\mathcal B(H)$ a unital $*$-algebra homomorphism, and $p:B\to\mathbb C$ a unital $*$-character. Assume $|p(b)|\le\|R(b)\|$ for every $b\in B$. Given a finite set $C_0\subseteq B$ and $\varepsilon>0$, there are a measurable space $S$, a nonzero finite measure $\nu$ on $S$, unital $*$-characters $\chi_s:B\to\mathbb C$, and a bounded complex-linear isometry $V:L^2(S,\nu)\to H$ such that:

1. $s\mapsto\chi_s(b)$ is measurable and $|\chi_s(b)|\le\|R(b)\|$ for every $b\in B$ and every $s\in S$.
2. $V(\chi_{\cdot}(b)h)=R(b)V(h)$ for every $b\in B$ and $h\in L^2(S,\nu)$, with multiplication interpreted almost everywhere.
3. For almost every $s$, $|\chi_s(c)-p(c)|\le\varepsilon$ for every $c\in C_0$.
