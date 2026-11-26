---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/EigenvalueSeparation/AlmostEverywhereEigen/PositiveMeasureNorms/Speciso.lean",
  "declarations": [
    "PositivityTheory.Rg.BcB.E2.P.speciso"
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

## An L2 isometry from a vector spectral measure

[Theorem REP.1241](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.BcB.E2.P.speciso/)

Let $H$ be a complex Hilbert space, $S$ a compact Hausdorff space with its Borel measurable structure, and $\pi:C(S,\mathbb C)\to\mathcal B(H)$ a unital complex $*$-algebra homomorphism. Let $v\in H$ and $\nu$ a finite regular measure on $S$ such that $$\int_S f(s)\,d\nu(s)=\langle v,\pi(f)v\rangle\qquad(f\in C(S,\mathbb C)).$$ There is a bounded complex-linear isometry $V:L^2(S,\nu)\to H$ satisfying $$V(fh)=\pi(f)V(h)\qquad(f\in C(S,\mathbb C),\ h\in L^2(S,\nu)).$$ Multiplication here is understood up to almost-everywhere equality, and the inner product is linear in the second argument.
